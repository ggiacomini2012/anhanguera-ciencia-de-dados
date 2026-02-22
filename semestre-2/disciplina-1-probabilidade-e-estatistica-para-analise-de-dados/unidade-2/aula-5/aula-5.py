import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1. CRIANDO NOSSO CONJUNTO DE DADOS (Cenário: Salários por Departamento)
# Simulando dados de funcionários em uma empresa de tecnologia
data = {
    'departamento': ['TI', 'TI', 'TI', 'TI', 'TI', 'RH', 'RH', 'RH', 'RH', 'Vendas', 'Vendas', 'Vendas'],
    'salario': [5000, 5500, 4800, 5200, 15000, 30000, 3200, 3100, 3300, 4000, 4200, 4100]
}

df = pd.DataFrame(data)

print("--- 📊 ANÁLISE DESCRITIVA GERAL ---")

# 2. MEDIDAS DE TENDÊNCIA CENTRAL
media = df['salario'].mean()
mediana = df['salario'].median()
moda = df['salario'].mode()[0]

print(f"Média Salarial: R$ {media:.2f} (O 'equilíbrio' - sensível a outliers)")
print(f"Mediana: R$ {mediana:.2f} (O 'meio real' - robusta)")
print(f"Moda: R$ {moda:.2f} (O valor que mais se repete)")

# 3. MEDIDAS DE DISPERSÃO
amplitude = df['salario'].max() - df['salario'].min()
variancia = df['salario'].var()
desvio_padrao = df['salario'].std()

print(f"\nAmplitude: R$ {amplitude:.2f} (Distância entre os extremos)")
print(f"Variância: {variancia:.2f} (Dispersão quadrática)")
print(f"Desvio Padrão: R$ {desvio_padrao:.2f} (Quanto os salários fogem da média)")

# 4. ANÁLISE POR DEPARTAMENTO (Agrupamento)
print("\n--- 🏢 RESUMO POR DEPARTAMENTO ---")
resumo_depto = df.groupby('departamento')['salario'].describe()
print(resumo_depto)

# 5. VISUALIZAÇÃO (BOXPLOT)
# O Boxplot nos ajuda a ver os Outliers (como o salário de 15k e 30k que fogem do padrão)
plt.figure(figsize=(10, 6))
df.boxplot(column='salario', by='departamento', grid=False, patch_artist=True)
plt.title('Distribuição Salarial por Departamento')
plt.suptitle('') # Remove o título automático do pandas
plt.ylabel('Salário (R$)')
plt.show()

print("\n✅ Arquivo aula-5.py gerado com sucesso!")