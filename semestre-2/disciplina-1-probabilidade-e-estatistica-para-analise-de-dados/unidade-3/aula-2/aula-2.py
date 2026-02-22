import numpy as np
import scipy.stats as stats

def executar_aula_probabilidade():
    print("=== AULA 2: DISTRIBUIÇÕES NA PRÁTICA (PYTHON) ===\n")

    # 1. DISTRIBUIÇÃO NORMAL (O SINO)
    # Simulando alturas de uma população (Média=1.75m, Desvio Padrão=0.10)
    print("--- 1. Distribuição Normal ---")
    media, desvio = 1.75, 0.10
    # Qual a probabilidade de alguém ter EXATAMENTE entre 1.70m e 1.80m?
    prob_normal = stats.norm.cdf(1.80, media, desvio) - stats.norm.cdf(1.70, media, desvio)
    print(f"Probabilidade de altura entre 1.70m e 1.80m: {prob_normal*100:.2f}%")
    print("Dica: Usamos a CDF (FDA) para calcular a área sob o sino!\n")

    # 2. DISTRIBUIÇÃO BINOMIAL (SUCESSO OU FRACASSO)
    # Fábrica: 10 tentativas, chance de defeito de 5% (0.05)
    print("--- 2. Distribuição Binomial ---")
    n, p = 10, 0.05
    # Qual a chance de encontrar EXATAMENTE 1 produto defeituoso em 10?
    prob_binom = stats.binom.pmf(1, n, p)
    print(f"Chance de ter exatamente 1 defeito em 10 produtos: {prob_binom*100:.2f}%")
    print("Dica: PMF é usada para eventos discretos (contáveis).\n")

    # 3. DISTRIBUIÇÃO T DE STUDENT (AMOSTRAS PEQUENAS)
    print("--- 3. Distribuição t de Student ---")
    graus_liberdade = 10  # Ex: Amostra de 11 pessoas (n-1)
    # Qual a chance de um valor estar abaixo de 1.5 desvios na t de Student?
    prob_t = stats.t.cdf(1.5, df=graus_liberdade)
    print(f"Probabilidade acumulada (t < 1.5): {prob_t*100:.2f}%")
    print("Dica: Note que as caudas são mais largas que na Normal.\n")

    # 4. O DESAFIO DO ANALISTA (INFERÊNCIA)
    print("--- 4. Exemplo prático: Amostragem ---")
    populacao_tamanho = 10000
    tamanho_amostra = 178
    defeitos_encontrados = 9
    proporcao_amostral = defeitos_encontrados / tamanho_amostra
    
    print(f"Baseado em {tamanho_amostra} testes, a taxa de defeitos é {proporcao_amostral*100:.2f}%.")
    print(f"Projeção para 10.000 unidades: ~{int(proporcao_amostral * populacao_tamanho)} defeitos.")

if __name__ == "__main__":
    executar_aula_probabilidade()