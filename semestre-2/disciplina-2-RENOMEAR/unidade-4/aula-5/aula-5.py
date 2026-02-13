# arquivo: aula-5.py

# ==============================================================================
# EXEMPLIFICANDO NORMALIZAÇÃO E ENGENHARIA REVERSA EM PYTHON
#
# Este script simula o processo de normalização de dados, transformando
# uma estrutura de dados "plana" e redundante em um modelo mais organizado,
# similar ao que faríamos em um banco de dados relacional.
#
# A "Engenharia Reversa" é demonstrada ao extrairmos as estruturas
# de dados normalizadas a partir de uma única fonte de dados "brutos".
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. DADOS BRUTOS E NÃO-NORMALIZADOS
#    Imagine que esta é a informação que extraímos de um sistema legado.
#    Note a redundância: o nome do cliente e o nome do produto se repetem
#    para cada item do pedido. Isso é um problema!
# ------------------------------------------------------------------------------
dados_nao_normalizados = [
    {
        "pedido_id": 1,
        "cliente_id": 101,
        "nome_cliente": "João Silva",
        "email_cliente": "joao.silva@email.com",
        "item_id": 1,
        "nome_produto": "Notebook Pro",
        "preco_produto": 2500.00,
        "quantidade": 1
    },
    {
        "pedido_id": 1,
        "cliente_id": 101,
        "nome_cliente": "João Silva",
        "email_cliente": "joao.silva@email.com",
        "item_id": 2,
        "nome_produto": "Mouse Sem Fio",
        "preco_produto": 75.00,
        "quantidade": 2
    },
    {
        "pedido_id": 2,
        "cliente_id": 102,
        "nome_cliente": "Maria Oliveira",
        "email_cliente": "maria.o@email.com",
        "item_id": 3,
        "nome_produto": "Monitor 27 pol",
        "preco_produto": 950.00,
        "quantidade": 1
    },
    {
        "pedido_id": 3,
        "cliente_id": 101,
        "nome_cliente": "João Silva",
        "email_cliente": "joao.silva@email.com",
        "item_id": 1,
        "nome_produto": "Notebook Pro",
        "preco_produto": 2500.00,
        "quantidade": 1
    }
]

# ------------------------------------------------------------------------------
# 2. ENGENHARIA REVERSA E NORMALIZAÇÃO
#    Vamos extrair e organizar esses dados em "tabelas" separadas
#    para eliminar a redundância.
# ------------------------------------------------------------------------------

# Dicionários para armazenar os dados normalizados
clientes = {}
produtos = {}
pedidos = {}

print("--- Processo de Normalização Iniciado ---")

# Iteramos sobre os dados brutos para preencher nossas "tabelas"
for item in dados_nao_normalizados:
    # "Tabela" de Clientes (entidade independente)
    cliente_id = item["cliente_id"]
    if cliente_id not in clientes:
        clientes[cliente_id] = {
            "nome": item["nome_cliente"],
            "email": item["email_cliente"]
        }

    # "Tabela" de Produtos (entidade independente)
    item_id = item["item_id"]
    if item_id not in produtos:
        produtos[item_id] = {
            "nome": item["nome_produto"],
            "preco": item["preco_produto"]
        }

    # "Tabela" de Pedidos (entidade de relacionamento)
    pedido_id = item["pedido_id"]
    if pedido_id not in pedidos:
        pedidos[pedido_id] = {
            "cliente_id": cliente_id,  # Chave Estrangeira!
            "itens": []
        }
    
    # Adicionamos os itens ao pedido correspondente
    pedidos[pedido_id]["itens"].append({
        "item_id": item_id,       # Chave Estrangeira!
        "quantidade": item["quantidade"]
    })

print("--- Normalização Concluída ---")

# ------------------------------------------------------------------------------
# 3. VERIFICANDO OS DADOS NORMALIZADOS
#    Agora, podemos imprimir as novas estruturas de dados organizadas.
# ------------------------------------------------------------------------------

print("\n### TABELA DE CLIENTES ###")
for id, dados in clientes.items():
    print(f"ID: {id}, Nome: {dados['nome']}, E-mail: {dados['email']}")

print("\n### TABELA DE PRODUTOS ###")
for id, dados in produtos.items():
    print(f"ID: {id}, Nome: {dados['nome']}, Preço: R${dados['preco']:.2f}")

print("\n### TABELA DE PEDIDOS ###")
for id, dados in pedidos.items():
    print(f"Pedido ID: {id}, Cliente ID: {dados['cliente_id']}")
    for item in dados["itens"]:
        print(f"  -> Item ID: {item['item_id']}, Quantidade: {item['quantidade']}")

# ------------------------------------------------------------------------------
# 4. BENEFÍCIOS DO MODELO NORMALIZADO
#    - Sem repetição de dados de clientes e produtos.
#    - Se o nome do "João Silva" mudar, só precisamos atualizar em UM lugar
#      (na tabela de clientes), não em todos os pedidos que ele fez.
#    - Ocupa menos espaço e é mais eficiente para buscar informações.
# ------------------------------------------------------------------------------

print("\n--- Demonstração Concluída ---")