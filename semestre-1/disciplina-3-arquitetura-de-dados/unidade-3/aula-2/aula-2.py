
from datetime import datetime
import pandas as pd

# --- METADADOS DE NEGÓCIO: Dicionário que explica o que os dados significam ---
METADADOS = {
    "Vendas": "Transações brutas de vendas do sistema PDV.",
    "Clientes_CRM": "Informações de clientes (ID, Nome, Cidade) do sistema CRM.",
    "DW_Fato_Vendas": "Tabela central no DW (Schema Estrela), com chaves e métricas consolidadas.",
    "ETL_Timestamp": "Registro de data/hora em que o processo de carga (LOAD) ocorreu."
}

def identificar_fontes_e_extrair():
    """Passo 1: Simula a Extração (E) de dados de fontes heterogêneas."""
    print("1. 🔍 EXTRAÇÃO DE DADOS (E): Identificando e coletando dados brutos...")
    
    # Fonte 1: Dados de Vendas Brutas (Simulação de um sistema de PDV)
    dados_vendas = {
        'transacao_id': [101, 102, 103, 104, 105],
        'id_cliente_bruto': ['C1', 'C2', 'C3', 'C1', 'C6'], # C6 é um dado 'não íntegro'
        'produto_sku': ['SKU001', 'SKU002', 'SKU001', 'SKU003', 'SKU004'],
        'valor_bruto': [150.00, 55.50, 150.00, 200.00, 75.00],
        'data_transacao': ['2023-10-10', '2023-10-10', '2023-10-11', '2023-10-12', '2023-10-12']
    }
    df_vendas = pd.DataFrame(dados_vendas)
    
    # Fonte 2: Dados de Clientes (Simulação de um sistema CRM)
    dados_clientes = {
        'id_crm': ['C1', 'C2', 'C3', 'C4', 'C5'],
        'nome_cliente': ['Alice', 'Bruno', 'Carla', 'Daniel', 'Eduarda'],
        'cidade_cliente': ['São Paulo', 'Rio de Janeiro', 'São Paulo', 'Belo Horizonte', 'Recife']
    }
    df_clientes = pd.DataFrame(dados_clientes)
    
    print(f"   -> Dados de Vendas Extraídos ({len(df_vendas)} linhas).")
    print(f"   -> Dados de Clientes Extraídos ({len(df_clientes)} linhas).")
    
    # Retornamos os DataFrames brutos (simulando a Staging Area inicial)
    return df_vendas, df_clientes

def aplicar_transformacao(df_vendas, df_clientes):
    """Passo 2: Simula a Transformação (T) e Limpeza de dados."""
    print("\n2. 🧹 TRANSFORMAÇÃO DE DADOS (T): Limpeza, Padronização e Integração...")
    
    # TAREFA 1: Limpeza - Lidando com 'Dados Não-Íntegros' (ID do cliente que não existe no CRM)
    # C6 existe em vendas, mas não em clientes. Vamos registrá-lo e removê-lo ou tratá-lo.
    clientes_validos = df_clientes['id_crm'].tolist()
    
    # Identifica transações com IDs inválidos para o LOG de Metadados Técnicos
    transacoes_invalidas = df_vendas[~df_vendas['id_cliente_bruto'].isin(clientes_validos)]
    if not transacoes_invalidas.empty:
        print(f"   ⚠️ Metadado Técnico: {len(transacoes_invalidas)} transações com 'id_cliente_bruto' não encontrado no CRM foram identificadas.")
    
    # Remove as linhas não íntegras para garantir a integridade referencial do DW
    df_vendas_limpo = df_vendas[df_vendas['id_cliente_bruto'].isin(clientes_validos)].copy()
    
    # TAREFA 2: Padronização/Cálculo - Cria uma métrica de fato
    # Suponha que o valor final (métrica do DW) é o valor_bruto - 10% de imposto simulado
    df_vendas_limpo['valor_liquido'] = df_vendas_limpo['valor_bruto'] * 0.90
    
    # TAREFA 3: Integração (Criação do esquema estrela)
    # Merge com os dados de clientes para obter a Dimensão 'Cidade'
    # Esta é a formação da "Tabela Fato" (Fato Vendas) no DW
    df_fato = pd.merge(
        df_vendas_limpo, 
        df_clientes[['id_crm', 'cidade_cliente']],
        left_on='id_cliente_bruto',
        right_on='id_crm',
        how='inner' # Garante apenas registros íntegros
    )
    
    # Seleciona as colunas finais para o DW, criando chaves de negócio e métricas
    df_fato_dw = df_fato[[
        'transacao_id',
        'id_cliente_bruto',
        'produto_sku',
        'cidade_cliente', # Dimensão extraída
        'valor_liquido', # Métrica (Fato)
        'data_transacao'
    ]]
    
    print(f"   -> Tabela Fato (DW) criada e limpa ({len(df_fato_dw)} linhas).")
    return df_fato_dw

def carregar_no_data_warehouse(df_fato_dw):
    """Passo 3: Simula a Carga (L) dos dados no Repositório do DW."""
    print("\n3. 💾 CARGA DE DADOS (L): Inserindo dados na Tabela Fato do Repositório DW...")
    
    # Simulação de inserção no banco de dados do DW
    nome_tabela_dw = METADADOS["DW_Fato_Vendas"] # Exemplo de Metadado de Negócio em uso
    print(f"   -> Carregando {len(df_fato_dw)} registros na tabela: '{nome_tabela_dw}'.")
    
    # Adiciona o Metadado Técnico (Timestamp) ao processo
    timestamp_carga = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Exibição do Repositório Final (Simulação de consulta analítica)
    print("\n   --- REPOSITÓRIO DW (Fato Vendas) ---")
    print(df_fato_dw.head())
    
    # Exemplo de consulta analítica: Vendas por Cidade
    vendas_por_cidade = df_fato_dw.groupby('cidade_cliente')['valor_liquido'].sum().reset_index()
    print("\n   --- ANÁLISE DW (Exemplo de Consulta Analítica) ---")
    print(vendas_por_cidade)
    
    print(f"\n4. 📝 METADADO TÉCNICO: ETL Concluído em: {timestamp_carga}")

# --- Execução do Processo de Implantação e Uso do DW (Simulado) ---
if __name__ == "__main__":
    print(f"🚀 INÍCIO DO PROCESSO ETL PARA DATA WAREHOUSE (Aula {2}) 🚀")
    
    # I. Extração e Staging
    df_vendas_bruto, df_clientes_bruto = identificar_fontes_e_extrair()
    
    # II. Transformação (Limpeza e Integração)
    df_fato_final = aplicar_transformacao(df_vendas_bruto, df_clientes_bruto)
    
    # III. Carga no Repositório DW e Uso
    carregar_no_data_warehouse(df_fato_final)
    
    print("\n✅ PROCESSO CONCLUÍDO. O Repositório DW está pronto para análises!")