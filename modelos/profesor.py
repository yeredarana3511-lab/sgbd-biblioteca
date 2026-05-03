from modelos.usuario import Usuario


class Profesor(Usuario):
    """
    Representa a un profesor dentro del sistema de biblioteca.
    """

    max_libros: int = 8

    def __init__(
        self,
        nombre: str,
        email: str,
        contrasena_hash: str,
        departamento: str,
    ) -> None:
        super().__init__(nombre, email, contrasena_hash)
        self.departamento = departamento
        self.libros_actualmente_prestados: int = 0

    @property
    def departamento(self) -> str:
        return self._departamento

    @departamento.setter
    def departamento(self, valor: str) -> None:
        if not valor.strip():
            raise ValueError("El departamento no puede estar vacío.")
        self._departamento = valor.strip()

    def puede_pedir_prestado(self) -> bool:
        """
        Indica si el profesor aún puede pedir libros prestados.
        """
        return self.libros_actualmente_prestados < self.max_libros

    def to_dict(self) -> dict:
        """
        Convierte el profesor a diccionario.
        """
        return {
            "id": self.id,
            "fecha_creacion": self.fecha_creacion.isoformat(),
            "rol": self.__class__.__name__.lower(),
            "nombre": self.nombre,
            "email": self.email,
            "departamento": self.departamento,
            "libros_prestados": self.libros_actualmente_prestados,
            "max_libros": self.max_libros,
        }

    def __str__(self) -> str:
        """
        Devuelve una representación del profesor.
        """
        return f"[Profesor] {self.nombre} - Depto. de {self.departamento}"