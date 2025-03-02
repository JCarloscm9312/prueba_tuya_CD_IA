# GENERACIÓN DE EMBEDDINGS

import pandas as pd
import openai
import chromadb
from config import OPENAI_API_KEY, EMBEDDING_MODEL, EMBEDDINGS_DIR, DB_NAME

# Carga de datos
#df = pd.read_csv(DATA_FILE)

# Inicializar ChromaDB
chroma_client = chromadb.PersistentClient(path=EMBEDDINGS_DIR)
collection = chroma_client.get_or_create_collection(DB_NAME)

# Inicializar cliente de Openai
client = openai.OpenAI(api_key=OPENAI_API_KEY)

# Función para obtener embeddings
def get_embedding(text):
    """Obtiene el embedding de un texto"""
    response = client.embeddings.create(
        input=text,
        model=EMBEDDING_MODEL
    )
    return response.data[0].embedding

# Generar embeddings y almacenarlos en ChromaDB
def add_to_database(df):
    print("Generando embeddings y almacenando en ChromaDB...")
    for i, row in tqdm(df.iterrows(), total=len(df)):
        text = row["clean_text"]
        embedding = get_embedding(text)
        collection.add(
            ids=[str(i)],
            embeddings=[embedding],
            documents=[row["clean_text"]], 
            metadatas=[{"filename": row["filename"], "chunk_id": row["chunk_id"]}]
        )

    print(f"Base de datos vectorial guardada en {EMBEDDINGS_DIR}")


