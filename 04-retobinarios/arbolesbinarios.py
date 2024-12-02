
# Árbol binario

arbol_binario = [
    1,
    [7,
      [2, [], []],
      [6,
        [5, [], []],
        [11, [], []]]],
    [9, [],
      [9,
        [5, [], []],
        []]]
]

def max_valor_arbol(arbol):
    if not arbol:
        return float('-inf')
    
    pila = [arbol]
    max_valor = float('-inf')

    while pila:
        nodo = pila.pop()
        
        if not nodo:
            continue

        valor = nodo[0]
        izquierdo = nodo[1] if len(nodo) > 1 else []
        derecho = nodo[2] if len(nodo) > 2 else []



        if valor > max_valor:
            max_valor = valor

        if derecho:
            pila.append(derecho)

        if izquierdo:
            pila.append(izquierdo)

    return max_valor


# Llamo a la funcion

mayor_valor = max_valor_arbol(arbol_binario)
print("El mayor valor en el árbol binario es:", mayor_valor)

