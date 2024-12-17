"""
Enunciado
Crea una clase Triangulo que:

Se construya a partir del valor de la longitud sus tres lados en centímetros.
Tenga un método validar que compruebe que esos tres valores forman un triángulo.
Tenga un método get_tipo que devuelva el tipo de triángulo según sus lados. Inicialmente el resultado será 'indefinido'.
Crea una clase para cada tipo de triángulo según sus lados que herede de la clase Triangulo de forma que:
La clase Equilatero solamente aceptará un lado para crearlo y el método get_tipo devolverá como resultado el valor 'equilátero'.
La clase Isosceles solamente aceptará dos valores en el constructor. El primero de ellos corresponderá a la longitud de los dos lados iguales en centímetros y el segundo al tercer lado. El método get_tipo devolverá la cadena 'isósceles'.
La clase Escaleno se construye con el valor de los tres lados y el método get_tipo devolverá el valor 'escaleno'.
Instanciar tres triángulos, uno de cada tipo y, para cada uno de ellos, utilizar el método validar para comprobar que los valores utilizados permiten la creación de un triángulo válido.
Para cada uno de los triángulos anteriores, comprobar el resultado del método get_tipo.
Utilizar el método isinstance para comprobar que los tres triángulos anteriores son de tipo Triangulo además del tipo específico correspondiente (Equilatero, Isosceles o Escaleno).
Por último, comprobar que la creación de un triángulo con los valores 1, 2, 4 no genera un triángulo válido.
"""


class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
        self.tipo = 'indefinido'

    def validar(self):
        return self.lado1 + self.lado2 > self.lado3 and \
               self.lado1 + self.lado3 > self.lado2 and \
               self.lado2 + self.lado3 > self.lado1

    def get_tipo(self):
        return self.tipo

class Equilatero(Triangulo):
    def __init__(self, lado):
        super().__init__(lado, lado, lado)
        self.tipo = 'equilátero'

class Isosceles(Triangulo):
    def __init__(self, lado_igual, lado_diferente):
        super().__init__(lado_igual, lado_igual, lado_diferente)
        self.tipo = 'isósceles'

class Escaleno(Triangulo):
    def __init__(self, lado1, lado2, lado3):
        super().__init__(lado1, lado2, lado3)
        self.tipo = 'escaleno'

# Instanciar triángulos
triangulo_equilatero = Equilatero(5)
triangulo_isosceles = Isosceles(4, 3)
triangulo_escaleno = Escaleno(3, 4, 5)
triangulo_invalido = Triangulo(1, 2, 4)

# Validar y obtener tipo
if triangulo_equilatero.validar():
    print(f"El triángulo equilátero es {triangulo_equilatero.get_tipo()}")
else:
    print("El triángulo equilátero no es válido")

# ... repetir para los otros triángulos

# Comprobar tipos
print(isinstance(triangulo_equilatero, Triangulo))  # True
print(isinstance(triangulo_equilatero, Equilatero))  # True
print(isinstance(triangulo_invalido, Triangulo))  # True (pero no es válido)