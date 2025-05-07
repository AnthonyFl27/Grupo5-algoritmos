'''Una docente de informática en una secundaria revisa tareas impresas que sus estudiantes colocan
sobre su escritorio. Siempre revisa primero la última tarea entregada. Implementa un sistema que
permita agregar tareas (push), revisar una (pop), y mostrar cuál es la siguiente en revisar (peek),
todo usando una pila.'''
# Anthony King Flores Garcia

class Nodo: # inicializamos clase nodo
    def __init__(self, dato): 
        self.dato = dato # almacenamos datos de la tarea 
        self.siguiente = None # apuntamos al siguiente nodo de la pila 

# inicializamos una pila vacia  
class Pila:
    def __init__(self):
        self.cima = None # almacenamos el nodo que esta en la cima 

    # metodo para agregar nuevo nodo a la pila 
    def push(self, dato):
        nuevo_nodo = Nodo(dato) # crea un nodo con los datos recibidos
        nuevo_nodo.siguiente = self.cima # apunta ese nuevo nodo al que esta en la cima 
        self.cima = nuevo_nodo # actualiza para el nuevo nodo este en la cima 

    # metodo que elimina y devuelve el nodo en la cima de la pila 
    def pop(self):
        if self.cima is None: # si la pila esta vacia, no devuelve nada 
            return None
        dato = self.cima.dato # guarda el dato en la cima 
        self.cima = self.cima.siguiente # el que esta debajo del eliminado, lo mueve a la cima 
        return dato # devolvemos el dato del eliminado

    # metodo para mostrar dato en la cima sin eliminarlo 
    def peek(self):
        if self.cima is None: # si la cima esta vacia, no devuelve nada 
            return None
        return self.cima.dato # si es lo contrario, nos devuelve el dato en la cima 

    # metodo que verifica si la pila esta vacia 
    def is_empty(self):
        return self.cima is None # si la cima esta vacia nos devuelve true y si hay elementos nos devuelve false 

    # metodo que nos devuelve todos los elementos 
    def items(self):
        actual = self.cima # empieza desde la cima          ------------------------------------------------------------|
        # lista de elementos vacia, almacenera todos los datos                                                          |
        elementos = []      #                                                                                           | ----- recorre pila desde la cima hasta abajo
        while actual is not None: # mientras que en nuestra pila actual haya datos                                      |
            elementos.append(actual.dato) # se agrega el contenido dato del nodo actual a la lista elementos.           |
            actual = actual.siguiente  #                    ------------------------------------------------------------|
        return elementos # cuando ya no hay mas nodos, nos retorna la lista de elementos con todos los datos que fueron recorridos 

# metodo para menu 
def mostrar_menu():
    print("\n--- MENÚ DE REVISION DE TAREAS ---")
    print("1. Agregar tarea")
    print("2. Revisar última tarea")
    print("3. Ver próxima tarea a revisar")
    print("4. Mostrar todas las tareas pendientes")
    print("5. Salir")

# linstanciamos el objeto Pila donde almacenaremos las tareas como nodos 
pila_tareas = Pila() # al principio estara vacia 

while True:
    mostrar_menu()
    opcion = input("Selecciona una opción (1-5): ")

    if opcion == "1":
        estudiante = input("Nombre del estudiante: ")
        titulo = input("Título de la tarea: ")
        tarea = {
            "estudiante": estudiante,
            "titulo": titulo
        }
        pila_tareas.push(tarea) # insertamos al inicio estos datos tarea en la pila de tareas 
        print("Tarea agregada con éxito.")

    elif opcion == "2":
        # variable revisada que es igual a Pop para quitar la tarea en la cima y la tarea que esta abajo sube a la cima 
        revisada = pila_tareas.pop()
        if revisada: # si hay tareas por revisar, las revisas 
            print(f"Tarea revisada y eliminada: {revisada['titulo']} de {revisada['estudiante']}")
        else: # si no hay, no hay tareas en nuestra pila 
            print("no hay tareas pendientes.")

    elif opcion == "3":
        # variable siguiente que es igual al metodo Peek para ver la siguiente tarea en la cima a revisar sin revisarla e eliminarla
        siguiente = pila_tareas.peek()
        if siguiente: # si en la pila hay tarea en la cima, con peek la visualizamos sin revisarla 
            print(f"Próxima tarea a revisar: {siguiente['titulo']} de {siguiente['estudiante']}")
        else: # si no hay tareas pendiente en la cima 
            print("no hay tareas pendientes.")

    elif opcion == "4":
        # variable tareas, el cual usaremos items para recorrerlas y imprimirlas en orden LIFO
        tareas = pila_tareas.items()
        if tareas: # si hay tareas, aplica el metodo items y las imprime en orden lifo
            print("\nLista de tareas pendientes (última arriba):")
            for idx, t in enumerate(tareas):
                print(f"{idx+1}. {t['titulo']} - {t['estudiante']}")
        else: # si no hay tareas en la pila, no las imprime 
            print("No hay tareas en la pila.")

    elif opcion == "5":
        print("Cerrando revisión de tareas.")
        break

    else:
        print("Opción no válida. Intenta de nuevo.")
