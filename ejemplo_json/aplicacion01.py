print("aplicacion01")

from utils import lista_libros01

USUARIO_ELECCION = """
    Ingresar:
        "a" agregue un nuevo libro
        "l"   lista de libros
        "m"  ingrese libro leido
        "b"  borre si desea un leido
        "s"   salir del programa
    Su eleccion es: """


def menu():
    lista_libros01.crear_tabla()
    usuario_ingreso = input(USUARIO_ELECCION)
    while usuario_ingreso != "s":
        if usuario_ingreso == "a":
            agregar_libro()
        elif usuario_ingreso == "l":
            lista_libro()
        elif usuario_ingreso == "m":
            leido_libro()
        elif usuario_ingreso == "b":
            borrar_libro()
        else:
            print("Por favor intente nuevamente los datos ingresado no son correctos")
        usuario_ingreso = input(USUARIO_ELECCION)


def agregar_libro():
    nombre = input("NOMBRE LIBRO NUEVO: ")
    autor = input("NOMBRE DEL AUTOR LIBRO: ")

    lista_libros01.agregar(nombre, autor)


def lista_libro():
    libros = lista_libros01.devolver_libros()
    for libro in libros:
        read = "LEIDO" if libro["read"] else "FALTA LEER"
        print(f"el nombre es {libro['nombre']} y el autor es {libro['autor']}, leido: {read}")


def leido_libro():
    nombre = input("INGRESE NOMBRE LIBRO LEIDO: ")
    lista_libros01.marcar_libro_leido(nombre)


def borrar_libro():
    nombre = input("BORRAR LIBRO DE LISTA NOMBRE: ")
    lista_libros01.eliminar(nombre)

menu()
