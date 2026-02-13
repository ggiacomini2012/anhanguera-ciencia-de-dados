import math

# --- DADOS DA AULA ---
# Vendas mensais (em milhares de reais) de Janeiro a Dezembro
vendas = [50, 45, 60, 55, 70, 65, 80, 75, 90, 85, 100, 95]
meses = [
    "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
    "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
]

print("📊 ANALISADOR ESTATÍSTICO - AULA 02")
print("-" * 40)

# 1. CÁLCULO DA MÉDIA
# A média é o "ponto de equilíbrio" (Soma de tudo / quantidade)
media = sum(vendas) / len(vendas)

# 2. CÁLCULO DA MEDIANA
# A mediana é o valor central com os dados ordenados
vendas_ordenadas = sorted(vendas)
n = len(vendas_ordenadas)
meio = n // 2

if n % 2 == 0:
    # Se par, média dos dois valores centrais
    mediana = (vendas_ordenadas[meio - 1] + vendas_ordenadas[meio]) / 2
else:
    # Se ímpar, valor do meio
    mediana = vendas_ordenadas[meio]

# 3. CÁLCULO DO DESVIO PADRÃO
# Mede o quanto os dados "fogem" da média (dispersão)
soma_variancia = sum((x - media) ** 2 for x in vendas)
desvio_padrao = math.sqrt(soma_variancia / n)

# --- EXIBIÇÃO DOS RESULTADOS ---
print(f"📈 Total de meses analisados: {n}")
print(f"💰 Média de Vendas: R$ {media:.2f} mil")
print(f"⚖️ Mediana de Vendas: R$ {mediana:.2f} mil")
print(f"🎢 Desvio Padrão: R$ {desvio_padrao:.2f} mil")
print("-" * 40)

# Insight Prático
if desvio_padrao > 15:
    print("⚠️ Atenção: O desvio padrão está alto! Suas vendas oscilam muito.")
else:
    print("✅ Boa! Suas vendas são constantes e previsíveis.")

print("-" * 40)