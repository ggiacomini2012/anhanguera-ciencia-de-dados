# ==============================================================================
# Módulo de Estruturas de Dados e Algoritmos: Grafos em Python
# ==============================================================================
# Este script Python serve como um guia prático e completo para a unidade de ensino
# sobre Grafos. Ele aborda a representação de grafos, operações básicas,
# algoritmos de busca e algoritmos para problemas de caminho mais curto e
# árvore geradora mínima.
#
# Cada função e classe é cuidadosamente comentada para facilitar a compreensão
# dos conceitos teóricos.
#
# ==============================================================================

import heapq

class Grafo:
    """
    Classe para representar um grafo usando uma lista de adjacências.
    A estrutura de dados principal é um dicionário onde as chaves são os vértices
    e os valores são dicionários de vértices adjacentes e seus respectivos pesos.
    """
    def __init__(self):
        self.grafo = {}

    def adicionar_vertice(self, vertice):
        """Adiciona um novo vértice ao grafo."""
        if vertice not in self.grafo:
            self.grafo[vertice] = {}
            print(f"Vértice '{vertice}' adicionado.")
        else:
            print(f"Vértice '{vertice}' já existe.")

    def adicionar_aresta(self, origem, destino, peso=1):
        """
        Adiciona uma aresta (ponderada) entre dois vértices.
        A aresta é bidirecional (não dirigida) por padrão.
        """
        if origem in self.grafo and destino in self.grafo:
            self.grafo[origem][destino] = peso
            self.grafo[destino][origem] = peso
            print(f"Aresta adicionada entre '{origem}' e '{destino}' com peso {peso}.")
        else:
            print(f"Erro: Um ou ambos os vértices '{origem}', '{destino}' não existem.")

    def remover_vertice(self, vertice):
        """Remove um vértice e todas as arestas conectadas a ele."""
        if vertice in self.grafo:
            # Remove o vértice da lista de adjacências
            del self.grafo[vertice]
            # Remove todas as arestas que apontam para o vértice removido
            for outro_vertice in self.grafo:
                if vertice in self.grafo[outro_vertice]:
                    del self.grafo[outro_vertice][vertice]
            print(f"Vértice '{vertice}' e suas arestas foram removidos.")
        else:
            print(f"Erro: Vértice '{vertice}' não encontrado.")

    def remover_aresta(self, origem, destino):
        """Remove uma aresta entre dois vértices."""
        if origem in self.grafo and destino in self.grafo[origem]:
            del self.grafo[origem][destino]
            del self.grafo[destino][origem] # Bidirecional
            print(f"Aresta entre '{origem}' e '{destino}' removida.")
        else:
            print(f"Erro: Aresta entre '{origem}' e '{destino}' não existe.")

    def mostrar_grafo(self):
        """Imprime a representação do grafo."""
        print("\n--- Representação do Grafo ---")
        for vertice, vizinhos in self.grafo.items():
            print(f"Vértice {vertice}: {vizinhos}")
        print("----------------------------")

# ==============================================================================
# Algoritmos de Busca em Grafos
# ==============================================================================

def busca_em_largura(grafo, inicio):
    """
    Implementação do algoritmo de Busca em Largura (BFS).
    Explora os vizinhos do nó atual antes de se mover para o próximo nível.
    """
    print("\n--- Executando Busca em Largura (BFS) ---")
    visitados = set()
    fila = [inicio]
    caminho = []

    visitados.add(inicio)

    while fila:
        vertice_atual = fila.pop(0)
        caminho.append(vertice_atual)

        for vizinho in grafo.grafo[vertice_atual]:
            if vizinho not in visitados:
                visitados.add(vizinho)
                fila.append(vizinho)

    return caminho

def busca_em_profundidade(grafo, inicio):
    """
    Implementação do algoritmo de Busca em Profundidade (DFS).
    Explora o mais profundamente possível em cada ramo antes de voltar.
    """
    print("\n--- Executando Busca em Profundidade (DFS) ---")
    visitados = set()
    pilha = [inicio]
    caminho = []

    while pilha:
        vertice_atual = pilha.pop()
        if vertice_atual not in visitados:
            visitados.add(vertice_atual)
            caminho.append(vertice_atual)

            # Para um caminho consistente, os vizinhos podem ser adicionados em ordem reversa
            for vizinho in sorted(grafo.grafo[vertice_atual].keys(), reverse=True):
                if vizinho not in visitados:
                    pilha.append(vizinho)
    
    return caminho

# ==============================================================================
# Algoritmo de Dijkstra para o Problema da Rota de Logística
# ==============================================================================

def dijkstra(grafo, inicio):
    """
    Algoritmo de Dijkstra para encontrar o caminho mais curto de um
    vértice inicial para todos os outros vértices.
    """
    print(f"\n--- Executando Algoritmo de Dijkstra a partir do vértice '{inicio}' ---")
    distancias = {vertice: float('infinity') for vertice in grafo.grafo}
    distancias[inicio] = 0
    caminhos = {vertice: None for vertice in grafo.grafo}
    fila_prioridade = [(0, inicio)]

    while fila_prioridade:
        distancia_atual, vertice_atual = heapq.heappop(fila_prioridade)

        if distancia_atual > distancias[vertice_atual]:
            continue

        for vizinho, peso in grafo.grafo[vertice_atual].items():
            distancia = distancia_atual + peso
            if distancia < distancias[vizinho]:
                distancias[vizinho] = distancia
                caminhos[vizinho] = vertice_atual
                heapq.heappush(fila_prioridade, (distancia, vizinho))

    return distancias, caminhos

