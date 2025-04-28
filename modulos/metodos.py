from clases import Paciente

# metodo para insertar un paciente 
def insertar_paciente(lista, nombre, edad, sintoma, prioridad): # recibe la lista y los datos del paciente 
    nuevo_paciente = Paciente(nombre, edad, sintoma, prioridad) # crea el nuevo paciente 
    if lista.primero is None: # si la lista esta vacia 
        lista.primero = nuevo_paciente # el nuevo paciente es el primero 
        
    else: # si no esta vacia 
        actual = lista.primero # empieza desde el primero 
        while actual.siguiente is not None: # mientras haya pacientes en la lista 
            actual = actual.siguiente # avanza al siguiente paciente 
        actual.siguiente = nuevo_paciente # agrega el nuevo paciente al final de la lista

def mostrar_pacientes(lista): # metodo para mostrar los pacientes
    if lista.primero is None: # si la lista esta vacia 
        print("No hay pacientes en la lista") # mensaje de que no hay pacientes 
    else: # si no esta vacia 
        actual = lista.primero # empieza desde el primero 
        while actual is not None: # mientras haya pacientes en la lista 
            print(f"Nombre: {actual.nombre}, Edad: {actual.edad}, Sintoma: {actual.sintoma}, Prioridad: {actual.prioridad}") # muestra los datos del paciente 
            actual = actual.siguiente # avanza al siguiente paciente

def eliminar_paciente(lista, nombre):  # método para eliminar un paciente
    if lista.primero is None:  # si la lista está vacía
        print("No hay pacientes en la lista")  # mensaje de que no hay pacientes
        return False  # no se eliminó nada
    else:
        actual = lista.primero  # empieza desde el primero
        anterior = None  # variable para guardar el paciente anterior
        while actual is not None:  # mientras haya pacientes en la lista
            if actual.nombre == nombre:  # si el paciente es el que se quiere eliminar
                if anterior is None:  # si es el primero de la lista
                    lista.primero = actual.siguiente  # el siguiente paciente es el primero
                else:  # si no es el primero
                    anterior.siguiente = actual.siguiente  # el siguiente del anterior es el siguiente del actual
                print(f"Paciente {nombre} eliminado")
                return True  # paciente eliminado exitosamente
            anterior = actual
            actual = actual.siguiente
        print(f"No se encontró paciente con nombre {nombre}")
        return False  # paciente no encontrado
