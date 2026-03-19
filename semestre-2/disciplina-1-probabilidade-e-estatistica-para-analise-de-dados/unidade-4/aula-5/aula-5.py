import numpy as np
from statsmodels.stats.proportion import proportions_ztest

def simulacao_teste_ab():
    print("📢 Iniciando Teste A/B de Marketing (Versão A vs Versão B)")
    
    # Dados do Estudo de Caso da Aula 5:
    # Versão A: 500 clientes, 20% de conversão (100 sucessos)
    # Versão B: 500 clientes, 25% de conversão (125 sucessos)
    
    n_a = 500
    n_b = 500
    conv_a = 100 # 20% de 500
    conv_b = 125 # 25% de 500
    
    # Preparando dados para o Statsmodels
    sucessos = np.array([conv_a, conv_b])
    amostras = np.array([n_a, n_b])
    
    # Executando o Teste Z para Proporções
    # H0: As proporções são iguais
    # H1: As proporções são diferentes
    z_stat, p_valor = proportions_ztest(count=sucessos, nobs=amostras)
    
    print(f"\n📊 Resultados do Teste Z:")
    print(f"   - Taxa Conv. A: {(conv_a/n_a)*100:.1f}%")
    print(f"   - Taxa Conv. B: {(conv_b/n_b)*100:.1f}%")
    print(f"   - Estatística Z: {z_stat:.4f}")
    print(f"   - P-Valor: {p_valor:.4f}")
    
    # Decisão
    alpha = 0.05
    if p_valor < alpha:
        print("\n✅ CONCLUSÃO: Existe uma diferença significativa! A Versão B é superior.")
    else:
        print("\n❌ CONCLUSÃO: Não há diferença significativa. As taxas são estatisticamente iguais.")

    print("\n💡 Nota: Embora a Versão B pareça melhor (25% vs 20%), a estatística nos diz")
    print("se essa diferença é GRANDE o suficiente para não ser apenas acaso.")

if __name__ == "__main__":
    simulacao_teste_ab()
