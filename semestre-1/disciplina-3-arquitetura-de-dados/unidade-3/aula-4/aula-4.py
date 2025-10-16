import pandas as pd
from datetime import datetime

# --- 1. ETAPA DE EXTRAÇÃO (E) - Simulando o ODS ---
# O ODS é caótico e transacional. Temos vendas detalhadas e despadronizadas.

print("1. EXTRAÇÃO: Capturando dados brutos do ODS (Operacional)")
dados_ods = {
    'id_transacao': [101, 102, 103, 104, 105, 106],
    'data_venda': ['2025-09-01', '2025-09-01', '2025-09-02', '2025-09-02', '2025-09-03', '2025-09-03'],
    'regiao_venda': ['Sudeste', 'sudeste', 'Norte', 'Norte', 'Sul', 'SUL'], # Dados inconsistentes
    'nome_produto': ['TV 50', 'FONE Bluetooth', 'TV 50', 'FONE Bluetooth', 'TV 50', 'FONE Bluetooth'],
    'valor_bruto': [2500.50, 150.00, 2500.50, 150.00, 2500.50, 150.00],
    'quantidade': [1, 2, 1, 3, 1, 4]
}

df_ods = pd.DataFrame(dados_ods)
print("\nDados Brutos (ODS):\n", df_ods)


# --- 2. ETAPA DE TRANSFORMAÇÃO (T) - Preparando para o DW ---
# Aqui fazemos a limpeza, padronização e cálculo de métricas (coração do ETL).

print("\n2. TRANSFORMAÇÃO: Limpeza, Padronização e Enriquecimento")

# T1: Tratamento de inconsistências de região (Padronização)
df_ods['regiao_venda'] = df_ods['regiao_venda'].str.title()
print("\nRegiões padronizadas:", df_ods['regiao_venda'].unique())

# T2: Conversão de tipos de dados
df_ods['data_venda'] = pd.to_datetime(df_ods['data_venda'])

# T3: Criação de métricas de FATO (Enriquecimento)
df_ods['receita_total'] = df_ods['valor_bruto'] * df_ods['quantidade']

# T4: Seleção das colunas relevantes para o DW (Estrutura Analítica)
df_dw = df_ods[['data_venda', 'regiao_venda', 'nome_produto', 'quantidade', 'receita_total']]


# --- 3. ETAPA DE CARGA (L) - Movendo para o DW Simulador ---
# O DW contém dados limpos e prontos para agregação.

print("\n3. CARGA: Dados prontos para o Data Warehouse (DW)")
print("\nDados Limpos e Enriquecidos (DW):\n", df_dw)


# --- 4. CONSULTAS SQL / ANÁLISE (O uso da informação) ---
# Simulação de consultas SQL complexas para gerar relatórios (usando pandas como motor SQL)

print("\n4. CONSULTAS ANALÍTICAS (Simulando SQL para Relatórios)")

# 4.1. Consulta 1: Total de Receita por Região (GROUP BY e SUM em SQL)
print("\n--- Insight 1: Receita Total por Região ---")
# SELECT regiao_venda, SUM(receita_total) FROM df_dw GROUP BY regiao_venda
receita_por_regiao = df_dw.groupby('regiao_venda')['receita_total'].sum().reset_index()
# Formatação para Relatório
receita_por_regiao['receita_total'] = receita_por_regiao['receita_total'].map('R$ {:,.2f}'.format)
print(receita_por_regiao)

# 4.2. Consulta 2: Produto com Maior Quantidade Vendida (GROUP BY, SUM e ORDER BY em SQL)
print("\n--- Insight 2: Ranking de Produtos por Volume de Venda ---")
# SELECT nome_produto, SUM(quantidade) FROM df_dw GROUP BY nome_produto ORDER BY SUM(quantidade) DESC
vendas_por_produto = df_dw.groupby('nome_produto')['quantidade'].sum().reset_index()
ranking_produtos = vendas_por_produto.sort_values(by='quantidade', ascending=False)
produto_mais_vendido = ranking_produtos.iloc[0]

print(ranking_produtos)
print(f"\n✅ Produto Mais Vendido (KPI): {produto_mais_vendido['nome_produto']} com {produto_mais_vendido['quantidade']} unidades.")

# 4.3. Conclusão: Relatório para Tomada de Decisão
print("\n--- 5. CONSTRUÇÃO DE RELATÓRIO E DECISÃO ---")
if produto_mais_vendido['nome_produto'] == 'TV 50':
    print("Decisão Acionável: A 'TV 50' tem alta receita, mas o 'FONE Bluetooth' tem alto volume. Estratégia: Promover o 'FONE Bluetooth' como item de 'venda cruzada' para aumentar a receita por transação.")
else:
    print("Decisão Acionável: A TV 50 é o carro-chefe em receita. Devemos focar em maximizar a margem de lucro deste produto.")