# CONFIGURACIÓN DEL PROYECTO

import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# Rutas de datos
DATA_DIR = "../data/01_raw/"
PROCESSED_DATA_FILE = "../data/02_processed/clean_texts.csv"
EMBEDDINGS_DIR = "../data/03_embeddings/"

# Configuración de OpenAI
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
EMBEDDING_MODEL = "text-embedding-ada-002"
LLM_MODEL = "gpt-4"

# Base de datos vectorial
DB_NAME = "chroma_db"
CHUNK_SIZE = 500
