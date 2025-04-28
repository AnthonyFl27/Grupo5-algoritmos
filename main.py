# problema numero 3 de listas enlazadas
# autores: Anthony Flores, Juan Putoy, Dosson Narváez, Roberto Lopez 

"""Una clínica recibe pacientes en orden de llegada. Cada paciente debe ser ingresado al sistema
con los siguientes datos: nombre completo, edad, síntoma principal y prioridad (de 1 a 5). El
sistema debe permitir insertar nuevos pacientes, recorrer la lista para mostrar el orden de
atención, y eliminar a un paciente una vez atendido."""

class Lista_Pacientes: # clase para la lista de pacientes 
    def __init__(self):
        self.primero = None # None porque aun no hay pacientes 

# importe de modulos 
from modulos.metodos import insertar_paciente, mostrar_pacientes, eliminar_paciente
from os import system
lista = Lista_Pacientes()

while True: # bucle del menu 
        print("\n═════════ Menú de la Clínica ═════════\n")
        
        print("1. Insertar paciente")
        print("2. Mostrar pacientes")
        print("3. Eliminar paciente atendido")
        print("4. Salir del programa\n")

        opcion = input("Seleccione una opcion: ")
        print("\n═══════════════════════════════════════\n\n")

        # insertar el paciente y datos 
        if opcion == "1":
            nombre = input("Ingrese nombre del paciente: ")
            edad = int(input("Ingrese la edad del paciente: "))
            sintoma = input("Ingrese sintoma del paciente: ")
            prioridad = int(input("Ingrese la prioridad(1-5): "))
            insertar_paciente(lista, nombre, edad, sintoma, prioridad)
            print("El paciente ha sido agregado...")
            input()
            system("cls")
            

        elif opcion == "2":
            mostrar_pacientes(lista)
            input("Presione Enter para continuar...")
            system("cls")
        
        elif opcion == "3":
            nombre = input("Ingrese el nombre del paciente a eliminar: ")
            eliminado = eliminar_paciente(lista, nombre)
            if eliminado:
                print("Paciente atendido y eliminado de la lista.")
                input("Presione Enter para continuar...")
                system("cls")
            else:
                print("No se pudo eliminar el paciente.")
                input("Presione Enter para continuar...")
                system("cls")

        
        elif opcion == "4":
            print("Saliendo del programa...")
            break

        else:
            print("Inserte una opcion valida")
            input()
            system("cls")
