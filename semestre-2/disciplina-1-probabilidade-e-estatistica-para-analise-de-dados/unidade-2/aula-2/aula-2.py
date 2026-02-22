import statistics

# 📊 Dados: Comparando dois atletas (Pontuação em 5 jogos)
# Atleta A: Muito consistente
# Atleta B: "Oito ou oitenta"
atleta_a = [20, 22, 21, 19, 20]
atleta_b = [5, 40, 10, 35, 12]

def analisar_dispersao(nome, dados):
    print(f"--- 📈 Análise: {nome} ---")
    print(f"Dados: {dados}")
    
    # 1. Média (Para contexto)
    media = statistics.mean(dados)
    
    # 2. Amplitude (Máximo - Mínimo)
    amplitude = max(dados) - min(dados)
    
    # 3. Variância
    variancia = statistics.variance(dados)
    
    # 4. Desvio Padrão (O mais importante!)
    desvio_padrao = statistics.stdev(dados)
    
    print(f"⚖️ Média: {media}")
    print(f"📏 Amplitude: {amplitude}")
    print(f"🧬 Variância: {variancia:.2f}")
    print(f"🎯 Desvio Padrão: {desvio_padrao:.2f}")
    print("-" * 30, "\n")

# Executando a comparação
analisar_dispersao("Atleta A (Consistente)", atleta_a)
analisar_dispersao("Atleta B (Irregular)", atleta_b)

print("💡 CONCLUSÃO:")
print("Note que ambos têm a mesma MÉDIA (20.4), mas o Atleta B tem um")
print("DESVIO PADRÃO muito maior, indicando que ele é menos previsível.")