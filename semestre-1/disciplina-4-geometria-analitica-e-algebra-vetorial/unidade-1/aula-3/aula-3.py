# aula-3.py
# Exemplo de Resolução de Sistemas de Equações Lineares (SEL)
# utilizando o Método de Eliminação de Gauss.

import numpy as np

def eliminacao_de_gauss(A_aumentada):
    """
    Implementa o método de Eliminação de Gauss para resolver um SEL.

    Args:
        A_aumentada (numpy.array): Matriz aumentada do sistema [A | B].

    Returns:
        numpy.array: Vetor solução X, ou None se o sistema for impossível.
    """
    n = A_aumentada.shape[0] # Número de equações (linhas)
    
    # 1. Fase de Eliminação (Transformação para forma triangular superior)
    print("--- 1. Fase de Eliminação (Escalonamento) ---")
    
    for i in range(n):
        # 1.1. Encontrar o pivô (elemento A[i, i])
        # A escolha de pivô (pivoteamento) simples é feita aqui (i, i)
        
        # Opcional: Busca por pivô para evitar divisão por zero ou aumentar estabilidade
        # Por simplicidade, vamos assumir que o pivô não é zero.
        if A_aumentada[i, i] == 0:
            print(f"⚠️ Atenção: Pivô zero na linha {i+1}. O sistema pode ser singular ou instável.")
            # Em uma implementação completa, faríamos um pivoteamento parcial (troca de linhas).
            return None 

        for j in range(i + 1, n):
            # Fator de eliminação (Multiplicador)
            m = A_aumentada[j, i] / A_aumentada[i, i]
            
            # Aplicar a operação elementar: Linha j = Linha j - m * Linha i
            # Para zerar o elemento A[j, i]
            A_aumentada[j, i:] = A_aumentada[j, i:] - m * A_aumentada[i, i:]
            
        print(f"\nApós zerar a coluna {i+1} abaixo do pivô:")
        print(A_aumentada.round(4))

    # 2. Fase de Retrossubstituição (Cálculo das variáveis)
    print("\n--- 2. Fase de Retrossubstituição ---")
    
    X = np.zeros(n) # Vetor solução [B, E, P]
    
    # Começa da última linha (n-1) e vai até a primeira (0)
    for i in range(n - 1, -1, -1):
        # A[i, n] é o termo b_i (lado direito da equação)
        # A[i, i:n] são os coeficientes a_i, i a a_i, n-1
        
        # S(j=i+1 até n-1) de (A[i, j] * X[j])
        soma_termos_ja_calculados = np.dot(A_aumentada[i, i+1:n], X[i+1:n])
        
        # X[i] = (b_i - soma_termos_ja_calculados) / a_i, i
        X[i] = (A_aumentada[i, n] - soma_termos_ja_calculados) / A_aumentada[i, i]
        
        print(f"Incógnita {i+1} calculada: X[{i+1}] = {X[i]:.4f}")
        
    return X

# --- Exemplo da Confeitaria (Aula 3) ---
# Incógnitas: x1 (B=Brigadeiro), x2 (E=Beijinho), x3 (P=Pé de Moleque)

# Sistema de Equações:
# 1. B + E + P = 250 (Total de doces)
# 2. 1.5B + 2E + 3.5P = 570 - 10 (Custo total - Taxa de entrega) -> 1.5B + 2E + 3.5P = 560
# 3. P = 2/3 * B  -> 3P = 2B -> -2B + 0E + 3P = 0

# Matriz Aumentada [A | B]:
# Colunas: [B, E, P, | Termo_Independente]
A_aumentada = np.array([
    [1,   1,   1,   250],
    [1.5, 2,   3.5, 560],
    [-2,  0,   3,   0  ]
], dtype=float)

print("Sistema Original - Matriz Aumentada:")
print(A_aumentada)
print("\n" + "="*50)

solucao = eliminacao_de_gauss(A_aumentada.copy()) # Usamos .copy() para não modificar a original

print("\n" + "="*50)

if solucao is not None:
    # A solução deve ser: B=120, E=50, P=80
    
    # Nomes das variáveis para melhor visualização
    variaveis = ["Brigadeiros (B)", "Beijinhos (E)", "Pé de Moleque (P)"]
    
    print("✨ Solução Encontrada (Quantidade de Doces):")
    for i, nome in enumerate(variaveis):
        print(f"- {nome}: {solucao[i]:.0f} unidades")
        
    print(f"\n✅ A quantidade de Beijinhos (E) é: {solucao[1]:.0f}")
else:
    print("❌ O sistema não pôde ser resolvido pelo método (pivô zero ou singular).")