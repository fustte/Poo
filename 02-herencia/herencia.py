class Animal:

    def __init__(self, nombre):
        self.nombre = nombre


class Mamifero(Animal):
    
    def __init__(self, nombre):
        super().__init(nombre)

class Ave(Animal):

    def __init__(self, nombre, color_plumas='blanco'):
        super().__init__(nombre)
        self.plumas = color_plumas

class Humano(Mamifero):

    def__init__(self, nombre):
    super().__init__(nombre, 2)
    self.apellido = ''
