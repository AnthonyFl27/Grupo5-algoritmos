from modulos.clases import NodoPaciente

def insertar_paciente(lista, nombre, edad, sintoma, prioridad):
    nuevo_paciente = NodoPaciente(nombre, edad, sintoma, prioridad)
    if lista.inicio is None:
        lista.inicio = nuevo_paciente
    else:
        actual = lista.inicio
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = nuevo_paciente

def mostrar_pacientes(lista):
    if lista.inicio is None:
        print("No hay pacientes en la lista.")
        return
    actual = lista.inicio
    while actual:
        print(f"Nombre: {actual.nombre}, Edad: {actual.edad}, Síntoma: {actual.sintoma}, Prioridad: {actual.prioridad}")
        actual = actual.siguiente

def eliminar_paciente(lista, nombre):
    actual = lista.inicio
    anterior = None
    while actual:
        if actual.nombre == nombre:
            if anterior is None:
                lista.inicio = actual.siguiente
            else:
                anterior.siguiente = actual.siguiente
            return True
        anterior = actual
        actual = actual.siguiente
    return False
