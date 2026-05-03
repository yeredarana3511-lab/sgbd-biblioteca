from collections import Counter, defaultdict
from typing import Dict, List, Tuple

from modelos.prestamo import Prestamo


def libro_mas_prestado(prestamos: List[Prestamo]) -> Tuple[str, int]:
    """Devuelve el título del libro más prestado y su cantidad."""
    if not prestamos:
        return ("Ninguno", 0)

    titulos = (prestamo.libro.titulo for prestamo in prestamos)
    return Counter(titulos).most_common(1)[0]


def usuario_con_mas_prestamos(prestamos: List[Prestamo]) -> Tuple[str, int]:
    """Devuelve el usuario con más préstamos y su cantidad."""
    if not prestamos:
        return ("Nadie", 0)

    nombres = (prestamo.usuario.nombre for prestamo in prestamos)
    return Counter(nombres).most_common(1)[0]


def distribucion_por_genero(prestamos: List[Prestamo]) -> Dict[str, int]:
    """Cuenta préstamos agrupados por género del libro."""
    distribucion = defaultdict(int)

    for prestamo in prestamos:
        distribucion[prestamo.libro.genero] += 1

    return dict(distribucion)


def multa_promedio(multas_cobradas: List[float]) -> float:
    """Calcula el promedio de multas cobradas."""
    if not multas_cobradas:
        return 0.0

    return round(sum(multas_cobradas) / len(multas_cobradas), 2)