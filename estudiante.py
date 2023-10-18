from usuario import Usuario
from curso import Curso


class Estudiante(Usuario):
    def __init__(self, legajo: int, anio_inscripcion_carrera: int, nombre: str, apellido: str, email: str, contrasenia: str):
        super().__init__(nombre, apellido, email, contrasenia)
        self.__legajo = legajo
        self.__anio_inscripcion_carrera = anio_inscripcion_carrera
        self.__mis_cursos = []

    def __str__(self) -> str:
        pass

    def matricular_en_curso(self, curso: Curso):
        self.mis_cursos.append(curso)

    @property
    def mis_cursos(self)->list:
        return self.__mis_cursos
