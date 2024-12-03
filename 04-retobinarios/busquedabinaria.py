# Creo clase Nodo

class Nodo:
    def __init__(self, valor):
    self.valor = Value
    self.izquierdo = None
    self.derecho = None

    def __repr__(self):
        return str(self.valor)
    
class Arbol:
    def __init__(self):
        self.raiz = None
        self.coste_ultima_busqueda = 0

    def insertar(self, valor):
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self._insertar_recursivo(self.raiz, valor)

    def _insertar_recursivo(self, nodo valor):
        if valor < nodo.valor:
            if nodo.izquierdo is None:
                nodo.izquierdo = Nodo(valor)

            else:
                self._insertar_recursivo(nodo.izquierdo, valor)
    
    def _insertar_recursivo(self, nodo valor):
        if valor < nodo.valor:
            if nodo.derecho is None:
                nodo.derecho = Nodo(valor)

            else:
                self._insertar_recursivo(nodo.derecho, valor)

    