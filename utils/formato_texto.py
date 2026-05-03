import unicodedata

def normalizar_titulo(titulo: str) -> str:
    """
    Normaliza el título de un libro eliminando caracteres no válidos,
    espacios extra y capitalizando cada palabra.
    """
    caracteres_validos = []
    for char in titulo:
        if char.isalnum() or char.isspace() or char == ',':
            caracteres_validos.append(char)
            
    titulo_filtrado = "".join(caracteres_validos)
    
    palabras = titulo_filtrado.split()
    
    palabras_formateadas = [palabra.capitalize() for palabra in palabras]
    
    titulo_final = " ".join(palabras_formateadas)
    
    return titulo_final


def generar_slug(texto: str) -> str:
    """
    Genera un slug limpio a partir de un texto.
    """
    texto = texto.lower()
    
    texto_normalizado = unicodedata.normalize('NFKD', texto)
    texto_sin_acentos = texto_normalizado.encode('ascii', 'ignore').decode('utf-8')
    
    caracteres_limpios = []
    for char in texto_sin_acentos:
        if char.isalnum():
            caracteres_limpios.append(char)
        else:
            caracteres_limpios.append(' ')
            
    texto_crudo = "".join(caracteres_limpios)
    
    slug_final = "-".join(texto_crudo.split())
    
    return slug_final


def formatear_reporte_libro(libro_dict: dict) -> str:
    """
    Genera un reporte en texto plano de un libro.
    """
    reporte = f"""\
=============================================
             FICHA BIBLIOGRÁFICA             
=============================================
{'Título:':<10} {libro_dict.get('titulo', 'No especificado')}
{'Autor:':<10} {libro_dict.get('autor', 'No especificado')}
{'ISBN:':<10} {libro_dict.get('isbn', 'No especificado')}
{'Año:':<10} {libro_dict.get('año', 'No especificado')}
{'Género:':<10} {libro_dict.get('genero', 'No especificado')}
============================================="""
    return reporte


def buscar_en_texto(haystack: str, needle: str) -> bool:
    """
    Busca si un texto está dentro de otro ignorando mayúsculas/minúsculas.
    """
    texto_principal_min = haystack.lower()
    busqueda_min = needle.lower()
    
    return busqueda_min in texto_principal_min