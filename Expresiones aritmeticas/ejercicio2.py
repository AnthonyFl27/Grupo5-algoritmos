class Pila:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def is_empty(self):
        return len(self.items) == 0

def parentesis_balanceados(cadena):
    pila = Pila()
    pares = {')': '(', '}': '{', ']': '['}

    for caracter in cadena:
        if caracter in '({[':
            pila.push(caracter)
        elif caracter in ')}]':
            if pila.is_empty() or pila.pop() != pares[caracter]:
                return False
    return pila.is_empty()

# --- Ejecución interactiva ---
if __name__ == "__main__":
    cadena = input("Ingrese una cadena con paréntesis: ")
    if parentesis_balanceados(cadena):
        print("✅ Los paréntesis están balanceados.")
    else:
        print("❌ Los paréntesis NO están balanceados.")
