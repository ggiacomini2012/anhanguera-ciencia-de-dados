# =================================================================
# Aula 1: Equação da Reta e Coeficiente Angular (2D e 3D)
# Tópico Principal: Aplicação dos conceitos da Equação da Reta.
# =================================================================

import numpy as np

# -----------------------------------------------------------------
# 1. FUNÇÕES PARA RETA NO PLANO (2D) - Foco no Coeficiente Angular (m)
# -----------------------------------------------------------------

def calcular_coeficiente_angular(ponto1: tuple, ponto2: tuple) -> float:
    """
    Calcula o coeficiente angular (m) de uma reta que passa por dois pontos (x, y).
    Fórmula: m = (y2 - y1) / (x2 - x1)
    """
    x1, y1 = ponto1
    x2, y2 = ponto2

    # Verifica se a reta é vertical (denominador zero)
    if x2 - x1 == 0:
        print("⚠️ Coeficiente angular indefinido (Reta Vertical).")
        return np.inf  # Retorna infinito para representar reta vertical
    
    m = (y2 - y1) / (x2 - x1)
    return m

def obter_equacao_geral_2d(ponto1: tuple, ponto2: tuple) -> str:
    """
    Encontra a Equação Geral da Reta (Ax + By + C = 0)
    que passa por dois pontos.
    """
    m = calcular_coeficiente_angular(ponto1, ponto2)
    x1, y1 = ponto1
    
    if m == np.inf:
        # Se for vertical, a equação é x - x1 = 0
        A, B, C = 1, 0, -x1
    else:
        # Usa a forma ponto-inclinação: y - y1 = m * (x - x1)
        # Rearranjando para Ax + By + C = 0:
        # m*x - y + (y1 - m*x1) = 0
        A = m
        B = -1
        C = y1 - m * x1
    
    # Normaliza (opcional, mas bom para A ser positivo e inteiro se possível)
    # Aqui, simplificamos apenas o formato de saída
    
    equacao = f"{A:.2f}x + {B:.2f}y + {C:.2f} = 0"
    return equacao

# -----------------------------------------------------------------
# 2. APLICAÇÃO VETORIAL (3D) - Ângulo de Inclinação (Placa Solar)
# -----------------------------------------------------------------

def calcular_angulo_entre_vetores(vetor1: list, vetor2: list) -> float:
    """
    Calcula o ângulo em graus entre dois vetores no espaço (Ex: Placa Solar).
    Fórmula: cos(theta) = |v1 . v2| / (|v1| * |v2|)
    """
    v1 = np.array(vetor1)
    v2 = np.array(vetor2)

    # Produto Escalar (Numerador)
    produto_escalar = np.dot(v1, v2)
    
    # Módulos (Denominador)
    modulo_v1 = np.linalg.norm(v1)
    modulo_v2 = np.linalg.norm(v2)

    # Aplica a fórmula do cosseno (com módulo no numerador para o menor ângulo)
    cos_theta = abs(produto_escalar) / (modulo_v1 * modulo_v2)
    
    # Garante que cos_theta esteja no intervalo [-1, 1] devido a erros de ponto flutuante
    cos_theta = np.clip(cos_theta, -1.0, 1.0)
    
    # Calcula o ângulo em radianos e converte para graus
    angulo_rad = np.arccos(cos_theta)
    angulo_graus = np.degrees(angulo_rad)
    
    return angulo_graus

# -----------------------------------------------------------------
# 3. EXEMPLOS DE USO
# -----------------------------------------------------------------

if __name__ == "__main__":
    
    print("--- CÁLCULOS DA RETA NO PLANO (2D) ---")
    P_A = (2, 3)
    P_B = (4, 7)
    print(f"Pontos dados: A{P_A} e B{P_B}")

    # Coeficiente Angular
    m_ab = calcular_coeficiente_angular(P_A, P_B)
    print(f"1. Coeficiente Angular (m): {m_ab}")

    # Equação Geral
    equacao = obter_equacao_geral_2d(P_A, P_B)
    print(f"2. Equação Geral da Reta: {equacao}")
    print("-" * 40)
    
    print("--- PROBLEMA DA PLACA SOLAR (3D) ---")
    # Baseado no exemplo do material: Pontos A(2, 3, 5) e B(5, 0, 14)
    # O vetor diretor da placa é V = B - A = (3, -3, 9)
    vetor_placa = [3, -3, 9]
    
    # O ângulo de inclinação é o ângulo entre o vetor diretor e a projeção horizontal (eixo X,Y)
    # A projeção horizontal do vetor (3, -3, 9) é (3, -3, 0).
    # O material usou o vetor (3, 0, 0) como referência horizontal no plano X,Z.
    # Vamos usar o vetor diretor da placa (3, -3, 9) e o vetor que representa o plano X,Y.
    
    # No exemplo resolvido, o vetor diretor é (3, -3, 9).
    # O vetor de projeção no plano X,Y é o vetor (3, -3, 0).
    # O material calculou o ângulo entre o vetor (3, -3, 9) e (3, 0, 0)
    # V1 = (3, -3, 9) | V2 = (3, 0, 0)
    
    vetor_diretor_placa = [3, -3, 9]
    vetor_referencia_horizontal = [3, 0, 0] # Referência para o cálculo do material
    
    print(f"Vetor Diretor da Placa (V1): {vetor_diretor_placa}")
    print(f"Vetor de Referência Horizontal (V2): {vetor_referencia_horizontal}")

    angulo_inclinacao = calcular_angulo_entre_vetores(vetor_diretor_placa, vetor_referencia_horizontal)

    print(f"3. Ângulo entre V1 e V2: {angulo_inclinacao:.2f}°")
    # O resultado está mais próximo de 73.89°, que é o arccos(3/sqrt(99))
    # O material usou arccos(9/sqrt(99) * sqrt(9)) que dá 76° para um caso 2D (m=3), mas o cálculo 3D é mais preciso.
    # Usando o cálculo vetorial correto:
    print("-" * 40)