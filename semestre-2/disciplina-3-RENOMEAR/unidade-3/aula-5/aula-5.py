import pandas as pd
from datetime import datetime

# ==============================================================================
# 1. EXTRAÇÃO (E) - Simulando Dados de Múltiplas Fontes (ODS)
# ==============================================================================

# Fonte 1: Dados brutos de vendas do Site (com alguns erros)
dados_site_brutos = {
    'id_transacao': [101, 102, 103, 104, 105],
    'produto': ['Notebook X', 'MousePad', 'Fone Pro', 'Teclado Mec', 'MousePad'],
    'valor_bruto': [1500.50, 50.00, 'R$ 200,99', 450.00, 50.00], # Erro: formato de moeda
    'localizacao': ['SP', 'RJ', 'sp', 'MG', 'rj'], # Erro: inconsistência de caixa
    'data_compra': ['2024-10-15', '2024-10-16', '2024-10-16', '2024-10-17', '2024-10-17'],
    'status_entrega': ['ENTREGUE', 'PENDENTE', 'ENTREGUE', 'ENTREGUE', 'PENDENTE']
}
df_site = pd.DataFrame(dados_site_brutos)

# Fonte 2: Dados de Avaliações do Aplicativo
dados_app_avaliacao = {
    'id_produto': [1003, 1002, 1004],
    'nome_produto': ['Fone Pro', 'MousePad', 'Teclado Mec'],
    'avaliacao': [5, 4, 5]
}
df_avaliacao = pd.DataFrame(dados_app_avaliacao)

print("--- 1. Extração: Dados Brutos do Site ---")
print(df_site)

# ==============================================================================
# 2. METADADOS - Definindo a Estrutura (Governança de Dados)
# ==============================================================================

# Metadados de Negócio e Técnicos para o Data Warehouse
metadados_dw = {
    'Tabela_Fato_Vendas': {
        'coluna': 'valor_venda_liquido',
        'tipo': 'Float',
        'regra_transformacao': 'Valor bruto - 10% de imposto',
        'descricao_negocio': 'Valor final da transação após impostos.'
    },
    'Tabela_Dim_Local': {
        'coluna': 'uf',
        'tipo': 'String',
        'regra_transformacao': 'Converter para Maiúsculas e Padronizar. Ex: SP',
        'descricao_negocio': 'Unidade Federativa padronizada para análise geográfica.'
    }
}

print("\n--- 2. Metadados: Regra para Valor de Venda Líquido ---")
print(f"Coluna: {metadados_dw['Tabela_Fato_Vendas']['coluna']}")
print(f"Regra: {metadados_dw['Tabela_Fato_Vendas']['regra_transformacao']}")

# ==============================================================================
# 3. TRANSFORMAÇÃO (T) - Limpeza e Padronização de Dados
# ==============================================================================

# Aplicando a "Regra de Transformação" do Metadado para 'valor_bruto'
def limpar_e_converter_valor(valor):
    try:
        # Remove caracteres indesejados e converte para float
        if isinstance(valor, str):
            valor = valor.replace('R$', '').replace(',', '.').strip()
        return float(valor)
    except:
        # Se falhar, retorna 0 ou um valor de erro (limpeza/tratamento de exceções)
        return 0.0

df_site['valor_limpo'] = df_site['valor_bruto'].apply(limpar_e_converter_valor)

# 3.1. Criação da Métrica (Cálculo de Fato) - Baseado no Metadado
IMPOSTO_PERCENTUAL = 0.10
df_site['valor_venda_liquido'] = df_site['valor_limpo'] * (1 - IMPOSTO_PERCENTUAL)

# 3.2. Padronização da Dimensão (Localização) - Baseado no Metadado
df_site['uf'] = df_site['localizacao'].str.upper()

# 3.3. Junção de Fontes (Integração de Dados)
# Simulando a necessidade de mapear o nome do produto para um ID
# Em um DW real, faríamos joins com tabelas de Dimensão Produto
df_site['id_produto'] = df_site['produto'].astype('category').cat.codes + 1001

# Selecionando colunas que iriam para o DW (Esquema Estrela/Fato)
df_fato = df_site[['id_transacao', 'id_produto', 'uf', 'data_compra', 'valor_venda_liquido']].copy()
df_fato['data_carga'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S") # Metadado Operacional (Data de Carga)

print("\n--- 3. Transformação: Dados Finais para o DW (Fato Vendas) ---")
print(df_fato)

# ==============================================================================
# 4. CARGA (L) e ANÁLISE (OLAP/BI) - Simulação de Consulta
# ==============================================================================

# Em um ambiente real, 'df_fato' seria carregado no banco de dados (DW - Camada de Apresentação)

# Simulação de Consulta Analítica (OLAP) - Agregação Rápida
# Pergunta: Qual o total de vendas líquidas por UF? (Slice e Aggregate)
analise_vendas_uf = df_fato.groupby('uf')['valor_venda_liquido'].sum().reset_index()

print("\n--- 4. Análise: Vendas Líquidas Agregadas por UF ---")
print(analise_vendas_uf)

# Adicionando um exemplo de Data Mart (Vendas x Avaliação)
df_dim_prod = df_site[['id_produto', 'produto']].drop_duplicates()
df_analise_final = pd.merge(analise_vendas_uf, df_dim_prod, left_on='id_produto', right_on='id_produto', how='left')
# ... (O merge direto aqui seria complexo sem IDs consistentes, focaremos no exemplo anterior)

# Conclusão
print("\n✅ Processo ETL e Metadados simulado com sucesso!")
print(f"Total de Registros carregados (Fato Vendas): {len(df_fato)}")