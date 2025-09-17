import pandas as pd

def criar_tabela_original():
    """
    Cria e retorna um DataFrame do pandas representando a tabela original
    com dados não-normalizados do formulário do clube de futebol.
    Esta tabela contém redundâncias e dependências funcionais mal definidas.
    """
    dados = {
        'NumeroJogo': [101, 102, 103, 104, 105],
        'DataPartida': ['2023-10-25', '2023-11-02', '2023-11-10', '2023-11-18', '2023-11-25'],
        'LocalJogo': ['Estádio Municipal', 'Arena Olímpica', 'Estádio Municipal', 'Estádio do Morumbi', 'Arena Olímpica'],
        'CidadeLocal': ['Santa Catarina', 'Rio de Janeiro', 'Santa Catarina', 'São Paulo', 'Rio de Janeiro'],
        'NomeOponente': ['Time A', 'Time B', 'Time C', 'Time D', 'Time E'],
        'CodigoJogador': ['J001', 'J002', 'J001', 'J003', 'J002'],
        'NomeJogador': ['João Silva', 'Maria Santos', 'João Silva', 'Pedro Rocha', 'Maria Santos'],
        'PosicaoJogador': ['Atacante', 'Meio-campo', 'Atacante', 'Defensor', 'Meio-campo'],
        'GolsMarcados': [2, 1, 0, 3, 1]
    }
    return pd.DataFrame(dados)

def normalizar_para_primeira_forma_normal(df_original):
    """
    A 1ª Forma Normal (1FN) garante que cada célula contenha um único valor atômico.
    Neste exemplo, a tabela original já está em 1FN.
    """
    print("--- 1ª FORMA NORMAL (1FN) ---")
    print("A tabela original já atende à 1FN, pois não há grupos repetitivos ou listas em uma única célula.")
    return df_original.copy()

def normalizar_para_segunda_forma_normal(df_1fn):
    """
    A 2ª Forma Normal (2FN) remove dependências parciais.
    Nossa chave primária é a combinação de (NumeroJogo, CodigoJogador).
    'NomeJogador' e 'PosicaoJogador' dependem apenas de 'CodigoJogador', não da chave inteira.
    'LocalJogo' e 'CidadeLocal' dependem apenas de 'NumeroJogo', não da chave inteira.
    Vamos separar essas informações em novas tabelas.
    """
    print("\n--- 2ª FORMA NORMAL (2FN) ---")
    
    # Tabela 1: JOGOS (Dependência de NumeroJogo)
    tabela_jogos = df_1fn[['NumeroJogo', 'DataPartida', 'LocalJogo', 'CidadeLocal', 'NomeOponente']].drop_duplicates().reset_index(drop=True)
    print("\n[Tabela JOGOS] - Removendo dependência parcial de 'LocalJogo' e 'CidadeLocal'.")
    print(tabela_jogos)

    # Tabela 2: JOGADORES (Dependência de CodigoJogador)
    tabela_jogadores = df_1fn[['CodigoJogador', 'NomeJogador', 'PosicaoJogador']].drop_duplicates().reset_index(drop=True)
    print("\n[Tabela JOGADORES] - Removendo dependência parcial de 'NomeJogador' e 'PosicaoJogador'.")
    print(tabela_jogadores)
    
    # Tabela 3: ATUACOES (Tabela de ligação, com a chave primária composta)
    tabela_atuacoes = df_1fn[['NumeroJogo', 'CodigoJogador', 'GolsMarcados']].copy()
    print("\n[Tabela ATUACOES] - Tabela de ligação que mantém o relacionamento entre JOGOS e JOGADORES.")
    print(tabela_atuacoes)
    
    return tabela_jogos, tabela_jogadores, tabela_atuacoes

def normalizar_para_terceira_forma_normal(tabela_jogos):
    """
    A 3ª Forma Normal (3FN) remove dependências transitivas.
    Em nossa tabela 'JOGOS', o 'CidadeLocal' depende de 'LocalJogo', que não é a chave primária.
    Vamos separar essa informação em uma nova tabela de LOCALIZACAO.
    """
    print("\n--- 3ª FORMA NORMAL (3FN) ---")
    
    # Tabela 1: LOCALIZACOES (Dependência transitiva de CidadeLocal)
    tabela_localizacoes = tabela_jogos[['LocalJogo', 'CidadeLocal']].drop_duplicates().reset_index(drop=True)
    print("\n[Tabela LOCALIZACOES] - Removendo a dependência transitiva de 'CidadeLocal'.")
    print(tabela_localizacoes)

    # Tabela 2: JOGOS_NORMALIZADA (Tabela de jogos agora referenciando a nova tabela)
    tabela_jogos_normalizada = tabela_jogos.drop(columns=['CidadeLocal']).copy()
    print("\n[Tabela JOGOS_NORMALIZADA] - Tabela JOGOS após a normalização.")
    print(tabela_jogos_normalizada)

    return tabela_localizacoes, tabela_jogos_normalizada


# --- Execução do processo de Normalização ---
if __name__ == "__main__":
    print("--------------------------------------------------")
    print("      EXEMPLO DE NORMALIZAÇÃO DE DADOS EM PYTHON     ")
    print("--------------------------------------------------")

    # Passo 1: Criação da tabela não-normalizada
    df_formulario = criar_tabela_original()
    print("\n[Tabela Original - Formulário do Clube]")
    print(df_formulario)
    
    # Passo 2: Normalização para 1FN
    df_1fn = normalizar_para_primeira_forma_normal(df_formulario)
    
    # Passo 3: Normalização para 2FN
    jogos, jogadores, atuacoes = normalizar_para_segunda_forma_normal(df_1fn)
    
    # Passo 4: Normalização para 3FN
    localizacoes, jogos_normalizada = normalizar_para_terceira_forma_normal(jogos)

    print("\n--------------------------------------------------")
    print("           PROCESSO DE NORMALIZAÇÃO FINALIZADO       ")
    print("--------------------------------------------------")
    print("Observe como o processo de normalização dividiu uma única tabela com redundâncias em tabelas menores, mais organizadas e eficientes, eliminando a repetição de dados.")