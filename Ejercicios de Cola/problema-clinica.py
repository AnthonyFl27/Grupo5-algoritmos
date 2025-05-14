from os import system

class Nodo:
    def __init__(self,dato):
        self.dato = dato
        self.siguiente = None

class Cola:
    def __init__(self):
        self.frente = None
        self.final = None

    def Insertar(self,dato):
        nuevo = Nodo(dato)
        if self.final is None:
            self.frente = self.final = nuevo
        else:
            self.final.siguiente = nuevo
            self.final = nuevo
            print("Elemento insertado: ", dato)

    def Eliminar(self):
        if self.frente is None:
            print("Cola vacia")
            return None
        else:
            eliminado = self.frente.dato
            self.frente = self.frente.siguiente
            if self.frente is None:
                self.final = None
            print("Elemento eliminado: ", eliminado)
            return eliminado
    
    def Imprimir(self):
        if self.frente is None:
            print("Cola vacia")
            return
        else:
            print("Contenido de la cola, desde el frente hasta el final:")
            actual = self.frente
            while actual is not None:
                print(actual.dato, end=" -> ")
                actual = actual.siguiente
            print("None")

# cola vacia 
cola = Cola()

while True:
    try:
        print("1. insertar paciente")
        print("2. mostrar paciente ingresando a la cola")
        print("3. eliminar paciente atendido")
        print("4. consultar pacientes pendientes")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            paciente = input("ingrese paciente: ")
            cola.Insertar((paciente))
            print(f"Paciente ya en cola {paciente}.")
            input("Presione enter para continuar...")
            system("cls")
        
        elif opcion == "2":
            if cola.frente is not None:
                usuario, archivo = cola.frente.dato
                print(f"primer paciente en la cola: {paciente}")
                input("Presione Enter para continuar...")
                system("cls")
            else:
                print("No hay solicitudes pendientes.")
                input("Presione Enter para continuar...")
                system("cls")
        
        elif opcion == "3":
            if cola.frente is not None:
                usuario, archivo = cola.Eliminar()
                print(f"Paciente {usuario} atentido y eliminado..")
                input("Presione Enter para continuar...")
                system("cls")
            else:
                print("No hay solicitudes pendientes.")
                input("Presione Enter para continuar...")
                system("cls")
        
        elif opcion == "4":
            if cola.frente is not None:
                print("Pacientes pendientes por atender:")
                actual = cola.frente
                while actual is not None:
                    usuario, archivo = actual.dato
                    print(f"- Usuario: {usuario}")
                    actual = actual.siguiente
                input("Presione Enter para continuar...")
                system("cls")
            else:
                print("No hay solicitudes pendientes.")
                input("Presione Enter para continuar...")
                system("cls")
        
        elif opcion == "5":
            break

        else:
            print("Opción inválida. Debe ingresar un número entre 1 y 5.")
            input("Presione Enter para continuar...")
            system("cls")

    except ValueError:
        print("Opción inválida. Debe ingresar un número entre 1 y 5.")
        input("Presione Enter para continuar...")
        system("cls")
        
        continue