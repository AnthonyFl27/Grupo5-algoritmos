# Simulador de cola de atención en una clínica

cola_pacientes = []

def mostrar_menu():
    print("\n--- Clínica - Sistema de Atención ---")
    print("1. Registrar llegada de paciente")
    print("2. Atender siguiente paciente")
    print("3. Mostrar pacientes en espera")
    print("4. Salir")

def registrar_paciente():
    nombre = input("Ingrese el nombre del paciente: ")
    cola_pacientes.append(nombre)
    print(f"Paciente '{nombre}' ha sido registrado.")

def atender_paciente():
    if len(cola_pacientes) == 0:
        print("No hay pacientes en espera.")
    else:
        paciente = cola_pacientes.pop(0)
        print(f"Paciente '{paciente}' ha sido atendido.")

def mostrar_pacientes():
    if len(cola_pacientes) == 0:
        print("No hay pacientes en espera.")
    else:
        print("\nLista de pacientes en espera:")
        for i, paciente in enumerate(cola_pacientes, start=1):
            print(f"{i}. {paciente}")

# Bucle principal del sistema
while True:
    mostrar_menu()
    opcion = input("Seleccione una opción (1-4): ")

    if opcion == "1":
        registrar_paciente()
    elif opcion == "2":
        atender_paciente()
    elif opcion == "3":
        mostrar_pacientes()
    elif opcion == "4":
        print("Saliendo del sistema. ¡Gracias!")
        break
    else:
        print("Opción no válida. Intente de nuevo.")
