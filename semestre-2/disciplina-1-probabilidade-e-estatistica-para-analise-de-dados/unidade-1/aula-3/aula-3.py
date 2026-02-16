import random

def linha_separadora():
    print("-" * 50)

# --- SIMULAÇÃO 1: Lei dos Grandes Números (Lançamento de Moedas) ---
def simular_moeda(lancamentos):
    print(f"\n🚀 Simulando {lancamentos} lançamentos de moeda...")
    resultados = {"Cara": 0, "Coroa": 0}
    
    for _ in range(lancamentos):
        resultado = random.choice(["Cara", "Coroa"])
        resultados[resultado] += 1
    
    for face, qtd in resultados.items():
        porcentagem = (qtd / lancamentos) * 100
        print(f"🔹 {face}: {qtd} vezes ({porcentagem:.2f}%)")

# --- SIMULAÇÃO 2: Probabilidade Total (Risco de Seguro) ---
def calcular_risco_seguro():
    print("\n📊 Cálculo de Probabilidade Total de Sinistro (Reclamação)")
    
    # Cenários: [Probabilidade do Perfil ocorrer, Chance de bater o carro]
    # Perfil A: Jovem, Urbano, Histórico Ruim
    # Perfil B: Experiente, Rural, Histórico Bom
    perfis = {
        "Perfil A (Alto Risco)": {"p_perfil": 0.30, "p_sinistro": 0.80},
        "Perfil B (Baixo Risco)": {"p_perfil": 0.70, "p_sinistro": 0.10}
    }
    
    prob_total_sinistro = 0
    
    for nome, dados in perfis.items():
        contribuicao = dados["p_perfil"] * dados["p_sinistro"]
        prob_total_sinistro += contribuicao
        print(f"✅ {nome}: {dados['p_perfil']*100}% da frota | Risco Individual: {dados['p_sinistro']*100}%")
    
    print(f"\n📈 A Probabilidade Total de qualquer cliente bater o carro é: {prob_total_sinistro * 100:.2f}%")

# --- EXECUÇÃO ---
if __name__ == "__main__":
    print("🎓 AULA 3: PRÁTICA DE PROBABILIDADE COM PYTHON")
    linha_separadora()
    
    # Demonstração da convergência (Lei dos Grandes Números)
    simular_moeda(10)      # Poucos lançamentos (impreciso)
    simular_moeda(100000)  # Muitos lançamentos (próximo de 50%)
    
    linha_separadora()
    
    # Demonstração de Probabilidade Total
    calcular_risco_seguro()
    
    linha_separadora()
    print("Simulação concluída com sucesso! 💡")