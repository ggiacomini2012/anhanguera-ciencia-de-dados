import numpy as np

# Tópico Principal: Matrizes, Matriz Inversa e Resolução de Sistemas Lineares (A * X = B)
# Exemplo prático: O problema dos componentes eletrônicos (A, B, C)

# 1. Definição da Matriz dos Coeficientes (A)
# Coeficientes das variáveis A, B, C nas 3 equações.
# 2A + 1B + 1C = 150
# 4A + 3B + 0C = 240
# 0A + 5B + 3C = 350
A = np.array([
    [2, 1, 1],  # Linha 1: Coeficientes da 1ª equação
    [4, 3, 0],  # Linha 2: Coeficientes da 2ª equação
    [0, 5, 3]   # Linha 3: Coeficientes da 3ª equação
])

# 2. Definição do Vetor de Termos Independentes (B)
# Resultados das vendas
B = np.array([150, 240, 350])

print(f"--- Aula 5: Álgebra Linear em Python ---\n")
print("1. Matriz dos Coeficientes (A):")
print(A)
print("\n2. Vetor de Termos Independentes (B):")
print(B)
print("\n" + "="*40 + "\n")

# --- Verificação da Invertibilidade (Determinante) ---
det_A = np.linalg.det(A)
print(f"3. Determinante de A (det(A)): {det_A:.2f}")

if det_A == 0:
    print("⚠️ O Determinante é zero. A matriz não é invertível e o sistema não pode ser resolvido por Matriz Inversa.")
    # Neste caso, teríamos que usar Eliminação de Gauss ou outras técnicas.
else:
    # --- Resolução pelo Método da Matriz Inversa (X = A⁻¹ * B) ---
    try:
        # 4. Cálculo da Matriz Inversa (A⁻¹)
        A_inversa = np.linalg.inv(A)
        print("\n4. Matriz Inversa (A⁻¹):")
        print(A_inversa.round(4)) # Arredondando para melhor visualização

        # 5. Cálculo da Solução (X = A⁻¹ * B)
        # O np.linalg.solve é o modo mais robusto, mas vamos demonstrar a multiplicação A_inversa * B
        X = np.dot(A_inversa, B)

        print("\n5. Solução (X = A⁻¹ * B) - Preços dos componentes:")
        print("---------------------------------------")
        print(f"  Componente A (X[0]): R$ {X[0]:.2f}")
        print(f"  Componente B (X[1]): R$ {X[1]:.2f}")
        print(f"  Componente C (X[2]): R$ {X[2]:.2f}")
        print("---------------------------------------")
        print("\n✅ Solução: X = [30.00, 40.00, 50.00] (O mesmo resultado do escalonamento!)")

    except np.linalg.LinAlgError:
        print("\n❌ Erro: Não foi possível calcular a Matriz Inversa (Singularidade).")

# --- Solução alternativa (NumPy resolve diretamente) ---
# X_solve = np.linalg.solve(A, B)
# print(f"\nVerificação (np.linalg.solve): {X_solve.round(2)}")