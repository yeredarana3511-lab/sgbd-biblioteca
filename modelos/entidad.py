from abc import ABC, abstractmethod
from datetime import datetime
import uuid


class Entidad(ABC):
    """
    Clase base abstracta para todas las entidades del sistema.
    Define atributos comunes y métodos obligatorios.
    """

    def __init__(self) -> None:
        self._id: str = str(uuid.uuid4())
        self._fecha_creacion: datetime = datetime.now()

    @property
    def id(self) -> str:
        """Obtiene el identificador único."""
        return self._id

    @property
    def fecha_creacion(self) -> datetime:
        """Obtiene la fecha de creación."""
        return self._fecha_creacion

    @abstractmethod
    def __str__(self) -> str:
        """Devuelve una representación en texto."""
        pass

    @abstractmethod
    def to_dict(self) -> dict:
        """Convierte la entidad a diccionario."""
        pass