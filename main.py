# problema numero 3 de listas enlazadas
# autores: Anthony Flores, Juan Putoy, Dosson Narváez, Roberto Lopez 

"""Una clínica recibe pacientes en orden de llegada. Cada paciente debe ser ingresado al sistema
con los siguientes datos: nombre completo, edad, síntoma principal y prioridad (de 1 a 5). El
sistema debe permitir insertar nuevos pacientes, recorrer la lista para mostrar el orden de
atención, y eliminar a un paciente una vez atendido."""

# importe de modulos 
from modulos.clases import Lista_pacientes
from modulos.metodos import insertar_paciente, mostrar_pacientes, eliminar_paciente

lista = Lista_pacientes()

while True: # bucle del menu 
        print("\n=== Menú de la Clínica ===")
        
        print("1. insertar paciente")
        print("2. mostrar pacientes")
        print("3. eliminar paciente atendido")
        print("4. salir del programa...")

        opcion = input("Eliga una opcion: ")

        # insertar el paciente y datos 
        if opcion == "1":
            nombre = input("ingrese nombre del paciente: ")
            edad = int(input("ingrese la edad del paciente: "))
            sintoma = input("ingrese sintoma del paciente: ")
            prioridad = int(input("ingrese la prioridad(1-5): "))
            insertar_paciente(lista, nombre, edad, sintoma, prioridad)
            print("el paciente a sido agregado")

        elif opcion == "2":
            mostrar_pacientes(lista)
        
        elif opcion == "3":
            nombre = input("Ingrese el nombre del paciente a eliminar: ")
            eliminado = eliminar_paciente(lista, nombre)
            if eliminado:
                print("Paciente atendido y eliminado de la lista.")
            else:
                print("No se pudo eliminar el paciente.")

        
        elif opcion == "4":
            print("saliendo del programa...")
            break

        else:
            print("inserte una opcion valida")
