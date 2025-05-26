class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class Pila:
    def __init__(self):
        self.cima = None

    def push(self, dato):
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.siguiente = self.cima
        self.cima = nuevo_nodo

    def pop(self):
        if self.cima is None:
            return None
        dato = self.cima.dato
        self.cima = self.cima.siguiente
        return dato

    def Cima (self):
        if self.cima is None:
            return None
        return self.cima.dato
    
    def Imprimir(self):
        actual = self.cima
        while actual is not None:
            print(actual.dato, end="\n")
            actual = actual.siguiente
        print()