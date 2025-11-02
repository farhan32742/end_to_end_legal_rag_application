"""
Optimized RAG Service for FastAPI
Loads models and vector store once at initialization for maximum performance
"""
import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_community.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain.retrievers import MultiQueryRetriever
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough, RunnableLambda
from langchain.schema import StrOutputParser
from pathlib import Path

load_dotenv()

class RAGService:
    """RAG Service that preloads all models for fast responses"""
    
    def __init__(self):
        """Initialize the RAG service - loads everything once"""
        print("📚 Loading vector store and models...")
        
        # Find vector store path
        self.index_path = self._find_vector_store()
        
        # Load embeddings model
        print("   Loading embeddings model...")
        self.embed_model = GoogleGenerativeAIEmbeddings(
            model="models/text-embedding-004",
            google_api_key=os.getenv("GOOGLE_API_KEY")
        )
        
        # Load vector store (done once at startup)
        print("   Loading FAISS vector store...")
        self.vector_store = FAISS.load_local(
            self.index_path,
            embeddings=self.embed_model,
            allow_dangerous_deserialization=True
        )
        
        # Load LLM model (done once at startup)
        print("   Loading LLM model...")
        self.llm_model = init_chat_model("groq:llama-3.1-8b-instant")
        
        # Setup retriever
        print("   Setting up retriever...")
        retriever = self.vector_store.as_retriever(
            search_type="mmr",
            search_kwargs={"k": 3}
        )
        self.multi_retriever = MultiQueryRetriever.from_llm(
            retriever=retriever,
            llm=self.llm_model
        )
        
        # Create prompt template
        self.prompt_template = PromptTemplate(
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
        
        # Build RAG chain (done once)
        self.rag_chain = (
            {
                "context": self.multi_retriever | RunnableLambda(self._format_docs),
                "question": RunnablePassthrough()
            }
            | self.prompt_template
            | self.llm_model
            | StrOutputParser()
        )
        
        print("✅ All models loaded successfully!")
    
    def _find_vector_store(self):
        """Find the vector store path"""
        possible_paths = [
            "vectorstore/constitution_index",
            Path(__file__).parent.parent.parent / "vectorstore" / "constitution_index",
            "./vectorstore/constitution_index",
        ]
        
        for path in possible_paths:
            if isinstance(path, str):
                path_obj = Path(path)
            else:
                path_obj = path
            
            if path_obj.exists():
                return str(path_obj)
        
        raise FileNotFoundError(
            f"Vector store not found. Checked: {possible_paths}. "
            "Please run Legal_RAG_application.py first to create the vector store."
        )
    
    def _format_docs(self, docs):
        """Format retrieved documents into a string"""
        return "\n\n".join(doc.page_content for doc in docs)
    
    async def get_answer(self, question: str) -> str:
        """
        Get answer for a question using the preloaded RAG chain
        This is fast because everything is already loaded!
        """
        try:
            # Invoke RAG chain (everything is already loaded, so this is fast)
            answer = self.rag_chain.invoke(question)
            return answer
        except Exception as e:
            raise Exception(f"Error getting answer: {str(e)}")

