from app import estudiantes, profesores, cursos

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
    profesor_actual = None
    email= input("Ingrese EMAIL: ")
    password= input("Ingrese CONTRASEÑA: ")
    for profesor in profesores:
        if email== profesor.email:
            profesor_actual=profesor
    if profesor_actual:
        if profesor_actual.validar_credenciales(email,password):
            return profesor_actual
        else:
            print("ERROR DE INGRESO")
    else:
        print("Email incorrecto: Debe darse de alta en alumnado.")




def ver_cursos():
    for curso in cursos:
        print(f"Materia: {curso}  Carrera: Tecnicatura Universitaria en Programación")


ver_cursos()
