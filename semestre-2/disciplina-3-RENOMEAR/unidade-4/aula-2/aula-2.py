# aula-2.py
# Exemplo de Processamento, Algoritmo e a Etapa T (Transform) do ETL
# Tema: Arquitetura de Dados - Otimização de Transações de E-commerce

from typing import List, Dict, Any

# 1. ETAPA 'E' (Extract): Simulação de dados brutos extraídos de um sistema legado
# Perceba as inconsistências (letras maiúsculas/minúsculas, espaços extras, abreviações)
dados_brutos: List[Dict[str, Any]] = [
    {"id_transacao": 101, "cliente_id": "C001", "produto": "laptop-gamer", "qtd": 1, "preco_unitario": 5000.00, "cidade": "sao paulo"},
    {"id_transacao": 102, "cliente_id": "C002", "produto": "Mouse ergonômico", "qtd": 2, "preco_unitario": 150.50, "cidade": "rio de janeiro "},
    {"id_transacao": 103, "cliente_id": "C001", "produto": "LAPTOP-GAMER", "qtd": 1, "preco_unitario": 5000.00, "cidade": "S. Paulo"},
    {"id_transacao": 104, "cliente_id": "C003", "produto": "teclado usb", "qtd": 5, "preco_unitario": 89.90, "cidade": " Curitiba"},
    {"id_transacao": 105, "cliente_id": "C004", "produto": "cabo de rede", "qtd": 20, "preco_unitario": 15.00, "cidade": "São Paulo"},
]

# 2. ETAPA 'T' (Transform) e Processamento/Algoritmo

def processar_dados_transacionais(dados_brutos: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Função principal de Transformação que implementa algoritmos de limpeza e cálculo.

    A função exemplifica o Processamento de Algoritmo em 3 passos:
    1. Padronização de dados (Limpeza e Consistência).
    2. Cálculo de valor agregado (Processamento Simples).
    3. Aplicação de Regra de Negócio (Classificação).
    """
    dados_transformados = []
    
    # Dicionário de padronização (Algoritmo de Mapeamento)
    mapa_cidades = {
        "sao paulo": "São Paulo",
        "S. Paulo": "São Paulo",
        "rio de janeiro ": "Rio de Janeiro",
        " Curitiba": "Curitiba"
    }
    
    mapa_produtos = {
        "laptop-gamer": "Laptop Gamer",
        "LAPTOP-GAMER": "Laptop Gamer",
        "Mouse ergonômico": "Mouse Ergonômico",
        "teclado usb": "Teclado USB",
        "cabo de rede": "Cabo de Rede"
    }

    print("--- 🧠 Início do Processamento de Algoritmo (ETL: Transform) ---")
    
    for registro in dados_brutos:
        # Cria uma cópia para não alterar a lista original (Boas práticas)
        registro_transformado = registro.copy()

        # 1. Padronização de Dados (Limpeza e Consistência)
        # Aplica o mapeamento e o método .strip() para remover espaços
        cidade_bruta = registro_transformado.get("cidade", "").strip()
        registro_transformado["cidade"] = mapa_cidades.get(cidade_bruta, cidade_bruta)

        # Transforma e padroniza o produto:
        produto_bruto = registro_transformado.get("produto", "")
        registro_transformado["produto"] = mapa_produtos.get(produto_bruto, produto_bruto)


        # 2. Cálculo (Processamento do Algoritmo)
        # Adiciona o campo de valor_total (agregado)
        preco = registro_transformado.get("preco_unitario", 0.0)
        quantidade = registro_transformado.get("qtd", 0)
        valor_total = preco * quantidade
        registro_transformado["valor_total"] = round(valor_total, 2)
        
        
        # 3. Aplicação de Regra de Negócio (Classificação - Algoritmo de Decisão)
        # Classifica o cliente com base na regra de negócio
        if registro_transformado["qtd"] >= 10:
            registro_transformado["status_cliente"] = "VIP (Grande Volume)"
        elif registro_transformado["valor_total"] >= 5000:
            registro_transformado["status_cliente"] = "VIP (Alto Valor)"
        else:
            registro_transformado["status_cliente"] = "Padrão"

        dados_transformados.append(registro_transformado)
        
    print("--- ✅ Processamento Concluído ---")
    return dados_transformados

# 3. ETAPA 'L' (Load): Simulação de carregamento e visualização do resultado
def simular_carregamento(dados_transformados: List[Dict[str, Any]]):
    """Simula a carga dos dados transformados em um Data Warehouse (DW)."""
    print("\n--- 📦 Início da Simulação de Carga (ETL: Load) no DW ---")
    # Tabela formatada para visualização do dado "limpo"
    for dado in dados_transformados:
        print(f"| ID: {dado['id_transacao']} | Produto: {dado['produto']:<16} | Cidade: {dado['cidade']:<15} | Total: R$ {dado['valor_total']:<8.2f} | Status: {dado['status_cliente']}")
    print("--- Fim da Carga. Dados prontos para BI! ---")
    
    # Exemplo de consulta (Processamento de Consulta pós-ETL)
    vips = [d for d in dados_transformados if "VIP" in d["status_cliente"]]
    print(f"\n💡 Insight de BI: {len(vips)} transações classificadas como VIP.")

# Execução do ETL
dados_limpos_e_prontos = processar_dados_transacionais(dados_brutos)
simular_carregamento(dados_limpos_e_prontos)