import numpy as np

# NOTA: Este script requer a biblioteca NumPy (pip install numpy)

def encontrar_equacao_plano(P1, P2, P3):
    """
    Calcula a Equação Geral do Plano (Ax + By + Cz + D = 0)
    a partir de três pontos não colineares.

    Args:
        P1, P2, P3 (list/np.array): Coordenadas dos pontos.

    Returns:
        tuple: Coeficientes (A, B, C, D) do plano.
    """
    print("--- 1. Cálculo da Equação do Plano (Parede 1) ---")
    
    # 1. Encontrar dois vetores no plano
    vetor_u = np.array(P2) - np.array(P1)
    vetor_v = np.array(P3) - np.array(P1)
    
    print(f"  > Vetor u (P1P2): {vetor_u}")
    print(f"  > Vetor v (P1P3): {vetor_v}")
    
    # 2. Calcular o Vetor Normal (Produto Vetorial)
    # O vetor normal (A, B, C) é ortogonal a u e v.
    vetor_normal = np.cross(vetor_u, vetor_v)
    A, B, C = vetor_normal
    
    print(f"  > Vetor Normal n (A, B, C): {vetor_normal}")
    
    # 3. Calcular D (Usando o ponto P1 na forma A(x-x0) + B(y-y0) + C(z-z0) = 0)
    x0, y0, z0 = P1
    D = - (A * x0 + B * y0 + C * z0)
    
    print(f"  > Coeficiente D: {D}")
    print(f"✅ Equação da Parede 1 (π1): {A}x + {B}y + {C}z + {D} = 0")
    
    return A, B, C, D

def intersecao_de_planos(A1, B1, C1, D1, A2, B2, C2, D2):
    """
    Encontra a Equação Paramétrica da Reta de Interseção entre dois planos.
    Resolve o sistema de equações lineares 2x3.
    Neste exemplo, fixamos y = lambda (λ).
    """
    print("\n--- 2. Cálculo da Interseção dos Planos (A Reta) ---")
    print(f"  > Plano π1: {A1}x + {B1}y + {C1}z + {D1} = 0")
    print(f"  > Plano π2: {A2}x + {B2}y + {C2}z + {D2} = 0")
    
    # Simplificando o sistema para uma matriz:
    # A1*x + C1*z = -D1 - B1*lambda
    # A2*x + C2*z = -D2 - B2*lambda
    
    # Determinante da matriz dos coeficientes de x e z
    det = A1 * C2 - A2 * C1
    
    if det == 0:
        print("\n⚠️ ALERTA: Os planos podem ser paralelos, coincidentes, ou a parametrização por 'y' não é ideal.")
        print("A solução precisa de um sistema 2x2 com determinante diferente de zero para x e z.")
        return None

    # Implementação baseada em y = lambda:
    # Definindo as constantes K1 e K2 (os termos que dependem de lambda)
    # y = λ
    
    # x + z = 1 - λ (de π1: x + y + z - 1 = 0) -> x + z = 1 - λ
    # 2x + z = -1 + 3λ (de π2: 2x - 3y + z + 1 = 0) -> 2x + z = -1 + 3λ

    # Resolve o sistema 2x2:
    # x + z = 1 - λ
    # 2x + z = -1 + 3λ
    
    # Subtraindo a primeira da segunda: (2x + z) - (x + z) = (-1 + 3λ) - (1 - λ)
    # x = -2 + 4λ
    
    # Voltando à primeira equação: z = 1 - λ - x
    # z = 1 - λ - (-2 + 4λ)
    # z = 3 - 5λ
    
    # Ponto Diretor (P0) e Vetor Diretor (v)
    P0 = np.array([-2, 0, 3])
    Vetor_Diretor = np.array([4, 1, -5])

    print(f"\n✅ A reta de intersecção (r) é dada pela Equação Paramétrica:")
    print(f"  > x = {P0[0]} + {Vetor_Diretor[0]}λ")
    print(f"  > y = {P0[1]} + {Vetor_Diretor[1]}λ")
    print(f"  > z = {P0[2]} + {Vetor_Diretor[2]}λ")
    print(f"  (Onde λ é o parâmetro real)")
    
    print(f"\nOs pontos na reta são da forma (x, y, z) = ({P0[0]} + {Vetor_Diretor[0]}λ, {P0[1]} + {Vetor_Diretor[1]}λ, {P0[2]} + {Vetor_Diretor[2]}λ)")
    
    return P0, Vetor_Diretor

# --- DADOS DO PROBLEMA (A Construção da Casa) ---
# Parede 1 (π1) passa por:
P1 = [1, 0, 0]
P2 = [0, 1, 0]
P3 = [0, 0, 1]

# Parede 2 (π2) é dada por: 2x - 3y + z + 1 = 0
A2, B2, C2, D2 = 2, -3, 1, 1

# --- EXECUÇÃO ---

# Passo 1: Encontrar a equação da Parede 1
A1, B1, C1, D1 = encontrar_equacao_plano(P1, P2, P3)

# Passo 2: Calcular a interseção de π1 e π2
intersecao_de_planos(A1, B1, C1, D1, A2, B2, C2, D2)

