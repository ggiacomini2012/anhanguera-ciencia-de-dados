import math

# --- 1. FUNÇÕES ESSENCIAIS ---

def calcular_produto_escalar(v1, v2):
    """
    Calcula o Produto Escalar (Dot Product) de dois vetores 3D.
    O produto escalar é a soma do produto das componentes correspondentes.
    """
    # Exemplo: v1=(x1, y1, z1) e v2=(x2, y2, z2) -> Resultado = x1*x2 + y1*y2 + z1*z2
    if len(v1) != len(v2):
        raise ValueError("Os vetores devem ter a mesma dimensão.")
    
    produto = sum(c1 * c2 for c1, c2 in zip(v1, v2))
    return produto

def calcular_modulo(v):
    """
    Calcula o Módulo (comprimento) de um vetor 3D.
    Usa o Teorema de Pitágoras generalizado (raiz quadrada da soma dos quadrados das componentes).
    """
    soma_quadrados = sum(c**2 for c in v)
    modulo = math.sqrt(soma_quadrados)
    return modulo

def calcular_angulo_entre_vetores(v1, v2):
    """
    Calcula o ângulo (em graus) entre dois vetores usando a fórmula:
    cos(theta) = (v1 . v2) / (||v1|| * ||v2||)
    """
    prod_escalar = calcular_produto_escalar(v1, v2)
    mod_v1 = calcular_modulo(v1)
    mod_v2 = calcular_modulo(v2)
    
    # Previne divisão por zero se um vetor for o vetor nulo
    if mod_v1 == 0 or mod_v2 == 0:
        return 0.0 # Define 0 graus como resultado se houver vetor nulo
    
    # O valor do cosseno deve estar entre -1 e 1
    cos_theta = prod_escalar / (mod_v1 * mod_v2)
    cos_theta_clamped = max(-1.0, min(1.0, cos_theta))
    
    # Encontra o ângulo em radianos e converte para graus
    angulo_radianos = math.acos(cos_theta_clamped)
    angulo_graus = math.degrees(angulo_radianos)
    
    return angulo_graus

# --- 2. SITUAÇÃO-PROBLEMA (ESTRUTURA METÁLICA) ---

# Vetores que representam as hastes metálicas:
VETOR_U = (2, 4, 4)
VETOR_V = (3, 2, -1)

print("--- Aula 2: Produto Escalar e Ângulo entre Vetores ---")
print(f"Vetores em análise (Hastes da estrutura):")
print(f"Vetor U: {VETOR_U}")
print(f"Vetor V: {VETOR_V}")
print("-" * 40)

# 1. CÁLCULO DO PRODUTO ESCALAR
produto = calcular_produto_escalar(VETOR_U, VETOR_V)
print(f"1. Produto Escalar (U . V): {produto}")

# 2. CÁLCULO DOS MÓDULOS
modulo_u = calcular_modulo(VETOR_U)
modulo_v = calcular_modulo(VETOR_V)
print(f"2. Módulo do Vetor U (||U||): {modulo_u}")
print(f"3. Módulo do Vetor V (||V||): {modulo_v:.4f} (aprox.)")
print("-" * 40)

# 3. CÁLCULO DO ÂNGULO
angulo = calcular_angulo_entre_vetores(VETOR_U, VETOR_V)
print(f"4. Ângulo entre U e V: {angulo:.2f} graus")
print("\n✅ PROBLEMA RESOLVIDO: O ângulo entre as hastes metálicas é de aproximadamente 63.48 graus.")