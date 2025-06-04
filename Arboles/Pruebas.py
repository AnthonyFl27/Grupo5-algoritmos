from os import system
from Arbol import ArbolBin
from Arbol import Nodo

print("Arbol Binario de Búsqueda")
arbol = ArbolBin()
valores = input("Ingresa los valores que deseas insertar separados por espacios: ").split()
for valor in valores:
    arbol.insertar(valor)

while True:
    print("Menu de opciones:")
    print("1. Buscar un valor")
    print("2. Insertar uno o varios valores")
    print("3. Eliminar un valor")
    print("4. Recorrido en inorden")
    print("5. Recorrido en preorden")
    print("6. Recorrido en postorden")
    print("7. Salir")
    opcion = input("Selecciona una opción (1-7): ")
    
    if opcion == '1':
        valor = input("Ingresa el valor a buscar: ")
        if arbol.buscar(valor):
            print(f"El valor {valor} está en el árbol.")
        else:
            print(f"El valor {valor} no está en el árbol.")
        input("Presiona Enter para continuar...")
        system("cls")

    elif opcion == '2':
        opc = input("¿Deseas insertar un solo valor (1) o varios valores (2)? ")
        if opc == '1':
            valor = input("Ingresa el valor a insertar: ")
            arbol.insertar(valor)
            print(f"Valor {valor} insertado.")
        elif opc == '2':
            valores = input("Ingresa los valores separados por espacios: ").split()
            for valor in valores:
                arbol.raiz = arbol.insertar_recursivo(arbol.raiz, valor)
            print("Valores insertados.")
        else:
            print("Opción no válida.")
        input("Presiona Enter para continuar...")
        system("cls")
    
    elif opcion == '3':
        valor = input("Ingresa el valor a eliminar: ")
        if arbol.buscar(valor):
            print(f"Valor {valor} eliminado.")
            arbol.eliminarnodo(valor)
        else:
            print(f"El valor {valor} no se encontró en el árbol.")
        input("Presiona Enter para continuar...")
        system("cls")

    elif opcion == '4':
        print("Recorrido en inorden:")
        arbol.inorden(arbol.raiz)
        print()
        input("Presiona Enter para continuar...")
        system("cls")

    elif opcion == '5':
        print("Recorrido en preorden:")
        arbol.preorden(arbol.raiz)
        print()
        input("Presiona Enter para continuar...")
        system("cls")

    elif opcion == '6':
        print("Recorrido en postorden:")
        arbol.postorden(arbol.raiz)
        print()
        input("Presiona Enter para continuar...")
        system("cls")
    
    elif opcion == '7':
        print("Saliendo del programa.")
        input("Presiona Enter para salir...")
        system("cls")
        break

    else:
        print("Opción no válida. Inténtalo de nuevo.")
        input("Presiona Enter para continuar...")
        system("cls")
