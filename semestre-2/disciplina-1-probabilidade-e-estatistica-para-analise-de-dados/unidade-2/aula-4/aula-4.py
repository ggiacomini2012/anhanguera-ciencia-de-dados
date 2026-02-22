import numpy as np
import pandas as pd

# Configurando uma semente para que os resultados sejam sempre iguais (reprodutibilidade)
np.random.seed(123)

print("--- 1. SIMULAÇÃO DE POPULAÇÃO E AMOSTRAGEM SIMPLES ---")
# Simulando a renda de uma cidade (População de 1 milhão)
# Média = 5000, Desvio Padrão = 1500
populacao_renda = np.random.normal(loc=5000, scale=1500, size=1000000)

# Extraindo uma amostra aleatória de 1000 pessoas
amostra = np.random.choice(populacao_renda, size=1000, replace=False)

print(f"Média da Amostra: {amostra.mean():.2f}")
print(f"Desvio Padrão da Amostra: {amostra.std():.2f}\n")


print("--- 2. PESQUISA ELEITORAL (PROPORÇÃO BINÁRIA) ---")
# 1 = Voto Candidato A (55%), 0 = Voto Candidato B (45%)
populacao_eleitores = np.random.binomial(n=1, p=0.55, size=10000000)

# Amostra de 5000 eleitores
amostra_eleitores = np.random.choice(populacao_eleitores, size=5000, replace=False)
proporcao_a = amostra_eleitores.mean()

print(f"Proporção estimada de votos para o Candidato A: {proporcao_a:.4f}")
print(f"Isso representa {proporcao_a * 100:.2f}% de intenção de voto.\n")


print("--- 3. TÉCNICA DE BOOTSTRAP (RE-AMOSTRAGEM) ---")
# Queremos saber o Erro Padrão da nossa média sem olhar a população de novo
def bootstrap_media(dados, n_repeticoes=1000):
    medias_boot = []
    for _ in range(n_repeticoes):
        # Sorteia com reposição (a essência do bootstrap)
        amostra_resample = np.random.choice(dados, size=len(dados), replace=True)
        medias_boot.append(amostra_resample.mean())
    return np.array(medias_boot)

# Aplicando o Bootstrap na amostra de eleitores
resultados_boot = bootstrap_media(amostra_eleitores)
erro_padrao_boot = resultados_boot.std()

print(f"Erro padrão estimado pelo Bootstrap: {erro_padrao_boot:.6f}")
print("O Bootstrap nos diz o quanto essa média 'balança' se repetíssemos o teste.")