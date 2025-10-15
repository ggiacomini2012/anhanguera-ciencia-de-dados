import pandas as pd
from datetime import datetime

# --- 1. SIMULAÇÃO DAS FONTES DE ORIGEM DE DADOS ---
print("--- 1. Coleta de Dados das Fontes de Origem (A 'Cidade' do Exemplo) ---")

# Fonte 1: Sistema de Ponto de Venda (PDV - Dados de Transação Brutos)
dados_vendas = [
    {'id_transacao': 1001, 'sku': 'PROD01', 'quantidade': 2, 'valor_unitario': 25.00, 'data': '2023-10-15 10:30:00', 'id_cliente_origem': 'CLI_A'},
    {'id_transacao': 1002, 'sku': 'PROD02', 'quantidade': 1, 'valor_unitario': 150.00, 'data': '2023-10-15 11:45:00', 'id_cliente_origem': 'CLI_B'},
    {'id_transacao': 1003, 'sku': 'PROD01', 'quantidade': 3, 'valor_unitario': 25.00, 'data': '2023-10-15 12:00:00', 'id_cliente_origem': 'CLI_A'},
]
df_vendas = pd.DataFrame(dados_vendas)
df_vendas['valor_total'] = df_vendas['quantidade'] * df_vendas['valor_unitario']

print("\n[Fonte PDV (Transacional) - 3 Registros]")
print(df_vendas[['id_transacao', 'sku', 'valor_total', 'data']].head(2))

# Fonte 2: Sistema de Gerenciamento de Clientes (CRM - Dados Descritivos)
dados_clientes_crm = [
    {'id_cliente_origem': 'CLI_A', 'nome_cliente': 'Alice Silva', 'cidade': 'São Paulo', 'segmento': 'Premium'},
    {'id_cliente_origem': 'CLI_B', 'nome_cliente': 'Bruno Lima', 'cidade': 'Rio de Janeiro', 'segmento': 'Standard'},
    {'id_cliente_origem': 'CLI_C', 'nome_cliente': 'Carlos Souza', 'cidade': 'São Paulo', 'segmento': 'Premium'},
]
df_clientes_crm = pd.DataFrame(dados_clientes_crm)

print("\n[Fonte CRM (Descritiva) - 3 Registros]")
print(df_clientes_crm[['id_cliente_origem', 'nome_cliente', 'cidade']].head(2))


# --- 2. MODELO DE LOJA DE DADOS OPERACIONAIS (ODS) ---
print("\n" + "="*50)
print("--- 2. Consolidação no ODS (O 'Pit-Stop' Operacional) ---")

# O ODS integra os dados transacionais e descritivos em tempo real (ou quase).
# Aqui, simulamos um JOIN para ter uma visão mais completa da transação.
df_ods = pd.merge(df_vendas, df_clientes_crm, on='id_cliente_origem', how='left')
df_ods['data_carga_ods'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

print("\n[Dados Integrados no ODS - Visão Operacional Detalhada]")
print(df_ods[['id_transacao', 'data', 'nome_cliente', 'cidade', 'valor_total']].head(3))


# --- 3. MODELAGEM DIMENSIONAL (OLAP) ---
print("\n" + "="*50)
print("--- 3. Construção do Modelo Dimensional (O 'Arsenal Estratégico') ---")

# Os dados são transformados do ODS para o formato FATO e DIMENSÃO.

# 3.1. Criação da Tabela DIMENSÃO_CLIENTE
# Seleciona e normaliza colunas do ODS para a Dimensão.
dim_cliente = df_ods[['id_cliente_origem', 'nome_cliente', 'cidade', 'segmento']].drop_duplicates().reset_index(drop=True)
# Adiciona uma chave artificial (Surrogate Key)
dim_cliente['id_cliente'] = dim_cliente.index + 1
print("\n[Tabela DIMENSÃO_CLIENTE (Quem? Onde?)]")
print(dim_cliente[['id_cliente', 'nome_cliente', 'cidade']].head(3))


# 3.2. Criação da Tabela FATO_VENDA
# A Tabela Fato contém as métricas (o 'O QUE') e as chaves estrangeiras.

# Pré-processamento: Cria a chave para o JOIN
df_fato = pd.merge(df_ods, dim_cliente[['id_cliente_origem', 'id_cliente']], on='id_cliente_origem', how='left')

fato_venda = df_fato[[
    'id_transacao',
    'id_cliente',           # Chave Estrangeira da Dimensão Cliente
    'data',                 # Seria a chave para a Dimensão Tempo
    'sku',                  # Seria a chave para a Dimensão Produto
    'quantidade',           # Métrica
    'valor_total'           # Métrica
]]
print("\n[Tabela FATO_VENDA (Métricas e Chaves)]")
print(fato_venda[['id_transacao', 'id_cliente', 'quantidade', 'valor_total']].head(3))

# --- 4. ANÁLISE OLAP SIMULADA ---
print("\n" + "="*50)
print("--- 4. Análise (OLAP): Roll Up e Slice & Dice ---")

# Exemplo de ROLL UP: Agregando o valor total por Segmento do Cliente
analise_rollup = fato_venda.merge(dim_cliente[['id_cliente', 'segmento']], on='id_cliente')
vendas_por_segmento = analise_rollup.groupby('segmento')['valor_total'].sum().reset_index()

print("\nAnálise 1 (Roll Up): Vendas Totais Agregadas por Segmento do Cliente:")
print(vendas_por_segmento)

# Exemplo de SLICE: Filtrando vendas apenas de uma cidade
cidade_filtro = 'São Paulo'
vendas_sao_paulo = analise_rollup[analise_rollup['cidade'] == cidade_filtro]
vendas_cidade = vendas_sao_paulo.groupby('nome_cliente')['valor_total'].sum().reset_index()

print(f"\nAnálise 2 (Slice): Vendas em {cidade_filtro}:")
print(vendas_cidade)

print("\n✅ O Python, através de bibliotecas como Pandas, é ideal para simular a ETL (Extração, Transformação e Carga) e as análises do OLAP.")