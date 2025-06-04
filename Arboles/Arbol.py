class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.left = None
        self.right = None

class ArbolBin:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
       self.raiz = self.insertar_recursivo(self.raiz, valor)

    def insertar_recursivo(self, node, valor):
        if node is None:
            return Nodo(valor)

        if valor < node.valor:
            node.left = self.insertar_recursivo(node.left, valor)
        else:
            node.right = self.insertar_recursivo(node.right, valor)
        
        return node
    
    def buscar(self, valor):
        return self.buscar_recursivo(self.raiz, valor)
    
    def buscar_recursivo(self, node, valor):
        if node is None:
            return False
        
        if node.valor == valor:
            return True
        
        elif valor < node.valor:
            return self.buscar_recursivo(node.left, valor)
        else:
            return self.buscar_recursivo(node.right, valor)
    

    def eliminarnodo(self, valor):
        self.raiz = self.eliminar_recursivo(self.raiz, valor)
    
    def eliminar_recursivo(self, node, valor):
        if node is None:
            return node
        
        if valor < node.valor:
            node.left = self.eliminar_recursivo(node.left, valor)
        elif valor > node.valor:
            node.right = self.eliminar_recursivo(node.right, valor)
        else:
            # Nodo con un solo hijo o sin hijos
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            
            # Nodo con dos hijos: obtener el sucesor inorden (el más pequeño del subárbol derecho)
            min_larger_node = self.min_value_node(node.right)
            node.valor = min_larger_node.valor
            node.right = self.eliminar_recursivo(node.right, min_larger_node.valor)

        return node

    def min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current
    

    def inorden(self, node):
        if node is not None:
            self.inorden(node.left)
            print(node.valor, end=' ')
            self.inorden(node.right)
    
    def preorden(self, node):
        if node is not None:
            print(node.valor, end=' ')
            self.preorden(node.left)
            self.preorden(node.right)

    def postorden(self, node):
        if node is not None:
            self.postorden(node.left)
            self.postorden(node.right)
            print(node.valor, end=' ')
