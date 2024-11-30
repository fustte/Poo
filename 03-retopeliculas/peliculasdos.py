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

    def __str__(self):
        return f"{self.nombre} ({self.direccion})"

    def agregar_pase(self, pase):
        self.pases.append(pase)

    def ver_cartelera(self):
        cartelera = {}
        for pase in self.pases:
            if pase.pelicula.titulo not in cartelera:
                cartelera[pase.pelicula.titulo] = []
            cartelera[pase.pelicula.titulo].append(pase.hora)
        return cartelera
    
       

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