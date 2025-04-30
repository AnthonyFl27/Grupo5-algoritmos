def ordena(pila):
    pila_aux = []
    while pila:
        tmp = pila.pop()
        while pila_aux and pila_aux[-1] > tmp:
            pila.append(pila_aux.pop())
        pila_aux.append(tmp)
    while pila_aux:
        pila.append(pila_aux.pop())
    return pila

# Pila global
pila = []

def mostrar_menu():
    print("\n--- MENÚ ---")
    print("1. Agregar número a la pila")
    print("2. Mostrar pila actual")
    print("3. Ordenar pila de mayor a menor")
    print("4. Vaciar pila")
    print("5. Salir")

while True:
    mostrar_menu()
    opcion = input("Elige una opción: ")

    if opcion == "1":
        valor = int(input("Ingresa un número entero: "))
        pila.append(valor)
    elif opcion == "2":
        print("Pila actual:", pila)
    elif opcion == "3":
        pila = ordena(pila)
        print("Pila ordenada:", pila)
    elif opcion == "4":
        pila.clear()
        print("Pila vaciada.")
    elif opcion == "5":
        print("Adiós.")
        break
    else:
        print("Opción no válida. Intenta de nuevo.")
