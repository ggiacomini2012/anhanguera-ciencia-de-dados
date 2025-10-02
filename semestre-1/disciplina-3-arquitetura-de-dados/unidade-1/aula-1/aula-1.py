# Arquivo: aula-1.py
# Aula 1: Introdução à Arquitetura de Dados - A Pirâmide DIKW e o E-commerce

import pandas as pd
from typing import List, Dict

# 1. DADOS (Data): O Petróleo Bruto do E-commerce
# Registros brutos de transações (exemplo de dados de baixo nível)
raw_data: List[Dict] = [
    {"transacao_id": 1001, "cliente_id": "C001", "produto_cor": "azul", "valor": 150.00, "data": "2023-09-01"},
    {"transacao_id": 1002, "cliente_id": "C002", "produto_cor": "verde", "valor": 50.00, "data": "2023-09-01"},
    {"transacao_id": 1003, "cliente_id": "C001", "produto_cor": "verde", "valor": 200.00, "data": "2023-09-02"},
    {"transacao_id": 1004, "cliente_id": "C003", "produto_cor": "azul", "valor": 80.00, "data": "2023-09-02"},
    {"transacao_id": 1005, "cliente_id": "C002", "produto_cor": "vermelho", "valor": 120.00, "data": "2023-09-03"},
]

print("--- 1. DADOS (Data) Brutos ---")
# Estes são os fatos isolados, sem contexto de negócio.
df_dados = pd.DataFrame(raw_data)
print(df_dados.to_markdown(index=False))
print("\n" + "="*50 + "\n")


# 2. INFORMAÇÃO (Information): Contextualizando os Dados
# A arquitetura de dados (ETL/processamento) refina os dados brutos.
# Exemplo: Agrupar por cliente e calcular o valor total gasto e o número de compras.
def refinar_para_informacao(df: pd.DataFrame) -> pd.DataFrame:
    """Transforma dados brutos em informação contextualizada."""
    df_info = df.groupby('cliente_id').agg(
        total_gasto=('valor', 'sum'),
        num_compras=('transacao_id', 'count')
    ).reset_index()
    # Adicionando um contexto: ticket médio
    df_info['ticket_medio'] = df_info['total_gasto'] / df_info['num_compras']
    return df_info

df_informacao = refinar_para_informacao(df_dados)

print("--- 2. INFORMAÇÃO (Information) Contextualizada ---")
# Agora sabemos o QUE e QUANTO cada cliente comprou.
print(df_informacao.to_markdown(index=False, floatfmt=".2f"))
print("\n" + "="*50 + "\n")


# 3. CONHECIMENTO (Knowledge): Encontrando Padrões e Relações
# Cruzar informações para gerar conclusões (análise de dados).
def gerar_conhecimento(df_raw: pd.DataFrame) -> str:
    """Gera conhecimento a partir do cruzamento de dados de cor e cliente."""
    
    # Objetivo: Descobrir clientes que compraram AZUL e depois VERDE.
    # Passo 1: Filtrar as compras por cor.
    df_azul = df_raw[df_raw['produto_cor'] == 'azul']['cliente_id'].unique()
    df_verde = df_raw[df_raw['produto_cor'] == 'verde']['cliente_id'].unique()
    
    # Passo 2: Encontrar a interseção (clientes que compraram ambas as cores).
    clientes_ambas_cores = set(df_azul) & set(df_verde)
    
    # Passo 3: Gerar a conclusão (Conhecimento).
    if clientes_ambas_cores:
        return f"PADRÃO ENCONTRADO: Os clientes {', '.join(clientes_ambas_cores)} compraram produtos AZUIS e VERDES.\nIsso sugere uma relação de compra cruzada ('Cross-selling')."
    else:
        return "Nenhum padrão de compra cruzada AZUL/VERDE encontrado neste período."

conhecimento_gerado = gerar_conhecimento(df_dados)

print("--- 3. CONHECIMENTO (Knowledge) - Padrão Descoberto ---")
# O padrão é a INFERÊNCIA, o 'COMO' as coisas funcionam.
print(conhecimento_gerado)
print("\n" + "="*50 + "\n")


# 4. SABEDORIA (Wisdom): Aplicando o Conhecimento para Ação Estratégica
# A sabedoria é a aplicação do conhecimento para a tomada de decisão (O PORQUÊ).

def aplicar_sabedoria(conhecimento: str, ticket_medio: float) -> str:
    """Transforma o conhecimento em uma Ação Estratégica de Negócio (Sabedoria)."""
    
    estrategia = []
    
    # Sabedoria 1: Ação Baseada no Padrão (Cross-selling)
    if "AZUIS e VERDES" in conhecimento:
        estrategia.append("AÇÃO ESTRATÉGICA (Sabedoria): Criar uma campanha de 'cross-selling' oferecendo um desconto em produtos VERDES para clientes que acabaram de comprar AZUL, visando aumentar o valor do carrinho. (Ciclo OODA: Ação!)")
    
    # Sabedoria 2: Ação Baseada no Ticket Médio (Retenção)
    if ticket_medio > 150.00:
        estrategia.append("AÇÃO ESTRATÉGICA (Sabedoria): Clientes com alto Ticket Médio (> R$150.00) devem ser movidos para um 'Programa de Fidelidade Ouro' para garantir a retenção de alto valor.")
    
    return "\n".join(estrategia)

# Exemplo de Sabedoria focada no cliente de maior valor
cliente_c001_gasto = df_informacao[df_informacao['cliente_id'] == 'C001']['total_gasto'].iloc[0]
estrategia_sabedoria = aplicar_sabedoria(conhecimento_gerado, cliente_c001_gasto)


print("--- 4. SABEDORIA (Wisdom) - Direcional Estratégico ---")
# A Sabedoria informa a alta direção sobre as decisões a serem tomadas.
print("Meta de Negócio: Aumentar o Valor de Vida do Cliente (CLV) e o Ticket Médio.")
print("Resultado da Arquitetura de Dados (Sabedoria):")
print(estrategia_sabedoria)
print("\n" + "="*50 + "\n")

# CONCLUSÃO: O papel da Arquitetura de Dados é construir os dutos e sistemas
# que garantem que essa progressão do DADOS para a SABEDORIA seja fluida,
# confiável e escalável, suportando o Ciclo OODA de forma contínua.