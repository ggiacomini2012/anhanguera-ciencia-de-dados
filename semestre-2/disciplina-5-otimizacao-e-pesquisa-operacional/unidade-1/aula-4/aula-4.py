"""
S2-D5-U1-A4: Ferramentas da Pesquisa Operacional
Este código exemplifica a aplicação de diferentes ferramentas de PO para resolver
problemas reais, diferenciando modelos Determinísticos de Estocásticos.
"""

import random
import time
import sys

# Garante que o terminal aceite emojis no Windows
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding='utf-8')

def separador(titulo):
    print(f"\n{'='*10} {titulo} {'='*10}")

def modelo_deterministico():
    """
    Exemplo de Programação Linear (Determinística)
    Problema: Maximizar lucro na venda de dois produtos com estoque fixo.
    """
    separador("📉 MODELO DETERMINÍSTICO (Programação Linear)")
    
    # Variáveis conhecidas (Constantes)
    lucro_produto_a = 50
    lucro_produto_b = 30
    estoque_maximo = 100
    
    print(f"📦 Estoque disponível: {estoque_maximo}")
    print(f"💰 Lucro A: R${lucro_produto_a} | Lucro B: R${lucro_produto_b}")
    
    # Lógica Determinística: Escolher o de maior lucro até esgotar o estoque
    qtd_a = estoque_maximo
    lucro_total = qtd_a * lucro_produto_a
    
    print(f"🎯 Decisão Ótima: Produzir {qtd_a} unidades do Produto A.")
    print(f"✅ Lucro Total Garantido: R${lucro_total}")
    print("💡 Nota: Como os dados são fixos e conhecidos, a solução é exata.")

def modelo_estocastico():
    """
    Exemplo de Teoria das Filas (Estocástico)
    Problema: Simular o tempo de espera em um caixa com chegada aleatória de clientes.
    """
    separador("🎲 MODELO ESTOCÁSTICO (Teoria das Filas)")
    
    clientes = ["Cliente 1", "Cliente 2", "Cliente 3", "Cliente 4"]
    tempo_total_espera = 0
    
    print("⏳ Iniciando simulação de fila...")
    
    for cliente in clientes:
        # Variável aleatória (Tempo de atendimento varia entre 1 e 5 minutos)
        tempo_atendimento = random.randint(1, 5)
        print(f"👤 {cliente} sendo atendido... (Levou {tempo_atendimento} min)")
        tempo_total_espera += tempo_atendimento
        time.sleep(0.3)
        
    media_espera = tempo_total_espera / len(clientes)
    print(f"\n📊 Resultado da Simulação:")
    print(f"⏱️ Tempo total: {tempo_total_espera} min")
    print(f"平均 Média de espera: {media_espera:.2f} min/cliente")
    print("💡 Nota: O resultado pode variar a cada execução (Aleatoriedade).")

def metaheuristica():
    """
    Exemplo de Heurística (Busca de Solução Aceitável)
    Problema: Encontrar uma boa rota entre cidades (Simplificado).
    """
    separador("🧠 OUTRAS TÉCNICAS (Heurística)")
    
    print("🗺️ Buscando 'Caminho mais curto' em uma rede complexa...")
    time.sleep(0.5)
    
    # Simula uma busca que não garante o ótimo, mas é rápida
    print("🚀 Heurística 'Vizinho mais Próximo' aplicada!")
    print("✅ Rota encontrada com sucesso (Solução 'Boa o suficiente' para tempo real).")
    print("💡 Nota: Usado quando o problema é complexo demais para métodos exatos.")

def main():
    print("🛠️  CAIXA DE FERRAMENTAS DA PESQUISA OPERACIONAL  🛠️")
    
    modelo_deterministico()
    modelo_estocastico()
    metaheuristica()
    
    print("\n" + "="*40)
    print("🚀 INSIGHT DATA SCIENCE:")
    print("A escolha da ferramenta depende da incerteza dos dados.")
    print("Dados fixos? Use Determinísticos. Incerteza/Variação? Vá de Estocásticos!")
    print("="*40)

if __name__ == "__main__":
    main()