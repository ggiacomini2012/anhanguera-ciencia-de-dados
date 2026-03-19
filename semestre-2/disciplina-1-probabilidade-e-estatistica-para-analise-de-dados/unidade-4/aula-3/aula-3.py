# ============================================================
# Aula 3 - Unidade 4: Testes de Hipóteses
# Teste Z, Teste t de Student e Teste Qui-quadrado
# ============================================================

import numpy as np
from scipy import stats

np.random.seed(42)


# ============================================================
# PARTE 1: TESTE Z
# ============================================================
# Quando usar:
#   - Amostra grande (n > 30)
#   - Variância POPULACIONAL conhecida
#   - Distribuição aproximadamente normal

print("=" * 60)
print("TESTE Z — nova estratégia de marketing")
print("=" * 60)

# H0: taxa de conversão = 5% (sem efeito da nova estratégia)
# H1: taxa de conversão ≠ 5%

media_pop = 0.05        # média da população (antes da estratégia)
media_amostra = 0.07    # média da amostra (após nova estratégia)
desvio_pop = 0.02       # desvio padrão CONHECIDO da população
n = 50                  # tamanho da amostra

z_score = (media_amostra - media_pop) / (desvio_pop / np.sqrt(n))
valor_p = 2 * (1 - stats.norm.cdf(abs(z_score)))  # bicaudal

print(f"Z-score: {z_score:.4f}")
print(f"Valor p: {valor_p:.2e}")

alpha = 0.05
if valor_p < alpha:
    print(f"-> p < {alpha}: REJEITA H0.")
    print("-> A nova estratégia gerou impacto significativo na conversão.")
else:
    print(f"-> p >= {alpha}: NÃO rejeita H0.")

# Intervalo de confiança 95% para o teste Z
z_critico = stats.norm.ppf(1 - alpha / 2)  # ≈ 1.96
margem = z_critico * (desvio_pop / np.sqrt(n))
ic_lower = media_amostra - margem
ic_upper = media_amostra + margem
print(f"\nIC 95%: [{ic_lower:.4f}, {ic_upper:.4f}]")


# ============================================================
# PARTE 2: TESTE T DE STUDENT
# ============================================================
# Quando usar:
#   - Amostra pequena (n < 30) OU variância DESCONHECIDA
#   - Distribuição aproximadamente normal

print("\n" + "=" * 60)
print("TESTE T — campanhas publicitárias A vs. B")
print("=" * 60)

# Dados de vendas (10 lojas por campanha)
vendas_A = np.array([150, 160, 145, 170, 155, 165, 140, 175, 150, 160])
vendas_B = np.array([180, 175, 165, 160, 170, 185, 175, 180, 165, 170])

# Duas amostras independentes (variância desconhecida → teste t de Welch)
resultado_t = stats.ttest_ind(vendas_A, vendas_B)

print(f"Média A: {vendas_A.mean():.1f}  |  Média B: {vendas_B.mean():.1f}")
print(f"Estatística t: {resultado_t.statistic:.4f}")
print(f"Valor p: {resultado_t.pvalue:.6f}")

if resultado_t.pvalue < alpha:
    print(f"-> p < {alpha}: REJEITA H0.")
    print("-> Há diferença significativa entre as vendas das campanhas A e B.")
else:
    print(f"-> p >= {alpha}: NÃO rejeita H0.")

# Intervalo de confiança 95% para diferença de médias
diff_media = vendas_A.mean() - vendas_B.mean()
se = np.sqrt(vendas_A.std(ddof=1)**2 / len(vendas_A) +
             vendas_B.std(ddof=1)**2 / len(vendas_B))
df = len(vendas_A) + len(vendas_B) - 2
t_critico = stats.t.ppf(1 - alpha / 2, df=df)
ic = (diff_media - t_critico * se, diff_media + t_critico * se)
print(f"\nIC 95% para (média_A - média_B): [{ic[0]:.2f}, {ic[1]:.2f}]")
print("Se o IC não inclui 0, confirma diferença significativa.")


# ============================================================
# PARTE 3: TESTE QUI-QUADRADO
# ============================================================
# Quando usar:
#   - Variáveis CATEGÓRICAS
#   - Testar independência entre duas variáveis

print("\n" + "=" * 60)
print("TESTE QUI-QUADRADO — gênero vs. preferência de produto")
print("=" * 60)

# Tabela de contingência:
#               Produto A   Produto B
# Masculino        50          30
# Feminino         20          40
tabela = np.array([[50, 30],
                   [20, 40]])

print("Tabela de contingência:")
print("             Produto A  Produto B")
print(f"Masculino:     {tabela[0,0]}         {tabela[0,1]}")
print(f"Feminino:      {tabela[1,0]}         {tabela[1,1]}")

resultado_qui = stats.chi2_contingency(tabela, correction=True)
chi2, p_qui, df_qui, esperado = resultado_qui

print(f"\nQui-quadrado: {chi2:.4f}")
print(f"Graus de liberdade: {df_qui}")
print(f"Valor p: {p_qui:.6f}")

if p_qui < alpha:
    print(f"-> p < {alpha}: REJEITA H0.")
    print("-> Há associação significativa entre gênero e preferência de produto.")
else:
    print(f"-> p >= {alpha}: NÃO rejeita H0. Variáveis são independentes.")


# ============================================================
# PARTE 4: GUIA DE ESCOLHA DO TESTE CERTO
# ============================================================
print("\n" + "=" * 60)
print("GUIA: QUAL TESTE USAR?")
print("=" * 60)

guia = [
    ("Variável contínua + n>30 + variância conhecida", "Teste Z"),
    ("Variável contínua + n<30 OU variância desconhecida", "Teste t de Student"),
    ("Variáveis categóricas, testar associação",         "Teste Qui-quadrado"),
]

for situacao, teste in guia:
    print(f"• {situacao}")
    print(f"  → {teste}\n")
