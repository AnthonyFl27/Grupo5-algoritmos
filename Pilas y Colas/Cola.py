class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class Cola:
    def __init__(self):
        self.frente = None
        self.final = None

    def Insertar(self, dato):
        nuevo = Nodo(dato)
        if self.final is None:
            self.frente = self.final = nuevo
        else:
            self.final.siguiente = nuevo
            self.final = nuevo

    def Eliminar(self):
        if self.frente is None:
            print("Cola vacía")
            return None
        else:
            dato = self.frente.dato
            self.frente = self.frente.siguiente
            if self.frente is None:
                self.final = None
            return dato

    def Imprimir(self):
        actual = self.frente
        if actual is None:
            print("Cola vacía")
        else:
            while actual is not None:
                print(actual.dato, end=" -> ")
                actual = actual.siguiente
            print("None")