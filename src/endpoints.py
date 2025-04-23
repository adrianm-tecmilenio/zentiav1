import os
import io

import pdfplumber
from dotenv import load_dotenv
from fastapi import APIRouter, UploadFile, File, HTTPException
from pydantic import BaseModel
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import AzureOpenAIEmbeddings

from src.vector_db import get_pinecone_index, upsert_in_batches, query_vectors

load_dotenv()

router = APIRouter()

# Inicializar embeddings
embeddings = AzureOpenAIEmbeddings(
    dimensions=1024,
    model=os.getenv("AZURE_EMBEDDINGS_DEPLOYMENT"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_key=os.getenv("OPENAI_API_KEY"),
    openai_api_version=os.getenv("OPENAI_API_VERSION")
)

class Body(BaseModel):
    message: str

class Response(BaseModel):
    response: str

async def load_pdfs_and_store_embeddings(files: list[UploadFile]):
    """Carga PDFs, extrae texto y almacena embeddings en Pinecone."""
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=2200, chunk_overlap=300)
    index = get_pinecone_index(os.getenv("PINECONE_INDEX"), dimension=1024)

    for file in files:
        # Leer el archivo PDF en memoria
        pdf_bytes = file.file.read()
        pdf_stream = io.BytesIO(pdf_bytes)

        # Usar pdfplumber para extraer texto y tablas
        with pdfplumber.open(pdf_stream) as pdf:
            text = ""
            for page in pdf.pages:
                # Extraer texto
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"

                # Extraer tablas (opcional)
                tables = page.extract_tables()
                for table in tables:
                    # Convertir la tabla a texto
                    table_text = "\n".join(["\t".join(map(str, row)) for row in table])
                    text += table_text + "\n"

        if not text.strip():
            print("⚠️ Advertencia: No se extrajo texto del PDF.")
            continue

        # Dividir el texto en chunks
        chunks = text_splitter.split_text(text)
        
        # Generar embeddings para cada chunk
        embeddings_list = embeddings.embed_documents(chunks)

        vectors = []
        for i, (chunk, embedding) in enumerate(zip(chunks, embeddings_list)):
            vector_id = f"{file.filename}_{i}"
            vectors.append((vector_id, embedding, {"text": chunk}))

        # Insertar vectores en lotes
        upsert_in_batches(index, vectors, batch_size=100)
        print(f"✅ {len(vectors)} vectores insertados en el índice de Pinecone.")

@router.post("/upload-pdf")
async def upload_pdfs(files: list[UploadFile] = File(...)):
    """Sube PDFs y almacena sus embeddings."""
    try:
        await load_pdfs_and_store_embeddings(files)
        return {"message": "Documentos cargados correctamente."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al cargar documentos: {str(e)}")

@router.post("/delete-all")
async def delete_all_records():
    """Elimina todos los registros del índice de Pinecone."""
    try:
        index = get_pinecone_index(os.getenv("PINECONE_INDEX"))
        index.delete(delete_all=True)
        return {"message": "Todos los registros eliminados exitosamente."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al eliminar registros: {str(e)}")

async def query_similar_vectors(query_text: str, top_k: int = 5) -> list[str]:
    """
    Función para consultar vectores similares en Pinecone.
    
    Args:
        query_text (str): Texto de la consulta
        top_k (int, optional): Número de resultados a devolver. Defaults to 5.
        
    Returns:
        list[str]: Lista de textos relevantes encontrados
    """
    try:
        # Generar embedding para la consulta
        query_embedding = embeddings.embed_query(query_text)
        
        # Consultar vectores similares
        results = query_vectors(
            index_name=os.getenv("PINECONE_INDEX"),
            query_vector=query_embedding,
            top_k=top_k
        )
        
        # Devolver lista de textos relevantes
        return [match["metadata"]["text"] for match in results["matches"]]
    except Exception as e:
        raise Exception(f"Error al consultar vectores: {str(e)}")

@router.post("/query")
async def query_endpoint(body: Body) -> Response:
    """Endpoint para consultar vectores similares en Pinecone."""
    try:
        # Usar la función query_similar_vectors
        relevant_texts = await query_similar_vectors(body.message)
        
        # Construir respuesta con los textos más relevantes
        response_text = "\n\n".join(relevant_texts)
        return Response(response=response_text)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al consultar vectores: {str(e)}")