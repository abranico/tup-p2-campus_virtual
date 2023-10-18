from usuario import Usuario
from curso import Curso


class Profesor(Usuario):
    def __init__(self, titulo: str, anio_egreso: int, nombre: str, apellido: str, email: str, contrasenia: str):
        super().__init__(nombre, apellido, email, contrasenia)
        self.__titulo = titulo
        self.__anio_egreso = anio_egreso
        self.__mis_cursos = []

    def __str__(self) -> str:
        pass

    def dictar_curso(self, curso: Curso):
        self.__mis_cursos.append(curso)
    
    @property
    def mis_cursos(self)->list:
        return self.__mis_cursos
