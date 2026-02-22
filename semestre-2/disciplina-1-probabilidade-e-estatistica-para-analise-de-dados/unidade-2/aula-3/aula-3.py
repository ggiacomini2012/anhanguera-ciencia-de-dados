import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Configuração para reprodutibilidade (o mesmo 'set.seed' do R)
np.random.seed(123)

# 1. Gerando dados fictícios de IMC
# Jovens Adultos: Média 24, Desvio Padrão 3
jovens_adultos = np.random.normal(loc=24, scale=3, size=100)

# Meia-Idade: Média 27, Desvio Padrão 4
meia_idade = np.random.normal(loc=27, scale=4, size=100)

# 2. Criando o DataFrame (Nossa tabela de dados)
dados = pd.DataFrame({
    'IMC': np.concatenate([jovens_adultos, meia_idade]),
    'Grupo': ['Jovens Adultos'] * 100 + ['Meia Idade'] * 100
})

# 3. Calculando as Estimativas (Quartis e Percentis)
print("--- RESUMO ESTATÍSTICO (Quartis) ---")
resumo = dados.groupby('Grupo')['IMC'].describe()
print(resumo)

# Calculando um percentil específico (ex: Percentil 90)
p90 = dados.groupby('Grupo')['IMC'].quantile(0.90)
print(f"\n--- PERCENTIL 90 --- \n{p90}")

# 4. Criando o Boxplot com Seaborn (Visualização)
plt.figure(figsize=(10, 6))
sns.boxplot(x='Grupo', y='IMC', data=dados, palette='Set2')

# Adicionando detalhes ao gráfico
plt.title('Comparação de IMC: Jovens Adultos vs Meia-Idade', fontsize=14)
plt.xlabel('Grupo Etário', fontsize=12)
plt.ylabel('Índice de Massa Corporal (IMC)', fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Exibindo o gráfico
print("\nGerando o gráfico de Boxplot...")
plt.show()