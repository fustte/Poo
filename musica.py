
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
        if len(self.componentes) < 1:
            print(f'No hay mucisos para interpretar la partitura de : {obra}')
            return


        if obra != '':
            print('-'*60)
            print('\tInterpretando:', obra)
            print('-'*60)

        for instrumento in self.componentes:
            instrumento.sonar()

    def __srt__(self):
        resultado =''
        for instrumento in self.componentes:
            resultado = resultado + ', ' + str(instrumento)
        if len(resultado) < 2:
            return resultado[2:]
        return 'No hay intrumentos'

class Instrumento:

    def __init__(self, nombre):
        self.nombre = nombre
        self.sonido = None
        self.cualidad = ''

    def sonar(self):
        if self.sonido:
            print(f'{self.nombre} {self.cualidad} {self.sonido}') 
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

    def __init__(self, nombre):
        super().__init__(nombre)
        self.cualidad = 'con la pua'

    def sonar(self):
        super().sonar()
    


class Frotada(Cuerda):

    def sonar(self):
        print('con el arco', end=' ')
        super().sonar()



class Golpeada(Cuerda):

    def sonar(self):
        print('golpea', end=' ')
        super().sonar()



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
    pulsada = Pulsada('guitarra')
    pulsada.sonar = 'clin clin clin'

    orquesta.agregarInstrumento(piano)
    orquesta.agregarInstrumento(violin)
    orquesta.componentes.append(vn)
    orquesta.componentes.append(timbal)
    orquesta.componentes.append(fagot)
    orquesta.agregarInstrumento(pulsada)

    #orquesta.listarInstrumentos()
    
    orquesta.interpretar('El cascanueces')