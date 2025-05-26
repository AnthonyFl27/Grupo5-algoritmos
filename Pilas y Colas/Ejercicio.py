'''Objetivo:
Dado una cola con elementos y una pila vacía, desarrollar un programa que procese la cola de forma que:
→	Los elementos que se encuentran en posiciones pares (0, 2, 4, ...) permanezcan en la cola.
→	Los elementos que se encuentran en posiciones impares (1, 3, 5, ...) se transfieran a la pila.

Consideraciones:
→	La posición de los elementos se cuenta a partir de cero (la primera posición es la 0, la segunda es la 1, etc.).
→	La operación debe realizarse recorriendo la cola una sola vez.
→	Al finalizar, la pila contendrá los elementos impares en orden LIFO y 
la cola solo los elementos pares en su orden original.'''

from Cola import Cola
from Pila import Pila
cola= Cola()
pila = Pila()
# Iniciamos el programa llenando la cola con elementos que el usuario inrgesa
while True:
    elemento = input("Ingrese un elemento a la cola (o 'fin' para terminar): ")
    if elemento.lower() == 'fin':
        break
    cola.Insertar(elemento)
# Procesamos la cola
posicion = 0  # Contador de posiciones
#recorremos la cola y transferimos elementos a la pila o los dejamos en la cola
while cola.final is not None:  # Mientras la cola no esté vacía
    elemento = cola.frente.dato  # Obtenemos el elemento al frente de la cola
    if posicion % 2 == 0:  # Posición par
        cola.Insertar(elemento)
    else:  # Posición impar
        pila.push(elemento)
    posicion += 1
# Mostramos los resultados
print("Elementos en la cola (posiciones pares):")
cola.Imprimir()
print("Elementos en la pila (posiciones impares):")
pila.Imprimir()