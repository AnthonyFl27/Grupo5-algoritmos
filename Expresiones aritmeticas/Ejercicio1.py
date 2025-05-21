#invertir palabras en una frase 
# Ejemplo : "Hola Mundo" -> "Mundo Hola"
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

    def cima (self):
        if self.cima is None:
            return None
        return self.cima.dato
    
    def imprimir(self):
        actual = self.cima
        while actual is not None:
            print(actual.dato, end="\n")
            actual = actual.siguiente
        print()

def invertir_frase(frase):
        pila = Pila()
        palabras = frase.split()

        for palabra in palabras:
            pila.push(palabra)

        frase_invertida = ""
        while pila.cima is not None:
            frase_invertida += pila.pop() + " "
        return frase_invertida.strip()
# Pedimos que el usuario ingrese una frase y cada palabra se almacenara como un nodo en la pila
# Ejemplo de uso
frase = input("Ingrese una frase: ")
resultado = invertir_frase(frase)
print("Frase invertida:", resultado)





