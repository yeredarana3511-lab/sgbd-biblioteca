import datetime
from utils.validadores import validar_isbn13


class Libro:
    """
    Representa un libro dentro del sistema de biblioteca.
    """

    def __init__(
        self,
        titulo: str,
        autor: str,
        isbn: str,
        anio: int,
        genero: str,
    ) -> None:
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.anio = anio
        self.genero = genero
        self._disponible = True

    @property
    def titulo(self) -> str:
        return self._titulo

    @titulo.setter
    def titulo(self, valor: str) -> None:
        if not valor.strip():
            raise ValueError("El título no puede estar vacío.")
        self._titulo = valor.strip()

    @property
    def autor(self) -> str:
        return self._autor

    @autor.setter
    def autor(self, valor: str) -> None:
        if not valor.strip():
            raise ValueError("El autor no puede estar vacío.")
        self._autor = valor.strip()

    @property
    def isbn(self) -> str:
        return self._isbn

    @isbn.setter
    def isbn(self, valor: str) -> None:
        if not validar_isbn13(valor):
            raise ValueError(f"El ISBN ({valor}) no es válido.")
        self._isbn = valor

    @property
    def anio(self) -> int:
        return self._anio

    @anio.setter
    def anio(self, valor: int) -> None:
        anio_actual = datetime.datetime.now().year
        if not 1440 <= valor <= anio_actual:
            raise ValueError(f"Año inválido: {valor}")
        self._anio = valor

    @property
    def genero(self) -> str:
        return self._genero

    @genero.setter
    def genero(self, valor: str) -> None:
        if not valor.strip():
            raise ValueError("El género no puede estar vacío.")
        self._genero = valor.strip()

    @property
    def disponible(self) -> bool:
        return self._disponible

    @disponible.setter
    def disponible(self, estado: bool) -> None:
        if not isinstance(estado, bool):
            raise TypeError("Debe ser True o False")
        self._disponible = estado

    def __str__(self) -> str:
        estado = "Disponible" if self.disponible else "Prestado"
        return f"{self.titulo} - {self.autor} ({self.anio}) [{estado}]"

    def __repr__(self) -> str:
        return (
            f"Libro(titulo='{self.titulo}', autor='{self.autor}', "
            f"isbn='{self.isbn}', anio={self.anio}, genero='{self.genero}')"
        )

    def __eq__(self, otro: object) -> bool:
        if not isinstance(otro, Libro):
            return NotImplemented
        return self.isbn == otro.isbn

    def to_dict(self) -> dict:
        return {
            "titulo": self.titulo,
            "autor": self.autor,
            "isbn": self.isbn,
            "anio": self.anio,
            "genero": self.genero,
            "disponible": self.disponible,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Libro":
        libro = cls(
            titulo=data["titulo"],
            autor=data["autor"],
            isbn=data["isbn"],
            anio=data["anio"],
            genero=data["genero"],
        )
        if "disponible" in data:
            libro.disponible = data["disponible"]
        return libro