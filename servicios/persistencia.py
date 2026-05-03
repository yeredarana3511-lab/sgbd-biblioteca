import json
import os
from typing import Any, Dict, List

from modelos.libro_fisico import LibroFisico
from modelos.libro_digital import LibroDigital
from modelos.alumno import Alumno
from modelos.profesor import Profesor
from modelos.administrador import Administrador


def guardar_datos(
    ruta: str,
    libros: List[Any],
    usuarios: List[Any],
    prestamos: List[Any],
) -> None:
    """Guarda los datos del sistema en un archivo JSON."""
    datos = {
        "libros": [libro.to_dict() for libro in libros],
        "usuarios": [usuario.to_dict() for usuario in usuarios],
        "prestamos": [
            {
                "usuario": prestamo.usuario.nombre,
                "libro": prestamo.libro.titulo,
                "activo": prestamo.activo,
            }
            for prestamo in prestamos
        ],
    }

    try:
        with open(ruta, "w", encoding="utf-8") as archivo:
            json.dump(datos, archivo, indent=4, ensure_ascii=False)
        print(f"[OK] Datos guardados en {ruta}")
    except IOError as error:
        print(f"[ERROR] No se pudo guardar: {error}")


def cargar_datos(ruta: str) -> Dict[str, List[Any]]:
    """Carga datos desde JSON y reconstruye objetos básicos."""
    vacio = {"libros": [], "usuarios": [], "prestamos": []}

    if not os.path.exists(ruta):
        return vacio

    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            data = json.load(archivo)
    except json.JSONDecodeError:
        print("[ERROR] El archivo JSON está corrupto.")
        return vacio
    except IOError as error:
        print(f"[ERROR] No se pudo leer el archivo: {error}")
        return vacio

    libros = []

    for item in data.get("libros", []):
        try:
            tipo = item.get("tipo", "")
            titulo = item.get("titulo", "Sin título")
            autor = item.get("autor", "Anónimo")
            isbn = item.get("isbn", "9780306406157")
            anio = item.get("anio", 2000)
            genero = item.get("genero", "General")

            if tipo == "librofisico":
                libro = LibroFisico(
                    titulo,
                    autor,
                    isbn,
                    anio,
                    genero,
                    item.get("ubicacion", "Estante 1"),
                    item.get("num_ejemplares", 1),
                )
            elif tipo == "librodigital":
                libro = LibroDigital(
                    titulo,
                    autor,
                    isbn,
                    anio,
                    genero,
                    item.get("formato", "PDF"),
                    item.get("tamano_mb", 1.0),
                    item.get("url_descarga", "http://biblioteca.com"),
                )
            else:
                continue

            if "disponible" in item:
                libro.disponible = item["disponible"]

            libros.append(libro)

        except ValueError as error:
            print(f"[Ignorado] Libro corrupto: {error}")

    usuarios = []

    for item in data.get("usuarios", []):
        try:
            rol = item.get("rol", "")
            nombre = item.get("nombre", "Usuario")
            email = item.get("email", "test@edu.mx")

            if rol == "alumno":
                usuario = Alumno(
                    nombre,
                    email,
                    "hash_bd",
                    item.get("carrera", "General"),
                    item.get("semestre", 1),
                )
            elif rol == "profesor":
                usuario = Profesor(
                    nombre,
                    email,
                    "hash_bd",
                    item.get("departamento", "General"),
                )
            elif rol == "administrador":
                usuario = Administrador(
                    nombre,
                    email,
                    "hash_bd",
                    item.get("nivel_acceso", 1),
                )
            else:
                continue

            if "libros_prestados" in item:
                usuario.libros_actualmente_prestados = item["libros_prestados"]

            usuarios.append(usuario)

        except ValueError as error:
            print(f"[Ignorado] Usuario corrupto: {error}")

    return {
        "libros": libros,
        "usuarios": usuarios,
        "prestamos": data.get("prestamos", []),
    }