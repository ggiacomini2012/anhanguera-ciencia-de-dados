import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns

# Configuração de estilo para os gráficos
sns.set_theme(style="whitegrid")

def aula_pratica_estatistica():
    print("🚀 Iniciando Simulação de Teste de Hipóteses (Novo Medicamento)")
    
    # 1. Gerando dados simulados (30 pacientes)
    # Média real de 115 mmHg, desvio padrão de 10
    np.random.seed(123)
    amostra = np.random.normal(loc=115, scale=10, size=30)
    
    # 2. Teste t de uma amostra (Comparando contra o valor de referência: 120 mmHg)
    # Hipótese Nula (H0): média = 120
    # Hipótese Alternativa (H1): média != 120
    t_stat, p_valor = stats.ttest_1samp(amostra, popmean=120)
    
    print(f"\n📊 Resultados do Teste:")
    print(f"   - Média da Amostra: {np.mean(amostra):.2f} mmHg")
    print(f"   - Estatística t: {t_stat:.4f}")
    print(f"   - P-Valor: {p_valor:.4f}")
    
    # 3. Intervalo de Confiança (95%)
    dof = len(amostra) - 1
    conf_level = 0.95
    mean = np.mean(amostra)
    sem = stats.sem(amostra)
    intervalo = stats.t.interval(conf_level, dof, loc=mean, scale=sem)
    
    print(f"   - Intervalo de Confiança (95%): [{intervalo[0]:.2f}, {intervalo[1]:.2f}]")
    
    # 4. Decisão Teórica
    alpha = 0.05
    if p_valor < alpha:
        print("\n✅ CONCLUSÃO: Rejeitamos a Hipótese Nula! O medicamento é eficaz.")
    else:
        print("\n❌ CONCLUSÃO: Falha ao rejeitar a Hipótese Nula. Sem evidências suficientes.")

    # 5. Visualização (Gráfico de Densidade)
    plt.figure(figsize=(10, 6))
    sns.kdeplot(amostra, fill=True, color="skyblue", label="Distribuição da Amostra")
    plt.axvline(120, color="red", linestyle="--", label="Média de Referência (120)")
    plt.axvline(mean, color="green", linestyle="-", label="Média da Amostra")
    
    plt.title("O Medicamento funcionou? (Análise de Pressão Arterial)")
    plt.xlabel("Pressão Arterial (mmHg)")
    plt.ylabel("Densidade")
    plt.legend()
    
    print("\n📈 Gráfico gerado com sucesso! (Feche a janela para continuar)")
    plt.show()

if __name__ == "__main__":
    aula_pratica_estatistica()
