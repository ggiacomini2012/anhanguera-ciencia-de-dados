import numpy as np

# 🤖 Dados de Teste do Assistente Virtual
# Precisão das respostas (0 a 100%)
precisao = [85, 90, 78, 92, 88, 70, 95, 80, 82, 89]

# Satisfação dos clientes (Nota de 1 a 5)
satisfacao = [4, 5, 3, 5, 4, 2, 5, 4, 4, 5]

print("--- 📊 RELATÓRIO DE DESEMPENHO: ASSISTENTE VIRTUAL ---")

# 1. Calculando a Média (Estatística Descritiva)
media_precisao = np.mean(precisao)
media_satisfacao = np.mean(satisfacao)

print(f"✅ Média de Precisão: {media_precisao:.2f}%")
print(f"⭐ Média de Satisfação: {media_satisfacao:.2f} / 5.0")

# 2. Calculando a Correlação (Relação entre as variáveis)
# A correlação varia de -1 a 1. 
# Perto de 1 significa que quando a precisão sobe, a satisfação também sobe!
correlacao = np.corrcoef(precisao, satisfacao)[0, 1]

print(f"\n🔗 Correlação (Precisão vs Satisfação): {correlacao:.4f}")

# 3. Interpretação Simples
if correlacao > 0.7:
    print("\n💡 INSIGHT: Existe uma forte relação positiva!")
    print("Quanto mais preciso o assistente, mais feliz o cliente fica. ✨")
else:
    print("\n💡 INSIGHT: A relação não é tão clara.")
    print("Talvez outros fatores (como tempo de espera) afetem a satisfação. 🤔")

print("\n--- FIM DO PROCESSAMENTO ---")