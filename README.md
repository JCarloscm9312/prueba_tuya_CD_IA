# 📚 RAG con LLMs - Proyecto de Búsqueda Semántica

Este repositorio contiene un sistema de **Retrieval-Augmented Generation (RAG)** utilizando **OpenAI embeddings y ChromaDB** para mejorar la generación de respuestas en lenguaje natural.

## 🚀 Características

✔ Procesamiento de documentos `.txt`  
✔ Generación y almacenamiento de embeddings en **ChromaDB**  
✔ Recuperación de documentos relevantes con búsqueda semántica  
✔ Generación de respuestas usando **GPT-4**  
✔ Código modular en Python con notebooks para experimentación  


## 🛠 Instalación

**1️⃣ Clonar el repositorio**
git clone https://github.com/tu-usuario/rag-llm-project.git
cd rag-llm-project


**2️⃣ Crear un entorno virtual (opcional)**
python -m venv env
source env/bin/activate  # En macOS/Linux
env\Scripts\activate  # En Windows

**3️⃣ Instalar dependencias**
pip install -r requirements.txt

**4️⃣ Configurar variables de entorno**
OPENAI_API_KEY=tu_api_key_aqui

🚀 Uso
Ejecutar el pipeline RAG
Para hacer una consulta y obtener las respuestas requeridas en la prueba:
python src/main.py

🏗 Tecnologías utilizadas
Python 3.8+
OpenAI API (text-embedding-ada-002, gpt-4)
ChromaDB (Base de datos vectorial)
FAISS (Alternativa para almacenamiento de embeddings)
Jupyter Notebook (Análisis y pruebas)

👨‍💻 Autor
JUAN CARLOS CABRERA MUÑOZ
📧 jcarloscm9312@gmail.com




