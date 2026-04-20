class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None

class ArbolNone:
    def __init__(self):
        self.raiz = None

    def agregar(self, dato):
        if self.raiz is None:
            self.raiz = Nodo(dato)
        else:
            self.__agregar_recursivo(self.raiz, dato)

    def __agregar_recursivo(self, nodo, dato):
        if dato < nodo.valor:
            if nodo.izquierdo is None:
                nodo.izquierdo = Nodo(dato)
            else:
                self.__agregar_recursivo(nodo.izquierdo, dato)
        elif dato > nodo.valor:
            if nodo.derecho is None:
                nodo.derecho = Nodo(dato)
            else:
                self.__agregar_recursivo(nodo.derecho, dato)

    def preorden(self, nodo):
        if nodo is None:
            return
        print(nodo.valor, end=" ")
        if nodo.izquierdo is None and nodo.derecho is not None:
            print("None", end=" ")
        if nodo.derecho is None and nodo.izquierdo is not None:
            print("None", end=" ")
        self.preorden(nodo.izquierdo)
        self.preorden(nodo.derecho)

    def inorden(self, nodo):
        if nodo is None:
            return
        if nodo.izquierdo is None and nodo.derecho is not None:
            print("None", end=" ")
        self.inorden(nodo.izquierdo)
        print(nodo.valor, end=" ")
        self.inorden(nodo.derecho)
        if nodo.derecho is None and nodo.izquierdo is not None:
            print("None", end=" ")

    def postorden(self, nodo):
        if nodo is None:
            return
        if nodo.izquierdo is None and nodo.derecho is not None:
            print("None", end=" ")
        self.postorden(nodo.izquierdo)
        self.postorden(nodo.derecho)
        if nodo.derecho is None and nodo.izquierdo is not None:
            print("None", end=" ")
        print(nodo.valor, end=" ")

arbol = ArbolNone()
datos = [3, 1, 4, 2, 5]
for d in datos:
    arbol.agregar(d)

print("Preorden:", end=" ")
arbol.preorden(arbol.raiz)
print("\nInorden:", end=" ")
arbol.inorden(arbol.raiz)
print("\nPostorden:", end=" ")
arbol.postorden(arbol.raiz)