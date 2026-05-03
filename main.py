import os

from modelos.libro_fisico import LibroFisico
from modelos.libro_digital import LibroDigital
from modelos.alumno import Alumno
from modelos.profesor import Profesor
from modelos.administrador import Administrador
from modelos.prestamo import Prestamo
from servicios.gestor_prestamos import realizar_prestamo
from servicios.persistencia import cargar_datos, guardar_datos
from utils.display import generar_reporte


RUTA_DATOS = "datos/biblioteca.json"


def seed_data() -> tuple:
    """Crea datos iniciales para probar el sistema."""
    libros = [
        LibroFisico("1984", "George Orwell", "9780451524935", 1949, "Distopía", "A1", 3),
        LibroFisico("Dune", "Frank Herbert", "9780306406157", 1965, "Ciencia Ficción", "B2", 2),
        LibroFisico("El Principito", "A. Saint-Exupéry", "9780156012195", 1943, "Infantil", "C3", 5),
        LibroDigital("Clean Code", "Robert C. Martin", "9780132350884", 2008, "Programación", "PDF", 5.0, "url/clean"),
        LibroDigital("Python Tricks", "Dan Bader", "9781775093305", 2017, "Tecnología", "EPUB", 2.5, "url/python"),
    ]

    usuarios = [
        Alumno("Ana Silva", "ana@edu.mx", "hash1", "Ingeniería", 5),
        Profesor("Dr. López", "lopez@edu.mx", "hash2", "Ciencias"),
        Administrador("Admin Root", "admin@edu.mx", "hash3", 5),
    ]

    prestamos = [
        Prestamo(usuarios[0], libros[0]),
        Prestamo(usuarios[1], libros[3]),
    ]

    return libros, usuarios, prestamos


def mostrar_menu() -> None:
    """Muestra el menú principal."""
    print("\n" + "=" * 35)
    print("📚 SISTEMA DE BIBLIOTECA SGBD")
    print("=" * 35)
    print("[1] Agregar libro")
    print("[2] Buscar libro")
    print("[3] Registrar usuario")
    print("[4] Prestar libro")
    print("[5] Devolver libro")
    print("[6] Ver reportes")
    print("[0] Salir")


def main() -> None:
    """Ejecuta el menú principal del sistema."""
    os.makedirs("datos", exist_ok=True)

    data = cargar_datos(RUTA_DATOS)
    libros = data.get("libros", [])
    usuarios = data.get("usuarios", [])
    prestamos = data.get("prestamos", [])

    if not libros:
        libros, usuarios, prestamos = seed_data()

    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")

        try:
            match opcion:
                case "1":
                    titulo = input("Título: ")
                    autor = input("Autor: ")
                    anio = int(input("Año: "))
                    genero = input("Género: ")
                    ubicacion = input("Ubicación: ")

                    libro = LibroFisico(
                        titulo,
                        autor,
                        "9780306406157",
                        anio,
                        genero,
                        ubicacion,
                        1,
                    )
                    libros.append(libro)
                    print("✅ Libro agregado.")

                case "2":
                    termino = input("Buscar por título: ").lower()
                    resultados = [
                        libro for libro in libros
                        if termino in libro.titulo.lower()
                    ]

                    if resultados:
                        for libro in resultados:
                            print("-", libro)
                    else:
                        print("❌ No se encontraron libros.")

                case "3":
                    nombre = input("Nombre: ")
                    email = input("Email: ")
                    carrera = input("Carrera: ")

                    usuario = Alumno(nombre, email, "hash_demo", carrera, 1)
                    usuarios.append(usuario)
                    print("✅ Usuario registrado.")

                case "4":
                    for i, usuario in enumerate(usuarios):
                        print(f"[{i}] {usuario}")

                    id_usuario = int(input("ID usuario: "))

                    for i, libro in enumerate(libros):
                        estado = "Disponible" if libro.disponible else "Prestado"
                        print(f"[{i}] {libro.titulo} - {estado}")

                    id_libro = int(input("ID libro: "))

                    prestamo = realizar_prestamo(
                        usuarios[id_usuario],
                        libros[id_libro],
                    )
                    prestamos.append(prestamo)
                    print("✅ Préstamo realizado.")

                case "5":
                    activos = [
                        prestamo for prestamo in prestamos
                        if getattr(prestamo, "activo", False)
                    ]

                    if not activos:
                        print("No hay préstamos activos.")
                        continue

                    for i, prestamo in enumerate(activos):
                        print(f"[{i}] {prestamo}")

                    seleccion = int(input("ID préstamo a devolver: "))
                    activos[seleccion].devolver()
                    print("✅ Libro devuelto.")

                case "6":
                    print(generar_reporte(libros + usuarios))

                case "0":
                    guardar_datos(RUTA_DATOS, libros, usuarios, prestamos)
                    print("👋 Datos guardados. Saliendo...")
                    break

                case _:
                    print("⚠️ Opción inválida.")

        except ValueError as error:
            print(f"❌ Error de valor: {error}")
        except KeyError as error:
            print(f"❌ Error de clave: {error}")
        except IndexError:
            print("❌ ID fuera de rango.")
        except Exception as error:
            print(f"❌ Error inesperado: {error}")


if __name__ == "__main__":
    main()