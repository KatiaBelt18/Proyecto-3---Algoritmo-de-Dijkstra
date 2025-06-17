from Nodo import *
from Arista import *
import random
import heapq


'Clase Grafo'
class Grafo: 
    def __init__(self):
        self.nodos = []         # Lista para almacenar los nodos del grafo
        self.aristas = []       # Lista para almacenar las aristas como pares de nodos
        self.atributos = {}     # Diccionario para atributos adicionales (opcional, no se usa aquí)
        self.adyacencias = {}

    def agregar_Nodo(self, n):
        # Agrega un nodo al grafo si no está ya presente
        if n not in self.nodos:
            nodo = Nodo(n)                          # Crea una instancia de Nodo (se espera que exista esta clase)
            self.nodos.append(nodo.identificador)   # Agrega el identificador del nodo a la lista de nodos

    def agregar_Arista(self, origen, destino):
        if origen in self.nodos and destino in self.nodos:
            peso = random.randint(1, 100)               # Generar peso aleatorio entre 1 y 100
            arista = Arista(origen, destino, peso)      # Pasar el peso a la Arista
            self.aristas.append(arista)                 # Guardar objeto Arista completo


    def mostrar_grafo(self):
        # Imprime los nodos del grafo
        print("Nodos:")
        for nodo in self.nodos:
            print(f"  Nodo {nodo}")

        # Imprime las aristas del grafo
        print("\nAristas:")
        for arista in self.aristas:
            print(f"  {arista.origen} -> {arista.destino} (peso: {arista.peso})")
    

    def exportar_a_gv(self, nombre_archivo, nombre_grafo="Grafo"):
        with open(nombre_archivo, 'w') as f:
            f.write(f'digraph {nombre_grafo} {{\n')

            # Escribir los nodos
            for nodo in self.nodos:
                f.write(f'    {nodo}[label="N{nodo}"];\n')

            # Escribir las aristas con sus pesos
            for arista in self.aristas:
                f.write(f'    {arista.origen} -> {arista.destino}[label="{arista.peso}"];\n')

            f.write('}\n')

        print(f"Grafo exportado exitosamente en formato Graphviz a {nombre_archivo}")

    def exportar_dijkstra_gv(self, archivo, inicio, padres):
        """
        Exporta el grafo en formato .gv para Gephi, 
        coloreando en rojo las aristas que forman el árbol de caminos más cortos desde 'inicio'.

        Args:
            archivo (str): nombre del archivo de salida.
            inicio (int): nodo desde donde se calcula Dijkstra.
            padres (dict): diccionario con el padre de cada nodo.
        """
        with open(archivo, 'w') as f:
            f.write("graph Grafo {\n")

            # Escribir nodos
            for nodo in self.nodos:
                f.write(f'    {nodo} [label="N{nodo}"];\n')

            ya_escritas = set()

            for arista in self.aristas:
                u, v = arista.origen, arista.destino
                peso = arista.peso

                # Evitar duplicados
                if (v, u) in ya_escritas:
                    continue
                ya_escritas.add((u, v))

                # Verifica si esta arista está en el árbol de caminos más cortos
                es_roja = (padres.get(v) == u) or (padres.get(u) == v)
                color = "red" if es_roja else "black"

                f.write(f'    {u} -- {v} [label="{peso}", color={color}];\n')

            f.write("}\n")



    def construir_adyacencias(self):
        self.adyacencias = {nodo: [] for nodo in self.nodos}
        for arista in self.aristas:
            u, v, w = arista.origen, arista.destino, arista.peso
            self.adyacencias[u].append((v, w))
            self.adyacencias[v].append((u, w))  # si el grafo no es dirigido


    def dijkstra(self, inicio):
        """
        Algoritmo de Dijkstra para obtener el árbol de caminos más cortos desde 'inicio'.

        Returns:
            arbol (Grafo): subgrafo con las aristas del camino más corto
            distancias (dict): distancia mínima desde inicio a cada nodo
            padres (dict): padre de cada nodo en el camino más corto
        """

        distancias = {nodo: float('inf') for nodo in self.nodos}
        distancias[inicio] = 0
        padres = {}
        visitados = set()
        heap = [(0, inicio)]

        # Árbol de caminos más cortos
        arbol = Grafo()
        for nodo in self.nodos:
            arbol.agregar_Nodo(nodo)

        while heap:
            dist_actual, actual = heapq.heappop(heap)
            if actual in visitados:
                continue
            visitados.add(actual)

            for arista in self.aristas:
                # Grafo no dirigido: revisamos ambos sentidos
                if arista.origen == actual:
                    vecino = arista.destino
                elif arista.destino == actual:
                    vecino = arista.origen
                else:
                    continue

                if vecino in visitados:
                    continue

                nueva_dist = dist_actual + arista.peso
                if nueva_dist < distancias[vecino]:
                    distancias[vecino] = nueva_dist
                    padres[vecino] = actual
                    heapq.heappush(heap, (nueva_dist, vecino))

                    # Agrega la arista al árbol de caminos más cortos
                    arbol.agregar_Arista(actual, vecino)

        return arbol, distancias, padres
 

    """
    METODOS DE LA CLASE GRAFO PARA LOS ALGORITMOS BFS Y DFS
    """
    #Búsqueda a lo ancho 
    'Genera un árbol a partir de un grao. Explora desde s y hacia fuera'
    'en todas direcciones posibles, añadiendo nodos una capa a la vez.'
    'param: self -> grafo'
    'param: s    -> nodo'

    def BFS(self, s):
        print("Algoritmo BFS\n")
        
        layer = []                # Lista de capas (cada capa es una lista de nodos)
        cont_capa = 0             # Contador de capa
        nodo_descubierto = []     # Lista para nodos descubiertos
        padres = {}               # Diccionario de descubridores
        nodeSource = None         # Nodo fuente

        if s not in self.nodos:
            print("No se encuentra el nodo en el modelo")
            return False

        nodeSource = s
        nodo_descubierto.append(nodeSource)
        layer.append([nodeSource])  # Capa 0

        while layer[cont_capa]:
            nueva_capa = []

            for u in layer[cont_capa]:
                vecinos = []
                for arista in self.aristas:
                    a, b = arista
                    if a == u and b not in nodo_descubierto:
                        vecinos.append(b)
                    elif b == u and a not in nodo_descubierto:
                        vecinos.append(a)

                for v in vecinos:
                    if v not in nodo_descubierto:
                        nodo_descubierto.append(v)
                        nueva_capa.append(v)
                        padres[v] = u  # u descubrió a v

            layer.append(nueva_capa)
            cont_capa += 1

        if not layer[-1]:
            layer.pop()

        for i, capa in enumerate(layer):
            print(f"Capa {i}: {capa}")

        # Guardar resultado del recorrido
        self.bfs_resultado = {
            'capas': layer,
            'padres': padres,
            'visitados': nodo_descubierto
        }

        return self.bfs_resultado

                

    #Busqueda en profundidad
    def DFS_recursiva(self, s, explorados=None, arbol=None):
        """
        DFS recursiva desde un nodo s.
        - s: nodo origen
        - explorados: conjunto de nodos visitados
        - arbol: lista de aristas (tuplas) que forman el árbol DFS
        """
        if s not in self.nodos:
            print("El nodo no pertenece al modelo")
            return False

        if explorados is None:
            explorados = set()
        if arbol is None:
            arbol = []

        explorados.add(s)

        # Obtener vecinos del nodo actual
        vecinos = []
        for a, b in self.aristas:
            if a == s and b not in explorados:
                vecinos.append(b)
            elif b == s and a not in explorados:
                vecinos.append(a)

        # Recorrer vecinos no explorados
        for v in vecinos:
            if v not in explorados:
                arbol.append((s, v))  # Agregar arista al árbol DFS
                self.DFS_recursiva(v, explorados, arbol)

        return arbol

        
    def DFS_iterativa(self, s):
        if s not in self.nodos:
            print("El nodo no pertenece al modelo")
            return False

        visitados = set()
        arbol_dfs = []
        stack = [(s, None)]  # Pila de tuplas (nodo, padre), el padre de s es None

        while stack:
            u, padre = stack.pop()

            if u not in visitados:
                visitados.add(u)

                if padre is not None:
                    arbol_dfs.append((padre, u))  # Registrar la arista desde el padre a u

                # Buscar vecinos no visitados
                vecinos = []
                for a, b in self.aristas:
                    if a == u and b not in visitados:
                        vecinos.append(b)
                    elif b == u and a not in visitados:
                        vecinos.append(a)

                # Agregar vecinos con el nodo actual como padre
                for v in reversed(vecinos):  # reversed para DFS correcto
                    stack.append((v, u))

        return arbol_dfs
    


        
    

    



        
