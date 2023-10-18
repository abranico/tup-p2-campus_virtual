class Curso:
    def __init__(self, nombre: str, contrasenia_matriculacion: str):
        self.__nombre = nombre
        self.__contrasenia_matriculacion = Curso.generar_contrasenia()

    def __str__(self) -> str:
        return f"{self.nombre}"
    @classmethod
    def generar_contrasenia(cls) -> str:
        return "a"

    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def contrasenia(self):
        return self.__contrasenia_matriculacion