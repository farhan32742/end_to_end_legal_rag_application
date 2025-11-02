import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import PyPDFLoader
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_groq import ChatGroq
from langchain.retrievers import MultiQueryRetriever
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough, RunnableLambda
from langchain.schema import StrOutputParser

# Load environment variables
load_dotenv()
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

# PDF loading function
def load_pdf(file_path):
    loader = PyPDFLoader(file_path)
    documents = loader.load()
    return documents

# Text splitting function
def split_text(documents):
    splitter = RecursiveCharacterTextSplitter(chunk_size=2000, chunk_overlap=400)
    chunks = splitter.split_documents(documents)
    return chunks

# Embedding and FAISS creation
def embedding_text(chunks, embed_model):
    vector_store = FAISS.from_documents(chunks, embed_model)
    return vector_store

# Combine retrieved docs into formatted string
def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

if __name__ == "__main__":
    index_path = "vectorstore/constitution_index"
    pdf_path = "D:\\GENERATIVE AI\\legal_end_to_end_chatbot\\constitution.pdf"

    # Load model and embeddings
    model = init_chat_model("groq:llama-3.1-8b-instant")
    embed_model = GoogleGenerativeAIEmbeddings(
        model="models/text-embedding-004",
        google_api_key=os.getenv("GOOGLE_API_KEY")
    )

    # Load or create vector store
    if os.path.exists(index_path):
        print("Loading FAISS vector store from disk...")
        vector_store = FAISS.load_local(index_path, embeddings=embed_model, allow_dangerous_deserialization=True)
    else:
        print("Creating FAISS vector store...")
        document = load_pdf(pdf_path)
        chunks = split_text(document)
        vector_store = embedding_text(chunks, embed_model)
        vector_store.save_local(index_path)
        print("FAISS vector store saved to disk.")

    # Setup retriever
    retriever = vector_store.as_retriever(search_type="mmr", search_kwargs={"k": 3})
    multi_retriever = MultiQueryRetriever.from_llm(retriever=retriever, llm=model)

    # Prompt Template
    prompt_template = PromptTemplate(
        input_variables=["context", "question"],
        template="""
You are a helpful and knowledgeable legal assistant well-versed in the Constitution of Pakistan.
Your job is to answer questions strictly based on the given context. If the context does not contain enough information, say "The context is insufficient to answer this question."

Always include the Article or Section number in your answer if available in the context.

Use a formal, yet simple and understandable legal tone suitable for a Pakistani legal audience.

--------------------
Context:
{context}

Question:
{question}

Answer:"""
    )

    # RAG Chain
    rag_chain = (
        {"context": retriever | RunnableLambda(format_docs), "question": RunnablePassthrough()}
        | prompt_template
        | model
        | StrOutputParser()
    )

    # Example user query
    user_question = "What language is declared as the national language of Pakistan in the Constitution?"
    answer = rag_chain.invoke(user_question)

    print("\nAnswer from Legal RAG system:")
    print(answer)
