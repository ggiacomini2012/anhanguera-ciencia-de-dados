from collections import deque

class GrafoTransporte:
    def __init__(self):
        """
        Inicializa a estrutura do grafo de transporte.
        O grafo é um dicionário onde as chaves são as interseções (vértices)
        e os valores são listas de interseções de destino (arestas).
        """
        self.grafo = {}

    def adicionar_via(self, origem, destino):
        """
        Adiciona uma via (aresta direcionada) ao grafo.
        Representa uma rua de mão única.
        """
        if origem not in self.grafo:
            self.grafo[origem] = []
        if destino not in self.grafo:
            self.grafo[destino] = []
        self.grafo[origem].append(destino)

    def bloquear_via(self, origem, destino):
        """
        Simula o bloqueio de uma via removendo a aresta correspondente.
        Isso torna o caminho intransitável.
        """
        if origem in self.grafo and destino in self.grafo[origem]:
            self.grafo[origem].remove(destino)
            print(f"✅ Via de {origem} para {destino} foi bloqueada.")
        else:
            print(f"❌ Erro: A via de {origem} para {destino} não existe ou já está bloqueada.")

    def encontrar_rota_alternativa(self, inicio, fim):
        """
        Usa o algoritmo de Busca em Largura (BFS) para verificar se existe
        um caminho entre dois pontos, mesmo com vias bloqueadas.
        Retorna True se houver uma rota, False caso contrário.
        """
        # Se os pontos de início ou fim não existirem, não há como encontrar uma rota.
        if inicio not in self.grafo or fim not in self.grafo:
            return False

        fila = deque([inicio])
        visitados = {inicio}

        while fila:
            vertice_atual = fila.popleft()

            # Se o vértice atual for o destino, encontramos uma rota.
            if vertice_atual == fim:
                return True

            # Explora os vizinhos do vértice atual
            for vizinho in self.grafo[vertice_atual]:
                if vizinho not in visitados:
                    visitados.add(vizinho)
                    fila.append(vizinho)

        # Se a fila esvaziar e o destino não foi alcançado, não há rota.
        return False

# --- Configurando o grafo do problema ---
rede_viaria = GrafoTransporte()
cidades = ['A', 'B', 'C', 'D', 'E', 'F']

# Adicionando as vias com base na Figura 1 (Grafos do exercício)
# A -> B, A -> C
rede_viaria.adicionar_via('A', 'B')
rede_viaria.adicionar_via('A', 'C')
# B -> A, B -> D
rede_viaria.adicionar_via('B', 'A')
rede_viaria.adicionar_via('B', 'D')
# C -> E
rede_viaria.adicionar_via('C', 'E')
# D -> B, D -> E
rede_viaria.adicionar_via('D', 'B')
rede_viaria.adicionar_via('D', 'E')
# E -> C, E -> F
rede_viaria.adicionar_via('E', 'C')
rede_viaria.adicionar_via('E', 'F')
# F -> D
rede_viaria.adicionar_via('F', 'D')

# --- Executando o cenário do problema ---
print("--- Situação Inicial: Verificando rotas ---")
origem_desejada = 'A'
destino_desejado = 'F'
if rede_viaria.encontrar_rota_alternativa(origem_desejada, destino_desejado):
    print(f"✅ Existe uma rota de {origem_desejada} para {destino_desejada}.")
else:
    print(f"❌ Não existe uma rota de {origem_desejada} para {destino_desejada}.")

print("\n--- Simulando o bloqueio da via B -> D ---")
rede_viaria.bloquear_via('B', 'D')
print("\n--- Verificando a rota após o primeiro bloqueio ---")
if rede_viaria.encontrar_rota_alternativa(origem_desejada, destino_desejado):
    print(f"✅ Ainda existe uma rota de {origem_desejada} para {destino_desejada}.")
else:
    print(f"❌ A rota de {origem_desejada} para {destino_desejada} está bloqueada.")

print("\n--- Simulando um bloqueio adicional da via D -> E ---")
rede_viaria.bloquear_via('D', 'E')
print("\n--- Verificando a rota após o segundo bloqueio ---")
if rede_viaria.encontrar_rota_alternativa(origem_desejada, destino_desejado):
    print(f"✅ Ainda existe uma rota de {origem_desejada} para {destino_desejada}.")
else:
    print(f"❌ A rota de {origem_desejada} para {destino_desejada} está bloqueada.")