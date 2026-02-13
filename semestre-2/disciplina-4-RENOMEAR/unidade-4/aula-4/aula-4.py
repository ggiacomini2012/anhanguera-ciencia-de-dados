import numpy as np

# --- 1. Distância entre um Ponto e um Plano ---
# Fórmula: d(Po, π) = |ax0 + by0 + cz0 + d| / sqrt(a² + b² + c²)

def distancia_ponto_plano(P0, plano_coeffs):
    """
    Calcula a distância entre um ponto P0 e um plano π.
    :param P0: Coordenadas do ponto (x0, y0, z0) - array numpy.
    :param plano_coeffs: Coeficientes do plano (a, b, c, d) - array numpy.
    :return: Distância (float).
    """
    # Coeficientes do plano: a, b, c, d
    a, b, c, d = plano_coeffs
    x0, y0, z0 = P0

    # Numerador: |a*x0 + b*y0 + c*z0 + d|
    numerador = np.abs(a * x0 + b * y0 + c * z0 + d)

    # Denominador: ||n_pi|| = sqrt(a² + b² + c²)
    # n_pi é o vetor normal (a, b, c)
    denominador = np.linalg.norm(plano_coeffs[:3])

    if denominador == 0:
        return float('inf')  # Plano degenerado
        
    distancia = numerador / denominador
    return distancia

# --- 2. Distância entre Duas Retas Reversas ---
# Fórmula: d(r, s) = |[RS, vr, vs]| / ||vr x vs||
# O Produto Misto ( [RS, vr, vs] ) é calculado como o determinante da matriz
# formada pelos três vetores, ou (RS . (vr x vs)).

def distancia_retas_reversas(R, S, vr, vs):
    """
    Calcula a distância entre duas retas reversas r e s.
    :param R: Ponto da reta r.
    :param S: Ponto da reta s.
    :param vr: Vetor diretor da reta r.
    :param vs: Vetor diretor da reta s.
    :return: Distância (float).
    """
    # 1. Vetor RS (vetor que liga um ponto de cada reta)
    RS = S - R

    # 2. Produto Vetorial (vr x vs)
    v_produto_vetorial = np.cross(vr, vs)

    # Se o produto vetorial for o vetor nulo, as retas são paralelas (ou coincidentes)
    if np.all(v_produto_vetorial == 0):
        # A fórmula de retas reversas não se aplica; deve-se usar a fórmula
        # para retas paralelas (Distância Ponto-Reta).
        return "Retas paralelas ou coincidentes. Use a fórmula Ponto-Reta."

    # 3. Produto Misto ( [RS, vr, vs] ) = RS . (vr x vs)
    # O valor absoluto é o volume do paralelepípedo.
    numerador = np.abs(np.dot(RS, v_produto_vetorial))

    # 4. Norma do Produto Vetorial (||vr x vs||)
    # Este valor é a área da base do paralelepípedo.
    denominador = np.linalg.norm(v_produto_vetorial)

    distancia = numerador / denominador
    return distancia

# ----------------------------------------------------
#               EXECUÇÃO DOS EXEMPLOS
# ----------------------------------------------------
print("--- CÁLCULO DE DISTÂNCIAS EM GEOMETRIA ANALÍTICA ---")

# Exemplo 1: Distância entre Ponto e Plano
# Ponto P0(1, 1, 2) e Plano π: 2x - y + 2z + 4 = 0
P0_ex1 = np.array([1.0, 1.0, 2.0])
plano_ex1 = np.array([2.0, -1.0, 2.0, 4.0]) # Coeficientes (a, b, c, d)

d_ponto_plano = distancia_ponto_plano(P0_ex1, plano_ex1)
print(f"\n1. Distância Ponto-Plano:")
print(f"   Ponto P0: {P0_ex1}")
print(f"   Plano π: {plano_ex1[0]}x + {plano_ex1[1]}y + {plano_ex1[2]}z + {plano_ex1[3]} = 0")
print(f"   Distância calculada: {d_ponto_plano:.4f} (Confere com o resultado 3.0)")


# Exemplo 2: Distância entre Retas Reversas
# Reta r: X = R + h*vr; R(1, 1, 1), vr(-1, 2, 1)
# Reta s: X = S + t*vs; S(1, 1, 3), vs(2, 1, 3)
R_ex2 = np.array([1.0, 1.0, 1.0])
S_ex2 = np.array([1.0, 1.0, 3.0])
vr_ex2 = np.array([-1.0, 2.0, 1.0])
vs_ex2 = np.array([2.0, 1.0, 3.0])

d_reversas = distancia_retas_reversas(R_ex2, S_ex2, vr_ex2, vs_ex2)

# O resultado do material é 2*sqrt(3)/3, que é aproximadamente 1.1547
# Vamos calcular o valor esperado exato para comparação:
# Numerador |[RS, vr, vs]| = |-10| = 10
# Denominador ||vr x vs|| = ||(5, 5, -5)|| = sqrt(5² + 5² + (-5)²) = sqrt(75)
# d = 10 / sqrt(75) = 10 / (5*sqrt(3)) = 2 / sqrt(3) = 2*sqrt(3)/3 ≈ 1.1547

print(f"\n2. Distância Retas Reversas:")
print(f"   Reta r (Ponto R, Vetor vr): {R_ex2}, {vr_ex2}")
print(f"   Reta s (Ponto S, Vetor vs): {S_ex2}, {vs_ex2}")
print(f"   Distância calculada: {d_reversas:.4f} (Confere com 2*sqrt(3)/3 ≈ 1.1547)")