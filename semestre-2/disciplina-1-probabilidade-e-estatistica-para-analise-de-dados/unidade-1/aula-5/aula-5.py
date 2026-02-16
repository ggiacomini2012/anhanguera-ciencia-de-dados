import pandas as pd
import numpy as np
from scipy.stats import proportions_ztest
import matplotlib.pyplot as plt

# --- 1. PREPARAÇÃO DOS DADOS ---
# Campanha A: 200 conversões em 1000 exibições
# Campanha B: 250 conversões em 1000 exibições

conversoes = np.array([200, 250])
total_exibicoes = np.array([1000, 1000])

# --- 2. CÁLCULO DAS TAXAS (Estatística Descritiva) ---
taxa_A = conversoes[0] / total_exibicoes[0]
taxa_B = conversoes[1] / total_exibicoes[1]

print(f"📊 Taxa de Conversão Campanha A: {taxa_A:.2%}")
print(f"📊 Taxa de Conversão Campanha B: {taxa_B:.2%}")
print("-" * 30)

# --- 3. TESTE DE HIPÓTESE (Estatística Inferencial) ---
# H0 (Hipótese Nula): As taxas são iguais (a diferença é sorte)
# H1 (Hipótese Alternativa): As taxas são diferentes (a diferença é real)

z_score, p_valor = proportions_ztest(conversoes, total_exibicoes)

print(f"🔍 Valor-p (p-value): {p_valor:.4f}")

# Critério de decisão: Nível de significância de 5% (0.05)
if p_valor < 0.05:
    print("✅ Resultado: A diferença é ESTATISTICAMENTE SIGNIFICATIVA!")
    print("Podemos dizer que a Campanha B é realmente superior.")
else:
    print("❌ Resultado: A diferença NÃO é significativa.")
    print("A variação pode ter sido apenas fruto do acaso.")

# --- 4. VISUALIZAÇÃO (O 'ggplot2' do Python) ---
campanhas = ['Campanha A', 'Campanha B']
taxas = [taxa_A, taxa_B]

plt.figure(figsize=(8, 5))
plt.bar(campanhas, taxas, color=['skyblue', 'salmon'])
plt.ylabel('Taxa de Conversão')
plt.title('Comparativo de Performance: A vs B')
plt.ylim(0, 0.35) # Ajuste de escala para melhor visualização
for i, v in enumerate(taxas):
    plt.text(i, v + 0.01, f"{v:.1%}", ha='center', fontweight='bold')

plt.show()