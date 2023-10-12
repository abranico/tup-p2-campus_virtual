from usuario import Usuario
from curso import Curso


class Profesor(Usuario):
    def __init__(self, titulo: str, anio_egreso: int, nombre: str, apellido: str, email: str, contrasenia: str):
        super().__init__(nombre, apellido, email, contrasenia)
        self.__titulo = titulo
        self.__anio_egreso = anio_egreso

    def __str__(self) -> str:
        pass

    def dictar_curso(self, curso: Curso):
        pass
