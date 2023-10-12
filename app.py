from estudiante import Estudiante
from profesor import Profesor

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


def ingresar_como_alumno():
    pass


def ingresar_como_profesor():
    pass


def ver_cursos():
    pass


while True:
    print("1. Ingresar cómo alumno")
    print("2. Ingresar cómo profesor")
    print("3. Ver cursos")
    print("4. Salir")
    opcion = int(input("Ingrese una opcion: "))
    if opcion == 1:
        ingresar_como_alumno()
    elif opcion == 2:
        ingresar_como_profesor()
    elif opcion == 3:
        ver_cursos()
    elif opcion == 4:
        break
    else:
        print("Opcion incorrecta")
