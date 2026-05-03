from modelos.usuario import Usuario
from modelos.libro import Libro
from modelos.prestamo import Prestamo


def puede_realizar_prestamo(usuario: Usuario, libro: Libro) -> bool:
    """
    Verifica si se puede realizar un préstamo.
    """
    return usuario.puede_pedir_prestado() and libro.disponible


def realizar_prestamo(usuario: Usuario, libro: Libro) -> Prestamo:
    """
    Realiza un préstamo si cumple las reglas.
    """
    if not puede_realizar_prestamo(usuario, libro):
        raise ValueError("No se puede realizar el préstamo.")

    return Prestamo(usuario, libro)