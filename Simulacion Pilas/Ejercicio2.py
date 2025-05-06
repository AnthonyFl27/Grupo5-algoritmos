'''En una panadería tradicional en León, los panes recién horneados se apilan en una bandeja. El
primero que se vende es el último que se colocó. Simula el proceso de agregar panes a la bandeja
(push), vender uno (pop), y visualizar qué tipo de pan está listo para vender (peek).'''
#Roberto Carlos López Ramirez
#Iniciamos importando la libreria de pila
from Pila import Pila
from os import system
#Definimos la clase Panaderia
class Panaderia:
    #Definimos el constructor de la clase
    def __init__(self):
        self.pila = Pila()
    
    #Definimos el metodo para agregar panes a la bandeja
    def agregar_pan(self, pan):
        self.pila.push(pan)
        print(f"Pan '{pan}' agregado a la bandeja.")
        input("Presione Enter para continuar...")
        system("cls")
    
    #Definimos el metodo para vender un pan
    def vender_pan(self):
        if not self.pila.is_empty():
            pan = self.pila.pop()
            print(f"Pan '{pan}' vendido.")
            input("Presione Enter para continuar...")
            system("cls")
        else:
            print("No hay panes en la bandeja para vender.")
            input("Presione Enter para continuar...")
            system("cls")

#Simulando el proceso de agregar panes a la bandeja, vender uno y visualizar el que está listo para vender
panaderia = Panaderia()
while True:
    print("═════════════ Menú de Opciones ═════════════")
    print("1. Agregar pan")
    print("2. Vender pan")
    print("3. Mostrar pan en la bandeja")
    print("4. Salir")
    print("═════════════════════════════════════════════")
    opcion = input("Seleccione una opción: ")
        
    if opcion == "1":
        pan = input("Ingrese el tipo de pan: ")
        panaderia.agregar_pan(pan)
    elif opcion == "2":
        panaderia.vender_pan()
    elif opcion == "3":
        if not panaderia.pila.is_empty():
            pan = panaderia.pila.obtener_cima()  # Usar el método renombrado
            print(f"Pan en la bandeja: '{pan}'")
            input("Presione Enter para continuar...")
            system("cls")
        else:
            print("No hay panes en la bandeja.")
            input("Presione Enter para continuar...")
            system("cls")
    elif opcion == "4":
        break
    else:
        print("Opción no válida. Intente nuevamente.")
        input("Presione Enter para continuar...")
        system("cls")
