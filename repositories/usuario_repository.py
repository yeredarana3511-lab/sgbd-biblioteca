import sqlite3
from typing import List, Tuple
from repositories.sql_connection import get_connection

def crear_usuario(nombre: str, email: str, rol: str, limite_libros: int = 3) -> bool:
    """Registra un nuevo usuario en la base de datos."""
    sql = "INSERT INTO usuarios (nombre, email, rol, limite_libros) VALUES (?, ?, ?, ?)"
    try:
        with get_connection() as conn:
            conn.cursor().execute(sql, (nombre, email, rol, limite_libros))
            conn.commit()
            return True
    except sqlite3.Error as e:
        print(f"[SQL ERROR] Error al crear usuario: {e}")
        return False

def obtener_todos_los_usuarios() -> List[Tuple]:
    """Obtiene una lista con todos los usuarios registrados."""
    try:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM usuarios")
            return cursor.fetchall()
    except sqlite3.Error as e:
        print(f"[SQL ERROR] Error al obtener usuarios: {e}")
        return []
