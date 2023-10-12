from abc import ABC, abstractmethod


class Usuario(ABC):
    def __init__(self, nombre: str, apellido: str, email: str, contrasenia: str):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__email = email
        self.__contrasenia = contrasenia

    def __str__(self) -> str:
        pass

    def validar_credenciales(self, email, contrasenia) -> bool:
        if self.__email == email and self.__contrasenia == contrasenia:
            return True
        else:
            return False
