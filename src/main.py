from data_processing import clean_text, chunk_text
from embeddings import add_to_database
from retrieval import search_documents
from generation import generate_rag_response
from config import DATA_DIR, PROCESSED_DATA_FILE

def main():
    # Las siguientes lineas de codigo estan comentadas por que la base vectorial ya esta creada
    # Cargamos y preprocesamos los archivos
    #df = process_text_files(DATA_DIR)
    # Guardamos los datos preprocesados
    #df.to_csv(PROCESSED_DATA_FILE, index=False)
    # Generamos los embeddings y los guardamos en la base de datos vectorial
    #add_to_database(df)

    print("-------------------------------------------------------------------------")
    p1 = "¿ Cuáles son los nombres de las tarjetas que tiene disponibles Tuya S.A?."
    print(f"Pregunta 1: {p1}")
    respuesta1 = generate_rag_response(p1)
    print(f"Respuesta pregunta 1: {respuesta1}")
    print("-------------------------------------------------------------------------")
    p2 = "¿ Cuáles son los valores la tasa de interés y póliza del producto credicompras?."
    print(f"Pregunta 2: {p2}")
    respuesta2 = generate_rag_response(p2)
    print("-------------------------------------------------------------------------")
    print(f"Respuesta pregunta 2: {respuesta2}")
    print("-------------------------------------------------------------------------")
if __name__ == "__main__":
    main()