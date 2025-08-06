import pandas as pd
import os
from typing import List, Dict, Any
from pathlib import Path

class CourseSearch:
    def __init__(self, csv_path: str = None):
        """
        Inicializa el buscador de cursos con la ruta del archivo CSV
        """
        if csv_path is None:
            # Ruta por defecto relativa al directorio actual
            current_dir = Path(__file__).parent
            csv_path = current_dir / "skilling_products_with_keywords.csv"
        
        self.csv_path = csv_path
        self.df = None
        self._load_data()
    
    def _load_data(self):
        """
        Carga los datos del archivo CSV
        """
        try:
            self.df = pd.read_csv(self.csv_path)
            # Limpiar y normalizar las palabras clave
            self.df['palabras_clave_clean'] = self.df['palabras_clave'].str.lower().str.strip()
        except Exception as e:
            print(f"Error al cargar el archivo CSV: {e}")
            self.df = pd.DataFrame()
    
    def search_courses_by_keywords(self, keywords: List[str], max_results: int = 10) -> List[Dict[str, Any]]:
        """
        Busca cursos que contengan las palabras clave especificadas
        
        Args:
            keywords: Lista de palabras clave a buscar
            max_results: Número máximo de resultados a devolver
            
        Returns:
            Lista de diccionarios con información de los cursos encontrados
        """
        if self.df.empty:
            return []
        
        # Normalizar las palabras clave de búsqueda
        search_keywords = [kw.lower().strip() for kw in keywords]
        
        # Filtrar cursos que contengan al menos una de las palabras clave
        matching_courses = []
        
        for _, row in self.df.iterrows():
            course_keywords = row['palabras_clave_clean'].split(', ')
            course_keywords = [kw.strip() for kw in course_keywords]
            
            # Verificar si hay coincidencias
            matches = [kw for kw in search_keywords if any(search_kw in course_kw for course_kw in course_keywords for search_kw in [kw])]
            
            if matches:
                # Calcular score de relevancia (más palabras clave coincidentes = mayor score)
                score = len(matches) / len(search_keywords)
                
                matching_courses.append({
                    'titulo': row['Titulo'],
                    'enlace': row['Enlace'],
                    'precio_actual': row['Precio actual'],
                    'precio_original': row['Precio original'],
                    'palabras_clave': row['palabras_clave'],
                    'score_relevancia': score,
                    'palabras_coincidentes': matches
                })
        
        # Ordenar por score de relevancia (descendente) y limitar resultados
        matching_courses.sort(key=lambda x: x['score_relevancia'], reverse=True)
        
        return matching_courses[:max_results]
    
    def get_all_courses(self) -> List[Dict[str, Any]]:
        """
        Obtiene todos los cursos disponibles
        
        Returns:
            Lista de todos los cursos
        """
        if self.df.empty:
            return []
        
        courses = []
        for _, row in self.df.iterrows():
            courses.append({
                'titulo': row['Titulo'],
                'enlace': row['Enlace'],
                'precio_actual': row['Precio actual'],
                'precio_original': row['Precio original'],
                'palabras_clave': row['palabras_clave']
            })
        
        return courses
    
    def get_courses_by_category(self, category: str) -> List[Dict[str, Any]]:
        """
        Obtiene cursos por categoría específica
        
        Args:
            category: Categoría a buscar (ej: 'programacion', 'negocios', etc.)
            
        Returns:
            Lista de cursos de la categoría especificada
        """
        if self.df.empty:
            return []
        
        category = category.lower().strip()
        matching_courses = []
        
        for _, row in self.df.iterrows():
            course_keywords = row['palabras_clave_clean'].split(', ')
            course_keywords = [kw.strip() for kw in course_keywords]
            
            if category in course_keywords:
                matching_courses.append({
                    'titulo': row['Titulo'],
                    'enlace': row['Enlace'],
                    'precio_actual': row['Precio actual'],
                    'precio_original': row['Precio original'],
                    'palabras_clave': row['palabras_clave']
                })
        
        return matching_courses 