import sqlite3
from repositories.sql_connection import get_connection


def registrar_prestamo(usuario_id: int, libro_id: int) -> bool:
    """
    Registra un préstamo y marca el libro como no disponible.
    """
    sql_verificar = "SELECT disponible FROM libros WHERE id = ?"
    sql_prestamo = """
        INSERT INTO prestamos (usuario_id, libro_id, activo)
        VALUES (?, ?, 1)
    """
    sql_libro = "UPDATE libros SET disponible = 0 WHERE id = ?"

    try:
        with get_connection() as conn:
            cursor = conn.cursor()

            cursor.execute(sql_verificar, (libro_id,))
            resultado = cursor.fetchone()

            if resultado is None:
                print("El libro no existe.")
                return False

            if resultado[0] == 0:
                print("El libro no está disponible.")
                return False

            cursor.execute(sql_prestamo, (usuario_id, libro_id))
            cursor.execute(sql_libro, (libro_id,))
            conn.commit()
            return True

    except sqlite3.Error as error:
        print(f"[SQL ERROR] Error al registrar préstamo: {error}")
        return False
    
    registrar_evento(
    "PRESTAMO",
    "Se registró un préstamo",
    {"usuario_id": usuario_id, "libro_id": libro_id}
)


def devolver_prestamo(prestamo_id: int, libro_id: int) -> bool:
    """
    Devuelve un préstamo y marca el libro como disponible.
    """
    sql_prestamo = """
        UPDATE prestamos
        SET activo = 0, fecha_devolucion = CURRENT_TIMESTAMP
        WHERE id = ? AND activo = 1
    """
    sql_libro = "UPDATE libros SET disponible = 1 WHERE id = ?"

    try:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(sql_prestamo, (prestamo_id,))

            if cursor.rowcount == 0:
                print("No se encontró un préstamo activo con ese ID.")
                return False

            cursor.execute(sql_libro, (libro_id,))
            conn.commit()
            return True

    except sqlite3.Error as error:
        print(f"[SQL ERROR] Error al devolver préstamo: {error}")
        return False
    
    registrar_evento(
    "DEVOLUCION",
    "Se devolvió un préstamo",
    {"prestamo_id": prestamo_id, "libro_id": libro_id}
)
        
