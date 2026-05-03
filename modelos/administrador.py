from typing import Any
from modelos.usuario import Usuario


class Administrador(Usuario):
    """
    Representa a un administrador dentro del sistema.
    """

    def __init__(
        self,
        nombre: str,
        email: str,
        contrasena_hash: str,
        nivel_acceso: int = 1,
    ) -> None:
        super().__init__(nombre, email, contrasena_hash)
        self.nivel_acceso = nivel_acceso

    @property
    def nivel_acceso(self) -> int:
        return self._nivel_acceso

    @nivel_acceso.setter
    def nivel_acceso(self, valor: int) -> None:
        if not 1 <= valor <= 5:
            raise ValueError("El nivel de acceso debe estar entre 1 y 5.")
        self._nivel_acceso = valor

    def puede_pedir_prestado(self) -> bool:
        """El administrador siempre puede pedir libros."""
        return True

    # --- MÉTODOS EXCLUSIVOS ---

    def agregar_libro(self, libro: Any) -> None:
        print(
            f"[SISTEMA] '{self.nombre}' agregó: "
            f"{getattr(libro, 'titulo', 'Libro Desconocido')}"
        )

    def eliminar_usuario(self, usuario: Any) -> None:
        if self.nivel_acceso >= 3:
            print(
                f"[SISTEMA] '{self.nombre}' eliminó a: "
                f"{getattr(usuario, 'nombre', 'Usuario desconocido')}"
            )
        else:
            print("[ERROR] Nivel insuficiente (>=3 requerido)")

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "fecha_creacion": self.fecha_creacion.isoformat(),
            "rol": self.__class__.__name__.lower(),
            "nombre": self.nombre,
            "email": self.email,
            "nivel_acceso": self.nivel_acceso,
        }

    def __str__(self) -> str:
        return f"[Administrador] {self.nombre} (Nivel {self.nivel_acceso})"