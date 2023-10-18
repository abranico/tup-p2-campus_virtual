class Curso:
    def __init__(self, nombre: str, contrasenia_matriculacion: str):
        self.__nombre = nombre
        self.__contrasenia_matriculacion = contrasenia_matriculacion

    def __str__(self) -> str:
        return f"{self.nombre.title()}"

    def generar_contrasenia(self) -> str:
        pass

    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def contrasenia(self):
        return self.__contrasenia_matriculacion