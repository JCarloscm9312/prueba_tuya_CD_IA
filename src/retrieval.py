# Recuperación de información 

from embeddings import get_embedding, collection
import chromadb
from config import OPENAI_API_KEY, EMBEDDING_MODEL, EMBEDDINGS_DIR, DB_NAME

# Inicializar ChromaDB
chroma_client = chromadb.PersistentClient(path=EMBEDDINGS_DIR)
collection = chroma_client.get_or_create_collection(DB_NAME)

# Busqueda de información relevante en la base de datos vectorial
def search_documents(query, k=5):
    """Realiza una búsqueda en la base de datos vectorial"""
    query_embedding = get_embedding(query)
    results = collection.query(query_embeddings=[query_embedding], n_results=k)
    
    return results

#print(search_documents("seguros"))

