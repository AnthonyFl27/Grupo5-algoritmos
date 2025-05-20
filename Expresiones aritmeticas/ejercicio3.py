# Simulacion de una lista de reproduccion de musica 

class Nodo:
    def __init__(self, cancion):
        self.cancion = cancion
        self.siguiente = None
        self.anterior = None

class ListaReproduccion:
    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.actual = None

    # Agregar una nueva canción a la lista de reproducción
    def agregar_cancion(self, cancion):
        nuevo_nodo = Nodo(cancion)
        if not self.primero:  # Si la lista está vacía
            self.primero = self.ultimo = nuevo_nodo
        else:
            self.ultimo.siguiente = nuevo_nodo
            nuevo_nodo.anterior = self.ultimo
            self.ultimo = nuevo_nodo
        print(f"Canción '{cancion}' agregada a la lista de reproducción.")

    # Eliminar una canción de la lista de reproducción
    def eliminar_cancion(self, cancion):
        nodo_actual = self.primero
        while nodo_actual:
            if nodo_actual.cancion == cancion:
                if nodo_actual.anterior:
                    nodo_actual.anterior.siguiente = nodo_actual.siguiente
                if nodo_actual.siguiente:
                    nodo_actual.siguiente.anterior = nodo_actual.anterior
                if nodo_actual == self.primero:
                    self.primero = nodo_actual.siguiente
                if nodo_actual == self.ultimo:
                    self.ultimo = nodo_actual.anterior
                print(f"Canción '{cancion}' eliminada de la lista de reproducción.")
                return
            nodo_actual = nodo_actual.siguiente
        print(f"Canción '{cancion}' no encontrada en la lista de reproducción.")

    # Reproducir la siguiente canción
    def reproducir_siguiente(self):
        if not self.actual:
            self.actual = self.primero
        elif self.actual.siguiente:
            self.actual = self.actual.siguiente
        else:
            print("No hay más canciones en la lista.")
            return
        print(f"Reproduciendo: {self.actual.cancion}")

    # Reproducir la canción anterior
    def reproducir_anterior(self):
        if not self.actual:
            self.actual = self.ultimo
        elif self.actual.anterior:
            self.actual = self.actual.anterior
        else:
            print("No hay canciones anteriores en la lista.")
            return
        print(f"Reproduciendo: {self.actual.cancion}")

    # Mostrar la lista de reproducción actual
    def mostrar_lista(self):
        if not self.primero:
            print("La lista de reproducción está vacía.")
            return
        print("Lista de reproducción:")
        nodo_actual = self.primero
        while nodo_actual:
            print(f"- {nodo_actual.cancion}")
            nodo_actual = nodo_actual.siguiente

# Ejemplo de uso
lista = ListaReproduccion()

while True:
    print("\nOpciones:")
    print("1. Agregar canción")
    print("2. Eliminar canción")
    print("3. Reproducir siguiente canción")
    print("4. Reproducir canción anterior")
    print("5. Mostrar lista de reproducción")
    print("6. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        cancion = input("Ingrese el nombre de la canción: ")
        lista.agregar_cancion(cancion)
    elif opcion == "2":
        cancion = input("Ingrese el nombre de la canción a eliminar: ")
        lista.eliminar_cancion(cancion)
    elif opcion == "3":
        lista.reproducir_siguiente()
    elif opcion == "4":
        lista.reproducir_anterior()
    elif opcion == "5":
        lista.mostrar_lista()
    elif opcion == "6":
        print("Saliendo del programa.")
        break
    else:
        print("Opción no válida. Intente de nuevo.")