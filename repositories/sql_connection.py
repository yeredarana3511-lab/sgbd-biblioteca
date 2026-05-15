import sqlite3
import os
from config.settings import SQLITE_DB_PATH, DATA_DIR

def get_connection() -> sqlite3.Connection:
    """
    Retorna una conexión a la base de datos SQLite.
    Asegura que el directorio data/ exista y activa las Foreign Keys.
    """
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)
        
    conn = sqlite3.connect(SQLITE_DB_PATH)
    # Por defecto, SQLite desactiva las llaves foráneas. Las activamos:
    conn.execute("PRAGMA foreign_keys = 1")
    return conn

def inicializar_base_datos() -> None:
    """
    Crea las tablas necesarias en la base de datos si aún no existen.
    """
    try:
        with get_connection() as conn:
            cursor = conn.cursor()
            
            # Tabla usuarios
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS usuarios (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT NOT NULL,
                    email TEXT UNIQUE NOT NULL,
                    rol TEXT NOT NULL,
                    limite_libros INTEGER DEFAULT 3
                )
            """)
            
            # Tabla libros
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS libros (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    titulo TEXT NOT NULL,
                    autor TEXT NOT NULL,
                    isbn TEXT UNIQUE NOT NULL,
                    anio INTEGER,
                    genero TEXT,
                    tipo TEXT NOT NULL,
                    disponible BOOLEAN DEFAULT 1
                )
            """)
            
            # Tabla prestamos
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS prestamos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    usuario_id INTEGER NOT NULL,
                    libro_id INTEGER NOT NULL,
                    fecha_prestamo DATETIME DEFAULT CURRENT_TIMESTAMP,
                    fecha_devolucion DATETIME,
                    activo BOOLEAN DEFAULT 1,
                    FOREIGN KEY(usuario_id) REFERENCES usuarios(id),
                    FOREIGN KEY(libro_id) REFERENCES libros(id)
                )
            """)
    except sqlite3.Error as e:
        print(f"[SQL ERROR] Error al inicializar tablas: {e}")
