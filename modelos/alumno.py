from modelos.usuario import Usuario


class Alumno(Usuario):
    """
    Representa a un alumno dentro del sistema de biblioteca.
    """

    max_libros: int = 3

    def __init__(
        self,
        nombre: str,
        email: str,
        contrasena_hash: str,
        carrera: str,
        semestre: int,
    ) -> None:
        super().__init__(nombre, email, contrasena_hash)
        self.carrera = carrera
        self.semestre = semestre
        self.libros_actualmente_prestados: int = 0

    @property
    def carrera(self) -> str:
        return self._carrera

    @carrera.setter
    def carrera(self, valor: str) -> None:
        if not valor.strip():
            raise ValueError("La carrera no puede estar vacía.")
        self._carrera = valor.strip()

    @property
    def semestre(self) -> int:
        return self._semestre

    @semestre.setter
    def semestre(self, valor: int) -> None:
        if valor < 1:
            raise ValueError("El semestre debe ser 1 o mayor.")
        self._semestre = valor

    def puede_pedir_prestado(self) -> bool:
        """
        Indica si el alumno aún puede pedir libros prestados.
        """
        return self.libros_actualmente_prestados < self.max_libros

    def to_dict(self) -> dict:
        """
        Convierte el alumno a diccionario.
        """
        return {
            "id": self.id,
            "fecha_creacion": self.fecha_creacion.isoformat(),
            "rol": self.__class__.__name__.lower(),
            "nombre": self.nombre,
            "email": self.email,
            "carrera": self.carrera,
            "semestre": self.semestre,
            "libros_prestados": self.libros_actualmente_prestados,
            "max_libros": self.max_libros,
        }

    def __str__(self) -> str:
        """
        Devuelve una representación del alumno.
        """
        return (
            f"[Alumno] {self.nombre} - {self.carrera}, "
            f"semestre {self.semestre}"
        )