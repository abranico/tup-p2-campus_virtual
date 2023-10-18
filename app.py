from estudiante import Estudiante
from profesor import Profesor
from funciones import *

profesores = [
    Profesor("Ingenieria en Sistemas", 2005, "Carlos",
             "González", "carlos@gmail.com", "contrasenia1"),
    Profesor("Ingenieria en Sistemas", 2010, "Laura",
             "Martínez", "laura@gmail.com", "contrasenia2"),
    Profesor("Ingenieria en Sistemas", 2008, "Eduardo",
             "López", "eduardo@gmail.com", "contrasenia3"),
    Profesor("Profesorado de Ingles", 2003, "Ana",
             "Pérez", "ana@gmail.com", "contrasenia4"),
    Profesor("Profesorado de Ingles", 2012, "Javier",
             "Rodríguez", "javier@gmail.com", "contrasenia5")
]

estudiantes = [
    Estudiante(1, 2022, "Mariano", "Gómez",
               "mariano@gmail.com", "contrasenia1"),
    Estudiante(2, 2021, "Sofía", "Martínez",
               "sofia@gmail.com", "contrasenia2"),
    Estudiante(3, 2020, "Juan", "Pérez", "juan@gmail.com", "contrasenia3"),
    Estudiante(4, 2019, "Valentina", "Rodríguez",
               "valentina@gmail.com", "contrasenia4"),
    Estudiante(5, 2018, "Facundo", "López",
               "facundo@gmail.com", "contrasenia5")
]


def menu_principal():
    print("---------- MENU ----------")
    print("1. Ingresar cómo alumno")
    print("2. Ingresar cómo profesor")
    print("3. Ver cursos")
    print("4. Salir")
    return int(input("Ingrese una opcion: "))


def menu_alumno():
    print("---------- MENU ----------")
    print("1. Matricularse a un curso")
    print("2. Ver curso")
    print("3. Volver al menú principal")
    return int(input("Ingrese una opcion: "))

def menu_profesor():
    print("---------- MENU ----------")
    print("1. Dictar curso")
    print("2. Ver curso")
    print("3. Volver al menu principal")
    return int(input("Ingrese una opcion: "))



while True:
    opcion = menu_principal()
    if opcion == 1:
        alumno = ingresar_como_alumno()
        if alumno:
            while True:
                opcion = menu_alumno()
                if opcion == 1:
                    print(alumno)
                elif opcion == 2:
                    print(alumno.contrasenia)
                elif opcion == 3:
                    break
                else:
                    print("Opcion incorrecta")
    elif opcion == 2:
        profesor=ingresar_como_profesor()
        if profesor:
            while True:
                opcion = menu_profesor()
                if opcion==1:
                    pass
                elif opcion==2:
                    pass
                elif opcion==3:
                    pass
    elif opcion == 3:
        ver_cursos()
    elif opcion == 4:
        break
    else:
        print("Opcion incorrecta")
