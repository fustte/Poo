class Orquesta:

    def __init__(self):
        self.componentes = []  # lista de intrumentos
class Intrumento:
    pass


class Vientos(Instrumento):
    pass


class Percusion(Instrumento):
    pass


class Cuerda(Intrumento):
    pass


class Pulsada(Cuerda):
    pass


class Frotada(Cuerda):
    pass


class Golpeada(Cuerda):
    pass