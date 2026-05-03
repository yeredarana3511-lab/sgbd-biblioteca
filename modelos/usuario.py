from abc import abstractmethod

from modelos.entidad import Entidad
from utils.validadores import validar_email


class Usuario(Entidad):
    """
    Clase base abstracta para los usuarios del sistema.
    """

    def __init__(
        self,
        nombre: str,
        email: str,
        contrasena_hash: str,
    ) -> None:
        super().__init__()
        self.nombre = nombre
        self.email = email
        self.contrasena_hash = contrasena_hash

    @property
    def nombre(self) -> str:
        """Obtiene el nombre del usuario."""
        return self._nombre

    @nombre.setter
    def nombre(self, valor: str) -> None:
        if not valor.strip():
            raise ValueError("El nombre no puede estar vacío.")
        self._nombre = valor.strip()

    @property
    def email(self) -> str:
        """Obtiene el email del usuario."""
        return self._email

    @email.setter
    def email(self, valor: str) -> None:
        if not validar_email(valor):
            raise ValueError("El email no tiene formato válido.")
        self._email = valor.strip().lower()

    @property
    def contrasena_hash(self) -> str:
        """Obtiene la contraseña cifrada."""
        return self._contrasena_hash

    @contrasena_hash.setter
    def contrasena_hash(self, valor: str) -> None:
        if not valor.strip():
            raise ValueError("La contraseña no puede estar vacía.")
        self._contrasena_hash = valor.strip()

    @abstractmethod
    def puede_pedir_prestado(self) -> bool:
        """Indica si el usuario puede pedir libros prestados."""
        pass

    def __str__(self) -> str:
        """Devuelve representación del usuario."""
        return f"{self.__class__.__name__}: {self.nombre} <{self.email}>"