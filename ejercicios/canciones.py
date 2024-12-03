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