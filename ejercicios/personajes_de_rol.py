"""
Ejercicio POO. **Personajes de rol
Enunciado
Estás creando un programa que te ayude a ser el DM de una partida de rol.

Define una clase Personaje que permita crear personajes con sus características principales. La clase debe tener los siguientes atributos:

nombre: Nombre del personaje
fuerza: Número entre 0 y 20
destreza: Número entre 0 y 20
raza: una cadena con uno de los valores "elfo", "enano", "gnomo" o "humano"
jugador: Nombre del jugador al que pertenece el personaje

  Puedes crear un personaje solamente sabiendo el nombre, la raza y el jugador. Por defecto, la fuerza y la destreza serán cero.

Crea un método generar que permita establecer un valor para la fuerza y la destreza de forma aleatoria entre 3 y 17.

Crea un método que permita realizar un combate entre dos personajes. El combate se funciona de la siguiente manera:

  
El personajeA ataca al personajeB, se invoca el método ataca del personajeA.
Se lanza un dado de 20 (es decir, obtienes un número aleatorio entre 1 y 20).
Si sale 20 el personajeA gana automáticamente.
Si sale 1 el personajeB gana automáticamente.
En otro caso, se suma el valor de la fuerza y la destreza al valor obtenido. Esta será la puntuación del personajeA
Se lanza de nuevo un dado de 20 y el valor se suma con la fuerza y la destreza del personajeB.
Gana el personaje con mayor puntuación. Si ambas puntuaciones son iguales, pierde el atacante.
El método devuelve True si gana el personajeA y False si gana el personajeB.

Crea un personaje Elfo para ti de nombre Angrod y establece la fuerza y la destreza de forma aleatoria
Crea un personaje Enano para tu mejor amigo llamado Brokk y establece su fuerza en 15 y la destreza en 12
Haz que el elfo ataque al enano ¿quién gana?
tonybolanyo — 21/10/24, 19:29
Ayuda a la implementación
Números aleatorios: utiliza la función random.randint(a,b) para generar un números enteros aleatorios entre dos valores dados. Ref. https://docs.python.org/3/library/random.html?highlight=randint#random.randint
Python documentation
random — Generate pseudo-random numbers
Source code: Lib/random.py This module implements pseudo-random number generators for various distributions. For integers, there is uniform selection from a range. For sequences, there is uniform s...






"""

import random

class Personaje:
    def __init__(self, nombre, raza, jugador):
        self.nombre = nombre
        self.fuerza = 0
        self.destreza= 0
        self.raza = raza
        self.jugador = jugador

    def generar(self):
        self.fuerza = random.randint(3, 17)
        self.destreza = random.randint(3, 17)

    def ataca(self, otro_personaje):
        dado_a = random.randint(1, 20)
        if dado_a == 20:
            return True
        elif dado_a == 1:
            return False
        
        puntuacion_a = dado_a + self.fuerza + self.destreza

        dado_b = random.randint(1, 20)
        puntuacion_b = dado_b + otro_personaje.fuerza + otro_personaje.destreza

        if puntuacion_a > puntuacion_b:
            return True
        else:
            return False
        
    def __str__(self):
        return f"{self.nombre} (Raza: {self.raza}, Jugador: {self.jugador}, Fuerza: {self.fuerza}, Destreza: {self.destreza})"


angrod = Personaje("Angrod", "elfo", "DM")
brokk = Personaje("Brokk", "enano", "Amigo")

angrod.generar()

brokk.fuerza = 15
brokk.destreza = 12

print("Antes del combate:")
print(angrod)
print(brokk)

resultado = angrod.ataca(brokk)
ganador = angrod.nombre if resultado else brokk.nombre

print("\nResultado del combate:")
print(f"{angrod.nombre} ataca a {brokk.nombre}")
print(f"El ganador es: {ganador}")