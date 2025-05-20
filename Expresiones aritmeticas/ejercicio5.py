# función donde en una lista enlazada busca un valor y lo devuelve y si no lo encuentra se indica que el valor no esta en la lista.

class Nodo:
    def __init__(self, dato):
        # Inicializa un nodo con un dato y un puntero al siguiente nodo (inicialmente None)
        self.dato = dato
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        # Inicializa la lista enlazada con la cabeza como None
        self.cabeza = None

    def agregar(self, dato):
        # Agrega un nuevo nodo con el dato proporcionado al final de la lista
        nuevo_nodo = Nodo(dato)
        if not self.cabeza:  # Si la lista está vacía
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            # Recorre la lista hasta encontrar el último nodo
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo  # Agrega el nuevo nodo al final

    def buscar(self, valor):
        # Busca un valor en la lista y devuelve su posición o un mensaje si no se encuentra
        actual = self.cabeza
        posicion = 0
        while actual:  # Recorre la lista nodo por nodo
            if actual.dato == valor:  # Si encuentra el valor
                return f"El valor {valor} está en la posición {posicion}."
            actual = actual.siguiente
            posicion += 1
        return f"El valor {valor} no está en la lista."  # Si no encuentra el valor

# Menú para interactuar con el usuario
lista = ListaEnlazada()

while True:
    print("\nOpciones:")
    print("1. Agregar un valor a la lista")  # Opción para agregar un valor
    print("2. Buscar un valor en la lista")  # Opción para buscar un valor
    print("3. Salir")  # Opción para salir del programa
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        # Solicita al usuario un valor para agregar a la lista
        valor = input("Ingrese el valor a agregar: ")
        lista.agregar(valor)
        print(f"Valor {valor} agregado a la lista.")
    elif opcion == "2":
        # Solicita al usuario un valor para buscar en la lista
        valor = input("Ingrese el valor a buscar: ")
        print(lista.buscar(valor))
    elif opcion == "3":
        # Finaliza el programa
        print("Saliendo del programa.")
        break
    else:
        # Mensaje de error si la opción no es válida
        print("Opción no válida. Intente de nuevo.")