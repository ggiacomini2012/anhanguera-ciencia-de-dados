
# arquivo: aula-1.py
# Exemplo de Matrizes e Produto Matricial em Python

# TEMA: Cálculo de Custo de Produção usando Matrizes (Problema da Confeitaria)

# 1. Definição das Matrizes

# Matriz A (3x4): Quantidade de Ingredientes (Colunas) por Tipo de Doce (Linhas)
# Linhas: [Brigadeiro, Beijinho, Pé de Moleque]
# Colunas: [Ingrediente x, Ingrediente y, Ingrediente z, Ingrediente t]
matriz_ingredientes = [
    [3, 6, 1, 3],  # Brigadeiro
    [4, 4, 2, 2],  # Beijinho
    [0, 1, 1, 6]   # Pé de Moleque
]

# Matriz P (4x1): Preço unitário de cada Ingrediente (Matriz Coluna)
# Linhas: [Preço x, Preço y, Preço z, Preço t]
matriz_precos = [
    [0.20],  # Preço de x
    [0.80],  # Preço de y
    [1.20],  # Preço de z
    [2.80]   # Preço de t
]

# 2. Função para Multiplicação Matricial (A * P)

def multiplicar_matrizes(A, B):
    """
    Realiza o produto matricial C = A * B.
    Condição: O número de colunas de A deve ser igual ao número de linhas de B.
    """
    # Ordem de A: linhas_A (m) x colunas_A (p)
    linhas_A = len(A)
    colunas_A = len(A[0])
    
    # Ordem de B: linhas_B (p) x colunas_B (n)
    linhas_B = len(B)
    colunas_B = len(B[0])
    
    # 🚨 VERIFICAÇÃO DA REGRA DE OURO DO PRODUTO MATRICIAL: p deve ser igual!
    if colunas_A != linhas_B:
        raise ValueError("ERRO: O número de colunas da Matriz A deve ser igual ao número de linhas da Matriz B.")

    # Inicializa a Matriz C (Resultado) com zeros. Ordem: linhas_A (m) x colunas_B (n)
    C = [[0 for _ in range(colunas_B)] for _ in range(linhas_A)]

    # Itera sobre as linhas da Matriz A (i)
    for i in range(linhas_A):
        # Itera sobre as colunas da Matriz B (j)
        for j in range(colunas_B):
            # Itera sobre os elementos internos (k) para realizar a soma do produto
            # C[i][j] = Soma (A[i][k] * B[k][j])
            for k in range(colunas_A): # colunas_A é igual a linhas_B
                C[i][j] += A[i][k] * B[k][j]
                
    return C

# 3. Execução do Cálculo

print("--- Aula 1: Produto Matricial (Confeitaria) ---")

# Verifica as dimensões
m_A = len(matriz_ingredientes)
p_A = len(matriz_ingredientes[0])
p_P = len(matriz_precos)
n_P = len(matriz_precos[0])
print(f"Dimensões A (Ingredientes): {m_A}x{p_A}")
print(f"Dimensões P (Preços): {p_P}x{n_P}")
print(f"Condição de Multiplicação: Colunas de A ({p_A}) == Linhas de P ({p_P})")
print("---------------------------------------------")


try:
    matriz_custo = multiplicar_matrizes(matriz_ingredientes, matriz_precos)
    
    doces = ["Brigadeiro", "Beijinho", "Pé de Moleque"]
    
    print("\n✅ Matriz Custo (C = A * P):")
    for i in range(len(matriz_custo)):
        custo = matriz_custo[i][0]
        print(f"Custo do {doces[i]}: R$ {custo:.2f}")

    # Custo Brigadeiro = (3*0.20) + (6*0.80) + (1*1.20) + (3*2.80) = 0.60 + 4.80 + 1.20 + 8.40 = 15.00
    # Custo Beijinho = (4*0.20) + (4*0.80) + (2*1.20) + (2*2.80) = 0.80 + 3.20 + 2.40 + 5.60 = 12.00
    # Custo Pé de Moleque = (0*0.20) + (1*0.80) + (1*1.20) + (6*2.80) = 0.00 + 0.80 + 1.20 + 16.80 = 18.80
    
    print("\nResultado da Matriz Custo (3x1):")
    # Formatação para melhor visualização
    for linha in matriz_custo:
        print(f"| {linha[0]:6.2f} |")

except ValueError as e:
    print(f"\nERRO NA OPERAÇÃO: {e}")

# OBS: Em um ambiente real, poderíamos usar a biblioteca 'numpy' para este cálculo
# matriz_custo_numpy = np.dot(np.array(matriz_ingredientes), np.array(matriz_precos))
