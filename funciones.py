from app import estudiantes, profesores


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
