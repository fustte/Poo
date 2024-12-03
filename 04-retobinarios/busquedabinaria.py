# Creo clase Nodo

class Nodo:
    def __init__(self, valor):
    self.valor = valor
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

    def buscar(self, valor):
        self.coste_ultima_busqueda = 0
        return self._buscar_recursivo(self.raiz, valor)
    
    def _buscar_recursivo(self, nodo, valor):
        if nodo is None:
            return None
        self.coste_ultima_busqueda += 1

        if nodo.valor == valor:
            return nodo
        elif valor < nodo.valor:
            return self._buscar_recursivo(nodo.izquierdo, valor)
        else:
            return self._buscar_recursivo(nodo.derecho, valor)
        
    def eliminar(self, valor):
        self.raiz = self._eliminar_recursivo(self.raiz, valor)

    def _eliminar_recursivo(self, nodo, valor):
        if nodo is None:
            return nodo
        
        if valor < nodo.valor:
            nodo.izquierdo = self._eliminar_recursivo(nodo.izquierdo, valor)
        elif valor < nodo.valor:
            nodo.derecho = self._ekiminar_recursivo(nodo.derecho, valor)

        else:
            if nodo.izquierdo is None:
                return nodo.derecho
            elif nodo.derecho is None:
                return nodo.izquierdo
            nodo.valor = self._minimo_valor(nodo.derecho)
            nodo.derecho = self._eliminar_recursivo(nodo.derecho, nodo.valor)

        return nodo
    
    def _minimo_valor(self, nodo):
        while nodo.izquierdo is not None:
            nodo = nodo.izquierdo
        return nodo.valor
    
    def obtener_maximo(self):
        return self._obtener_maximo_recursivo(self.raiz)
    
    def _obtener_maximo_recursivo(self, nodo):
        if nodo.derecho is None:
            return nodo.valor
        return self._obtener_maximo_recursivo(nodo.derecho)
    
    def obtener_minimo(self):
        return self._obtener_maximo_recursivo(self.raiz)
    
    def _obtener_minimo_recursivo(self, nodo):
        if nodo.izquierdo is None:
            return nodo.valor
        return self._sumar_valores_recursivo(self.raiz)
    
    def sumar_valores(self):
        return self._sumar_valores_recursivo(self.raiz)
    
    def _sumar_valores_recursivo(self, nodo):
        if nodo is None:
            return 0
        return nodo.valor + self ._sumar_valores_recursivo(nodo.izquierdo) + self._sumar_valores_recursivo
    
    def contar_nodos(self):
        return self._contar_nodos_recursivo(self.raiz)
    
    def _contar_nodos_recursivo(self, nodo):
        if nodo is None:
            return 0
        return 1 + self._contar_nodos_recursivo(nodo.izquierdo) + self._contar_nodos_recursivo(nodo.derecho)
    
    

    

