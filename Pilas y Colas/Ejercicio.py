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

cola = Cola()
pila = Pila()

# Ingresar elementos a la cola
while True:
    elemento = input("Ingrese un elemento a la cola (o 'fin' para terminar): ")
    if elemento.lower() == 'fin':
        break
    cola.Insertar(elemento)

# Calcular tamaño inicial de la cola
tamaño_inicial = 0
actual = cola.frente
while actual:
    tamaño_inicial += 1
    actual = actual.siguiente

# Procesar la cola una sola vez
posicion = 0
for _ in range(tamaño_inicial):
    dato = cola.Eliminar()
    if posicion % 2 == 0:
        cola.Insertar(dato)  # Posición par → se queda en la cola
    else:
        pila.push(dato)      # Posición impar → se va a la pila
    posicion += 1

# Mostrar resultados
print("\nElementos en la cola (posiciones pares):")
cola.Imprimir()

print("Elementos en la pila (posiciones impares):")
pila.Imprimir()
