# -*- coding: utf-8 -*-

"""
Este script em Python foi criado para exemplificar os conceitos da aula sobre
estruturas de dados, modelagem computacional de problemas e o papel da linguagem
de programação.

Abordaremos três pontos centrais:
1.  A representação de um mapa com grafos para um sistema de navegação.
2.  O uso de uma pilha (Stack) para simular uma investigação de fraude.
3.  O papel do Python na implementação dessas estruturas.
"""

# =============================================================================
# Exemplo 1: Sistema de Navegação e o Problema do Caixeiro Viajante (Grafos)
# =============================================================================

print("--- Exemplo 1: Sistema de Navegação com Grafos ---")

# Na computação, um grafo é uma estrutura ideal para representar conexões.
# Aqui, as cidades são os "nós" e as estradas (com suas distâncias) são as "arestas".
# Essa representação é fundamental para qualquer GPS.

# Dicionário para representar as cidades e as distâncias entre elas.
# Este é um exemplo simples de um "grafo ponderado".
mapa_cidades = {
    'Aracaju': {'Salvador': 325, 'Maceió': 277},
    'Salvador': {'Aracaju': 325, 'Recife': 839},
    'Maceió': {'Aracaju': 277, 'Recife': 256},
    'Recife': {'Maceió': 256, 'Salvador': 839, 'João Pessoa': 121},
    'João Pessoa': {'Recife': 121}
}

def encontrar_rota_simples(mapa, cidade_inicial, cidade_final):
    """
    Função simples para encontrar uma rota possível entre duas cidades.
    Este não é um algoritmo otimizado como Dijkstra ou A*, mas ilustra
    como a estrutura de grafo é percorrida.
    """
    # Usamos uma lista como uma fila para explorar as cidades
    fila_exploracao = [[cidade_inicial]]
    rotas_exploradas = set()

    if cidade_inicial == cidade_final:
        return f"Você já está em {cidade_inicial}."

    while fila_exploracao:
        # Pega o primeiro caminho da fila
        rota_atual = fila_exploracao.pop(0)
        # A última cidade do caminho atual é o nosso ponto de partida
        cidade_atual = rota_atual[-1]

        if cidade_atual not in rotas_exploradas:
            # Pega as cidades vizinhas
            vizinhas = mapa.get(cidade_atual, {})

            # Explora as vizinhas
            for vizinha, _ in vizinhas.items():
                nova_rota = list(rota_atual)
                nova_rota.append(vizinha)

                # Se encontrarmos o destino, retornamos a rota
                if vizinha == cidade_final:
                    distancia_total = calcular_distancia(mapa, nova_rota)
                    return f"Rota encontrada: {' -> '.join(nova_rota)} | Distância: {distancia_total} km"
                
                # Adiciona a nova rota à fila para exploração
                fila_exploracao.append(nova_rota)
            
            # Marca a cidade como explorada
            rotas_exploradas.add(cidade_atual)
    
    return "Nenhuma rota encontrada."

def calcular_distancia(mapa, rota):
    """Calcula a distância total de uma rota."""
    distancia = 0
    for i in range(len(rota) - 1):
        cidade_origem = rota[i]
        cidade_destino = rota[i+1]
        distancia += mapa[cidade_origem][cidade_destino]
    return distancia


# Simulando a busca por uma rota
cidade_origem = 'Salvador'
cidade_destino = 'João Pessoa'
print(f"Buscando a melhor rota de {cidade_origem} para {cidade_destino}...\n")
melhor_rota = encontrar_rota_simples(mapa_cidades, cidade_origem, cidade_destino)
print(melhor_rota)
print("\nReflexão: A forma como os dados (cidades e ruas) são estruturados em um grafo impacta diretamente a eficiência do algoritmo de busca. Um grafo bem modelado permite que algoritmos como A* encontrem o caminho mais curto de forma muito mais rápida.\n")


# =============================================================================
# Exemplo 2: Detecção de Fraudes em Seguros (Pilhas - LIFO)
# =============================================================================

print("\n--- Exemplo 2: Detecção de Fraudes com Pilhas ---")

# Em uma investigação de fraude, muitas vezes precisamos rastrear eventos ou
# relações de forma retroativa. A pilha, com seu princípio "Último a Entrar,
# Primeiro a Sair" (LIFO), é perfeita para isso.

