# Generación de respuestas con el LLM

import openai
from config import OPENAI_API_KEY, LLM_MODEL
from retrieval import search_documents

# Inicializar cliente de Openai
client = openai.OpenAI(api_key=OPENAI_API_KEY)

# Función para generar respuestas con RAG
def generate_rag_response(query, k=15):
    """Recupera documentos relevantes y genera una respuesta con el LLM."""
    relevant_docs = search_documents(query, k)
    context = "\n".join([doc for doc in relevant_docs['documents'][0]])
    prompt = f"""
    Usa la siguiente información para responder la pregunta:
    
    {context}
    
    Pregunta: {query}
    """
    
    response = client.chat.completions.create(
        model=LLM_MODEL,
        messages=[{"role": "system", "content": "Eres un asistente virtual de la compañia de financiamiento Tuya S.A"},
                  {"role": "user", "content": prompt}],
        temperature=0.1
    )
    return response.choices[0].message.content

#print(generate_rag_response("sabes algo de tuya?"))