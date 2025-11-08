# aula-2.py
# Tema: Módulo e Versor de Vetores (2D e 3D)

import math

# ==============================================================================
# FUNÇÃO 1: CÁLCULO DAS COORDENADAS DO VETOR
# Dada a origem (A) e a extremidade (B), calcula o vetor V = B - A
# ==============================================================================
def calcular_vetor(A: tuple, B: tuple) -> tuple:
    """Calcula as coordenadas do vetor V = AB (B - A).
    Funciona para 2D (x, y) ou 3D (x, y, z)."""
    if len(A) != len(B):
        raise ValueError("Os pontos A e B devem ter o mesmo número de dimensões.")
    
    # Faz a subtração B - A componente por componente
    vetor = tuple(B[i] - A[i] for i in range(len(A)))
    return vetor

# ==============================================================================
# FUNÇÃO 2: CÁLCULO DO MÓDULO (NORMA) DO VETOR
# Aplica o Teorema de Pitágoras (extensão para 3D)
# ==============================================================================
def calcular_modulo(vetor: tuple) -> float:
    """Calcula o módulo (norma) de um vetor (2D ou 3D).
    Formula: ||v|| = sqrt(v_x^2 + v_y^2 + v_z^2 + ...)"""
    
    # Soma dos quadrados dos componentes: v_x^2 + v_y^2 + ...
    soma_quadrados = sum(comp ** 2 for comp in vetor)
    
    # Tira a raiz quadrada (Módulo)
    modulo = math.sqrt(soma_quadrados)
    return modulo

# ==============================================================================
# FUNÇÃO 3: CÁLCULO DO VERSOR (VETOR UNITÁRIO)
# Divide o vetor pelo seu módulo: Versor = V / ||V||
# ==============================================================================
def calcular_versor(vetor: tuple, modulo: float) -> tuple:
    """Calcula o versor (vetor unitário) do vetor.
    Versor tem a mesma direção e sentido, mas módulo 1."""
    
    if modulo == 0:
        return vetor  # Retorna o vetor nulo se o módulo for zero
        
    # Divide cada componente pelo módulo
    versor = tuple(comp / modulo for comp in vetor)
    return versor

# ==============================================================================
# EXEMPLOS PRÁTICOS
# ==============================================================================

print("--- Exemplo 1: Distância entre Cidades (2D) ---")
# Problema inicial da aula: A(63, 152) e B(73, 182)
A = (63, 152)
B = (73, 182)

vetor_AB = calcular_vetor(A, B)
modulo_AB = calcular_modulo(vetor_AB)

print(f"Ponto A (Origem): {A}")
print(f"Ponto B (Extremidade): {B}")
print(f"Vetor AB (Deslocamento): {vetor_AB}")
print(f"Módulo do Vetor (Distância): {modulo_AB:.2f} km")
print("-" * 40)


print("--- Exemplo 2: Vetor 3D e seu Versor ---")
# Vetor v = (3, 4, 12) no espaço
v = (3, 4, 12)

modulo_v = calcular_modulo(v)
versor_v = calcular_versor(v, modulo_v)

print(f"Vetor V: {v}")
print(f"Módulo de V: {modulo_v:.2f}")

# Demonstração: O versor tem módulo 1?
modulo_versor = calcular_modulo(versor_v)

print(f"Versor (Vetor Unitário): {versor_v}")
print(f"Verificação (Módulo do Versor): {modulo_versor:.2f}")

print("\nConceito: O Versor apenas indica a DIREÇÃO e SENTIDO do vetor V.")