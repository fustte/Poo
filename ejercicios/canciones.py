""""
Enunciado
Utilizando la clase Album del ejercicio 5, cambiar la lista de canciones para que, en lugar de tener una lista de tuplas, las canciones se guarden como objetos de la clase Cancion.

Define una clase Cancion que permita crear canciones con los atributos titulo y duracion. Para simplificar, la duración se guardará como una cadena de texto, por ejemplo, '3:15'

Modifica el método agregar_cancion para que permita agregar una canción como un objeto de tipo Cancion.

Comprueba que el parámetro recibido en el método agregar_cancion es de tipo Cancion. Si lo es, la canción se agregará a la lista de canciones del álbum, si no lo es se imprimirá un mensaje de error y se ignorará la acción.

Modifica el método mágico __str__ para obtener la información completa del disco fácilmente, pero usando ahora los objetos. Por ejemplo, el disco Born in the U.S.A. de Bruce Springsteen se mostrará de la siguiente manera:

Al imprimir por consola puedes utilizar la interpolación de datos en una cadena (string) usando el método .format() o la versión abreviada f'Cadena'.
Puedes utilizar la abreviatura \n para insertar un salto de línea dentro de una cadena.

Utiliza la función isinstance para hacer la comprobación del tipo de parámetro: https://docs.python.org/es/3/library/functi

"""

class Cancion:
    def __init__(self, titulo, duracion):
        self.titulo = titulo
        self.duracion = duracion

    def __str__(self):
        return f"{self.titulo} ({self.duracion})"

class Album:
    def __init__(self, titulo, fecha, interprete):
        self.titulo = titulo
        self.fecha = fecha
        self.interprete = interprete
        self.canciones = []

    def agregar_cancion(self, cancion):
        if isinstance(cancion, Cancion):
            self.canciones.append(cancion)
        else:
            print("Error: El parámetro debe ser un objeto de tipo Cancion.")

    def __str__(self):
        canciones_str = "\n".join(str(cancion) for cancion in self.canciones)
        return f"""
Álbum: {self.titulo}
Artista: {self.interprete}
Año: {self.fecha}
Canciones:
{canciones_str}
"""

# Ejemplo de uso:
cancion1 = Cancion("Born in the U.S.A.", "5:10")
cancion2 = Cancion("Dancing in the Dark", "4:05")

album = Album("Born in the U.S.A.", 1984, "Bruce Springsteen")
album.agregar_cancion(cancion1)
album.agregar_cancion(cancion2)

print(album)