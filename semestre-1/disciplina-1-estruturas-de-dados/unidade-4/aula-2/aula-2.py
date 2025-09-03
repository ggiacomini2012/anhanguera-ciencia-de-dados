# -*- coding: utf-8 -*-
# Importa as bibliotecas necessárias
import networkx as nx                  # Para criação, manipulação e estudo de grafos
import matplotlib.pyplot as plt        # Para visualização e plotagem de gráficos

# --- Configuração do Grafo de Transações ---

# Cria um grafo vazio. Usamos DiGraph para representar a direção das transações (Cliente -> Loja).
G = nx.DiGraph()

# Adiciona nós (vértices) que representam clientes e estabelecimentos (lojas).
# Definimos o tipo para facilitar a coloração e distinção visual.
G.add_node('Cliente A', type='cliente', saldo=1500.00)
G.add_node('Cliente B', type='cliente', saldo=800.00)
G.add_node('Loja da Esquina', type='loja', categoria='varejo')
G.add_node('E-commerce Tech', type='loja', categoria='online')
G.add_node('Viagens KPL', type='loja', categoria='serviço')
G.add_node('Estabelecimento Suspeito', type='loja', categoria='internacional')

# --- Adição de Arestas (Transações) com Atributos ---

# Adiciona arestas (transações) com atributos detalhados:
# 'peso': valor da transação
# 'tipo': tipo de operação (compra, saque)
# 'data': simula um timestamp
# 'local': localização da transação
# 'status': para simular se é suspeita ou legítima
print("Adicionando transações normais...")
G.add_edge('Cliente A', 'Loja da Esquina',
           weight=50.00, type='compra', data='2025-08-20 10:30', local='Balneário Camboriú', status='legítima')
G.add_edge('Cliente A', 'E-commerce Tech',
           weight=120.50, type='compra online', data='2025-08-20 14:15', local='Online', status='legítima')
G.add_edge('Cliente B', 'Loja da Esquina',
           weight=30.00, type='compra', data='2025-08-21 09:00', local='Balneário Camboriú', status='legítima')
G.add_edge('Cliente B', 'Viagens KPL',
           weight=750.00, type='serviço', data='2025-08-21 16:45', local='Online', status='legítima')

# --- Transação Potencialmente Fraudulenta ---
# Simulamos uma transação com características que podem indicar fraude:
# - Alto valor
# - De um cliente que geralmente faz transações menores
# - Em um estabelecimento incomum ou de categoria diferente
# - Realizada em um curto espaço de tempo após outras transações normais, e talvez em um local distante.
print("Adicionando transação potencialmente suspeita...")
G.add_edge('Cliente A', 'Estabelecimento Suspeito',
           weight=980.00, type='compra internacional', data='2025-08-20 15:00', local='Londres', status='suspeita')

# --- Preparação para Visualização ---

# Define as posições dos nós para a visualização.
# spring_layout tenta posicionar nós conectados mais próximos uns dos outros,
# tornando as relações mais evidentes.
pos = nx.spring_layout(G, k=0.7, iterations=50) # 'k' ajusta a distância entre os nós, 'iterations' a qualidade do layout.

# Define as cores dos nós baseadas no tipo (cliente ou loja)
node_colors = []
for node in G.nodes():
    if G.nodes[node]['type'] == 'cliente':
        node_colors.append('skyblue')  # Azul para clientes
    else:
        node_colors.append('lightcoral') # Vermelho claro para lojas

# Define os tamanhos dos nós (clientes maiores, lojas menores)
node_sizes = [600 if G.nodes[node]['type'] == 'cliente' else 400 for node in G.nodes()]

# Define as cores das arestas. Destaca as arestas suspeitas.
edge_colors = []
for u, v, data in G.edges(data=True):
    if data['status'] == 'suspeita':
        edge_colors.append('red')      # Vermelho para transações suspeitas
    else:
        edge_colors.append('gray')     # Cinza para transações legítimas

# Define as larguras das arestas. Arestas suspeitas podem ser mais grossas.
edge_widths = [2.5 if data['status'] == 'suspeita' else 1 for u, v, data in G.edges(data=True)]

# --- Visualização do Grafo ---

# Cria uma figura e eixos para o plot com um tamanho específico para melhor visualização.
plt.figure(figsize=(10, 8))

# Desenha os nós
nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=node_sizes, alpha=0.9, edgecolors='black')

# Desenha as arestas
nx.draw_networkx_edges(G, pos, edge_color=edge_colors, width=edge_widths, alpha=0.7, arrows=True, arrowstyle='->', arrowsize=20)

# Desenha os rótulos dos nós
node_labels = {node: node for node in G.nodes()}
nx.draw_networkx_labels(G, pos, labels=node_labels, font_size=10, font_weight='bold')

# Desenha os rótulos das arestas (informações da transação)
# Ajustamos o posicionamento dos rótulos para não se sobreporem.
edge_labels = {}
for u, v, data in G.edges(data=True):
    edge_labels[(u, v)] = f"Valor: R${data['weight']:.2f}\nLocal: {data['local']}"
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='darkgreen', font_size=8, alpha=0.8)

# Adiciona um título ao gráfico
plt.title('Detecção de Fraudes com Grafos no Banco KPL', size=15)

# Remove os eixos para uma visualização mais limpa
plt.axis('off')

# Exibe o gráfico
plt.show()

print("\nGrafo gerado com sucesso! Observe a transação em vermelho, indicando uma possível fraude.")

