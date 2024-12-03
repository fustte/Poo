
"""Enunciado
Crea una clase Triangulo que:

Se construya a partir del valor de sus tres ángulos
Los ángulos sean accesibles como atributos
Tenga un método comprobar_angulos que devuelva True si los ángulos son correctos (suman 180 grados)
 y False en caso contrario
 """

class Triangulo:
    def __init__(self, angulo1, angulo2, angulo3):
        self.angulo1 = angulo1
        self.angulo2 = angulo2
        self.angulo3 = angulo3
    
    def comprobar_angulos(self):
        return self.angulo1 + self.angulo2 + self.angulo3 == 180
    
    # comprobacion

triangulo = Triangulo(60, 60, 60)
print(f"Ángulos: {triangulo.angulo1}, {triangulo.angulo2}, {triangulo.angulo3}")
print(f"¿Ángulos correctos? {triangulo.comprobar_angulos()}")