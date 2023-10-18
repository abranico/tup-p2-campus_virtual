import random, string


def ingresar_como_alumno(estudiantes):
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

def ingresar_como_profesor(profesores):
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

def ver_cursos(cursos):
    for curso in cursos:
        print(f"Materia: {curso}  Carrera: Tecnicatura Universitaria en Programación")

def nuevo_curso(cursos, Curso, profesor):
    nombre_curso= input("Ingrese nombre del curso nuevo: ")
    matriculacion = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(5))
    curso_nuevo=Curso(nombre_curso, matriculacion)
    cursos.append(curso_nuevo)
    profesor.dictar_curso(curso_nuevo)
    print("El curso se agrego exitosamente.")
    print(f"Nombre: {nombre_curso}")
    print(f"Contraseña: {matriculacion}")

def profesor_mostrar_cursos(profesor):
    print("\n")
    for indice,curso in enumerate(profesor.mis_cursos):
        print(f"{indice+1} - {curso}")




