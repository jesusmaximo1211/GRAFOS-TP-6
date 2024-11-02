class Grafo:
    def __init__(self):
        self.vertices = {}
        self.aristas = []

    def agregar_vertice(self, nombre):
        self.vertices[nombre] = {}

    def agregar_arista(self, origen, destino, distancia):
        
        self.vertices[origen][destino] = distancia
        self.vertices[destino][origen] = distancia
        self.aristas.append((distancia, origen, destino))

    def arbol_expansion_minimo(self):
        aristas_ordenadas = sorted(self.aristas)
        padre = {v: v for v in self.vertices}
        rango = {v: 0 for v in self.vertices}

        def encontrar(v):
            if padre[v] != v:
                padre[v] = encontrar(padre[v])
            return padre[v]

        def unir(v1, v2):
            raiz1 = encontrar(v1)
            raiz2 = encontrar(v2)
            if raiz1 != raiz2:
                if rango[raiz1] > rango[raiz2]:
                    padre[raiz2] = raiz1
                else:
                    padre[raiz1] = raiz2
                    if rango[raiz1] == rango[raiz2]:
                        rango[raiz2] += 1

        arbol_minimo = []
        total_distancia = 0
        for distancia, origen, destino in aristas_ordenadas:
            if encontrar(origen) != encontrar(destino):
                unir(origen, destino)
                arbol_minimo.append((origen, destino, distancia))
                total_distancia += distancia

        return arbol_minimo, total_distancia

    def camino_mas_corto(self, inicio, fin):
        distancias = {v: float('inf') for v in self.vertices}
        distancias[inicio] = 0
        cola_prioridad = [(0, inicio)]
        anteriores = {v: None for v in self.vertices}

        while cola_prioridad:
            distancia_actual, actual = min(cola_prioridad, key=lambda x: x[0])
            cola_prioridad.remove((distancia_actual, actual))

            if actual == fin:
                break

            for vecino, peso in self.vertices[actual].items():
                distancia = distancia_actual + peso
                if distancia < distancias[vecino]:
                    distancias[vecino] = distancia
                    anteriores[vecino] = actual
                    cola_prioridad.append((distancia, vecino))

        camino = []
        actual = fin
        while actual is not None:
            camino.append(actual)
            actual = anteriores[actual]
        camino.reverse()

        return camino, distancias[fin]


casa = Grafo()

ambientes = ["cocina", "comedor", "cochera", "quincho", "baño 1", "baño 2",
             "habitación 1", "habitación 2", "sala de estar", "terraza", "patio"]

for ambiente in ambientes:
    casa.agregar_vertice(ambiente)

casa.agregar_arista("cocina", "comedor", 5)
casa.agregar_arista("cocina", "baño 1", 3)
casa.agregar_arista("cocina", "habitación 1", 7)
casa.agregar_arista("comedor", "sala de estar", 6)
casa.agregar_arista("comedor", "quincho", 4)
casa.agregar_arista("baño 1", "baño 2", 2)
casa.agregar_arista("baño 1", "habitación 1", 4)
casa.agregar_arista("habitación 1", "habitación 2", 5)
casa.agregar_arista("habitación 1", "sala de estar", 8)
casa.agregar_arista("habitación 2", "terraza", 6)
casa.agregar_arista("habitación 2", "patio", 4)
casa.agregar_arista("sala de estar", "terraza", 3)
casa.agregar_arista("terraza", "patio", 4)
casa.agregar_arista("patio", "quincho", 7)
casa.agregar_arista("patio", "cochera", 6)

arbol_minimo, total_cable = casa.arbol_expansion_minimo()
print("Árbol de Expansión Mínima (conexiones):")
for origen, destino, distancia in arbol_minimo:
    print(f"{origen} - {destino}: {distancia} metros")
print(f"Total de metros de cable necesarios: {total_cable}")

camino, distancia_total = casa.camino_mas_corto("habitación 1", "sala de estar")
print("\nCamino más corto de habitación 1 a sala de estar:", " -> ".join(camino))
print(f"Distancia total del cable de red: {distancia_total} metros")
