from modelos.libro import Libro
from modelos.libro_digital import LibroDigital
from modelos.libro_fisico import LibroFisico
from modelos.alumno import Alumno
from modelos.profesor import Profesor
from modelos.administrador import Administrador
from utils.display import mostrar_info, generar_reporte



def probar_polimorfismo() -> None:
    elementos = [
        Libro("El Principito", "A. Saint-Exupéry", "9780156012195", 1943, "Infantil"),

        LibroDigital(
            "Python Avanzado",
            "Luciano R.",
            "9781491946008",
            2015,
            "Programación",
            "PDF",
            12.5,
            "http://dl.com/py"
        ),

        LibroFisico(
            "Dune",
            "Frank Herbert",
            "9780306406157",
            1965,
            "Ciencia Ficción",
            "Sección B",
            4
        ),

        Alumno(
            "Laura Gómez",
            "laura@edu.mx",
            "hash123",
            "Medicina",
            3
        ),

        Profesor(
            "Dr. Arturo",
            "arturo@edu.mx",
            "hash456",
            "Matemáticas"
        ),

        Administrador(
            "Admin Root",
            "admin@edu.mx",
            "hash789",
            5
        ),
    ]

    print("=== PRUEBA DE POLIMORFISMO ===\n")

    for item in elementos:
        mostrar_info(item)

    print("\n=== REPORTE ===\n")
    print(generar_reporte(elementos))


if __name__ == "__main__":
    probar_polimorfismo()