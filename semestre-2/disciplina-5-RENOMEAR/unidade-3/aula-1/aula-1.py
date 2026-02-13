import numpy as np

# TEMA: Combinação Linear e Resolução de Sistemas Lineares (LI/LD)
# PROBLEMA: Encontrar os coeficientes (quantidades de hastes) que formam o vetor resultante.

# 1. Definindo os Vetores (Hastes da Treliça)
# Os vetores (v1, v2, v3) são as colunas da matriz de coeficientes A.

# Matriz A (Matriz dos Coeficientes do Sistema Linear):
# Coluna 1: Vetor v1 = (1, 2, 1)
# Coluna 2: Vetor v2 = (-1, 1, 0)
# Coluna 3: Vetor v3 = (1, 0, 1)
A = np.array([
    [1, -1, 1],  # Linha 1: 1*a1 - 1*a2 + 1*a3
    [2, 1, 0],   # Linha 2: 2*a1 + 1*a2 + 0*a3
    [1, 0, 1]    # Linha 3: 1*a1 + 0*a2 + 1*a3
])

# 2. Definindo o Vetor Resultante (Vetor B)
# O vetor resultante (0, 9, 2) é o termo independente do sistema.
B = np.array([0, 9, 2])

print("--- Problema de Combinação Linear da Treliça (Aula 1) ---")
print("\nMatriz dos Coeficientes (A):")
print(A)
print("\nVetor Resultante (B):")
print(B)

# 3. Teste de Independência Linear (Opcional, mas crucial)
# Se det(A) for diferente de zero, os vetores são LI e o sistema tem solução única.
try:
    determinante = np.linalg.det(A)
    print(f"\nDeterminante da Matriz A: {determinante:.2f}")

    if np.isclose(determinante, 0):
        print("Conclusão: O determinante é aproximadamente zero. Os vetores são LD (Linearmente Dependentes).")
    else:
        print("Conclusão: O determinante é diferente de zero. Os vetores são LI (Linearmente Independentes).")
        print("Isso garante que o sistema de combinação linear tem uma única solução.")

    # 4. Resolvendo o Sistema Linear A * X = B
    # O vetor 'X' conterá os escalares (a1, a2, a3) que são as quantidades de hastes.
    # Usamos np.linalg.solve para resolver sistemas de equações lineares.
    X = np.linalg.solve(A, B)

    # 5. Apresentação dos Resultados
    print("\n--- Solução Encontrada (Escalares) ---")
    # Arredondamos para evitar pequenas imprecisões de ponto flutuante
    a1, a2, a3 = np.round(X, decimals=2) 
    
    print(f"Quantidade de Haste 1 (α1): {a1}")
    print(f"Quantidade de Haste 2 (α2): {a2}")
    print(f"Quantidade de Haste 3 (α3): {a3}")

    print("\nVerificação (A * X deve ser igual a B):")
    B_verificacao = A @ X # Multiplicação de matrizes no NumPy
    print(f"Resultado da Combinação Linear (A * X): {B_verificacao.round(decimals=2)}")
    print(f"Vetor B Original: {B}")

    # A solução corresponde ao encontrado na explicação didática: α1=4, α2=1, α3=-2.

except np.linalg.LinAlgError as e:
    print(f"\nErro de Álgebra Linear: O sistema pode ser singular ou não quadrado. {e}")