from modelos.libro import Libro


def prueba_ordenamiento():
    inventario = [
        Libro("El Principito", "Saint-Exupéry", "9780306406157", 1943, "Infantil"),
        Libro("1984", "George Orwell", "9780306406157", 1949, "Distopía"),
        Libro("Cien Años de Soledad", "García Márquez", "9780306406157", 1967, "Ficción"),
        Libro("Dune", "Frank Herbert", "9780306406157", 1965, "Ciencia Ficción")
    ]

    print("--- ANTES DE ORDENAR ---")
    for libro in inventario:
        print(f"- {libro.titulo}")

    inventario_ordenado = sorted(inventario, key=lambda b: b.titulo)

    print("\n--- DESPUÉS DE ORDENAR ---")
    for libro in inventario_ordenado:
        print(f"- {libro.titulo}")


if __name__ == "__main__":
    prueba_ordenamiento()