import faiss
from langchain.embeddings import OpenAIEmbeddings
import pandas as pd

index = faiss.read_index("faiss_index")
df = pd.read_csv("courses_with_embeddings.csv")
embeddings = OpenAIEmbeddings(model="text-embedding-ada-002")

def search_courses(query, k=5):
    query_vector = embeddings.embed_text(query).reshape(1, -1)
    distances, indices = index.search(query_vector, k)
    results = df.iloc[indices[0]]
    return results[["title", "description", "link"]]

query = "data science basics"
results = search_courses(query)
print(results)

index = faiss.read_index("faiss_index")
df = pd.read_csv("courses_with_embeddings.csv")
embeddings = OpenAIEmbeddings(model="text-embedding-ada-002")

def search_courses(query, k=5):
    query_vector = embeddings.embed_text(query).reshape(1, -1)
    distances, indices = index.search(query_vector, k)
    results = df.iloc[indices[0]]
    return results[["title", "description", "link"]]

query = "data science basics"
results = search_courses(query)
print(results)
