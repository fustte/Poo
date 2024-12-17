"""
Ejercicio POO. Música
Enunciado
Vamos a crear una clase para almacenar información de un álbum o disco de música. PAra ello sigue los siguientes pasos:

Define una clase Album que permita crear discos de música con su los siguientes atributos:

titulo: Nombre del trabajo
fecha: Año de publicación del trabajo
interprete: Nombre del artista o del grupo que interpreta las canciones del disco

Inicialmente, al crear el disco, la lista de canciones estará vacía.

Crea un método agregar_canciones que permita agregar una canción con dos valores: la posición dentro del disco y su título. Las canciones se guardarán en la lista de canciones del álbum como una tupla (posicion, titulo).

Utiliza el método mágico __str__ para obtener la información completa del disco fácilmente. Por ejemplo, el disco Born in the U.S.A. de Bruce Springsteen se mostrará de la siguiente manera:

"""

class Album:
    def __init__(self, titulo, fecha, interprete):
        self.titulo = titulo
        self.fecha = fecha
        self.interprete = interprete
        self.canciones = []  # Lista vacía para almacenar las canciones

    def agregar_canciones(self, posicion, titulo):
        self.canciones.append((posicion, titulo))

    def __str__(self):
        canciones_str = "\n".join(f"{pos}. {titulo}" for pos, titulo in self.canciones)
        return f"""
Álbum: {self.titulo}
Artista: {self.interprete}
Año: {self.fecha}
Canciones:
{canciones_str}
"""
# Crear un nuevo álbum
album = Album("Born in the U.S.A.", 1984, "Bruce Springsteen")

# Agregar canciones
album.agregar_canciones(1, "Born in the U.S.A.")
album.agregar_canciones(2, "Dancing in the Dark")

# Imprimir la información del álbum
print(album)
