# ==============================================================================
# Aula 5: Vetores no Plano e no Espaço - Resolução do Problema do Semáforo
# Tópico Principal: Equilíbrio de Forças e Decomposição Vetorial (Estática)
#
# Este script Python calcula as tensões (T1 e T2) nos cabos de um semáforo
# em equilíbrio, aplicando as leis de decomposição e soma de vetores.
#
# Conceitos-chave:
# 1. Decomposição de Forças (Tensão) em componentes X e Y.
# 2. Condição de Equilíbrio: Soma das Forças Resultantes em X e Y deve ser zero (∑Fx=0, ∑Fy=0).
# 3. Uso das funções trigonométricas (seno, cosseno, tangente).
# ==============================================================================

import math

# 1. Dados do Problema (Grandezas Escalares)
# Os ângulos devem ser convertidos para radianos, pois a biblioteca 'math' usa radianos.
PESO_SEMAFORO_Fg = 122.0  # N
LIMITE_TENSAO_MAX = 100.0 # N

# Ângulos fornecidos em graus em relação à horizontal
angulo_t1_graus = 37.0
angulo_t2_graus = 53.0

# Conversão para Radianos
angulo_t1_rad = math.radians(angulo_t1_graus)
angulo_t2_rad = math.radians(angulo_t2_graus)

print("📐 Aplicação Prática: Equilíbrio do Semáforo 🚦")
print(f"Peso do Semáforo (Fg): {PESO_SEMAFORO_Fg} N")
print(f"Limiar Máximo de Tensão (T_max): {LIMITE_TENSAO_MAX} N\n")


# 2. Resolução do Sistema de Equilíbrio
# O problema é resolvido a partir da condição de Equilíbrio:
# ΣFx = 0  => -T1*cos(θ1) + T2*cos(θ2) = 0
# ΣFy = 0  => T1*sen(θ1) + T2*sen(θ2) - Fg = 0

# --- Passo A: Determinar T1 (Usando a Equação de T1 derivada no material) ---
# T1 = Fg / ( sen(θ1) + cos(θ1) * tan(θ2) )

# 1. Calcular o denominador da fórmula de T1
sen_t1 = math.sin(angulo_t1_rad)
cos_t1 = math.cos(angulo_t1_rad)
tan_t2 = math.tan(angulo_t2_rad)

denominador_t1 = sen_t1 + (cos_t1 * tan_t2)

# 2. Calcular T1
T1 = PESO_SEMAFORO_Fg / denominador_t1

# --- Passo B: Determinar T2 (Usando a Equação de Equilíbrio em X) ---
# T2 = T1 * ( cos(θ1) / cos(θ2) )

cos_t2 = math.cos(angulo_t2_rad)

T2 = T1 * (cos_t1 / cos_t2)


# 3. Exibição dos Resultados e Conclusão
print("--- TENSÕES CALCULADAS ---")
print(f"T1 (Cabo 1 a {angulo_t1_graus}°): {T1:.2f} N")
print(f"T2 (Cabo 2 a {angulo_t2_graus}°): {T2:.2f} N")
print(f"T3 (Cabo Vertical): {PESO_SEMAFORO_Fg:.2f} N\n")

# 4. Verificação da Segurança
print("--- VERIFICAÇÃO DE SEGURANÇA ---")

# Verifica se a tensão em T1 excede o limite
if T1 > LIMITE_TENSAO_MAX:
    print(f"❌ ALERTA! Tensão T1 ({T1:.2f} N) EXCEDEU o limite de {LIMITE_TENSAO_MAX} N.")
    quebra_t1 = True
else:
    print(f"✅ Cabo 1 OK. Tensão ({T1:.2f} N) está abaixo do limite.")
    quebra_t1 = False

# Verifica se a tensão em T2 excede o limite
if T2 > LIMITE_TENSAO_MAX:
    print(f"❌ ALERTA! Tensão T2 ({T2:.2f} N) EXCEDEU o limite de {LIMITE_TENSAO_MAX} N.")
    quebra_t2 = True
else:
    print(f"✅ Cabo 2 OK. Tensão ({T2:.2f} N) está abaixo do limite.")
    quebra_t2 = False

print("\n--- CONCLUSÃO FINAL ---")
if quebra_t1 or quebra_t2:
    print("🚨 UM OU MAIS CABOS VÃO QUEBRAR! O semáforo não permanecerá em equilíbrio.")
else:
    print("🎉 OS CABOS AGUENTAM! O semáforo permanecerá pendurado em equilíbrio, pois as tensões estão seguras.")
    
# Uma forma alternativa, mais direta, de calcular a resultante de dois vetores
# Usando a Regra da Soma Algébrica (Vetores A=(3,4) e B=(1, -2))
vetor_A_x, vetor_A_y = 3, 4
vetor_B_x, vetor_B_y = 1, -2

resultante_x = vetor_A_x + vetor_B_x
resultante_y = vetor_A_y + vetor_B_y

modulo_resultante = math.sqrt(resultante_x**2 + resultante_y**2)
direcao_rad = math.atan2(resultante_y, resultante_x) # atan2 lida com quadrantes

print("\n--- Exemplo de Soma Vetorial (Componentes) ---")
print(f"Vetor A: ({vetor_A_x}, {vetor_A_y})")
print(f"Vetor B: ({vetor_B_x}, {vetor_B_y})")
print(f"Vetor Resultante R = A + B: ({resultante_x}, {resultante_y})")
print(f"Módulo do Resultante: {modulo_resultante:.2f}")
print(f"Direção do Resultante: {math.degrees(direcao_rad):.2f}°")