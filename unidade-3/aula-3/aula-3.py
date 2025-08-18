# Importa o módulo sys para configurar a profundidade de recursão do Python, necessária para a Busca em Profundidade (DFS) em grafos grandes.
import sys

# Define uma profundidade de recursão alta para evitar erros de limite de recursão em grafos complexos.
sys.setrecursionlimit(2000)

class Grafo:
    """
    Uma classe para representar um grafo, com métodos para adicionar vértices e arestas,
    e para implementar algoritmos de teoria dos grafos.
    """
    def __init__(self, direcionado=True):
        """
        Inicializa o grafo.
        
        Args:
            direcionado (bool): Se o grafo é direcionado (padrão) ou não.
        """
        self.adjacencias = {}
        self.direcionado = direcionado

    def adicionar_vertice(self, vertice):
        """Adiciona um vértice ao grafo se ele ainda não existir."""
        if vertice not in self.adjacencias:
            self.adjacencias[vertice] = {}

    def adicionar_aresta(self, origem, destino, peso=1):
        """Adiciona uma aresta entre dois vértices."""
        self.adicionar_vertice(origem)
        self.adicionar_vertice(destino)
        self.adjacencias[origem][destino] = peso
        if not self.direcionado:
            self.adjacencias[destino][origem] = peso

    # --- Algoritmos de Caminhos Mais Curtos ---
    ## Apenas uma demonstração do algoritmo de Dijkstra
    def dijkstra(self, inicio):
        """
        Encontra o caminho mais curto de um vértice de início para todos os outros
        em um grafo ponderado sem pesos negativos.
        
        Args:
            inicio: O vértice de partida.
        
        Returns:
            dict: Um dicionário com as distâncias mais curtas de 'inicio' para cada vértice.
        """
        print(f"\n--- Algoritmo de Dijkstra para Caminho Mais Curto (início: {inicio}) ---")
        
        distancias = {vertice: float('inf') for vertice in self.adjacencias}
        distancias[inicio] = 0
        vertices_nao_visitados = list(self.adjacencias.keys())
        
        while vertices_nao_visitados:
            vertice_atual = min(vertices_nao_visitados, key=lambda v: distancias[v])
            
            if distancias[vertice_atual] == float('inf'):
                break # Todos os vértices restantes são inacessíveis
            
            vertices_nao_visitados.remove(vertice_atual)
            
            for vizinho, peso in self.adjacencias[vertice_atual].items():
                nova_distancia = distancias[vertice_atual] + peso
                if nova_distancia < distancias[vizinho]:
                    distancias[vizinho] = nova_distancia
        
        return distancias

    # --- Detecção de Ciclos com Busca em Profundidade (DFS) ---
    def _dfs_ciclo_util(self, vertice, visitados, pilha_recursao):
        """
        Função auxiliar recursiva para detecção de ciclo em grafos direcionados.
        """
        visitados.add(vertice)
        pilha_recursao.add(vertice)

        for vizinho in self.adjacencias.get(vertice, {}):
            if vizinho not in visitados:
                if self._dfs_ciclo_util(vizinho, visitados, pilha_recursao):
                    return True
            elif vizinho in pilha_recursao:
                print(f"  > Ciclo detectado: O vértice {vizinho} foi visitado novamente na mesma busca.")
                return True
        
        pilha_recursao.remove(vertice)
        return False
        
    def tem_ciclo(self):
        """
        Verifica se o grafo contém um ciclo usando o algoritmo de Busca em Profundidade (DFS).
        
        Returns:
            bool: True se um ciclo for encontrado, False caso contrário.
        """
        print("\n--- Verificando Ciclos (usando DFS) ---")
        visitados = set()
        pilha_recursao = set()
        for vertice in self.adjacencias:
            if vertice not in visitados:
                if self._dfs_ciclo_util(vertice, visitados, pilha_recursao):
                    return True
        return False

    # --- Identificação de Influenciadores (Problema da Aula) ---
    def grau_entrada(self, vertice):
        """
        Calcula o 'grau de entrada' de um vértice (número de arestas que chegam a ele).
        Em uma rede social, isso pode ser interpretado como a quantidade de 'seguidores'
        ou 'menções', um bom indicativo de influência.
        """
        grau = 0
        for origem in self.adjacencias:
            if vertice in self.adjacencias[origem]:
                grau += 1
        return grau

    def identificar_influenciadores(self):
        """
        Identifica os influenciadores com base no grau de entrada.
        Um influenciador é definido como um usuário com um grau de entrada
        significativamente maior que a média da rede.
        
        Returns:
            list: Uma lista dos vértices identificados como influenciadores.
        """
        print("\n--- Identificando Influenciadores ---")
        graus_entrada = {usuario: self.grau_entrada(usuario) for usuario in self.adjacencias}
        
        # Se o grafo estiver vazio, não há influenciadores.
        if not graus_entrada:
            return []

        # Calcula o grau de entrada médio para definir um limite.
        grau_medio = sum(graus_entrada.values()) / len(graus_entrada)
        print(f"  > Grau de entrada médio da rede: {grau_medio:.2f}")

        # Define um limiar (por exemplo, 1.5x a média) para identificar influenciadores.
        # Você pode ajustar esse valor para ser mais ou menos rigoroso.
        limiar_influencia = grau_medio * 1.5
        influenciadores = [usuario for usuario, grau in graus_entrada.items() if grau > limiar_influencia]

        print(f"  > Limiar de influência (grau > {limiar_influencia:.2f})")
        
        if influenciadores:
            print(f"  > Vértices com alto grau de entrada: {[f'{u} ({graus_entrada[u]})' for u in influenciadores]}")
        else:
            print("  > Nenhum influenciador identificado com o limiar atual.")
        
        return influenciadores