def reconstruir_caminho(caminhos, inicio, destino):
    """Reconstrói o caminho mais curto a partir do resultado de Dijkstra."""
    caminho = []
    vertice_atual = destino
    while vertice_atual is not None:
        caminho.insert(0, vertice_atual)
        if vertice_atual == inicio:
            break
        vertice_atual = caminhos.get(vertice_atual)
    
    if caminho[0] != inicio:
        return None  # Não foi possível encontrar o caminho
    
    return caminho

# ==============================================================================
# Algoritmo de Kruskal para Árvore Geradora Mínima (AGM)
# ==============================================================================

class DSU:
    """Estrutura de Dados Disjoint Set Union (União-Busca) para Kruskal."""
    def __init__(self, vertices):
        self.pai = {vertice: vertice for vertice in vertices}
        self.rank = {vertice: 0 for vertice in vertices}

    def encontrar(self, i):
        """Encontra a raiz do conjunto ao qual o elemento 'i' pertence."""
        if self.pai[i] == i:
            return i
        self.pai[i] = self.encontrar(self.pai[i])
        return self.pai[i]

    def uniao(self, i, j):
        """Une os conjuntos que contêm 'i' e 'j'."""
        raiz_i = self.encontrar(i)
        raiz_j = self.encontrar(j)
        if raiz_i != raiz_j:
            if self.rank[raiz_i] < self.rank[raiz_j]:
                self.pai[raiz_i] = raiz_j
            elif self.rank[raiz_i] > self.rank[raiz_j]:
                self.pai[raiz_j] = raiz_i
            else:
                self.pai[raiz_j] = raiz_i
                self.rank[raiz_i] += 1
            return True
        return False

def kruskal(grafo):
    """
    Algoritmo de Kruskal para encontrar a Árvore Geradora Mínima (AGM).
    """
    print("\n--- Executando Algoritmo de Kruskal (AGM) ---")
    arestas = []
    for origem, vizinhos in grafo.grafo.items():
        for destino, peso in vizinhos.items():
            if (origem, destino, peso) not in arestas and (destino, origem, peso) not in arestas:
                arestas.append((peso, origem, destino))
    
    # Ordena as arestas por peso
    arestas.sort()
    
    agm = []
    dsu = DSU(grafo.grafo.keys())
    
    for peso, origem, destino in arestas:
        if dsu.uniao(origem, destino):
            agm.append((origem, destino, peso))
            
    return agm

# ==============================================================================
# Demonstração Prática: Aplicação na Otimização de Rotas de Logística
# ==============================================================================
if __name__ == '__main__':
    print("==============================================================================")
    print("                 Iniciando a Demonstração da Aula de Grafos                   ")
    print("==============================================================================")

    # 1. Construção do Grafo
    print("\n-- Construindo o Grafo da Empresa de Logística --")
    empresa_logistica = Grafo()
    vertices = ['D', 'A', 'B', 'C', 'E', 'F']
    for v in vertices:
        empresa_logistica.adicionar_vertice(v)

    empresa_logistica.adicionar_aresta('D', 'A', 2)
    empresa_logistica.adicionar_aresta('D', 'B', 4)
    empresa_logistica.adicionar_aresta('A', 'C', 1)
    empresa_logistica.adicionar_aresta('A', 'B', 3)
    empresa_logistica.adicionar_aresta('B', 'E', 2)
    empresa_logistica.adicionar_aresta('C', 'F', 4)
    empresa_logistica.adicionar_aresta('E', 'F', 3)

    empresa_logistica.mostrar_grafo()

    # 2. Resolução do Desafio com o Algoritmo de Dijkstra
    print("\n-- Desafio: Rota Mais Curta do Depósito (D) para Todos os Pontos --")
    distancias_dijkstra, caminhos_dijkstra = dijkstra(empresa_logistica, 'D')

    print("\nDistâncias mais curtas do depósito 'D' para cada ponto:")
    for vertice, distancia in distancias_dijkstra.items():
        print(f"  -> Para '{vertice}': Distância de {distancia} km")

    print("\nCaminhos mais curtos para cada ponto:")
    for destino in distancias_dijkstra.keys():
        if destino != 'D':
            caminho_final = reconstruir_caminho(caminhos_dijkstra, 'D', destino)
            print(f"  -> Rota de 'D' para '{destino}': {' -> '.join(caminho_final)} (Total: {distancias_dijkstra[destino]} km)")

    # 3. Demonstração de Outros Algoritmos de Busca
    print("\n-- Demonstração de Busca em Largura (BFS) --")
    caminho_bfs = busca_em_largura(empresa_logistica, 'D')
    print(f"Caminho encontrado por BFS a partir de 'D': {caminho_bfs}")

    print("\n-- Demonstração de Busca em Profundidade (DFS) --")
    caminho_dfs = busca_em_profundidade(empresa_logistica, 'D')
    print(f"Caminho encontrado por DFS a partir de 'D': {caminho_dfs}")

    # 4. Demonstração de Algoritmo de Árvore Geradora Mínima
    print("\n-- Aplicação: Conexão de todos os pontos com o mínimo de cabo (Kruskal) --")
    agm_kruskal = kruskal(empresa_logistica)
    print("\nÁrvore Geradora Mínima (AGM) gerada por Kruskal:")
    custo_total = 0
    for origem, destino, peso in agm_kruskal:
        print(f"  -> Aresta: '{origem}' - '{destino}' (Peso: {peso})")
        custo_total += peso
    print(f"\nCusto total da AGM: {custo_total} km")

    print("\n==============================================================================")
    print("                       Fim da Demonstração da Aula                            ")
    print("==============================================================================")