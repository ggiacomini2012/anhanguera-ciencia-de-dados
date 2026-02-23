import numpy as np
from scipy import stats
from statsmodels.stats.proportion import proportions_ztest

# Configurando uma semente para resultados reproduzíveis (como o set.seed no R)
np.random.seed(123)

print("🧪 --- SIMULAÇÃO DE EXPERIMENTOS ESTATÍSTICOS --- 🧪\n")

# ---------------------------------------------------------
# CENÁRIO 1: Teste t de Student (Comparação de Médias)
# Exemplo: Eficácia de dois tratamentos (A e B)
# ---------------------------------------------------------
print("1. TESTE T DE STUDENT (Tratamentos)")
tratamento_a = np.random.normal(loc=60, scale=10, size=100)
tratamento_b = np.random.normal(loc=65, scale=10, size=100)

t_stat, p_val_t = stats.ttest_ind(tratamento_a, tratamento_b)

print(f"Média Tratamento A: {np.mean(tratamento_a):.2f}")
print(f"Média Tratamento B: {np.mean(tratamento_b):.2f}")
print(f"Valor-p: {p_val_t:.4f}")

if p_val_t < 0.05:
    print("Resultado: Diferença ESTATISTICAMENTE SIGNIFICATIVA! 🎉")
else:
    print("Resultado: Não há evidências de diferença significativa. 🤷‍♂️")


print("\n" + "-"*50 + "\n")


# ---------------------------------------------------------
# CENÁRIO 2: Teste A/B (Comparação de Proporções)
# Exemplo: Conversão de vendas em páginas de E-commerce
# ---------------------------------------------------------
print("2. TESTE A/B (Conversão de E-commerce)")
# Dados: 5000 visitantes por versão
visitantes_a, visitantes_b = 5000, 5000
# Simulando conversões (11.46% para A e 14.48% para B conforme o exemplo)
conversoes_a = 573 
conversoes_b = 724

sucessos = np.array([conversoes_a, conversoes_b])
amostras = np.array([visitantes_a, visitantes_b])

# Realizando o teste de proporções (Z-test)
z_stat, p_val_p = proportions_ztest(sucessos, amostras)

print(f"Taxa de Conversão A: {(conversoes_a/visitantes_a)*100:.2f}%")
print(f"Taxa de Conversão B: {(conversoes_b/visitantes_b)*100:.2f}%")
print(f"Valor-p: {p_val_p:.8f}")

if p_val_p < 0.05:
    print("Resultado: A Versão B é SUPERIOR! 🚀")
else:
    print("Resultado: As versões performam de forma similar. ⚖️")