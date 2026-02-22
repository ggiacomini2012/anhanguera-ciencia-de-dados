import numpy as np
from scipy import stats

# Configurando uma semente para que os resultados sejam replicáveis
np.random.seed(123)

print("--- 📊 SIMULAÇÃO DE AMOSTRAGEM PARA BIG DATA ---")

# 1. GERANDO A POPULAÇÃO (1 Milhão de indivíduos)
# Simulando a renda de uma cidade: média 5000, desvio padrão 1500
populacao = np.random.normal(loc=5000, scale=1500, size=1000000)

# 2. EXTRAINDO UMA AMOSTRA ALEATÓRIA SIMPLES
tamanho_amostra = 1000
amostra = np.random.choice(populacao, size=tamanho_amostra, replace=False)

# 3. ESTATÍSTICAS BÁSICAS
media_amostra = np.mean(amostra)
desvio_padrao_amostra = np.std(amostra, ddof=1)

print(f"Média da Amostra: {media_amostra:.2f}")
print(f"Desvio Padrão da Amostra: {desvio_padrao_amostra:.2f}")

# 4. TEOREMA DO LIMITE CENTRAL (TLC) na prática
# Vamos ver como a média se aproxima da real conforme a amostra cresce
for n in [30, 100, 1000]:
    sub_amostra = np.random.choice(populacao, size=n, replace=False)
    print(f"Média com n={n:4}: {np.mean(sub_amostra):.2f}")

# 5. TÉCNICA DE BOOTSTRAP (Reamostragem)
# Vamos estimar o erro padrão da média sem olhar para a população original
n_bootstrap = 1000
medias_bootstrap = []

for _ in range(n_bootstrap):
    # Gera uma nova amostra a partir da amostra original (com reposição)
    reamostra = np.random.choice(amostra, size=tamanho_amostra, replace=True)
    medias_bootstrap.append(np.mean(reamostra))

erro_padrao_boot = np.std(medias_bootstrap, ddof=1)
print(f"\nErro padrão estimado via Bootstrap: {erro_padrao_boot:.4f}")

# 6. INTERVALO DE CONFIANÇA (95%)
ic_inferior = np.percentile(medias_bootstrap, 2.5)
ic_superior = np.percentile(medias_bootstrap, 97.5)

print(f"Intervalo de Confiança 95% (Bootstrap): [{ic_inferior:.2f}, {ic_superior:.2f}]")