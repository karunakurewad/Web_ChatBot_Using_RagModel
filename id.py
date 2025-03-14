from dotenv import load_dotenv
import os

load_dotenv()


PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
PINECONE_ENV = os.getenv("PINECONE_ENV")
INDEX_NAME = "langchain-test-index"

import pinecone
pc = pinecone.Pinecone(api_key=PINECONE_API_KEY, environment=PINECONE_ENV)
index = pc.Index(INDEX_NAME)

print(index.describe_index_stats()['total_vector_count'])