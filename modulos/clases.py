# clases a utilizar 
class Paciente: # clase paciente 
    def __init__(self, nombre, edad, sintoma, prioridad): # constructor 
        # datos del paciente 
        self.nombre = nombre
        self.edad = edad
        self.sintoma = sintoma 
        self.prioridad = prioridad

        # al inicio el paciente no apunta a nadie 
        self.siguiente = None 

