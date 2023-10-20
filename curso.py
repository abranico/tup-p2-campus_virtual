import random
import string


class Curso:
    def __init__(self, nombre: str, contrasenia_matriculacion=None):
        self.__nombre = nombre

        if contrasenia_matriculacion is None:
            contrasenia_matriculacion = Curso.generar_contrasenia()
        self.__contrasenia_matriculacion = contrasenia_matriculacion

    def __str__(self) -> str:
        return f"{self.nombre}"

    @classmethod
    def generar_contrasenia(cls) -> str:
        return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(5))

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    @property
    def contrasenia(self):
        return self.__contrasenia_matriculacion

    @contrasenia.setter
    def contrasenia(self, nueva_contrasenia):
        self.__contrasenia_matriculacion = nueva_contrasenia
