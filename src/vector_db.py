import os
from dotenv import load_dotenv
from pinecone import Pinecone

load_dotenv()

# Instancia de Pinecone
pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))


def get_pinecone_index(index_name: str, dimension: int = 1536):
    """
    Obtiene un índice de Pinecone o indica que no existe.
    """
    try:
        
        # Obtener el índice
        return pc.Index(index_name)
    except Exception as e:
        raise Exception(f"Error al obtener el índice de Pinecone: {str(e)}")

def upsert_in_batches(index, vectors: list, batch_size: int = 100):
    """
    Inserta vectores en lotes para evitar exceder el límite de tamaño de Pinecone.
    """
    try:
        for i in range(0, len(vectors), batch_size):
            batch = vectors[i:i + batch_size]
            index.upsert(vectors=batch)
            print(f"Upserted batch {i // batch_size + 1}")
    except Exception as e:
        raise Exception(f"Error al insertar vectores en Pinecone: {str(e)}")

def query_vectors(index_name: str, query_vector: list, top_k: int = 5, include_metadata: bool = True):
    """
    Consulta vectores similares en un índice de Pinecone.
    
    Args:
        index_name (str): Nombre del índice
        query_vector (list): Vector de consulta
        top_k (int, optional): Número de resultados a devolver. Defaults to 5.
        include_metadata (bool, optional): Incluir metadatos en la respuesta. Defaults to True.
        
    Returns:
        dict: Resultados de la consulta
    """
    try:
        index = get_pinecone_index(index_name)
        return index.query(
            vector=query_vector,
            top_k=top_k,
            include_metadata=include_metadata
        )
    except Exception as e:
        raise Exception(f"Error al consultar vectores en Pinecone: {str(e)}") 