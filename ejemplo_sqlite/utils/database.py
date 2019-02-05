
from .database_connection import DatabaseConnection

def crear_tabla():
    with DatabaseConnection("data.db") as connection:

        cursor = connection.cursor()

        cursor.execute(
        "CREATE TABLE IF NOT EXISTS libros(nombre text primary key, autor text, read integer)")

def agregar(nombre, autor):
    with DatabaseConnection("data.db") as connection:
        cursor = connection.cursor()

        cursor.execute("INSERT INTO libros VALUES(?,?,0)",(nombre,autor))

def devolver_libros():
    with DatabaseConnection("data.db") as connection:
        cursor=connection.cursor()
        cursor.execute("SELECT * FROM libros")

        libros = [{"nombre":row[0],"autor": row[1],"read":row[2]} for row in cursor.fetchall()]

        return libros


def marcar_libro_leido(nombre):
    with DatabaseConnection("data.db") as connection:
        cursor=connection.cursor()
        cursor.execute("UPDATE libros SET read=1 WHERE nombre=?",(nombre,))

def eliminar(nombre):
    with DatabaseConnection("data.db") as connection:
        cursor=connection.cursor()
        cursor.execute("DELETE FROM libros WHERE nombre=?",(nombre,))

