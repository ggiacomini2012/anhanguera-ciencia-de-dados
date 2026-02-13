import pandas as pd
import json

# ==============================================================================
# 1. Gerenciamento com Dados Mestres (MDM)
# Exemplo: Tabela centralizada e limpa de Produtos (um 'dado mestre')
# ==============================================================================

print("--- 1. Exemplo de Dados Mestres (MDM): Produtos Consistentes ---")

# Dados mestres de produtos (A VERDADE ÚNICA)
dados_mestres_produtos = {
    'ID_Produto': [101, 102, 103, 104],
    'Nome_Produto': ['Monitor LED 27"', 'Teclado Mecânico RGB', 'Mouse Ergonômico', 'Webcam Full HD'],
    'Categoria': ['Hardware', 'Periféricos', 'Periféricos', 'Periféricos'],
    'Preco_Base': [950.00, 280.00, 150.00, 320.00]
}

df_produtos_mestres = pd.DataFrame(dados_mestres_produtos)
print("\nDataFrame de Produtos (MDM):\n", df_produtos_mestres)

# Simulação de um problema de inconsistência (duplicação de dados) em outro sistema
dados_sistema_vendas = {
    'ID_Venda': [1, 2, 3, 4],
    'Produto_Vendido': ['Monitor LED 27"', 'Teclado Mecanico RGB', 'Mouse Ergonômico', 'Monitor LED 27'], # Note as inconsistências
    'Preco_Venda': [955.00, 275.00, 150.00, 950.00]
}

df_vendas = pd.DataFrame(dados_sistema_vendas)
print("\nDataFrame de Vendas (Dados de Transação com Inconsistência):\n", df_vendas)

# O papel do MDM seria garantir que o 'Produto_Vendido' use apenas os nomes do 'df_produtos_mestres'.
# O MDM padroniza e evita erros na análise de inventário e vendas.

print("\n----------------------------------------------------------------")


# ==============================================================================
# 2. Gerenciamento com Dados Heterogêneos
# Exemplo: Integração de dados de clientes de diferentes formatos (SQL e NoSQL/JSON)
# ==============================================================================

print("--- 2. Exemplo de Dados Heterogêneos: Integrando Formatos ---")

# Dados da Tabela 1 (simulando uma tabela relacional SQL de informações básicas)
dados_cliente_sql = {
    'ID_Cliente': [1, 2, 3],
    'Nome': ['Ana Souza', 'Bruno Lima', 'Carla Reis'],
    'Email': ['ana@exemplo.com', 'bruno@exemplo.com', 'carla@exemplo.com']
}
df_sql = pd.DataFrame(dados_cliente_sql)
print("\nDados da Fonte Relacional (SQL):\n", df_sql)

# Dados da Tabela 2 (simulando um documento NoSQL/JSON de preferências e histórico)
# Um formato muito diferente do tabular do SQL
dados_cliente_nosql = [
    {
        "ID_Cliente": 1,
        "Preferencias": {"cor": "azul", "categoria": "Hardware"},
        "Historico_Compras": ["Mouse Ergonômico", "Monitor LED 27"]
    },
    {
        "ID_Cliente": 2,
        "Preferencias": {"cor": "verde", "categoria": "Periféricos"},
        "Historico_Compras": ["Teclado Mecânico RGB"]
    },
    # O cliente 3 pode não ter dados NoSQL ainda, mostrando a disparidade de fontes
]
print("\nDados da Fonte de Documento (NoSQL/JSON):\n", json.dumps(dados_cliente_nosql, indent=4))

# Processo de Integração (Unificação do dado heterogêneo)
df_nosql = pd.json_normalize(dados_cliente_nosql)
df_nosql.rename(columns={'Preferencias.cor': 'Pref_Cor', 'Preferencias.categoria': 'Pref_Categoria'}, inplace=True)
df_nosql = df_nosql[['ID_Cliente', 'Pref_Cor', 'Pref_Categoria', 'Historico_Compras']]

# Junção dos dados (A Mágica da Integração de Dados Heterogêneos)
df_integrado = pd.merge(df_sql, df_nosql, on='ID_Cliente', how='left')
print("\nResultado da Integração (Visão Unificada):\n", df_integrado)

print("\n----------------------------------------------------------------")

# ==============================================================================
# 3. Data Stewards: O Guardião da Qualidade
# Exemplo: Regra simples de qualidade definida por um Business Data Steward
# ==============================================================================

print("--- 3. Data Steward: Verificação de Qualidade ---")

# Regra de Negócio (Definida pelo Business Data Steward):
# "Nenhum produto com preço base superior a R$ 500,00 deve ser da categoria 'Periféricos'."

def verificar_qualidade_dados_mestres(dataframe):
    """Simula a ação de um Data Steward verificando a conformidade dos dados."""
    violacoes = dataframe[
        (dataframe['Preco_Base'] > 500.00) &
        (dataframe['Categoria'] == 'Periféricos')
    ]

    if not violacoes.empty:
        print(f"\n❌ VIOLAÇÃO ENCONTRADA! {len(violacoes)} registro(s) não está(ão) em conformidade com a regra de preço/categoria.")
        print(violacoes)
        # Um Technical Data Steward precisaria agora corrigir esses dados.
        return False
    else:
        print("\n✅ Verificação de Qualidade OK. Dados Mestres em conformidade com a regra de negócio.")
        return True

verificar_qualidade_dados_mestres(df_produtos_mestres)

