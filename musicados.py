
class Orquesta:

    def __init__(self, nombre=''):
        self.cuerda = []
        self.viento = []
        self.percusion = []

    def agregarInstrumento(self, instrumento):
        if isinstance(instrumento, Cuerda):
            self.cuerda.append(instrumento)
        elif isinstance(instrumento, Viento):
            self.viento.append(instrumento)
        elif isinstance(instrumento, Percusion):
            self.percusion.append(instrumento)
        else:
            raise TypeError(f'{instrumento} no es un tipo de instrumento conocido')

    def listarInstrumentos(self):
        print("Instrumentos de Cuerda:")
        for instrumento in self.cuerda:
            print(instrumento)
        print("Instrumentos de Viento:")
        for instrumento in self.viento:
            print(instrumento)
        print("Instrumentos de Percusión:")
        for instrumento in self.percusion:
            print(instrumento)

    def interpretar(self, obra=''):
        if not (self.cuerda or self.viento or self.percusion):
            print(f'No hay músicos para interpretar la partitura de : {obra}')
            return

        # Ordenar los instrumentos por nombre antes de interpretar
        self.cuerda.sort(key=lambda instrumento: instrumento.nombre)
        self.viento.sort(key=lambda instrumento: instrumento.nombre)
        self.percusion.sort(key=lambda instrumento: instrumento.nombre)

        if obra != '':
            print('-'*60)
            print('\tInterpretando:', obra)
            print('-'*60)

        for lista in [self.cuerda, self.viento, self.percusion]:
            for instrumento in lista:
                instrumento.sonar()

    def __str__(self):
        resultado = ''
        for lista in [self.cuerda, self.viento, self.percusion]:
            for instrumento in lista:
                resultado += f'{instrumento}, '
        if len(resultado) > 2:
            return resultado[:-2]  # Remover la última coma y espacio
        return 'No hay instrumentos'

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
    pass

class Percusion(Instrumento):
    pass

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
    pulsada.sonido = 'clin clin clin'

    orquesta.agregarInstrumento(piano)
    orquesta.agregarInstrumento(violin)
    orquesta.agregarInstrumento(vn)
    orquesta.agregarInstrumento(timbal)
    orquesta.agregarInstrumento(fagot)
    orquesta.agregarInstrumento(pulsada)
    
    orquesta.interpretar('El cascanueces')

