import numpy as np
from scipy import stats

# Configurando uma semente para resultados reprodutíveis
np.random.seed(123)

print("--- 📊 Aula 03: Análise Estatística com Python ---")

# 1. Gerando a amostra (Simulando 100 observações)
# Média real = 50, Desvio Padrão = 10
amostra = np.random.normal(loc=50, scale=10, size=100)

# 2. Cálculos Básicos
media_amostra = np.mean(amostra)
desvio_padrao = np.std(amostra, ddof=1)  # ddof=1 para desvio padrão amostral
n = len(amostra)

# 3. Cálculo do Intervalo de Confiança (IC) de 95%
confianca = 0.95
erro_padrao = desvio_padrao / np.sqrt(n)
# Usando a distribuição t de Student
graus_liberdade = n - 1
t_critico = stats.t.ppf((1 + confianca) / 2, graus_liberdade)

limite_inferior = media_amostra - t_critico * erro_padrao
limite_superior = media_amostra + t_critico * erro_padrao

print(f"\nMédia da Amostra: {media_amostra:.2f}")
print(f"IC 95%: [{limite_inferior:.2f}, {limite_superior:.2f}]")

# 4. Teste de Hipótese (One Sample t-test)
# H0: média = 50
t_stat, p_valor = stats.ttest_1samp(amostra, popmean=50)

print(f"\nTeste t (H0: média = 50):")
print(f"Estatística t: {t_stat:.4f}")
print(f"p-valor: {p_valor:.4f}")

if p_valor < 0.05:
    print("Resultado: Rejeitamos a hipótese nula (Diferença significativa).")
else:
    print("Resultado: Não há evidências para rejeitar a hipótese nula.")

# 5. Método Bootstrap (Reamostragem)
print("\n--- 🔄 Iniciando Bootstrap (1000 reamostragens) ---")
medias_boot = []
for _ in range(1000):
    # Gera uma amostra do mesmo tamanho, com reposição
    reamostra = np.random.choice(amostra, size=n, replace=True)
    medias_boot.append(np.mean(reamostra))

ic_boot_inf = np.percentile(medias_boot, 2.5)
ic_boot_sup = np.percentile(medias_boot, 97.5)

print(f"IC 95% Bootstrap: [{ic_boot_inf:.2f}, {ic_boot_sup:.2f}]")
