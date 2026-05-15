import sqlite3
from typing import List, Tuple, Optional
from repositories.sql_connection import get_connection

def crear_libro(titulo: str, autor: str, isbn: str, anio: int, genero: str, tipo: str) -> bool:
    """Inserta un nuevo libro protegiendo contra SQL Injection."""
    sql = """
        INSERT INTO libros (titulo, autor, isbn, anio, genero, tipo, disponible)
        VALUES (?, ?, ?, ?, ?, ?, 1)
    """
    try:
        with get_connection() as conn:
            conn.cursor().execute(sql, (titulo, autor, isbn, anio, genero, tipo))
            conn.commit()
            return True
    except sqlite3.Error as e:
        print(f"[SQL ERROR] Error al crear libro: {e}")
        return False

def obtener_todos_los_libros() -> List[Tuple]:
    """Obtiene el catálogo completo de libros."""
    try:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM libros")
            return cursor.fetchall()
    except sqlite3.Error as e:
        print(f"[SQL ERROR] Error al obtener libros: {e}")
        return []

def actualizar_libro(libro_id: int, titulo: str, autor: str) -> bool:
    """Actualiza la información básica de un libro."""
    sql = "UPDATE libros SET titulo = ?, autor = ? WHERE id = ?"
    try:
        with get_connection() as conn:
            conn.cursor().execute(sql, (titulo, autor, libro_id))
            conn.commit()
            return True
    except sqlite3.Error as e:
        print(f"[SQL ERROR] Error al actualizar libro: {e}")
        return False

def eliminar_libro(libro_id: int) -> bool:
    """Elimina un libro del sistema."""
    try:
        with get_connection() as conn:
            conn.cursor().execute("DELETE FROM libros WHERE id = ?", (libro_id,))
            conn.commit()
            return True
    except sqlite3.Error as e:
        print(f"[SQL ERROR] Error al eliminar libro: {e}")
        return False
