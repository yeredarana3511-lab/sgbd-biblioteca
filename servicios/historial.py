from typing import List, Optional


class Historial:
    """
    Gestiona el historial de acciones usando una pila (LIFO).
    """

    def __init__(self) -> None:
        self._pila: List[str] = []

    def agregar_accion(self, accion: str) -> None:
        self._pila.append(accion)

    def deshacer_ultima(self) -> Optional[str]:
        if not self._pila:
            return None
        return self._pila.pop()

    def ver_historial(self) -> List[str]:
        return self._pila.copy()