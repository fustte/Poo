
class Orquesta:

    def __init__(self, nombre= ''):


        self.componentes = []  # lista de intrumentos

    def agregarInstrumento(self, instrumento):
        if not isinstance(instrumento, Instrumento):
            raise TypeError(f'{instrumento} no es un instrumento')
        self.componentes.append(instrumento)

    def listarInstrumentos(self):
        for instrumento in self.componentes:
            print(instrumento)

    def interpretar(self, obra=''):
        if obra != '':
            print('-'*60)
            print('\tInterpretando:', obra)
            print('-'*60)

        for instrumento in self.componentes:
            instrumento.sonar()

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


class Viento(Instrumento):

    def sonar(self):
        print('sopla', end= ' ')
        super().sonar()



class Percusion(Instrumento):
    
    def sonar (self):
        print('golpea', end= ' ')
        super().sonar()
    


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
    piano.sonido = 'pin pin pin'
    violin = Frotada('violin 1')
    violin.sonido = 'flic flic flic'
    vn = Frotada('violin 2')
    vn.sonido = 'flac flac flac'
    timbal = Percusion('timbal principal')
    timbal.sonido = 'pum pum pum'
    fagot = Viento('fagot alto')
    fagot.sonido = 'fiu fiu fiu'

    orquesta.agregarInstrumento(piano)
    orquesta.agregarInstrumento(violin)
    orquesta.componentes.append(vn)
    orquesta.componentes.append(timbal)
    orquesta.componentes.append(fagot)

    #orquesta.listarInstrumentos()
    
    for instrumento in orquesta.componentes:
        instrumento.sonar()