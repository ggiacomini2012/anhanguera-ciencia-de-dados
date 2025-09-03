# ==============================================================================
# MÓDULO: ALGORITMOS DE GRAFOS PONDERADOS
# DESCRIÇÃO: Este arquivo contém as implementações dos algoritmos de Kruskal e Dijkstra,
#            além de uma breve explicação do algoritmo de Prim.
#            É projetado para demonstrar a aplicação desses algoritmos na resolução de
#            problemas de otimização em grafos.
# ==============================================================================
import sys

# --- Algoritmo de Kruskal -----------------------------------------------------
# O algoritmo de Kruskal é utilizado para encontrar a Árvore Geradora Mínima (MST)
# de um grafo. Ele ordena as arestas pelo peso e as adiciona à MST se não formarem um ciclo.
# A detecção de ciclos é feita eficientemente com a estrutura de dados Union-Find.
# -----------------------------------------------------------------------------
class GrafoKruskal:
    """
    Representa um grafo para a aplicação do algoritmo de Kruskal.
    """
    def __init__(self, vertices):
        self.V = vertices
        self.grafo = []

    def adicionar_aresta(self, u, v, w):
        """Adiciona uma aresta com peso w entre os vértices u e v."""
        self.grafo.append([u, v, w])

    def encontrar(self, pai, i):
        """Encontra o representante do subconjunto ao qual o elemento i pertence."""
        if pai[i] == i:
            return i
        return self.encontrar(pai, pai[i])

    def unir(self, pai, rank, x, y):
        """Realiza a união de dois subconjuntos x e y, otimizada por rank."""
        raiz_x = self.encontrar(pai, x)
        raiz_y = self.encontrar(pai, y)

        if rank[raiz_x] < rank[raiz_y]:
            pai[raiz_x] = raiz_y
        elif rank[raiz_x] > rank[raiz_y]:
            pai[raiz_y] = raiz_x
        else:
            pai[raiz_y] = raiz_x
            rank[raiz_x] += 1

    def kruskal(self):
        """
        Executa o algoritmo de Kruskal e imprime as arestas da MST e o custo total.
        """
        resultado = []
        i, e = 0, 0

        self.grafo = sorted(self.grafo, key=lambda item: item[2])

        pai = []
        rank = []

        for no in range(self.V):
            pai.append(no)
            rank.append(0)

        while e < self.V - 1:
            u, v, w = self.grafo[i]
            i = i + 1
            x = self.encontrar(pai, u)
            y = self.encontrar(pai, v)

            if x != y:
                e = e + 1
                resultado.append([u, v, w])
                self.unir(pai, rank, x, y)

        print("\n--- Algoritmo de Kruskal: Árvore Geradora Mínima ---")
        custo_total = 0
        for u, v, peso in resultado:
            print(f"Aresta: {u} - {v} | Custo: {peso}")
            custo_total += peso
        print(f"Custo Total da MST: {custo_total}")

# --- Algoritmo de Prim --------------------------------------------------------
# O algoritmo de Prim também encontra a MST. Ele funciona de forma incremental,
# expandindo a árvore a partir de um vértice inicial, sempre adicionando a
# aresta de menor peso que conecta um vértice na árvore a um vértice fora dela.
# A implementação completa é mais complexa e usa uma fila de prioridade, por isso
# não está incluída neste código para focar nos algoritmos principais descritos.
# O custo total e o resultado final, no entanto, são os mesmos do Kruskal.
# -----------------------------------------------------------------------------

# --- Algoritmo de Dijkstra ----------------------------------------------------
# O algoritmo de Dijkstra é usado para encontrar o caminho mais curto de um
# vértice de origem a todos os outros vértices em um grafo com pesos não negativos.
# Ele mantém um registro das distâncias mínimas encontradas até agora e as atualiza
# iterativamente.
# -----------------------------------------------------------------------------
class GrafoDijkstra:
    """
    Representa um grafo para a aplicação do algoritmo de Dijkstra.
    """
    def __init__(self, vertices):
        self.V = vertices
        self.grafo = [[0] * vertices for _ in range(vertices)]

    def distancia_minima(self, distancias, visitados):
        """Encontra o vértice com a menor distância que ainda não foi visitado."""
        minimo = sys.maxsize
        vertice_minimo = -1

        for v in range(self.V):
            if distancias[v] < minimo and not visitados[v]:
                minimo = distancias[v]
                vertice_minimo = v

        return vertice_minimo

    def imprimir_caminho(self, antecessores, j):
        """Imprime o caminho mais curto do vértice de origem até o vértice j."""
        if antecessores[j] == -1:
            print(j, end="")
            return
        self.imprimir_caminho(antecessores, antecessores[j])
        print(f" -> {j}", end="")

    def dijkstra(self, origem):
        """
        Executa o algoritmo de Dijkstra a partir de um vértice de origem.
        Imprime as distâncias mínimas e os caminhos.
        """
        distancias = [sys.maxsize] * self.V
        distancias[origem] = 0
        visitados = [False] * self.V
        antecessores = [-1] * self.V

        for _ in range(self.V):
            u = self.distancia_minima(distancias, visitados)
            if u == -1:
                break
            
            visitados[u] = True

            for v in range(self.V):
                if (
                    self.grafo[u][v] > 0
                    and not visitados[v]
                    and distancias[v] > distancias[u] + self.grafo[u][v]
                ):
                    distancias[v] = distancias[u] + self.grafo[u][v]
                    antecessores[v] = u

        print("\n--- Algoritmo de Dijkstra: Caminho Mais Curto ---")
        print("Vértice | Distância da Origem | Caminho Mais Curto")
        print("-" * 50)
        for i in range(self.V):
            print(f"{i:^7} | {distancias[i]:^19} | ", end="")
            self.imprimir_caminho(antecessores, i)
            print()

# ==============================================================================
# EXEMPLOS DE USO
# ==============================================================================
if __name__ == "__main__":
    # --- Exemplo de Kruskal (Chalés no Hotel Fazenda) ---
    g_kruskal = GrafoKruskal(4)
    g_kruskal.adicionar_aresta(0, 1, 10)
    g_kruskal.adicionar_aresta(0, 2, 6)
    g_kruskal.adicionar_aresta(0, 3, 5)
    g_kruskal.adicionar_aresta(1, 3, 15)
    g_kruskal.adicionar_aresta(2, 3, 4)
    g_kruskal.kruskal()

    # --- Exemplo de Dijkstra (Rotas de Viagem) ---
    g_dijkstra = GrafoDijkstra(9)
    g_dijkstra.grafo = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
                        [4, 0, 8, 0, 0, 0, 0, 11, 0],
                        [0, 8, 0, 7, 0, 4, 0, 0, 2],
                        [0, 0, 7, 0, 9, 14, 0, 0, 0],
                        [0, 0, 0, 9, 0, 10, 0, 0, 0],
                        [0, 0, 4, 14, 10, 0, 2, 0, 0],
                        [0, 0, 0, 0, 0, 2, 0, 1, 6],
                        [8, 11, 0, 0, 0, 0, 1, 0, 7],
                        [0, 0, 2, 0, 0, 0, 6, 7, 0]]
    
    g_dijkstra.dijkstra(0)