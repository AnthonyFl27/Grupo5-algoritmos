'''En un mercado de Chinandega, los sacos con productos se cargan en camiones uno encima de otro.
Al llegar a destino, el primer saco que se descarga es el último que se cargó. Simula este proceso
con una pila que permita apilar sacos (push), descargar uno (pop) y visualizar el que está encima
(peek).
'''

class Saco:

    """Clase que representa un saco con un nombre o contenido."""

    def __init__(self, contenido):
        self.contenido = contenido

    def __str__(self):
        return f"Saco de {self.contenido}"


class Camion:

    """Clase que simula un camión que carga sacos como una pila (LIFO)."""

    def __init__(self):
        self.sacos = []

    def cargar_saco(self, saco):

        """Agrega un saco encima de la pila (push)."""

        self.sacos.append(saco)
        print(f"{saco} cargado al camión.")

    def descargar_saco(self):

        """Remueve el saco que está encima (pop)."""

        if self.sacos:
            saco = self.sacos.pop()
            print(f"{saco} descargado del camión.")
            return saco
        else:
            print("No hay sacos para descargar.")
            return None

    def ver_saco_superior(self):

        """Muestra el saco que está en la cima de la pila (peek)."""

        if self.sacos:
            print(f"El saco encima es: {self.sacos[-1]}")
            return self.sacos[-1]
        else:
            print("No hay sacos en el camión.")
            return None


# Función principal para interactuar con el usuario

def interactuar_con_camion():
    camion = Camion()

    while True:
        print("\nOpciones:")
        print("1. Cargar saco")
        print("2. Descargar saco")
        print("3. Ver saco superior")
        print("4. Salir")

        opcion = input("Selecciona una opción (1-4): ")

        if opcion == '1':
            contenido_saco = input("Ingresa el contenido del saco: ")
            saco = Saco(contenido_saco)
            camion.cargar_saco(saco)

        elif opcion == '2':
            camion.descargar_saco()

        elif opcion == '3':
            camion.ver_saco_superior()

        elif opcion == '4':
            print("Saliendo del programa.")
            break

        else:
            print("Opción no válida. Intenta de nuevo.")

# Llamar a la función para interactuar con el camión

if __name__ == "__main__":
    interactuar_con_camion()
