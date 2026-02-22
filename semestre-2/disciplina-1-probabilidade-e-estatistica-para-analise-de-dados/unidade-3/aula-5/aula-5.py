import numpy as np
import pandas as pd

# Configurando a Semente (Seed) para que o "sorteio" seja sempre igual
np.random.seed(42)

print("--- 🛒 Simulação de Satisfação de Clientes ---")

# 1. Criando a POPULAÇÃO (O Oceano 🌊)
# Vamos imaginar 100.000 clientes com notas de satisfação de 0 a 10
populacao_satisfacao = np.random.normal(loc=7.5, scale=1.5, size=100000)
populacao_satisfacao = np.clip(populacao_satisfacao, 0, 10) # Garante que as notas fiquem entre 0 e 10

print(f"Média Real da População: {populacao_satisfacao.mean():.2f}")

# 2. Amostragem Aleatória Simples (O Copo d'água 🥛)
tamanho_amostra = 1000
amostra = np.random.choice(populacao_satisfacao, size=tamanho_amostra, replace=False)

media_amostral = amostra.mean()
print(f"Média da Amostra (1000 clientes): {media_amostral:.2f}")

# 3. Técnica de Bootstrap (Reamostragem 🥾)
# Vamos criar 5.000 "mini-amostras" a partir da nossa amostra de 1.000
n_iterações = 5000
medias_bootstrap = []

for _ in range(n_iterações):
    # Sorteia com reposição
    sub_amostra = np.random.choice(amostra, size=tamanho_amostra, replace=True)
    medias_bootstrap.append(sub_amostra.mean())

# 4. Intervalo de Confiança (95%)
# Buscamos os valores entre os percentis 2.5 e 97.5
limite_inferior = np.percentile(medias_bootstrap, 2.5)
limite_superior = np.percentile(medias_bootstrap, 97.5)

print("\n--- ✅ Resultado da Inferência ---")
print(f"Com 95% de confiança, a média de satisfação real")
print(f"está entre {limite_inferior:.2f} e {limite_superior:.2f}")

# 5. Demonstração do Teorema do Limite Central (TLC)
print(f"\nO desvio padrão das médias de bootstrap é: {np.std(medias_bootstrap):.4f}")
print("Note como a distribuição das médias é muito mais estreita e 'Normal' que a original!")