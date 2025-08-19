# -*- coding: utf-8 -*-
# Simulação de Jogo de Labirinto Usando Teoria de Grafos

import collections

# --- Implementação do Grafo ---

class Grafo:
    """
    Uma classe para representar um grafo usando uma lista de adjacências.
    """
    def __init__(self):
        """
        Inicializa o grafo com um dicionário vazio para armazenar os vértices
        e suas conexões.
        """
        self.vertices = collections.defaultdict(list)

    def adicionar_vertice(self, vertice):
        """
        Adiciona um vértice ao grafo se ele ainda não existir.
        
        Args:
            vertice: O nome ou identificador do vértice.
        """
        if vertice not in self.vertices:
            self.vertices[vertice] = []
            
    def adicionar_aresta(self, origem, destino):
        """
        Adiciona uma aresta bidirecional entre dois vértices.
        Isso simula um grafo não direcionado, como um labirinto onde
        se pode ir e voltar.
        
        Args:
            origem: O vértice de partida.
            destino: O vértice de chegada.
        """
        # Verifica se os vértices existem antes de adicionar a aresta
        self.adicionar_vertice(origem)
        self.adicionar_vertice(destino)
        
        # Adiciona a conexão em ambas as direções para um grafo não direcionado
        if destino not in self.vertices[origem]:
            self.vertices[origem].append(destino)
        if origem not in self.vertices[destino]:
            self.vertices[destino].append(origem)

    def obter_adjacencias(self, vertice):
        """
        Retorna uma lista dos vértices adjacentes ao vértice fornecido.
        
        Args:
            vertice: O vértice para o qual se deseja encontrar os vizinhos.
            
        Returns:
            Uma lista de vértices adjacentes.
        """
        return self.vertices.get(vertice, [])

# --- Construção do Labirinto (o grafo do problema) ---

def construir_labirinto():
    """
    Constrói e retorna o grafo que representa o labirinto.
    As salas são os vértices e as passagens são as arestas.
    
    Returns:
        Um objeto Grafo que representa o labirinto.
    """
    labirinto = Grafo()
    
    # Adicionando as conexões do labirinto de acordo com a Figura 13
    # Conexões do pentágono central
    labirinto.adicionar_aresta('v1', 'v2')
    labirinto.adicionar_aresta('v2', 'v3')
    labirinto.adicionar_aresta('v3', 'v4')
    labirinto.adicionar_aresta('v4', 'v5')
    labirinto.adicionar_aresta('v5', 'v1')
    
    # Conexões externas
    labirinto.adicionar_aresta('v4', 'v1A')
    labirinto.adicionar_aresta('v1A', 'v1B')
    labirinto.adicionar_aresta('v1B', 'v1C')
    labirinto.adicionar_aresta('v1C', 'v1D')
    
    labirinto.adicionar_aresta('v2', 'v1E')
    labirinto.adicionar_aresta('v1E', 'v2A')
    labirinto.adicionar_aresta('v2A', 'v2B')
    labirinto.adicionar_aresta('v2B', 'v2C')
    labirinto.adicionar_aresta('v2C', 'v2D')
    labirinto.adicionar_aresta('v2D', 'v2E')
    
    labirinto.adicionar_aresta('v3', 'v3A')
    labirinto.adicionar_aresta('v3A', 'v3B')
    labirinto.adicionar_aresta('v3B', 'v3C')
    labirinto.adicionar_aresta('v3C', 'v3D')
    
    labirinto.adicionar_aresta('v5', 'v5A')
    labirinto.adicionar_aresta('v5A', 'v5B')
    labirinto.adicionar_aresta('v5B', 'v5C')
    labirinto.adicionar_aresta('v5C', 'v5D')
    
    labirinto.adicionar_aresta('v1', 'v1E') # Esta conexão está faltando na descrição mas é necessária para fechar o ciclo da figura
    
    return labirinto

# --- Lógica do Jogo ---

def jogar_labirinto():
    """
    Função principal que gerencia a jogabilidade do labirinto.
    """
    labirinto = construir_labirinto()
    localizacao_atual = 'v1'  # O jogo começa na sala v1, conforme o problema
    
    print("Bem-vindo ao Labirinto! Digite 'sair' para encerrar o jogo a qualquer momento.")
    
    while True:
        # Mostra a localização atual e as opções de movimento
        print(f"\nSua localização atual: {localizacao_atual}")
        adjacencias = labirinto.obter_adjacencias(localizacao_atual)
        
        # Exibe as salas adjacentes de forma amigável
        if adjacencias:
            print("Salas adjacentes disponíveis para exploração:")
            for i, sala in enumerate(adjacencias, 1):
                print(f"{i}. {sala}")
        else:
            print("Você está em uma sala sem saídas! Fim do jogo.")
            break
            
        # Pede a entrada do jogador
        escolha = input("\nDigite o nome da sala para onde deseja ir (ex: v2): ").strip()
        
        # Opção para sair
        if escolha.lower() == 'sair':
            print("Saindo do jogo. Até a próxima!")
            break
            
        # Valida a escolha do jogador
        if escolha in adjacencias:
            localizacao_atual = escolha
        else:
            print("Escolha inválida. Por favor, selecione uma das salas disponíveis.")

# --- Execução do Programa ---

if __name__ == "__main__":
    jogar_labirinto()

