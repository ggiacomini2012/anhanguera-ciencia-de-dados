import numpy as np

def projecao_vetorial(u, v):
    """
    Calcula o vetor projeção de u sobre v.

    Fórmula: proj_v(u) = ((u . v) / ||v||^2) * v

    Args:
        u (np.array): O vetor que será projetado (a 'haste').
        v (np.array): O vetor direção sobre o qual u será projetado (a 'estrada').

    Returns:
        np.array: O vetor projeção.
        float: O comprimento (módulo) do vetor projeção.
    """
    # 1. Calcular o Produto Escalar (u . v)
    # np.dot(u, v)
    produto_escalar = np.dot(u, v)

    # 2. Calcular o Quadrado do Módulo de v (||v||^2)
    # np.dot(v, v) calcula a soma dos quadrados das componentes, que é ||v||^2
    modulo_v_quadrado = np.dot(v, v)

    # Verifica se o vetor v é o vetor nulo para evitar divisão por zero
    if modulo_v_quadrado == 0:
        print("⚠️ Erro: O vetor direção (v) não pode ser o vetor nulo.")
        return np.zeros_like(u), 0.0

    # 3. Calcular o Coeficiente Escalar (k)
    # k = (u . v) / ||v||^2
    coeficiente_escalar = produto_escalar / modulo_v_quadrado

    # 4. Calcular o Vetor Projeção
    # projecao = k * v
    vetor_projecao = coeficiente_escalar * v

    # 5. Calcular o Comprimento (Módulo) da Projeção
    comprimento_projecao = np.linalg.norm(vetor_projecao)

    return vetor_projecao, comprimento_projecao

# --- Exemplo da Aula: Haste de Sustentação no R² ---
print("--- Exemplo 1: Haste de Sustentação (R²) ---")

# Vetor u (Haste inclinada) e Vetor v (Barra base)
u_r2 = np.array([-2, 4])
v_r2 = np.array([5, 0])

projecao_r2, comprimento_r2 = projecao_vetorial(u_r2, v_r2)

print(f"Vetor U (haste): {u_r2}")
print(f"Vetor V (base):  {v_r2}")
print(f"Resultado da Projeção de U sobre V: {projecao_r2}")
print(f"Comprimento da Haste (Módulo da Projeção): {comprimento_r2:.2f}\n")
# O resultado esperado é vetor (-2, 0) e comprimento 2.00

# --- Exemplo Adicional no R³ ---
print("--- Exemplo 2: Projeção em 3D (R³) ---")

# Determine a projeção do vetor u = (1, 2, 3) na direção de v = (2, 1, 0).
u_r3 = np.array([1, 2, 3])
v_r3 = np.array([2, 1, 0])

projecao_r3, comprimento_r3 = projecao_vetorial(u_r3, v_r3)

print(f"Vetor U: {u_r3}")
print(f"Vetor V: {v_r3}")
print(f"Resultado da Projeção de U sobre V: {projecao_r3}")
print(f"Comprimento da Projeção: {comprimento_r3:.2f}")

# Cálculo manual da projeção R3:
# u.v = (1*2) + (2*1) + (3*0) = 4
# ||v||^2 = 2^2 + 1^2 + 0^2 = 5
# proj = (4/5) * (2, 1, 0) = (8/5, 4/5, 0) = (1.6, 0.8, 0.0)