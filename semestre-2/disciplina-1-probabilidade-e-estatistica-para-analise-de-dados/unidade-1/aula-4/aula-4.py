import pandas as pd
import numpy as np
from scipy import stats

def linha():
    print("=" * 60)

# --- 1. MANIPULAÇÃO DE DADOS (O estilo dplyr no Python) ---
def demonstrar_manipulacao():
    linha()
    print("🧪 SIMULANDO OPERAÇÕES DE E-COMMERCE (ESTILO DPLYR)")
    
    # Criando um dataset fictício
    data = {
        'produto': ['Smartphone', 'Laptop', 'Tablet', 'Fone', 'Smartwatch'],
        'quantidade': [10, 5, 15, 50, 20],
        'receita': [20000, 25000, 12000, 5000, 8000]
    }
    df = pd.DataFrame(data)

    # Mutate: Criando coluna de preço médio
    df['preco_medio'] = df['receita'] / df['quantidade']

    # Filter & Select: Produtos com receita > 10000
    top_produtos = df[df['receita'] > 10000][['produto', 'receita']]
    
    print("\nProdutos com Alta Receita:")
    print(top_produtos)
    linha()

# --- 2. DISTRIBUIÇÕES PROBABILÍSTICAS ---
def demonstrar_probabilidade():
    print("🎲 CÁLCULOS ESTATÍSTICOS")
    
    # Distribuição Normal (rnorm)
    # Simulando altura de clientes: média 175cm, desvio padrão 10
    alturas = np.random.normal(175, 10, 1000)
    print(f"\n🔹 Média das alturas simuladas: {np.mean(alturas):.2f}cm")

    # Probabilidade Cumulativa (pnorm)
    # Qual a chance de um cliente ter menos de 170cm?
    prob = stats.norm.cdf(170, 175, 10)
    print(f"🔹 Probabilidade de altura < 170cm: {prob*100:.2f}%")

    # Distribuição Poisson (rpois)
    # Chamadas no SAC por hora (média 5)
    chamadas = np.random.poisson(5, 5)
    print(f"🔹 Simulação de chamadas no SAC (5 horas): {chamadas}")
    linha()

# --- 3. REGRESSÃO LINEAR ---
def demonstrar_regressao():
    print("📈 REGRESSÃO LINEAR: INVESTIMENTO VS RETORNO")
    
    # X = Investimento em Marketing, Y = Vendas
    x = np.array([100, 200, 300, 400, 500])
    y = np.array([1050, 2100, 2950, 4100, 5050])
    
    slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
    
    print(f"\n🔹 Equação: Vendas = {slope:.2f} * Marketing + {intercept:.2f}")
    print(f"🔹 Precisão do Modelo (R²): {r_value**2:.4f}")
    linha()

if __name__ == "__main__":
    print("🎓 AULA 4: CIÊNCIA DE DADOS E PROBABILIDADE")
    demonstrar_manipulacao()
    demonstrar_probabilidade()
    demonstrar_regressao()
    print("🚀 Script finalizado com sucesso!")