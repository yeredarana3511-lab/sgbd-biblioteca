from collections import deque
from typing import Optional, Tuple, List

from modelos.usuario import Usuario
from modelos.libro import Libro


class GestorCola:
    """
    Gestiona la lista de espera de libros (FIFO).
    """

    def __init__(self) -> None:
        self._cola = deque()  # 👈 sin tipo explícito aquí

    def encolar_solicitud(self, usuario: Usuario, libro: Libro) -> None:
        self._cola.append((usuario, libro))

    def atender_siguiente(self) -> Optional[Tuple[Usuario, Libro]]:
        if not self._cola:
            return None
        return self._cola.popleft()

    def ver_cola(self) -> List[Tuple[Usuario, Libro]]:
        return list(self._cola)