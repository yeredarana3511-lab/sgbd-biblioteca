from modelos.libro import Libro
from utils.constantes import FORMATOS_VALIDOS


class LibroDigital(Libro):
    """
    Representa un libro digital dentro del sistema.
    """

    def __init__(
        self,
        titulo: str,
        autor: str,
        isbn: str,
        anio: int,
        genero: str,
        formato: str,
        tamano_mb: float,
        url_descarga: str,
    ) -> None:
        super().__init__(titulo, autor, isbn, anio, genero)
        self.formato = formato
        self.tamano_mb = tamano_mb
        self.url_descarga = url_descarga

    @property
    def formato(self) -> str:
        return self._formato

    @formato.setter
    def formato(self, valor: str) -> None:
        if valor.upper() not in FORMATOS_VALIDOS:
            raise ValueError(f"Formato inválido. Usa: {FORMATOS_VALIDOS}")
        self._formato = valor.upper()

    @property
    def tamano_mb(self) -> float:
        return self._tamano_mb

    @tamano_mb.setter
    def tamano_mb(self, valor: float) -> None:
        if valor <= 0:
            raise ValueError("El tamaño debe ser mayor a 0.")
        self._tamano_mb = valor

    @property
    def url_descarga(self) -> str:
        return self._url_descarga

    @url_descarga.setter
    def url_descarga(self, valor: str) -> None:
        if not valor.strip():
            raise ValueError("La URL no puede estar vacía.")
        self._url_descarga = valor.strip()

    def __str__(self) -> str:
        texto_base = super().__str__()
        return f"[eBook {self.formato} - {self.tamano_mb} MB] {texto_base}"

    def to_dict(self) -> dict:
        data = super().to_dict()
        data.update({
            "tipo": self.__class__.__name__.lower(),
            "formato": self.formato,
            "tamano_mb": self.tamano_mb,
            "url_descarga": self.url_descarga,
        })
        return data