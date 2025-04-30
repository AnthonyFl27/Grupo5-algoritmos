'''Ejercicio 1: Implementa un método que reciba una pila de enteros como único parámetro. 
Este método llamado “separarParImpar” deberá retornar la pila con los números pares en la parte inferior y
los impares en la superior.
'''

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
    #Definiendo el método separarParImpar
    def separarParImpar(self):
        pila_par = Pila()
        pila_impar = Pila()

        while self.cima is not None:
            dato = self.pop()
            if dato % 2 == 0:
                pila_par.push(dato)
            else:
                pila_impar.push(dato)

        # Volver a apilar los números pares y luego los impares
        while pila_par.cima is not None:
            self.push(pila_par.pop())
        while pila_impar.cima is not None:
            self.push(pila_impar.pop())

# Ejemplo de uso rellenado por el usuario
pila = Pila()
print("Ingrese los números para la pila (ingrese -1 para terminar):")
while True:
    num = int(input())
    if num == -1:
        break
    pila.push(num)

# Imprimir la pila original
print("Pila original:")
pila.imprimir()
#Imprimir la pila separada
print("Pila separada (pares abajo, impares arriba):")
pila.separarParImpar()
pila.imprimir()
