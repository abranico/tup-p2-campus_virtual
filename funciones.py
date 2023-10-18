import random
import string


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
    email = input("Ingrese EMAIL: ")
    password = input("Ingrese CONTRASEÑA: ")
    for profesor in profesores:
        if email == profesor.email:
            profesor_actual = profesor
    if profesor_actual:
        if profesor_actual.validar_credenciales(email, password):
            return profesor_actual
        else:
            print("ERROR DE INGRESO")
    else:
        print("Email incorrecto: Debe darse de alta en alumnado.")


def ver_cursos(cursos):
    for curso in cursos:
        print(
            f"Materia: {curso} Carrera: Tecnicatura Universitaria en Programación")


def nuevo_curso(cursos, Curso, profesor):
    nombre_curso = input("Ingrese nombre del curso nuevo: ")
    matriculacion = ''.join(random.choice(
        string.ascii_letters + string.digits) for _ in range(5))
    curso_nuevo = Curso(nombre_curso, matriculacion)
    cursos.append(curso_nuevo)
    profesor.dictar_curso(curso_nuevo)
    print("El curso se agrego exitosamente.")
    print(f"Nombre: {nombre_curso}")
    print(f"Contraseña: {matriculacion}")


def profesor_mostrar_cursos(profesor):
    print("\n")
    if len(profesor.mis_cursos) > 0:
        for indice, curso in enumerate(profesor.mis_cursos):
            print(f"{indice+1} - {curso}")
        seleccion = int(input("Seleccione un curso: "))
        if seleccion > 0 and seleccion <= len(profesor.mis_cursos):
            for curso in profesor.mis_cursos:
                if curso.nombre == profesor.mis_cursos[seleccion-1].nombre:
                    print(f"Nombre: {curso.nombre}")
                    print(f"Contraseña: {curso.contrasenia}")
        else:
            print("Curso inexistente.")
    else:
        print("No hay cursos para mostrar")


def matricularse_alumno(cursos, alumno):
    print("\n")
    encontrado = False
    for indice, curso in enumerate(cursos):
        print(f"{indice+1} - {curso}")

    seleccion = int(input("Seleccione un curso: "))
    if seleccion > 0 and seleccion <= len(cursos):
        for curso in alumno.mis_cursos:
            if curso.nombre == cursos[seleccion-1].nombre:
                print("El alumno ya se encuentra matriculado.")
                encontrado = True
        if not encontrado:
            matriculacion = input("Ingrese la clave de matriculacion: ")
            if matriculacion == cursos[seleccion-1].contrasenia:
                alumno.matricular_en_curso(cursos[seleccion-1])
            else:
                print("Clave de matriculacion incorrecta.")

    else:
        print("Curso inexistente.")


def alumno_mostrar_curso(alumno):
    print("\n")
    if len(alumno.mis_cursos) > 0:
        for indice, curso in enumerate(alumno.mis_cursos):
            print(f"{indice+1} - {curso}")

        seleccion = int(input("Seleccione un curso: "))
        if seleccion > 0 and seleccion <= len(alumno.mis_cursos):
            for curso in alumno.mis_cursos:
                if curso.nombre == alumno.mis_cursos[seleccion-1].nombre:
                    print(f"Nombre: {curso.nombre}")
                    print(f"Contraseña: {curso.contrasenia}")
        else:
            print("Curso inexistente.")
    else:
        print("No hay cursos para mostrar")
