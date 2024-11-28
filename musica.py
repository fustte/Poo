
class Orquesta:

    def __init__(self):
        self.componentes = []  # lista de intrumentos

    def agregarInstrumento(self, instrumento):
        if not isinstance(instrumento, Instrumento):
            raise TypeError(f'{instrumento} no es un instrumento')
        self.componentes.append(instrumento)

    def listarInstrumentos(self):
        for instrumento in self.componentes:
            print(instrumento)

class Instrumento:

    def __init__(self, nombre):
        self.nombre = nombre
        self.sonido = None

    def sonar(self):
        if self.sonido:
            print('self.sonido') 
        else:
            print('silencio')

    def __str__(self):
        return self.nombre


class Vientos(Instrumento):
    pass


class Percusion(Instrumento):
    pass


class Cuerda(Instrumento):
    pass


class Pulsada(Cuerda):
    pass


class Frotada(Cuerda):
    pass


class Golpeada(Cuerda):
    pass



if __name__ == '__main__':
    
    orquesta = Orquesta()
    
    piano = Golpeada('primer piano')
    violin = Frotada('violin 1')
    vn = Frotada('violin 2')
    timbal = Percusion('timbal principal')

    orquesta.agregarInstrumento(piano)
    orquesta.agregarInstrumento(violin)
    orquesta.componentes.append(vn)
    orquesta.componentes.append(timbal)

    orquesta.listarInstrumentos()