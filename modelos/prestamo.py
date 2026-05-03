from datetime import datetime
from typing import Optional

from modelos.usuario import Usuario
from modelos.libro import Libro


class Prestamo:
    """
    Representa un préstamo entre un usuario y un libro.
    """

    def __init__(self, usuario: Usuario, libro: Libro) -> None:
        if not isinstance(usuario, Usuario):
            raise TypeError("El parámetro 'usuario' debe ser Usuario.")

        if not isinstance(libro, Libro):
            raise TypeError("El parámetro 'libro' debe ser Libro.")

        if not usuario.puede_pedir_prestado():
            raise ValueError("El usuario no puede pedir más libros.")

        if not libro.disponible:
            raise ValueError("El libro no está disponible.")

        self.usuario = usuario
        self.libro = libro
        self.fecha_prestamo = datetime.now()
        self.fecha_devolucion: Optional[datetime] = None
        self.activo = True

        self.libro.disponible = False

        if hasattr(self.usuario, "libros_actualmente_prestados"):
            self.usuario.libros_actualmente_prestados += 1

    def devolver(self) -> None:
        """
        Procesa la devolución de un préstamo.
        """
        if not self.activo:
            raise ValueError("Este préstamo ya fue devuelto.")

        self.activo = False
        self.fecha_devolucion = datetime.now()
        self.libro.disponible = True

        if hasattr(self.usuario, "libros_actualmente_prestados"):
            if self.usuario.libros_actualmente_prestados > 0:
                self.usuario.libros_actualmente_prestados -= 1

    def __str__(self) -> str:
        estado = "VIGENTE" if self.activo else "FINALIZADO"
        fecha = self.fecha_prestamo.strftime("%d/%m/%Y")

        return (
            f"[Préstamo {estado}] "
            f"{self.usuario.nombre} → '{self.libro.titulo}' "
            f"({fecha})"
        )