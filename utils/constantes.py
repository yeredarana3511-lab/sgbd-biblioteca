# Límite máximo de libros en préstamo simultáneo para un estudiante
MAX_LIBROS_ALUMNO = 3
# Límite máximo de libros en préstamo simultáneo para un docente
MAX_LIBROS_PROFESOR = 5
# Costo de la penalización por cada día de retraso en la devolución (en pesos mexicanos)
MULTA_DIARIA_MXN = 15.00
# Formatos de material bibliográfico aceptados por el sistema
# Se usa una tupla ya que es inmutable (no debe modificarse durante la ejecución)
FORMATOS_VALIDOS = ("FISICO", "PDF", "EPUB")