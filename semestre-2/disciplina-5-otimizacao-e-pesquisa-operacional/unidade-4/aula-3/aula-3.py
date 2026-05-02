"""
S2-D5-U4-A3 — Atribuições e Coleta de Dados
Assunto: Módulos ASSIGN e RECORD no Arena
Exemplo: Fluxo de Atendimento com Categorias 🏦📊
"""

import random

# Configurações
NUM_ENTIDADES = 15
TEMPO_LAVAGEM_BASE = 5

def simulacao_com_estatisticas():
    print("📈 Iniciando Simulação com ASSIGN e RECORD 📈")
    print("-" * 60)
    
    total_tempo_sistema = 0
    contagem_vip = 0
    contagem_normal = 0
    
    # Lista para simular o "Record" de cada entidade
    historico_tempos = []

    for i in range(1, NUM_ENTIDADES + 1):
        # 1. Bloco CREATE: Entidade entra no sistema
        tempo_chegada = random.uniform(0, 20)
        
        # 2. Bloco ASSIGN: Atribuindo Atributos (Tipo e Cor)
        # Sorteia se é VIP (20% de chance) ou Normal
        tipo_cliente = "VIP" if random.random() < 0.2 else "Normal"
        cor_imagem = "Estrela Dourada" if tipo_cliente == "VIP" else "Círculo Azul"
        
        print(f"👤 Entidade {i:02d} | 🛠️ ASSIGN: Tipo={tipo_cliente:6s}, Icone={cor_imagem}")

        # 3. Bloco PROCESS (Simplificado)
        # VIPs têm atendimento 20% mais rápido por prioridade
        fator_velocidade = 0.8 if tipo_cliente == "VIP" else 1.0
        tempo_processo = TEMPO_LAVAGEM_BASE * fator_velocidade
        
        # 4. Bloco RECORD: Tabulando informações
        tempo_saida = tempo_chegada + tempo_processo
        tempo_no_sistema = tempo_saida - tempo_chegada # Intervalo de Tempo
        
        total_tempo_sistema += tempo_no_sistema
        historico_tempos.append(tempo_no_sistema)
        
        if tipo_cliente == "VIP":
            contagem_vip += 1
        else:
            contagem_normal += 1

    # 5. Relatórios Finais (Saída do Bloco RECORD / Reports)
    print("-" * 60)
    print("📊 RELATÓRIO DE ESTATÍSTICAS (RECORD) 📊")
    print(f"✅ Total Processado: {NUM_ENTIDADES}")
    print(f"👑 Clientes VIP: {contagem_vip} | 👥 Clientes Normais: {contagem_normal}")
    print(f"⏱️ Tempo Médio no Sistema: {sum(historico_tempos)/len(historico_tempos):.2f} min")
    print(f"🚀 Tempo Mínimo: {min(historico_tempos):.2f} min | 🐢 Tempo Máximo: {max(historico_tempos):.2f} min")
    
    print("-" * 60)
    print("💡 Insight: O módulo ASSIGN permitiu diferenciar o tratamento (VIP vs Normal),")
    print("   enquanto o RECORD capturou os KPIs para análise de performance.")

if __name__ == "__main__":
    random.seed(42)
    simulacao_com_estatisticas()
