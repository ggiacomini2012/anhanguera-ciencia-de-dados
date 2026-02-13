# Este script Python serve como um exemplo prático dos conceitos de Data Warehouse,
# ETL (Extração, Transformação, Carga) e Análise de Dados (OLAP), baseados na aula.
#
# Ele simula a coleta de dados de diferentes "fontes de dados" e a unificação
# e limpeza desses dados para um "repositório" central.

import json
from datetime import datetime

# --- 1. Ponto de Partida: Fontes de Dados (Sistemas OLTP) ---
# Os dados são coletados de sistemas operacionais transacionais (OLTP).
# Neste exemplo, temos dados de vendas e dados de reclamações de clientes.
# Note as inconsistências e a natureza transacional dos dados brutos.

# Fonte de Dados 1: Sistema de Vendas
# Dados sobre cada item vendido, com possíveis erros (ex: "camisA").
dados_vendas_originais = [
    {"id_venda": 101, "produto": "calca jeans", "quantidade": 2, "preco": 80.0, "data": "2023-01-15"},
    {"id_venda": 102, "produto": "camiseta", "quantidade": 1, "preco": 35.0, "data": "2023-01-15"},
    {"id_venda": 103, "produto": "camisA", "quantidade": 3, "preco": 35.0, "data": "2023-01-16"},
    {"id_venda": 104, "produto": "calcajeans", "quantidade": 1, "preco": 80.0, "data": "2023-01-16"},
]

# Fonte de Dados 2: Sistema de Reclamações de Clientes
# Dados sobre reclamações, com informações que podem ser úteis para análise.
dados_reclamacoes_originais = [
    {"id_reclamacao": 501, "id_venda": 103, "motivo": "produto danificado"},
    {"id_reclamacao": 502, "id_venda": 101, "motivo": "entrega atrasada"},
]

# Tabela de Dimensão: Produtos (para enriquecer os dados)
# Corresponde a um esquema de dimensão, facilitando a análise.
dimensao_produtos = {
    "calca jeans": {"categoria": "vestuario", "subcategoria": "calca"},
    "camiseta": {"categoria": "vestuario", "subcategoria": "camiseta"}
}


# --- 2. Processo de ETL (Extração, Transformação, Carga) ---

def extrair_dados():
    """
    Simula a etapa de Extração (E) do ETL.
    Coleta dados das fontes originais (OLTP).
    """
    print("Iniciando a etapa de Extração...")
    return dados_vendas_originais, dados_reclamacoes_originais

def transformar_dados(vendas_brutas, reclamacoes_brutas, dimensao_produtos):
    """
    Simula a etapa de Transformação (T) do ETL.
    Realiza a limpeza, integração e enriquecimento dos dados.
    """
    print("Iniciando a etapa de Transformação e Limpeza de Dados...")
    
    # 2.1. Limpeza de Dados (ex: "fuzzy lookup" e normalização)
    # Correção de erros de digitação e padronização.
    vendas_limpas = []
    for venda in vendas_brutas:
        # Normaliza o nome do produto para minúsculas e sem espaços extras.
        nome_produto = venda['produto'].lower().replace(" ", "")
        
        # Simula a "pesquisa difusa" ou correção.
        if "calca" in nome_produto:
            venda['produto'] = "calca jeans"
        elif "camisa" in nome_produto or "camiseta" in nome_produto:
            venda['produto'] = "camiseta"
        
        vendas_limpas.append(venda)
        
    # 2.2. Integração de Esquema e Enriquecimento de Dados
    # Combina dados de diferentes fontes e adiciona informações da tabela de dimensão.
    deposito_dados_integrado = []
    for venda in vendas_limpas:
        # Encontra informações da dimensão do produto
        info_produto = dimensao_produtos.get(venda['produto'], {})
        
        # Encontra reclamações associadas à venda (operação de "junção")
        reclamacao_associada = next((r for r in reclamacoes_brutas if r['id_venda'] == venda['id_venda']), None)
        
        # Cria um novo registro para o Data Warehouse (tabela de fatos)
        registro_fato = {
            "id_venda": venda['id_venda'],
            "produto": venda['produto'],
            "quantidade": venda['quantidade'],
            "preco_unitario": venda['preco'],
            "total_venda": venda['quantidade'] * venda['preco'],
            "data": datetime.strptime(venda['data'], "%Y-%m-%d").date(),
            "categoria_produto": info_produto.get("categoria", "N/A"),
            "subcategoria_produto": info_produto.get("subcategoria", "N/A"),
            "teve_reclamacao": "Sim" if reclamacao_associada else "Nao",
            "motivo_reclamacao": reclamacao_associada['motivo'] if reclamacao_associada else "N/A"
        }
        deposito_dados_integrado.append(registro_fato)
        
    return deposito_dados_integrado

def carregar_dados(dados_transformados):
    """
    Simula a etapa de Carga (L) do ETL.
    Armazena os dados transformados no "Data Warehouse".
    """
    print("Iniciando a etapa de Carga...")
    print(f"Dados prontos para o Data Warehouse (total de {len(dados_transformados)} registros):")
    # Usa `json.dumps` para uma formatação de saída amigável.
    print(json.dumps(dados_transformados, indent=2, default=str))
    return dados_transformados

def realizar_analise_olap(data_warehouse):
    """
    Simula uma consulta de Análise de Dados (OLAP) sobre o Data Warehouse.
    Os dados já estão limpos e prontos para agregação.
    """
    print("\n--- 3. Análise e Suporte à Decisão (OLAP) ---")
    print("Realizando uma análise sobre o Data Warehouse...")
    
    # Exemplo: total de vendas por categoria de produto.
    vendas_por_categoria = {}
    for registro in data_warehouse:
        categoria = registro['categoria_produto']
        total = registro['total_venda']
        if categoria in vendas_por_categoria:
            vendas_por_categoria[categoria] += total
        else:
            vendas_por_categoria[categoria] = total
            
    print("\nResumo OLAP: Total de vendas por categoria de produto:")
    for categoria, total in vendas_por_categoria.items():
        print(f"  - {categoria}: R$ {total:.2f}")

# --- Execução do Processo completo ---

if __name__ == "__main__":
    # 1. Extração dos dados das fontes
    vendas, reclamacoes = extrair_dados()
    
    # 2. Transformação e Limpeza dos dados
    dados_dw = transformar_dados(vendas, reclamacoes, dimensao_produtos)
    
    # 3. Carga dos dados no Data Warehouse
    data_warehouse = carregar_dados(dados_dw)
    
    # 4. Análise dos dados para tomada de decisão
    realizar_analise_olap(data_warehouse)
