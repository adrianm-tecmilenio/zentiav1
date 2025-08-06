#!/usr/bin/env python3
"""
Script de prueba para verificar la funcionalidad de búsqueda de cursos
"""

import sys
import os
from pathlib import Path

# Agregar el directorio src al path
sys.path.append(str(Path(__file__).parent / "src"))

from src.skilling.course_search import CourseSearch

def test_course_search():
    """Prueba la funcionalidad de búsqueda de cursos"""
    
    print("🧪 Iniciando pruebas de búsqueda de cursos...")
    
    # Inicializar el buscador de cursos
    try:
        course_searcher = CourseSearch()
        print("✅ Buscador de cursos inicializado correctamente")
    except Exception as e:
        print(f"❌ Error al inicializar el buscador: {e}")
        return
    
    # Prueba 1: Buscar cursos por palabras clave
    print("\n📚 Prueba 1: Búsqueda por palabras clave")
    keywords = ["programacion", "software"]
    cursos = course_searcher.search_courses_by_keywords(keywords, max_results=5)
    
    print(f"Palabras clave: {keywords}")
    print(f"Cursos encontrados: {len(cursos)}")
    
    for i, curso in enumerate(cursos, 1):
        print(f"  {i}. {curso['titulo']}")
        print(f"     Precio: {curso['precio_actual']}")
        print(f"     Score: {curso['score_relevancia']:.2f}")
        print(f"     Palabras coincidentes: {curso['palabras_coincidentes']}")
        print()
    
    # Prueba 2: Obtener todos los cursos
    print("\n📚 Prueba 2: Obtener todos los cursos")
    todos_cursos = course_searcher.get_all_courses()
    print(f"Total de cursos disponibles: {len(todos_cursos)}")
    
    # Prueba 3: Buscar por categoría
    print("\n📚 Prueba 3: Búsqueda por categoría")
    categoria = "negocios"
    cursos_categoria = course_searcher.get_courses_by_category(categoria)
    print(f"Cursos en categoría '{categoria}': {len(cursos_categoria)}")
    
    for i, curso in enumerate(cursos_categoria[:3], 1):
        print(f"  {i}. {curso['titulo']}")
    
    print("\n✅ Todas las pruebas completadas exitosamente!")

if __name__ == "__main__":
    test_course_search() 