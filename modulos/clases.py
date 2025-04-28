class NodoPaciente:
    def __init__(self, nombre, edad, sintoma, prioridad):
        self.nombre = nombre
        self.edad = edad
        self.sintoma = sintoma
        self.prioridad = prioridad
        self.siguiente = None

class ListaPacientes:
    def __init__(self):
        self.inicio = None
