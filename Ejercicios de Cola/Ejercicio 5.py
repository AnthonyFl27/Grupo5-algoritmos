'''Ejercicio #5: Gestión de acceso a archivos en un servidor 
Imagina un servidor de archivos en una red donde varios usuarios solicitan acceso a un mismo 
archivo compartido para su lectura. Para evitar conflictos o bloqueos, las solicitudes se atienden 
en el orden en que llegan. Diseña un programa en Python que simule este comportamiento 
utilizando una cola. El programa debe permitir registrar solicitudes de acceso (nombre del 
usuario y archivo solicitado), mostrar qué usuario está accediendo al archivo y eliminar la 
solicitud una vez atendida. También debe permitir consultar la lista de solicitudes pendientes.'''
from os import system
import Modulo
cola = Modulo.Cola()

while True:
    try:
        print("1. Solicitar acceso a un archivo")
        print("2. Mostrar usuario accediendo al archivo en cola")
        print("3. Eliminar solicitud atendida")
        print("4. Consultar solicitudes pendientes")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")
    
        if opcion == "1":
            usuario = input("Ingrese el nombre del usuario: ")
            archivo = input("Ingrese el nombre del archivo: ")
            cola.Insertar((usuario, archivo))
            print(f"Solicitud de acceso registrada para {usuario} al archivo {archivo}.")
            input("Presione Enter para continuar...")
            system("cls")
            
        elif opcion == "2":
            if cola.frente is not None:
                usuario, archivo = cola.frente.dato
                print(f"Usuario accediendo al archivo: {usuario} ({archivo})")
                input("Presione Enter para continuar...")
                system("cls")
            else:
                print("No hay solicitudes pendientes.")
                input("Presione Enter para continuar...")
                system("cls")
                
        elif opcion == "3":
            if cola.frente is not None:
                usuario, archivo = cola.Eliminar()
                print(f"Solicitud atendida y eliminada para {usuario} al archivo {archivo}.")
                input("Presione Enter para continuar...")
                system("cls")
            else:
                print("No hay solicitudes pendientes.")
                input("Presione Enter para continuar...")
                system("cls")
                
        elif opcion == "4":
            if cola.frente is not None:
                print("Solicitudes pendientes:")
                actual = cola.frente
                while actual is not None:
                    usuario, archivo = actual.dato
                    print(f"- Usuario: {usuario}, Archivo: {archivo}")
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