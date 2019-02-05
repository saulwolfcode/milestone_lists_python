print("lista_libros01")

archivo_libros = "libros.txt"


def crear_tabla():
    with open(archivo_libros, "w") as file:
        pass


def agregar(nombre, autor):
    with open(archivo_libros, "a") as file:
        file.write(f"{nombre},{autor},0\n")


def devolver_libros():
    with open(archivo_libros, "r") as file:
        lines = [line.strip().split(",") for line in file.readlines()]
        return [
            {"nombre": line[0], "autor": line[1], "read": line[2]}
            for line in lines
        ]


def _guardar_libros(libros):
    with open(archivo_libros, "w") as file:
        for libro in libros:
            file.write(f"{libro['nombre']},{libro['autor']},{libro['read']}\n")


def marcar_libro_leido(nombre):
    libros = devolver_libros()
    for libro in libros:
        if libro["nombre"] == nombre:
            libro["read"] = "1"
    _guardar_libros(libros)


def eliminar(nombre):
    libros = devolver_libros()
    libros = [libro for libro in libros if libro["nombre"] != nombre]
    _guardar_libros(libros)
