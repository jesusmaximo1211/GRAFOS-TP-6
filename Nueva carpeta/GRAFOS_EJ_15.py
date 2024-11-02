class Maravilla:
    def __init__(self, nombre, pais, tipo):
        self.nombre = nombre
        self.pais = pais
        self.tipo = tipo  

class Grafo:
    def __init__(self):
        self.vertices = {}
        self.aristas = {}

    def agregar_maravilla(self, nombre, pais, tipo):
        maravilla = Maravilla(nombre, pais, tipo)
        self.vertices[nombre] = maravilla

    def agregar_arista(self, nombre1, nombre2, distancia):
        self.aristas[(nombre1, nombre2)] = distancia
        self.aristas[(nombre2, nombre1)] = distancia  

class GrafoConKruskal(Grafo):
    def arbol_expansion_minimo(self):
        aristas_ordenadas = sorted(self.aristas.items(), key=lambda item: item[1])
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
        for (maravilla1, maravilla2), distancia in aristas_ordenadas:
            if encontrar(maravilla1) != encontrar(maravilla2):
                unir(maravilla1, maravilla2)
                arbol_minimo.append((maravilla1, maravilla2, distancia))

        return arbol_minimo

def paises_con_multiples_maravillas(grafo):
    conteo_paises = {}
    for maravilla in grafo.vertices.values():
        pais = maravilla.pais
        if pais not in conteo_paises:
            conteo_paises[pais] = 0
        conteo_paises[pais] += 1
    return [pais for pais, cantidad in conteo_paises.items() if cantidad > 1]


grafo_con_kruskal = GrafoConKruskal()


maravillas = {
    "Gran Muralla China": ("China", "arquitectónica"),
    "Petra": ("Jordania", "arquitectónica"),
    "Cristo Redentor": ("Brasil", "arquitectónica"),
    "Machu Picchu": ("Perú", "arquitectónica"),
    "Chichén Itzá": ("México", "arquitectónica"),
    "Coliseo de Roma": ("Italia", "arquitectónica"),
    "Taj Mahal": ("India", "arquitectónica"),
}
for nombre, (pais, tipo) in maravillas.items():
    grafo_con_kruskal.agregar_maravilla(nombre, pais, tipo)

distancias = {
    ("Gran Muralla China", "Petra"): 5983,
    ("Gran Muralla China", "Cristo Redentor"): 17655,
    ("Gran Muralla China", "Machu Picchu"): 17163,
    ("Gran Muralla China", "Chichén Itzá"): 13152,
    ("Gran Muralla China", "Coliseo de Roma"): 8124,
    ("Gran Muralla China", "Taj Mahal"): 3616,
    ("Petra", "Cristo Redentor"): 11047,
    ("Petra", "Machu Picchu"): 12639,
    ("Petra", "Chichén Itzá"): 11873,
    ("Petra", "Coliseo de Roma"): 2328,
    ("Petra", "Taj Mahal"): 4272,
    ("Cristo Redentor", "Machu Picchu"): 3250,
    ("Cristo Redentor", "Chichén Itzá"): 6580,
    ("Cristo Redentor", "Coliseo de Roma"): 9171,
    ("Cristo Redentor", "Taj Mahal"): 14585,
    ("Machu Picchu", "Chichén Itzá"): 4163,
    ("Machu Picchu", "Coliseo de Roma"): 10729,
    ("Machu Picchu", "Taj Mahal"): 17346,
    ("Chichén Itzá", "Coliseo de Roma"): 9485,
    ("Chichén Itzá", "Taj Mahal"): 15131,
    ("Coliseo de Roma", "Taj Mahal"): 6570
}
for (maravilla1, maravilla2), distancia in distancias.items():
    grafo_con_kruskal.agregar_arista(maravilla1, maravilla2, distancia)

arbol_minimo = grafo_con_kruskal.arbol_expansion_minimo()
print("Árbol de Expansión Mínimo:")
for maravilla1, maravilla2, distancia in arbol_minimo:
    print(f"{maravilla1} - {maravilla2}: {distancia} km")


paises_multiples_maravillas = paises_con_multiples_maravillas(grafo_con_kruskal)
print("Países con más de una maravilla arquitectónica:", paises_multiples_maravillas)
