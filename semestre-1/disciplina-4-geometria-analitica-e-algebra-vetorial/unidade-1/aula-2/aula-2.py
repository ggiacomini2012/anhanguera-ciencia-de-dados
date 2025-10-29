import numpy as np

# TEMA DA AULA: Determinantes de Matrizes Quadradas

def calcular_determinante_2x2(matriz_A):
    """
    Calcula o determinante de uma matriz 2x2.
    
    O determinante de A é o produto dos elementos da diagonal principal
    menos o produto dos elementos da diagonal secundária.
    
    A = [[a11, a12],
         [a21, a22]]
    det(A) = a11*a22 - a12*a21
    """
    if matriz_A.shape != (2, 2):
        raise ValueError("A matriz deve ser de ordem 2x2.")
    
    # Cálculo manual conforme a definição para matriz 2x2
    det_manual = matriz_A[0, 0] * matriz_A[1, 1] - matriz_A[0, 1] * matriz_A[1, 0]
    
    # Cálculo usando a função do NumPy (para comparação)
    det_numpy = np.linalg.det(matriz_A)
    
    print("\n--- Exemplo de Matriz 2x2 ---")
    print("Matriz A:\n", matriz_A)
    print(f"1. Cálculo Manual (a11*a22 - a12*a21): {det_manual}")
    print(f"2. Cálculo por NumPy (np.linalg.det): {det_numpy}")
    print("-" * 30)
    
    return det_manual

def calcular_determinante_3x3(matriz_A):
    """
    Calcula o determinante de uma matriz 3x3 (conceito de Regra de Sarrus).
    
    Para matrizes de ordem 3x3, utiliza-se a Regra de Sarrus.
    
    A regra consiste em:
    1. Somar os produtos das diagonais principais e suas paralelas[cite: 69].
    2. Subtrair os produtos das diagonais secundárias e suas paralelas[cite: 70].
    """
    if matriz_A.shape != (3, 3):
        raise ValueError("A matriz deve ser de ordem 3x3.")
        
    # No NumPy, a função linalg.det implementa métodos eficientes
    # (como decomposição LU ou Laplace) para calcular o determinante,
    # que é válido para matrizes de qualquer ordem[cite: 62].
    det_numpy = np.linalg.det(matriz_A)
    
    print("\n--- Exemplo de Matriz 3x3 (Regra de Sarrus/Laplace) ---")
    print("Matriz A:\n", matriz_A)
    print(f"Cálculo por NumPy (np.linalg.det): {det_numpy:.4f}")
    
    # Exemplo: Determinante Nulo (Propriedade: Duas linhas ou colunas iguais) 
    A_nula = np.array([
        [1, 2, 3],
        [4, 5, 6],
        [1, 2, 3] # Linha 1 e Linha 3 são iguais
    ])
    det_nula = np.linalg.det(A_nula)
    print("\n--- Exemplo de Propriedade: Determinante Nulo ---")
    print("Matriz com Linha 1 = Linha 3 (Determinante deve ser zero):\n", A_nula)
    print(f"Determinante: {det_nula:.10f} (muito próximo de zero)") # Note a precisão de ponto flutuante
    print("-" * 30)

    return det_numpy

# --- Execução dos Exemplos ---

# 1. Matriz 2x2
A_2x2 = np.array([
    [4, 1],
    [3, 5]
])
calcular_determinante_2x2(A_2x2) # det = (4*5) - (1*3) = 20 - 3 = 17

# 2. Matriz 3x3
# Exemplo adaptado do slide (Matriz A = [[2, 1, 0], [1, 1, 1], [3, 5, 0]])
A_3x3 = np.array([
    [2, 1, 0],
    [1, 1, 1],
    [3, 5, 0]
])
calcular_determinante_3x3(A_3x3)
# O determinante desta matriz é -7 (Calculado usando Laplace na última coluna que tem zeros [cite: 115])
# det = 0*A13 - 1*A23 + 0*A33
# -1 * det([[2, 1], [3, 5]]) = -1 * (10 - 3) = -7


# 3. Exemplo de matriz triangular (Propriedade: Produto da diagonal principal) 
A_triangular = np.array([
    [2, 3, 4],
    [0, 5, 6],
    [0, 0, 7]
])
det_triangular = np.linalg.det(A_triangular)
print("\n--- Exemplo de Propriedade: Matriz Triangular ---")
print("Matriz Triangular Superior:\n", A_triangular)
print(f"Produto da Diagonal Principal (2*5*7): 70")
print(f"Cálculo por NumPy (np.linalg.det): {det_triangular:.4f}")
print("-" * 30)