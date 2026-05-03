from modelos.libro import Libro


class LibroFisico(Libro):
    """
    Representa un libro físico dentro del sistema de biblioteca.
    """

    def __init__(
        self,
        titulo: str,
        autor: str,
        isbn: str,
        anio: int,
        genero: str,
        ubicacion: str,
        num_ejemplares: int,
    ) -> None:
        super().__init__(titulo, autor, isbn, anio, genero)
        self.ubicacion = ubicacion
        self.num_ejemplares = num_ejemplares

    @property
    def ubicacion(self) -> str:
        return self._ubicacion

    @ubicacion.setter
    def ubicacion(self, valor: str) -> None:
        if not valor.strip():
            raise ValueError("La ubicación no puede estar vacía.")
        self._ubicacion = valor.strip()

    @property
    def num_ejemplares(self) -> int:
        return self._num_ejemplares

    @num_ejemplares.setter
    def num_ejemplares(self, valor: int) -> None:
        if not isinstance(valor, int) or valor < 1:
            raise ValueError("Debe haber al menos 1 ejemplar.")
        self._num_ejemplares = valor

    def __str__(self) -> str:
        """
        Representación del libro físico.
        """
        texto_base = super().__str__()
        return f"[Físico x{self.num_ejemplares}] {texto_base} | Ubicación: {self.ubicacion}"

    def to_dict(self) -> dict:
        """
        Convierte el libro físico a diccionario.
        """
        data = super().to_dict()
        data.update({
            "tipo": self.__class__.__name__.lower(),
            "ubicacion": self.ubicacion,
            "num_ejemplares": self.num_ejemplares,
        })
        return data