'''En una campaña de donación de sangre en un hospital de Estelí, los datos de los donantes se
almacenan en una pila según el orden en que se procesan. Si ocurre un problema técnico, se debe
revertir el último registro. Implementa un sistema para registrar donantes (push), eliminar el último
(pop), y mostrar el donante actual en proceso.'''

# inicializamos la clase nodo 
class Nodo:
    def __init__(self, dato):
        self.dato = dato # almacena los datos del paciente 
        self.siguiente = None # enlace al siguiente nodo 

# clase de pila, gestiona la coleccion de nodos 
class Pila:
    def __init__(self):
        self.cima = None # almacena el nodo mas reciente, es decir el ultimo en la pila 

    # metodo para agregar donantes 
    def push(self, dato):
        nuevo_nodo = Nodo(dato) # crea un nuevo nodo con los datos del donante
        nuevo_nodo.siguiente = self.cima # el nuevo nodo apunta al que esta antes en la cima 
        self.cima = nuevo_nodo # ahora la cima esta un nuevo nodo que acabamos de ingresar 

    # metodo para quitar el ultimo donante
    def pop(self):
        if self.cima is None: # si no hay nodos en la cima 
            return None # no nos retorna nada
        dato = self.cima.dato # pero si hay nodos guarda el dato en la cima 
        self.cima = self.cima.siguiente # mueve a la cima al siguiente nodo 
        return dato # devolvera dato eliminado

    # para ver el donante actual
    def peek(self):
        if self.cima is None: # si no hay nada en la cima 
            return None # no nos devolvera nada
        return self.cima.dato # si hay un nodo en la cima nos devolvera el dato que esta en la cima 

    # verifica si nuestra pila esta vacia 
    def is_empty(self):
        return self.cima is None # retorna si la cima si no hay nada 

    # obtener la lista de los donantes 
    def items(self):
        actual = self.cima # actual sera el nodo que este en la cima 
        elementos = [] # variable elemento vacia 
        while actual is not None: # si actual no es Nada
            elementos.append(actual.dato) # agrega el dato del nodo a la lista 
            actual = actual.siguiente # avanza al siguiente nodo en la lista 
        return elementos # retorna los elementos, los datos de los nodos en la pila 

# menu interactivo en consola
def mostrar_menu():
    print("\n--- MENÚ DONANTES ---")
    print("1. Registrar donante")
    print("2. Eliminar último registro")
    print("3. Ver donante en proceso")
    print("4. Mostrar todos los donantes")
    print("5. Salir")

pila_donantes = Pila() # creamos una pila vacia para guardar donantes 

while True:
    mostrar_menu()
    opcion = input("Selecciona una opción (1-5): ")
    
    # input de datos que se almacenan en la clase nodo y atributo dato
    if opcion == "1":
        nombre = input("Nombre del donante: ")
        edad = input("Edad: ")
        tipo_sangre = input("Tipo de sangre: ")
        donante = {
            "nombre": nombre,
            "edad": edad,
            "tipo_sangre": tipo_sangre
        }
        # con nuestro metodo push agregamos los datos del donante a la pila 
        pila_donantes.push(donante)
        print(" donante registrado!!")


    elif opcion == "2":
        eliminado = pila_donantes.pop() # con el metodo pop eliminamos el ultimo donante de nuestra pila 
        if eliminado:
            print(f" donante eliminado: {eliminado['nombre']}")
        else:
            print("No hay donantes para eliminar:")

    elif opcion == "3":
        # con peek mostramos el donante actual, el que esta en la cima, sin eliminarlo 
        actual = pila_donantes.peek()
        if actual:
            print(f"Donante en proceso: {actual['nombre']}, {actual['edad']} años, Tipo: {actual['tipo_sangre']}")
        else:
            print("no hay donantes registrados")

    elif opcion == "4":
        # lo que hace items es recorrer desde la cima hacia el fondo y devuelve una lista con los datos de cada nodo.
        todos = pila_donantes.items() # llamamos items para que recorra la pila de la cima hacia abajo, extrayendo los datos de cada nodo 
        
        if todos: # si la lista todos tiene elementos 
            print("\n lista de donantes (ultimo arriba): ") # imprime la lista de donantes
            for idx, d in enumerate(todos): # idx indice de la posicion, D es la direccion del donante actual 
                print(f"{idx+1}. {d['nombre']} - {d['edad']} años - {d['tipo_sangre']}") # imprimimos datos del donante
        else: # si todos es una lista vacia, se le indica al usuario que no hay donantes 
            print("no hay donantes registrados.")

    elif opcion == "5":
        print("saliendo del programa, gracias!")
        break

    else:
        print("ingrese una opcion valida")
