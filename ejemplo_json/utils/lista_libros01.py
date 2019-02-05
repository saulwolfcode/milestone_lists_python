print("lista_libros01")

import json
archivo_libros = "libros.json"


def crear_tabla():
    with open(archivo_libros, "w") as file:
        json.dump([],file)


def agregar(nombre, autor):
    libros=devolver_libros()
    libros.append({"nombre":nombre,"autor":autor,"read":False})
    _guardar_libros(libros)

def devolver_libros():
    with open(archivo_libros, "r") as file:
        return json.load(file)

def _guardar_libros(libros):
    with open(archivo_libros, "w") as file:
        json.dump(libros,file)

def marcar_libro_leido(nombre):
    libros = devolver_libros()
    for libro in libros:
        if libro["nombre"] == nombre:
            libro["read"] = True
    _guardar_libros(libros)

def eliminar(nombre):
    libros = devolver_libros()
    libros = [libro for libro in libros if libro["nombre"] != nombre]
    _guardar_libros(libros)
