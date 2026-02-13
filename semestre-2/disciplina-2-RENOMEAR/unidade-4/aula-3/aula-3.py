# aula-3.py
# Exemplificação das Formas Normais de Boyce-Codd (FNBC) e 4FN

# ==============================================================================
# Conceitos Iniciais
# ==============================================================================
# A normalização é o processo de organizar um banco de dados para minimizar a
# redundância e as anomalias de inserção, atualização e exclusão.
# Vimos as 1FN, 2FN e 3FN, mas agora vamos mergulhar nas formas mais avançadas.

print("---")
print("Iniciando a jornada da Normalização Avançada...")
print("---")


# ==============================================================================
# Exemplo 1: Forma Normal de Boyce-Codd (FNBC)
# ==============================================================================
# A FNBC é uma versão mais rigorosa da 3FN.
# Uma tabela está na FNBC se e somente se cada determinante é uma chave candidata.
# Lembre-se: um determinante é um atributo (ou conjunto de atributos) que
# determina o valor de outro(s) atributo(s).

print("### Exemplo da FNBC: A Entidade 'Filho' ###")

# Cenário inicial (antes da normalização):
# Temos uma única tabela 'Filho' com dependências problemáticas.
# Suponhamos que Nome_Professor e Numero_Sala determinam um ao outro.
# Isso viola a FNBC, pois não são chaves candidatas.

tabela_filho_antes_fnbc = {
    'Nome_Filho': ['João', 'Maria', 'Pedro', 'João'],
    'Endereco_Filho': ['Rua A', 'Rua B', 'Rua C', 'Rua A'],
    'Data_Nascimento': ['10/01/2015', '15/05/2016', '20/09/2017', '10/01/2015'],
    'Nome_Escola': ['Escola X', 'Escola Y', 'Escola X', 'Escola Z'],
    'Numero_Sala': ['101', '205', '101', '302'],
    'Nome_Professor': ['Prof. Ana', 'Prof. Carlos', 'Prof. Ana', 'Prof. Paula']
}

print("\nCenário inicial - Tabela 'Filho' (violando a FNBC):")
import pandas as pd
df_antes_fnbc = pd.DataFrame(tabela_filho_antes_fnbc)
print(df_antes_fnbc)

# Ação: Dividir a tabela para remover a dependência.
# Criamos uma tabela para os dados do filho e outra para a relação Professor-Sala.

# Tabela 1: FILHO (Agora na FNBC)
tabela_filho_fnbc = {
    'Nome_Filho': ['João', 'Maria', 'Pedro', 'João'],
    'Endereco_Filho': ['Rua A', 'Rua B', 'Rua C', 'Rua A'],
    'Data_Nascimento': ['10/01/2015', '15/05/2016', '20/09/2017', '10/01/2015'],
    'Nome_Escola': ['Escola X', 'Escola Y', 'Escola X', 'Escola Z'],
    'Numero_Sala': ['101', '205', '101', '302']
}

# Tabela 2: SALA (Agora na FNBC)
tabela_sala_fnbc = {
    'Numero_Sala': ['101', '205', '302'],
    'Nome_Professor': ['Prof. Ana', 'Prof. Carlos', 'Prof. Paula'],
    'Nome_Escola': ['Escola X', 'Escola Y', 'Escola Z']
}

print("\nCenário normalizado - Tabela 'Filho' (na FNBC):")
df_filho_fnbc = pd.DataFrame(tabela_filho_fnbc)
print(df_filho_fnbc)

print("\nCenário normalizado - Tabela 'Sala' (na FNBC):")
df_sala_fnbc = pd.DataFrame(tabela_sala_fnbc)
print(df_sala_fnbc)

print("\n--> Observação: A dependência entre 'Nome_Professor' e 'Numero_Sala' foi isolada em uma tabela separada, garantindo que cada determinante seja uma chave candidata.")
print("---")


# ==============================================================================
# Exemplo 2: Quarta Forma Normal (4FN)
# ==============================================================================
# Uma tabela está na 4FN se não possui dependências multivaloradas.
# Isso acontece quando temos mais de um "fato" multivalorado em uma única tabela,
# levando a repetições e redundância.

print("### Exemplo da 4FN: A Entidade 'Compra' ###")

# Cenário inicial (antes da normalização):
# A tabela 'Compra' tenta juntar dois fatos multivalorados:
# 1. Qual produto um fornecedor oferece.
# 2. Qual comprador um fornecedor atende.
# CodFornecedor ->-> CodProduto (dependência multivalorada)
# CodFornecedor ->-> CodComprador (dependência multivalorada)

tabela_compra_antes_4fn = {
    'CodFornecedor': [101, 102, 110, 530, 101],
    'CodProduto': ['BA3', 'CJ10', '88A', 'BA3', 'BA3'],
    'CodComprador': ['01', '05', '25', '01', '25']
}

print("\nCenário inicial - Tabela 'Compra' (violando a 4FN):")
df_antes_4fn = pd.DataFrame(tabela_compra_antes_4fn)
print(df_antes_4fn)

# Ação: Dividir a tabela em duas, uma para cada fato multivalorado.

# Tabela 1: FORNECEDOR_PRODUTO (Agora na 4FN)
tabela_fornecedor_produto_4fn = {
    'CodFornecedor': [101, 102, 110, 530, 101],
    'CodProduto': ['BA3', 'CJ10', '88A', 'BA3', 'BA3']
}

# Tabela 2: FORNECEDOR_COMPRADOR (Agora na 4FN)
tabela_fornecedor_comprador_4fn = {
    'CodFornecedor': [101, 102, 110, 530],
    'CodComprador': ['01', '05', '25', '01']
}
# Nota: o registro (101, 25) na tabela original é um caso de anomalia ou
# repetição desnecessária, que a normalização corrige. Vamos assumir a
# separação dos fatos.

print("\nCenário normalizado - Tabela 'FornecedorProduto' (na 4FN):")
df_forn_prod_4fn = pd.DataFrame(tabela_fornecedor_produto_4fn)
print(df_forn_prod_4fn.drop_duplicates()) # Mostrando a tabela sem redundâncias

print("\nCenário normalizado - Tabela 'FornecedorComprador' (na 4FN):")
df_forn_comp_4fn = pd.DataFrame(tabela_fornecedor_comprador_4fn)
print(df_forn_comp_4fn.drop_duplicates()) # Mostrando a tabela sem redundâncias

print("\n--> Observação: A tabela original misturava dois fatos. Agora, cada tabela trata de um único fato, eliminando a redundância e as anomalias.")
print("---")
print("Fim da exemplificação. A normalização é a chave para a integridade dos dados!")