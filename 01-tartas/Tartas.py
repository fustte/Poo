#Tartas

"""
Ejercicio 1. Tartas
Enunciado
Como se acerca mi cumpleaños, estoy tratando de hacer varias tartas para ver cuál me gusta más. Crea una clase Tarta que permita almacenar el sabor y una puntuación de 0 a 5.

Ayuda a la implementación
Para crear la tarta solamente es necesario identificar el sabor. La puntuación inicial será 0 y se puede modificar una vez creada la tarta mediante un atributo.

Puedes comprobar si una tarta te gusta más que otra comparando los valores de sus atributos puntuacion.

Segunda parte (extra)
Crea una lista con cinco tartas.
Da a cada una una puntuación.
Haz una función que tomando la lista de tartas devuelva la tarta con mayor pountuación
 
"""


class Tarta:
    def __init__(self, sabor):
        self.sabor = sabor
        self.puntuacion = 0  # Puntuación inicial es 0

    def __lt__(self, other):
        return self.puntuacion < other.puntuacion

# Ejemplo
tarta_chocolate = Tarta("chocolate")
print(tarta_chocolate.sabor)  # Salida: chocolate
print(tarta_chocolate.puntuacion)  # Salida: 0


# Tartas con sus sabores
tartas = [
    Tarta("chocolate"),
    Tarta("vainilla"),
    Tarta("fresa"),
    Tarta("limón"),
    Tarta("manzana")
]

# Puntuaciones de cada tarta
tartas[0].puntuacion = 5
tartas[1].puntuacion = 3
tartas[2].puntuacion = 4
tartas[3].puntuacion = 2
tartas[4].puntuacion = 5

# Función para encontrar la tarta con mayor puntuación
def mejor_tarta(tartas):
    return max(tartas, key=lambda tarta: tarta.puntuacion)

# Ejemplo de uso
tarta_favorita = mejor_tarta(tartas)
print(f"La mejor tarta es de {tarta_favorita.sabor} con una puntuación de {tarta_favorita.puntuacion}")
