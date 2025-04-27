import clases # importe de las clases creadas 

# metodo para insertar un paciente 
def insertar_paciente(lista, nombre, edad, sintoma, prioridad): # recibe la lista y los datos del paciente 
    nuevo_paciente = clases.Paciente(nombre, edad, sintoma, prioridad) # crea el nuevo paciente 
    if lista.primero is None: # si la lista esta vacia 
        lista.primero = nuevo_paciente # el nuevo paciente es el primero 
    else: # si no esta vacia 
        actual = lista.primero # empieza desde el primero 
        while actual.siguiente is not None: # mientras haya pacientes en la lista 
            actual = actual.siguiente # avanza al siguiente paciente 
        actual.siguiente = nuevo_paciente # agrega el nuevo paciente al final de la lista