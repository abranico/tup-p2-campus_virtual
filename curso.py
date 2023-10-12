class Curso:
    def __init__(self, nombre: str, contrasenia_matriculacion: str):
        self.__nombre = nombre
        self.__contrasenia_matriculacion = contrasenia_matriculacion

    def __str__(self) -> str:
        pass

    def generar_contrasenia(self) -> str:
        pass