# --- Exemplo de Uso ---
if __name__ == "__main__":
    
    # 1. Demonstração de Caminhos Mais Curtos (Dijkstra)
    print("=+=+=+= Demonstrando Caminhos Mais Curtos (Dijkstra) =+=+=+=")
    # Grafo ponderado de um sistema de navegação (cidades e distâncias)
    sistema_navegacao = Grafo(direcionado=False)
    sistema_navegacao.adicionar_aresta('A', 'B', 10)
    sistema_navegacao.adicionar_aresta('A', 'C', 15)
    sistema_navegacao.adicionar_aresta('B', 'C', 5)
    sistema_navegacao.adicionar_aresta('B', 'D', 20)
    sistema_navegacao.adicionar_aresta('C', 'E', 12)
    sistema_navegacao.adicionar_aresta('D', 'E', 7)

    distancias_de_A = sistema_navegacao.dijkstra('A')
    print(f"  > Distâncias mais curtas a partir de 'A': {distancias_de_A}")
    print("-" * 50)
    
    # 2. Demonstração de Detecção de Ciclos
    print("\n=+=+=+= Demonstrando Detecção de Ciclos =+=+=+=")
    # Grafo direcionado com ciclo (dependência circular)
    projeto_dependencias = Grafo(direcionado=True)
    projeto_dependencias.adicionar_aresta('Tarefa A', 'Tarefa B')
    projeto_dependencias.adicionar_aresta('Tarefa B', 'Tarefa C')
    projeto_dependencias.adicionar_aresta('Tarefa C', 'Tarefa A') # Cria um ciclo

    tem_ciclo = projeto_dependencias.tem_ciclo()
    print(f"  > O grafo de dependências tem um ciclo? {tem_ciclo}")

    # Grafo sem ciclo
    arvore_genealogica = Grafo(direcionado=True)
    arvore_genealogica.adicionar_aresta('Avô', 'Pai')
    arvore_genealogica.adicionar_aresta('Pai', 'Filho')
    arvore_genealogica.adicionar_aresta('Avó', 'Mãe')
    arvore_genealogica.adicionar_aresta('Mãe', 'Filho')

    tem_ciclo_gen = arvore_genealogica.tem_ciclo()
    print(f"  > O grafo da árvore genealógica tem um ciclo? {tem_ciclo_gen}")
    print("-" * 50)

    # 3. Solução para o problema da aula: Identificação de Influenciadores
    print("\n=+=+=+= Solução do Problema da Aula: Identificação de Influenciadores =+=+=+=")
    # Cria a rede social proposta no enunciado da aula
    rede_social = Grafo(direcionado=True)
    rede_social.adicionar_aresta('Alice', 'Bob')
    rede_social.adicionar_aresta('Alice', 'Carol')
    rede_social.adicionar_aresta('Bob', 'Alice')
    rede_social.adicionar_aresta('Bob', 'Dave')
    rede_social.adicionar_aresta('Carol', 'Alice')
    rede_social.adicionar_aresta('Carol', 'Dave')
    rede_social.adicionar_aresta('Dave', 'Bob')
    rede_social.adicionar_aresta('Dave', 'Carol')
    rede_social.adicionar_aresta('Dave', 'Eve')
    rede_social.adicionar_aresta('Eve', 'Dave')

    influenciadores = rede_social.identificar_influenciadores()
    print(f"  > Influenciadores identificados: {influenciadores}")