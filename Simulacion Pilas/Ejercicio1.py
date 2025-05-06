'''Una oficina de atención ciudadana en una alcaldía municipal en Nicaragua recibe documentos para
revisión. Por cada solicitud, se apilan los documentos entregados en el orden en que llegan. El
personal debe revisar el último documento entregado primero. Se debe simular el proceso de
revisión, utilizando una pila, y permitir agregar nuevos documentos, eliminar el último revisado y
mostrar los pendientes.
'''
#Roberto Carlos López Ramirez
#Iniciamos importando la libreria de pila
from Pila import Pila
from os import system
#Definimos la clase Documentos
class Documentos:
    #Definimos el constructor de la clase
    def __init__(self):
        self.pila = Pila()
    
    #Definimos el metodo para agregar documentos a la pila
    def agregar_documento(self, documento):
        self.pila.push(documento)
        print(f"Documento '{documento}' agregado a la pila.")
        input("Presione Enter para continuar...")
        system("cls")
    
    #Definimos el metodo para eliminar el ultimo documento revisado
    def eliminar_documento(self):
        if not self.pila.is_empty():
            documento = self.pila.pop()
            print(f"Documento '{documento}' eliminado de la pila.")
            input("Presione Enter para continuar...")
            system("cls")
        else:
            print("No hay documentos en la pila para eliminar.")
            input("Presione Enter para continuar...")
            system("cls")
    
    #Definimos el metodo para mostrar los documentos pendientes
    def mostrar_documentos(self):
        if not self.pila.is_empty():  # Corregir la condición
            print("Documentos pendientes en la pila:")
            for documento in self.pila.items():
                print(documento)
            input("Presione Enter para continuar...")
            system("cls")
        else:
            print("No hay documentos pendientes en la pila.")
            input("Presione Enter para continuar...")
            system("cls")
    
    #Definimos el metodo para mostrar el documento en la cima de la pila
    def mostrar_documento_cima(self):
        if not self.pila.is_empty():
            documento = self.pila.peek()  # Usar el método renombrado
            print(f"Documento en la cima de la pila: '{documento}'")
            input("Presione Enter para continuar...")
            system("cls")
        else:
            print("No hay documentos en la pila.")
            input("Presione Enter para continuar...")
            system("cls")


#Creamos una instancia de la clase Documentos
documentos = Documentos()
#Iniciamos un ciclo para mostrar el menu de opciones al usuario
while True:
    #Solicitamos al usuario que ingrese una opcion
    #validamos que la opcion ingresada sea un numero entre 1 y 5
    try:
        print("═════════════ Menú de Documentos ═════════════")
        print("1. Agregar documento")
        print("2. Eliminar último documento revisado")
        print("3. Mostrar documentos pendientes")
        print("4. Mostrar documento en la cima")
        print("5. Salir")
        print("══════════════════════════════════════════════")
        opcion = int(input("Seleccione una opción (1-5): "))
    except ValueError:
        print("Opción inválida. Debe ingresar un número entre 1 y 5.")
        input("Presione Enter para continuar...")
        system("cls")
        continue
    #Verificamos la opcion ingresada por el usuario
    if opcion == 1:
        documento = input("Ingrese el nombre del documento a agregar: ")
        #Validamos que se haya ingresado un documento
        if not documento.strip():
            print("El nombre del documento no puede estar vacío.")
            input("Presione Enter para continuar...")
            system("cls")
            continue
        documentos.agregar_documento(documento)
    elif opcion == 2:
        documentos.eliminar_documento()
    elif opcion == 3:
        documentos.mostrar_documentos()   
    elif opcion == 4:
        documentos.mostrar_documento_cima()
    elif opcion == 5:
        print("Saliendo del programa.")
        break
    else:
        print("Opción inválida. Intente nuevamente.")
        input("Presione Enter para continuar...")
        system("cls")