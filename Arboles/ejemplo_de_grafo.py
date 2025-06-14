
from collections import deque

class Grafo:
    def __init__(self, es_dirigido=False):
        self.es_dirigido = es_dirigido
        self.adyacencia = {}

    def agregar_vertice(self, vertice):
        if vertice not in self.adyacencia:
            self.adyacencia[vertice] = set()

    def agregar_arista(self, origen, destino):
        self.agregar_vertice(origen)
        self.agregar_vertice(destino)
        self.adyacencia[origen].add(destino)
        if not self.es_dirigido:
            self.adyacencia[destino].add(origen)

    def obtener_vecinos(self, vertice):
        return self.adyacencia.get(vertice, set())

    def existe_arista(self, origen, destino):
        return destino in self.adyacencia.get(origen, set())

    def bfs(self, inicio):
        visitados = set()
        cola = deque([inicio])
        while cola:
            vertice = cola.popleft()
            if vertice not in visitados:
                print(vertice)
                visitados.add(vertice)
                cola.extend(self.adyacencia[vertice] - visitados)

    def dfs(self, inicio, visitados=None):
        if visitados is None:
            visitados = set()
        if inicio not in visitados:
            print(inicio)
            visitados.add(inicio)
            for vecino in self.adyacencia[inicio]:
                self.dfs(vecino, visitados)

    def imprimir(self):
        for vertice, vecinos in self.adyacencia.items():
            print(f"{vertice}: {', '.join(vecinos)}")

    def es_conexo(self):
        if not self.adyacencia:
            return True
        visitados = set()
        self.dfs(next(iter(self.adyacencia)), visitados)
        return len(visitados) == len(self.adyacencia)

    def encontrar_camino(self, inicio, fin, camino=None):
        if camino is None:
            camino = []
        camino = camino + [inicio]
        if inicio == fin:
            return camino
        if inicio not in self.adyacencia:
            return None
        for vecino in self.adyacencia[inicio]:
            if vecino not in camino:
                nuevo_camino = self.encontrar_camino(vecino, fin, camino)
                if nuevo_camino:
                    return nuevo_camino
        return None

# Ejemplo de uso:
g = Grafo()
g.agregar_arista("Managua", "Masaya")
g.agregar_arista("Managua", "León")
g.agregar_arista("Masaya", "Granada")
g.agregar_arista("Granada", "Rivas")

print("Lista de adyacencia:")
g.imprimir()

print("\nBúsqueda en amplitud (BFS) desde Managua:")
g.bfs("Managua")

print("\nBúsqueda en profundidad (DFS) desde Managua:")
g.dfs("Managua")

print("\n¿El grafo es conexo?")
print("Sí" if g.es_conexo() else "No")

print("\nCamino de Managua a Rivas:")
camino = g.encontrar_camino("Managua", "Rivas")
print(camino if camino else "No se encontró camino.")
