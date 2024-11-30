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

class Pelicula(show):
    def __init__(self, titulo):
        super().__init__(titulo)
        self.tipo = 'film'
        self.pases = []

    def agregar_pase(self, pase):
        self.pases.append(pase)

    def donde_la_veo(self):
        cines = {}
        for pase in self.pases:
            if pase.cine.nombre not in cines:
                cines[pase.cine.nombre] = []
            cines[pase.cine.nombre].append(pase.hora)
        return cines
    
class Pase:
    def __init__(self, cine, pelicula, hora):
        if not isinstance(cine, Cine):
            raise ValueError("El argumento cine debe ser una instancia de la lcase Cine")
        if not isinstance(pelicula, Pelicula):
            raise ValueError("El argumento pelicula debe ser una instancia de la clase pelicula")
        
        self.cine = cine
        self.pelicula = pelicula
        self.hora = hora
        cine.agregar_pase(self)
        pelicula.agregar_pase(self)

    def __str__(self):
        return f"Pase de '{self.pelicula.titulo}' en {self.cine.nombre} a las {self.hora}"
    
lista_cines = [
    
    Cine('Yelmo', 'CC Rincon de la Victoria'),
    Cine('Cinema', 'CC Rosaleda'),
    Cine('Albeniz', 'Málaga centro')

    ]

lista_peliculas = [

    Pelicula('Star Wars'),
    Pelicula('Avatar 2'),
    Pelicula('Wormwoos'),
    Pelicula('The Wire')

]

lista_pases = [

    Pase(lista_cines[0], lista_peliculas[0], '18:25'),
    Pase(lista_cines[0], lista_peliculas[1], '19:40'),
    Pase(lista_cines[1], lista_peliculas[3], '17:00'),
    Pase(lista_cines[1], lista_peliculas[2], '20:10'),
    Pase(lista_cines[2], lista_peliculas[0], '22:15'),

]

print(f"Cartelera de {lista_cines[0].nombre}:")
for pelicula, horas in lista_cines[0].ver_cartelera().items():
    print(f"{pelicula}:c{', '.join(horas)}")

print(f"\n¿Dónde se puede ver '{lista_peliculas[0].titulo}'?")
for cine, horas in lista_peliculas[0].donde_la_veo().items():
    print(f"{cine}: {', '.join(horas)}")
      
    
        
    






