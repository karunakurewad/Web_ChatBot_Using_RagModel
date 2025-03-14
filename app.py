import streamlit as st
import os
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain_pinecone import PineconeVectorStore
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import WebBaseLoader
from langchain.chains import RetrievalQA
from pinecone import Pinecone

# 🔹 Load API Keys from .env file
load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
PINECONE_ENV = os.getenv("PINECONE_ENV")
INDEX_NAME = "langchain-test-index"

# 🔹 Ensure API keys are loaded
if not GOOGLE_API_KEY or not PINECONE_API_KEY or not PINECONE_ENV:
    st.error("❌ Missing API Keys! Please check your .env file.")
    st.stop()

# 🔹 Initialize Pinecone Client
pc = Pinecone(api_key=PINECONE_API_KEY, environment=PINECONE_ENV)

# 🔹 Load and Process Data
loader = WebBaseLoader("https://brainlox.com/courses/category/technical")
docs = loader.load()
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
texts = text_splitter.split_documents(docs)

# 🔹 Create Embeddings
embeddings = GoogleGenerativeAIEmbeddings(
    model="models/embedding-001",
    google_api_key=GOOGLE_API_KEY,
    task_type="retrieval_query"
)

# 🔹 Store Data in Pinecone
if INDEX_NAME not in pc.list_indexes().names():
    pc.create_index(name=INDEX_NAME, dimension=768, metric="cosine")  # Adjust dimension based on embeddings

docsearch = PineconeVectorStore.from_documents(texts, embeddings, index_name=INDEX_NAME)

# 🔹 Set up AI Model
chat_model = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    google_api_key=GOOGLE_API_KEY,
    temperature=0.3
)

# 🔹 Define Prompt
prompt_template = """
You are an AI assistant retrieving technical course details from Brainlox.

Context:
{context}

Question:
{query}

Answer:
"""
prompt = PromptTemplate(template=prompt_template, input_variables=['context', 'query'])

# 🔹 Create Retriever and QA Chain
retriever = docsearch.as_retriever(search_kwargs={"k": 5})
qa_chain = RetrievalQA.from_chain_type(
    llm=chat_model,
    retriever=retriever
)

# 🔹 Debug: Print expected input keys
st.write(f"Expected input keys: {qa_chain.input_keys}")

# 🔹 Streamlit UI
st.title("🔍 Brainlox Course Search AI")
st.write("Ask about a technical course available on Brainlox.")

user_query = st.text_input("🔹 Type your question:")
if st.button("Search") and user_query:
    input_key = list(qa_chain.input_keys)[0]  # Get correct input key
    response = qa_chain.invoke({input_key: user_query})  # ✅ Fix dynamic key issue
    st.subheader("💡 Answer:")
    st.write(response["result"])
