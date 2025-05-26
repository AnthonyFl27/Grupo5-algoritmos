class Pila:
    def __init__(self):
        self.elementos = []

    def push(self, dato):
        self.elementos.append(dato)

    def pop(self):
        if not self.esta_vacia():
            return self.elementos.pop()
        else:
            print("Pila vacía")
            return None

    def esta_vacia(self):
        return len(self.elementos) == 0

    def Imprimir(self):
        if self.esta_vacia():
            print("Pila vacía")
        else:
            for elem in reversed(self.elementos):
                print(elem, end=" -> ")
            print("None")