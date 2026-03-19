# ============================================================
# Aula 2 - Unidade 4: Significância Estatística
# Métodos de Fisher e Neyman-Pearson
# ============================================================

import numpy as np
from scipy import stats

np.random.seed(123)


# ============================================================
# PARTE 1: MÉTODO DE FISHER — Valor p
# ============================================================
# O método de Fisher usa o valor p para medir evidência
# contra a hipótese nula (H0).
# Regra: se valor p < alpha (0.05), rejeita H0.

print("=" * 60)
print("MÉTODO DE FISHER")
print("=" * 60)

# Contexto: comparar eficácia de medicamento vs. placebo
grupo_tratamento = np.random.normal(loc=5.5, scale=1, size=100)
grupo_controle   = np.random.normal(loc=5.0, scale=1, size=100)

# Teste t de Welch (equivalente ao R: t.test)
resultado = stats.ttest_ind(grupo_tratamento, grupo_controle)

print(f"Estatística t:  {resultado.statistic:.4f}")
print(f"Valor p:        {resultado.pvalue:.2e}")

alpha = 0.05
if resultado.pvalue < alpha:
    print(f"-> valor p ({resultado.pvalue:.2e}) < alpha ({alpha})")
    print("-> REJEITA H0: há diferença significativa entre os grupos.")
else:
    print(f"-> valor p ({resultado.pvalue:.2e}) >= alpha ({alpha})")
    print("-> NÃO rejeita H0: diferença não é significativa.")


# ============================================================
# PARTE 2: MÉTODO DE NEYMAN-PEARSON
# ============================================================
# Foco em controlar dois tipos de erro:
#   Erro Tipo I  (α): rejeitar H0 quando ela é verdadeira (falso positivo)
#   Erro Tipo II (β): não rejeitar H0 quando ela é falsa  (falso negativo)
# Poder do teste = 1 - β

print("\n" + "=" * 60)
print("MÉTODO DE NEYMAN-PEARSON")
print("=" * 60)

# Contexto: comparar dois tratamentos para doença crônica
tratamento_A = np.random.normal(loc=60, scale=10, size=100)
tratamento_B = np.random.normal(loc=65, scale=10, size=100)

resultado_np = stats.ttest_ind(tratamento_A, tratamento_B)
alpha = 0.05

print(f"Estatística t:  {resultado_np.statistic:.4f}")
print(f"Valor p:        {resultado_np.pvalue:.5f}")

# Decisão formal com base no valor crítico
graus_liberdade = len(tratamento_A) + len(tratamento_B) - 2
valor_critico = stats.t.ppf(1 - alpha / 2, df=graus_liberdade)

print(f"Valor crítico:  ±{valor_critico:.4f}  (α={alpha}, bicaudal)")
print(f"t observado:    {abs(resultado_np.statistic):.4f}")

if abs(resultado_np.statistic) > valor_critico:
    print("-> t > valor crítico: REJEITA H0.")
    print("-> Conclusão: Tratamento B é significativamente diferente de A.")
else:
    print("-> t <= valor crítico: NÃO rejeita H0.")


# ============================================================
# PARTE 3: VISUALIZANDO ERROS TIPO I e TIPO II
# ============================================================
# Simulação: quantas vezes rejeitamos H0 erroneamente
# quando H0 É verdadeira (Erro Tipo I)?

print("\n" + "=" * 60)
print("SIMULAÇÃO: TAXA REAL DE ERRO TIPO I")
print("=" * 60)

N_simulacoes = 10_000
alpha = 0.05
rejeitou_h0 = 0

for _ in range(N_simulacoes):
    # Ambos os grupos vêm da mesma distribuição → H0 é verdadeira
    amostra_a = np.random.normal(loc=50, scale=10, size=30)
    amostra_b = np.random.normal(loc=50, scale=10, size=30)
    _, p = stats.ttest_ind(amostra_a, amostra_b)
    if p < alpha:
        rejeitou_h0 += 1

taxa_erro_tipo1 = rejeitou_h0 / N_simulacoes
print(f"Simulações: {N_simulacoes}")
print(f"Rejeições errôneas de H0: {rejeitou_h0}")
print(f"Taxa real de Erro Tipo I: {taxa_erro_tipo1:.3f}  (esperado ≈ {alpha})")


# ============================================================
# PARTE 4: COMPARAÇÃO RESUMIDA DOS MÉTODOS
# ============================================================
print("\n" + "=" * 60)
print("RESUMO: FISHER vs. NEYMAN-PEARSON")
print("=" * 60)
comparacao = {
    "Foco":             ("Evidência pelo valor p",         "Decisão formal com taxas de erro"),
    "Ferramenta":       ("Valor p",                        "Estatística de teste + valor crítico"),
    "Erro Tipo II":     ("Não considera explicitamente",   "Controla explicitamente (β)"),
    "Poder do teste":   ("Não faz parte do método",        "1 - β, fundamental no planejamento"),
}

for criterio, (fisher, np_) in comparacao.items():
    print(f"\n{criterio}:")
    print(f"  Fisher:         {fisher}")
    print(f"  Neyman-Pearson: {np_}")
