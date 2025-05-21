# Función para verificar si un carácter es un operador
def es_operador(caracter):
    return caracter in "+-*/^"

# Función que devuelve la prioridad de los operadores
def prioridad(operador):
    if operador == '^':
        return 3  # Mayor prioridad: potencia
    elif operador in "*/":
        return 2  # Multiplicación y división 
    elif operador in "+-":
        return 1  # Suma y resta
    return 0      # Si no es operador reconocido

# Función que convierte una expresión en notación infija a postfija
def infijo_a_postfijo(expresion):
    salida = []  # Lista para la expresión en notación postfija
    pila = []    # Pila para operadores
    # Separar paréntesis y dividir en tokens
    tokens = expresion.replace('(', ' ( ').replace(')', ' ) ').split()

    for token in tokens:
        if token.isnumeric():  # Si el token es un número
            salida.append(token)
        elif token == '(':  # Si es paréntesis izquierdo
            pila.append(token)
        elif token == ')':  # Si es paréntesis derecho
            # Desapilar hasta encontrar el paréntesis izquierdo
            while pila and pila[-1] != '(':
                salida.append(pila.pop())
            pila.pop()  # Quitar el '(' de la pila
        elif es_operador(token):  # Si es un operador
            # Desapilar operadores de mayor o igual prioridad (excepto ^ que es asociativo a la derecha)
            while (pila and pila[-1] != '(' and
                   (prioridad(pila[-1]) > prioridad(token) or
                    (prioridad(pila[-1]) == prioridad(token) and token != '^'))):
                salida.append(pila.pop())
            pila.append(token)  # Apilar el operador actual

    # Añadir al resultado los operadores restantes en la pila
    while pila:
        salida.append(pila.pop())

    return salida

# Función que evalúa una expresión postfija (notación polaca inversa)
def evaluar_postfijo(expresion_postfijo):
    pila = []  # Pila para el cálculo

    for token in expresion_postfijo:
        if token.isnumeric():  # Si el token es un número
            pila.append(int(token))
        else:
            # Extraer los dos últimos operandos
            b = pila.pop()
            a = pila.pop()
            # Realizar la operación correspondiente
            if token == '+':
                pila.append(a + b)
            elif token == '-':
                pila.append(a - b)
            elif token == '*':
                pila.append(a * b)
            elif token == '/':
                pila.append(a / b)
            elif token == '^':
                pila.append(a ** b)  # Potencia

    return pila[0]  # Resultado final

# Lista de expresiones en notación infija para evaluar
expresiones = [
    "5 * 4 + ( 9 / 3 + 8 * 2 )",
    "7 + 3 * ( 9 + 5 * 2 ^ 3 - 8 )",
    "4 * ( 2 + 3 - 2 ) * ( 4 + 8 - 5 )",
    "8 + 4 + ( ( 5 ^ 2 + 6 ) * 4 )",
    "6 * 2 + 8 - 3 * 2 / 2"
]

# Procesar cada expresión: convertir a postfijo y evaluar
for i, expr in enumerate(expresiones, start=1):
    postfijo = infijo_a_postfijo(expr)  # Convertir a notación postfija
    resultado = evaluar_postfijo(postfijo)  # Evaluar la expresión
    print(f"Expresión {i}: {expr}")
    print(f"Postfijo: {' '.join(postfijo)}")
    print(f"Resultado: {resultado}\n")
