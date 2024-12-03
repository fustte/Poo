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