
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from io import StringIO

# ==============================================================================
# 1. SIMULAÇÃO DO DATA LAKE (DATA BRUTO, NÃO ESTRUTURADO/SEMI-ESTRUTURADO)
# ==============================================================================
print("1. SIMULANDO O DATA LAKE 🌊 (Dados Brutos e Variados)")

# Simulação de um log de acesso (semi-estruturado)
log_data = """
timestamp,usuario,acao,dados_adicionais
2025-10-22 09:00:00,user_a,login,sucesso
2025-10-22 09:00:15,user_b,compra,item_id:45,valor:120.50
2025-10-22 09:01:00,user_a,navegacao,pagina:/produtos/eletronicos
2025-10-22 09:02:30,user_c,compra,item_id:12,valor:45.99
2025-10-22 09:03:05,user_b,feedback,nota:5,comentario:Produto excelente!
2025-10-22 09:04:10,user_d,login,erro:senha_invalida
"""
df_log = pd.read_csv(StringIO(log_data))

# Simulação de dados de vendas (estruturado)
vendas_data = {
    'usuario': ['user_b', 'user_c', 'user_e', 'user_f', 'user_g'],
    'total_compras': [3, 1, 10, 2, 5],
    'valor_total_gasto': [360.00, 45.99, 1500.00, 80.00, 520.00],
    'dias_desde_ultima_compra': [5, 12, 1, 30, 8]
}
df_vendas = pd.DataFrame(vendas_data)

print("\n--- Conteúdo do Data Lake (Log Bruto) ---")
print(df_log)
print("\n--- Conteúdo do Data Lake (Vendas Estruturadas) ---")
print(df_vendas)

# ==============================================================================
# 2. MINERAÇÃO DE DADOS (DATA MINING) - Descobrindo Padrões
# ==============================================================================
print("\n" + "="*80)
print("2. MINERAÇÃO DE DADOS ⛏️ (Clustering - Agrupamento de Clientes)")
print("Objetivo: Segmentar clientes com base em seu comportamento de compra.")

# 2.1. Preparação dos dados para Mineração (Limpeza/Transformação)
# Seleciona apenas as variáveis relevantes para a segmentação (RFM - Recência, Frequência, Monetaridade)
X = df_vendas[['total_compras', 'valor_total_gasto', 'dias_desde_ultima_compra']]

# Normalização/Escalonamento dos dados (importante para o K-Means)
X_norm = (X - X.mean()) / X.std()

# 2.2. Aplicação do Algoritmo de Mineração (K-Means Clustering)
# Vamos tentar segmentar em 3 grupos (Clientes de Alto, Médio e Baixo valor)
k = 3
kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
df_vendas['segmento'] = kmeans.fit_predict(X_norm)

# 2.3. Análise dos Resultados
print("\n--- Clientes Segmentados (Resultado da Mineração) ---")
print(df_vendas[['usuario', 'total_compras', 'valor_total_gasto', 'dias_desde_ultima_compra', 'segmento']])

print("\n--- Características de cada Segmento (Insight) ---")
insights = df_vendas.groupby('segmento')[['total_compras', 'valor_total_gasto', 'dias_desde_ultima_compra']].mean()
insights.columns = ['Média Compras', 'Média Gasto', 'Média Dias sem Compra']

# Interpretando os clusters (exemplo didático):
# Segmento 0: Alta Frequência, Alto Gasto, Baixa Recência (Clientes Premium)
# Segmento 1: Baixa Frequência, Baixo Gasto, Alta Recência (Clientes em Risco)
# Segmento 2: Média Frequência, Médio Gasto, Média Recência (Clientes Regulares)
print(insights.sort_values(by='Média Gasto', ascending=False))

# ==============================================================================
# 3. CRIAÇÃO DO DATA MART (DM) - Visão Focada para o Departamento de Marketing
# ==============================================================================
print("\n" + "="*80)
print("3. CRIANDO O DATA MART 🛒 (Focado para Marketing)")

# O Data Mart de Marketing precisa de dados processados e focados no cliente,
# incluindo o insight gerado pela mineração.

# 3.1. Fatiando o Data Lake/Dados Minados
# Cria um subconjunto de dados para o time de Marketing.
# O time de Marketing não precisa do "log_data" brutos, mas sim do resultado
# das vendas + o segmento (informação processada).
df_data_mart_marketing = df_vendas[['usuario', 'valor_total_gasto', 'segmento']]

# 3.2. Adicionando uma coluna de Ação Estratégica
# O insight da mineração (segmento) é transformado em uma ação.
def definir_estrategia(segmento):
    if segmento == insights['Média Gasto'].idxmax():
        return "Programa de Fidelidade Exclusivo" # Segmento 0
    elif segmento == insights['Média Dias sem Compra'].idxmax():
        return "Campanha de Retenção (Desconto)" # Segmento 1
    else:
        return "Oferta de Novo Produto" # Segmento 2

df_data_mart_marketing['estrategia_acao'] = df_data_mart_marketing['segmento'].apply(definir_estrategia)

print("\n--- Data Mart de Marketing (Pronto para Ação) ---")
print(df_data_mart_marketing)

print("\n🚀 Sucesso! O Data Mart agora fornece insights acionáveis de forma rápida e focada para a equipe de Marketing.")