# Vamos simular a análise de uma árvore genealógica para encontrar relações suspeitas.
# Usaremos uma classe para criar nossa própria estrutura de Pilha e deixá-la mais clara.
class Pilha:
    def __init__(self):
        self._items = []

    def esta_vazia(self):
        return not self._items

    def empilhar(self, item):
        """Adiciona um item ao topo da pilha."""
        self._items.append(item)
        print(f"INVESTIGAÇÃO: Adicionando '{item}' à pilha de investigação.")

    def desempilhar(self):
        """Remove e retorna o item do topo da pilha."""
        if self.esta_vazia():
            return None
        item_removido = self._items.pop()
        print(f"ANÁLISE: Analisando a conexão mais recente -> '{item_removido}'.")
        return item_removido

    def topo(self):
        """Retorna o item do topo sem removê-lo."""
        if self.esta_vazia():
            return None
        return self._items[-1]

# Cenário: Uma apólice de seguro de um veículo teve um sinistro suspeito.
# O beneficiário é 'Ana'. Vamos investigar as conexões a partir dela.
pilha_investigacao = Pilha()

# O investigador começa por 'Ana', a beneficiária.
pilha_investigacao.empilhar('Ana (Beneficiária)')

# Ao analisar 'Ana', descobre-se que o motorista no momento do acidente era 'Carlos'.
# A investigação adiciona 'Carlos' à pilha para ser o próximo a ser analisado.
pilha_investigacao.empilhar('Carlos (Motorista)')

# Ao investigar 'Carlos', descobre-se que a testemunha do acidente foi 'Sofia'.
# 'Sofia' é adicionada ao topo da pilha.
pilha_investigacao.empilhar('Sofia (Testemunha)')

print("\nIniciando a análise retroativa das conexões (princípio LIFO):")

# Agora, o sistema começa a analisar as conexões, da mais recente para a mais antiga.
# 1. Analisa Sofia
pessoa_analisada = pilha_investigacao.desempilhar()
# Ao analisar Sofia, o sistema consulta um banco de dados e descobre que ela é irmã de Carlos.
print(f"--> ALERTA: '{pessoa_analisada}' possui parentesco (irmã) com 'Carlos (Motorista)'. Fraude em potencial!\n")

# 2. Analisa Carlos
pessoa_analisada = pilha_investigacao.desempilhar()
# O sistema continua a análise e descobre que Carlos é cônjuge de Ana.
print(f"--> INFO: '{pessoa_analisada}' é cônjuge de 'Ana (Beneficiária)'.\n")

# 3. Analisa Ana
pessoa_analisada = pilha_investigacao.desempilhar()
print(f"--> INFO: '{pessoa_analisada}' é o ponto inicial da investigação.\n")

print("Reflexão: A estrutura de pilha permitiu analisar as conexões na ordem inversa em que foram descobertas. Isso é útil para rastrear eventos ou seguir uma cadeia de evidências 'para trás', uma abordagem comum em auditorias e investigações de fraude.\n")


# =============================================================================
# Exemplo 3: O Papel do Python
# =============================================================================

print("\n--- Exemplo 3: O Papel da Linguagem Python ---")

# Python facilita a implementação dessas estruturas de dados por várias razões:

# 1. Sintaxe Clara e Legível:
# Criar a classe Pilha ou representar o grafo com um dicionário é intuitivo.
# O código se assemelha quase a uma pseudolinguagem, facilitando o entendimento.

# 2. Tipagem Dinâmica:
# Não precisamos declarar os tipos das variáveis (`mapa_cidades`, `pilha_investigacao`).
# Python infere os tipos em tempo de execução, agilizando o desenvolvimento.

# 3. Vastas Bibliotecas:
# Para o exemplo de navegação, poderíamos usar bibliotecas como `networkx` para
# manipulação avançada de grafos e algoritmos prontos.
# Para análise de dados (como na fraude), bibliotecas como `pandas` e `numpy` são
# extremamente poderosas.

# 4. Paradigma Orientado a Objetos:
# A capacidade de criar classes (como a `Pilha`) nos permite modelar conceitos
# do mundo real de forma organizada e reutilizável.

print("Python atua como uma ferramenta poderosa e flexível, permitindo que o desenvolvedor")
print("se concentre na lógica do problema (a rota, a fraude) em vez de se preocupar")
print("com detalhes complexos de gerenciamento de memória ou sintaxe verbosa.")