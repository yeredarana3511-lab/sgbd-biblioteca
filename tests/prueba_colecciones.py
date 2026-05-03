from collections import deque, Counter, defaultdict


def prueba_colecciones():
    print("=== LISTA ===")
    catalogo = ["1984", "Dune"]
    catalogo.append("El Principito")
    print(catalogo)

    print("\n=== TUPLA ===")
    FORMATOS_VALIDOS = ("PDF", "EPUB", "MOBI")
    print(FORMATOS_VALIDOS)

    print("\n=== DICCIONARIO ===")
    usuarios = {
        "1001": "Ana",
        "1002": "Luis"
    }
    print(usuarios["1001"])

    print("\n=== SET ===")
    generos = ["Ficción", "Terror", "Ficción"]
    generos_unicos = set(generos)
    print(generos_unicos)

    print("\n=== DEQUE (COLA) ===")
    cola = deque(["Carlos", "Laura"])
    cola.append("Mario")
    print("Atendido:", cola.popleft())
    print("Cola actual:", list(cola))

    print("\n=== COUNTER ===")
    libros = ["1984", "Dune", "1984", "El Principito"]
    conteo = Counter(libros)
    print(conteo)
    print("Más frecuente:", conteo.most_common(1))

    print("\n=== DEFAULTDICT ===")
    deudas = defaultdict(float)
    deudas["Ana"] += 15.0
    deudas["Luis"] += 10.0
    print(dict(deudas))


if __name__ == "__main__":
    prueba_colecciones()