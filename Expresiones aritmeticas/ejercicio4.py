class Nodo:
    def __init__(self, nombre, prioridad):
        self.nombre = nombre
        self.prioridad = prioridad

    def __repr__(self):
        return f"{self.nombre} (prioridad {self.prioridad})"

class ColaPrioridad:
    def __init__(self):
        self.cola = []

    def insertar(self, elemento):
        for i in range(len(self.cola)):
            if elemento.prioridad < self.cola[i].prioridad:
                self.cola.insert(i, elemento)
                return
        self.cola.append(elemento)

    def eliminar(self):
        return self.cola.pop(0) if self.cola else None

    def mostrar(self):
        return '\n'.join(str(e) for e in self.cola) if self.cola else "Cola vacía"

def main():
    cola = ColaPrioridad()
    
    while True:
        print("\n--- COLA DE PRIORIDADES ---")
        print("1. Agregar elemento")
        print("2. Eliminar elemento de mayor prioridad")
        print("3. Mostrar cola")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Nombre del elemento: ")
            try:
                prioridad = int(input("Prioridad (número entero): "))
                cola.insertar(Nodo(nombre, prioridad))
                print(f"Elemento '{nombre}' agregado con prioridad {prioridad}.")
            except ValueError:
                print("Error: La prioridad debe ser un número entero.")
                continue

        elif opcion == "2":
            eliminado = cola.eliminar()
            if eliminado:
                print(f"Elemento eliminado: {eliminado}")
            else:
                print("La cola está vacía.")

        elif opcion == "3":
            print("\nElementos en la cola:")
            print(cola.mostrar())

        elif opcion == "4":
            print("Saliendo del programa...")
            break

        else:
            print("Opción inválida, por favor intente de nuevo.")

if __name__ == "__main__":
    main()
