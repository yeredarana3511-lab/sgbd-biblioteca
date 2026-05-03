from typing import Any, List


def mostrar_info(item: Any) -> None:
    """
    Muestra la información de cualquier objeto usando su método __str__.
    """
    print(f"Información del elemento: {str(item)}")

def generar_reporte(items: List[Any]) -> str:
    reporte = "=== REPORTE DEL SISTEMA ===\n"

    for i, item in enumerate(items, 1):
        try:
            data = item.to_dict()

            reporte += f"\n[Elemento {i}]\n"

            for clave, valor in data.items():
                reporte += f"  {clave.capitalize()}: {valor}\n"

        except AttributeError:
            reporte += f"\n[Elemento {i}]\n"
            reporte += f"  ERROR: {type(item).__name__} no tiene to_dict()\n"

    return reporte