# -------------------------------------------------------------------------
# S2-D5-U1-A5: Introdução à Pesquisa Operacional e Modelagem
# Objetivo: Demonstrar a lógica de um modelo matemático de decisão.
# -------------------------------------------------------------------------

"""
CENÁRIO:
Uma fábrica de software produz dois tipos de serviços:
1. Automação de Processos (Lucro: R$ 500)
2. Dashboards de BI (Lucro: R$ 300)

LIMITAÇÃO:
Temos apenas 40 horas de desenvolvimento disponíveis por semana.
- Automação consome 8 horas.
- Dashboard consome 4 horas.

PROBLEMA:
Quantas unidades de cada devemos produzir para MAXIMIZAR o lucro?
"""

def simular_otimizacao():
    print("🚀 Iniciando Simulador de Tomada de Decisão (PO)...")
    
    # Variáveis de Decisão (O que podemos controlar)
    lucro_automacao = 500
    lucro_dashboard = 300
    horas_disponiveis = 40
    
    melhor_lucro = 0
    melhor_combinacao = (0, 0)

    print("\n🔍 Analisando possibilidades dentro das restrições...")

    # Testando combinações simples (Brute Force didático)
    for qte_automacao in range(6): # Máximo 5 (5*8=40)
        for qte_dashboard in range(11): # Máximo 10 (10*4=40)
            
            # Cálculo da Restrição
            horas_usadas = (qte_automacao * 8) + (qte_dashboard * 4)
            
            # Verificando se a combinação é válida (não ultrapassa as 40h)
            if horas_usadas <= horas_disponiveis:
                lucro_total = (qte_automacao * lucro_automacao) + (qte_dashboard * lucro_dashboard)
                
                # Se for o melhor lucro até agora, salvamos
                if lucro_total > melhor_lucro:
                    melhor_lucro = lucro_total
                    melhor_combinacao = (qte_automacao, qte_dashboard)
                
                # print(f"   Opção: {qte_automacao} Automações + {qte_dashboard} Dashboards | Horas: {horas_usadas}h | Lucro: R${lucro_total}")

    print("\n" + "="*50)
    print("🏆 RESULTADO DA OTIMIZAÇÃO")
    print("="*50)
    print(f"✅ Melhor Estratégia: {melhor_combinacao[0]} Automações e {melhor_combinacao[1]} Dashboards")
    print(f"💰 Lucro Máximo: R$ {melhor_lucro}")
    print(f"⌛ Horas Utilizadas: {(melhor_combinacao[0]*8) + (melhor_combinacao[1]*4)}h de {horas_disponiveis}h")
    print("="*50)

    print("\n💡 INSIGHT DE DATA SCIENCE:")
    print("Enquanto a análise de dados nos diz o que aconteceu, a Pesquisa")
    print("Operacional nos diz qual o MELHOR caminho a seguir dadas as nossas")
    print("limitações. Isso transforma dados em dinheiro! 💎")

if __name__ == "__main__":
    simular_otimizacao()