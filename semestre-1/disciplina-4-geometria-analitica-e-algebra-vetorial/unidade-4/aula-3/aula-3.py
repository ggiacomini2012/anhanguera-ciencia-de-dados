import math

# --- 🎯 Tópico Principal: Geometria Analítica: Distância e Pontos Notáveis ---

def distancia_plano(p1: tuple, p2: tuple) -> float:
    """
    Calcula a distância euclidiana entre dois pontos (x, y) no plano (R²).
    Fórmula: d = sqrt((x2 - x1)² + (y2 - y1)²)
    """
    x1, y1 = p1
    x2, y2 = p2
    
    delta_x_quadrado = (x2 - x1) ** 2
    delta_y_quadrado = (y2 - y1) ** 2
    
    distancia = math.sqrt(delta_x_quadrado + delta_y_quadrado)
    return distancia

def distancia_espaco(p1: tuple, p2: tuple) -> float:
    """
    Calcula a distância euclidiana entre dois pontos (x, y, z) no espaço (R³).
    Fórmula: d = sqrt((x2 - x1)² + (y2 - y1)² + (z2 - z1)²)
    """
    x1, y1, z1 = p1
    x2, y2, z2 = p2
    
    delta_x_quadrado = (x2 - x1) ** 2
    delta_y_quadrado = (y2 - y1) ** 2
    delta_z_quadrado = (z2 - z1) ** 2
    
    distancia = math.sqrt(delta_x_quadrado + delta_y_quadrado + delta_z_quadrado)
    return distancia

def calcular_baricentro(a: tuple, b: tuple, c: tuple) -> tuple:
    """
    Calcula as coordenadas do Baricentro (centro de massa) de um triângulo.
    Fórmula: Gx = (xA + xB + xC) / 3 | Gy = (yA + yB + yC) / 3
    """
    # Coordenadas dos vértices
    xA, yA = a
    xB, yB = b
    xC, yC = c
    
    # Média aritmética das coordenadas X e Y
    g_x = (xA + xB + xC) / 3
    g_y = (yA + yB + yC) / 3
    
    return (g_x, g_y)

def distancia_ponto_a_reta(p: tuple, coeficientes_reta: tuple) -> float:
    """
    Calcula a distância de um ponto P(x0, y0) à reta geral Ax + By + C = 0.
    Fórmula: d = |A*x0 + B*y0 + C| / sqrt(A² + B²)
    """
    x0, y0 = p
    A, B, C = coeficientes_reta  # (A, B, C) da equação da reta
    
    # Numerador (valor absoluto)
    numerador = abs(A * x0 + B * y0 + C)
    
    # Denominador (raiz quadrada)
    denominador = math.sqrt(A**2 + B**2)
    
    # Evita divisão por zero (caso a reta não seja válida, A=B=0)
    if denominador == 0:
        return float('inf')  # Retorna infinito para indicar erro ou reta inválida
    
    distancia = numerador / denominador
    return distancia

# --- 🧪 Testes e Exemplos (Baseados na Explicação) ---

if __name__ == "__main__":
    print("--- 📐 Aula 3: Distância e Pontos Notáveis em Geometria Analítica ---")
    print("-" * 50)

    # 1. Distância entre Dois Pontos (R²)
    P_A_r2 = (1, 1)
    P_B_r2 = (4, 5)
    d_r2 = distancia_plano(P_A_r2, P_B_r2)
    print(f"1. Distância no Plano (R²):")
    print(f"   Pontos A={P_A_r2}, B={P_B_r2}")
    print(f"   Resultado: {d_r2:.2f} (Esperado: 5.00)")
    
    print("-" * 50)

    # 2. Distância entre Dois Pontos (R³)
    P_A_r3 = (1, 2, 3)
    P_B_r3 = (2, 4, 5)
    d_r3 = distancia_espaco(P_A_r3, P_B_r3)
    print(f"2. Distância no Espaço (R³):")
    print(f"   Pontos A={P_A_r3}, B={P_B_r3}")
    print(f"   Resultado: {d_r3:.2f} (Esperado: 3.00)")

    print("-" * 50)

    # 3. Baricentro de um Triângulo
    V_A = (1, 1)
    V_B = (2, 4)
    V_C = (3, 7)
    G = calcular_baricentro(V_A, V_B, V_C)
    print(f"3. Baricentro (Centro de Massa):")
    print(f"   Vértices: A={V_A}, B={V_B}, C={V_C}")
    print(f"   Baricentro G: ({G[0]:.2f}, {G[1]:.2f}) (Esperado: 2.00, 4.00)")

    print("-" * 50)

    # 4. Distância de Ponto à Reta (4x + 3y + 6 = 0)
    P_Reta = (-1, 3)
    Reta_Coef = (4, 3, 6)  # A=4, B=3, C=6
    d_reta = distancia_ponto_a_reta(P_Reta, Reta_Coef)
    print(f"4. Distância de Ponto P={P_Reta} à Reta {Reta_Coef[0]}x + {Reta_Coef[1]}y + {Reta_Coef[2]} = 0:")
    print(f"   Resultado: {d_reta:.2f} (Esperado: 2.20)")
    print("-" * 50)