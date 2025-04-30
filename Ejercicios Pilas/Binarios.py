def Convbinario(numero):

    # Creamos una pila vacía para almacenar los restos de la división

    pila = []

    # Mientras el número sea mayor que 0, seguimos dividiéndolo entre 2

    while numero > 0:
        residuo = numero % 2       # Obtenemos el residuo 0 o 1
        pila.append(str(residuo))  # Lo agregamos a la pila como cadena
        numero //= 2               # Dividimos el número por 2 usando división entera

    # Ahora vamos a reconstruir el número binario sacando los elementos de la pila

    binario = ''
    while pila:
        binario += pila.pop()      # Sacamos cada elemento, último en entrar, primero en salir.

    # Mostramos el resultado final con el formato solicitado

    print(f"Salida -> [{binario}]")


# Solicitamos al usuario que introduzca un número entero

entrada = int(input("Entrada -> "))

# Llamamos a la función para convertir el número a binario

Convbinario(entrada)
