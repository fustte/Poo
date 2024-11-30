from datetime import date

class show:
    def __init__(self, titulo, tipo):
        self.titulo = titulo
        self.tipo = tipo
        self.terminada = False
        self.fecha_entrada = date.today()

    def marcar_terminada(self):
        self.terminada = True

    
    def __str__(self):
        vista = "Si" if self.terminada else "No"
        return f"Títutlo: {self.titulo}\tTipo: {self.tipo}\tVisto: {vista}\tFecha de Entrada: {self.fecha_entrada}"
    
class Cine:
    def __init__(self, nombre, direccion):
        self.nombre = nombre
        self.direccion = direccion
        self.pases = []

    



mis_pelis = [

        show('Star Wars', 'film'),
        show('Avatar 2', 'film'),
        show('Wormwood', 'doc'),
        show('The Wire', 'serie')
    
    ]

for show in mis_pelis:
    if show.titulo == "The Wire":
        show.marcar_terminada()

for show in mis_pelis: