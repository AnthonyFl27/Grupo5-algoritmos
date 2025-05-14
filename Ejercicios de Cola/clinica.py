# Simulador de cola de atención en una clínica usando clases

class Paciente:
    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self):
        return self.nombre

class Clinica:
    def __init__(self):
        self.cola_pacientes = []

    def registrar_paciente(self, nombre):
        paciente = Paciente(nombre)
        self.cola_pacientes.append(paciente)
        print(f"Paciente '{paciente}' ha sido registrado.")

    def atender_paciente(self):
        if not self.cola_pacientes:
            print("No hay pacientes en espera.")
        else:
            paciente = self.cola_pacientes.pop(0)
            print(f"Paciente '{paciente}' ha sido atendido.")

    def mostrar_pacientes(self):
        if not self.cola_pacientes:
            print("No hay pacientes en espera.")
        else:
            print("\nLista de pacientes en espera:")
            for i, paciente in enumerate(self.cola_pacientes, start=1):
                print(f"{i}. {paciente}")

class SistemaClinica:
    def __init__(self):
        self.clinica = Clinica()

    def mostrar_menu(self):
        print("\n--- Clínica - Sistema de Atención ---")
        print("1. Registrar llegada de paciente")
        print("2. Atender siguiente paciente")
        print("3. Mostrar pacientes en espera")
        print("4. Salir")

    def ejecutar(self):
        while True:
            self.mostrar_menu()
            opcion = input("Seleccione una opción (1-4): ")

            if opcion == "1":
                nombre = input("Ingrese el nombre del paciente: ")
                self.clinica.registrar_paciente(nombre)
            elif opcion == "2":
                self.clinica.atender_paciente()
            elif opcion == "3":
                self.clinica.mostrar_pacientes()
            elif opcion == "4":
                print("Saliendo del sistema. ¡Gracias!")
                break
            else:
                print("Opción no válida. Intente de nuevo.")

# Ejecutar el sistema
if __name__ == "__main__":
    sistema = SistemaClinica()
    sistema.ejecutar()
