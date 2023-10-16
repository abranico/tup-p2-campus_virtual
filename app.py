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
    estudiante_actual = None
    email = input("Ingrese EMAIL: ")
    password = input("Ingrese CONTRASEÑA: ")
    for estudiante in estudiantes:
        if email == estudiante.email:
            estudiante_actual = estudiante
    if estudiante_actual:
        if estudiante_actual.validar_credenciales(email, password):
            return estudiante_actual
        else:
            print("ERROR DE INGRESO")
    else:
        print("Email incorrecto: Debe darse de alta en alumnado.")


def ingresar_como_profesor():
    pass


def ver_cursos():
    pass


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
        ingresar_como_profesor()
    elif opcion == 3:
        ver_cursos()
    elif opcion == 4:
        break
    else:
        print("Opcion incorrecta")
