# PREPROCESADO Y ALMACENAMIENTO DE LOS TEXTOS
from config import CHUNK_SIZE
import re

# Preprocesado de los textos
def clean_text(text):
    """Realiza una limpieza básica del texto sin tokenización ni lematización."""
    text = text.lower()  # Convertir a minúsculas
    text = re.sub(r'[^\w\s.,!?;:]', '', text)  # Eliminar caracteres especiales excepto puntuación básica
    text = re.sub(r'\s+', ' ', text).strip()  # Remover espacios múltiples
    return text

# DIvisión de los textos en grupos de palabras
def chunk_text(text, chunk_size=CHUNK_SIZE):
    """Divide el texto en fragmentos de tamaño específico respetando las palabras completas."""
    words = text.split()  # Dividir el texto en palabras
    chunks = []
    current_chunk = []
    current_length = 0
    
    for word in words:
        if current_length + len(word) + 1 > chunk_size:  # +1 para el espacio entre palabras
            chunks.append(" ".join(current_chunk))
            current_chunk = []
            current_length = 0
        
        current_chunk.append(word)
        current_length += len(word) + 1  # Considerar el espacio
    
    if current_chunk:  # Agregar el último fragmento si quedó texto
        chunks.append(" ".join(current_chunk))
    
    return chunks


# Aplicación de las funciones a los documentos
def process_text_files(directory):
    """Carga y preprocesa todos los archivos TXT en un directorio."""
    data = []
    
    for filename in tqdm(os.listdir(directory)):
        if filename.endswith(".txt"):
            file_path = os.path.join(directory, filename)
            with open(file_path, "r", encoding="utf-8") as f:
                raw_text = f.read()
                cleaned_text = clean_text(raw_text)
                chunks = chunk_text(cleaned_text)
                for idx, chunk in enumerate(chunks):
                    data.append({"filename": filename, "chunk_id": idx, "clean_text": chunk})
    
    return pd.DataFrame(data)