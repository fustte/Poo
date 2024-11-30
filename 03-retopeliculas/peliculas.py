
from datetime import date

class Show:
    def __init__(self, titulo. tipo):
        self.titulo = titulo
        self.tipo = tipo
        self.terminada = False
        self.fecha_entrada = date.today()

    def marcar_terminada(self):
        self.terminada = True

    def marcar_terminada(self):
        self.terminada = True
    def __str__(self):
        return f"Títutlo: {self.titulo}\tTipo: {self.tipo}\tTerminada: {self.terminada}\tFecha de Entrada: {self.fecha_entrada}"
    
    mis_pelis = [

        show('Star Wars', 'film')
        show('Avatar 2', 'film')
        show('Wormwood', 'doc')
        show('the wire', 'serie')
    
    ]

for show in mis_pelis:
    if show.titulo == "The wire":
        show.marcar_terminada()



    