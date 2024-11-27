class Orquesta:

    def __init__(self):
        self.componentes = []  # lista de intrumentos

    def agregarInstrumento(self, instrumento):
        if not isinstance(instrumento, Instrumento):
            raise TypeError(f'{instrumento} no es un instrumento')
        


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