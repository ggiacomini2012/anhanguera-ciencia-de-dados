# ==============================================================================
# DISCIPLINA: Otimização e Pesquisa Operacional (PO)
# AULA 2: Definição do Problema e Tomada de Decisão
# ==============================================================================

import time

def print_cabecalho(texto):
    print(f"\n{'-'*60}\n📌 {texto.upper()}\n{'-'*60}")

print_cabecalho("Classificador de Decisão PO")

# Vamos construir um simulador simples que ajude a classificar o nível 
# da decisão e nos traga clareza sobre o tipo de problema que temos na mão.

class DecisaoPO:
    def __init__(self, impacto_financeiro, incerteza_percentual, tempo_disponivel_dias):
        """
        Recebe fatores para determinar os riscos e o ecossistema do problema.
        """
        self.impacto_financeiro = impacto_financeiro # Ex: em Reais
        self.incerteza_percentual = incerteza_percentual # 0 a 100
        self.tempo_disponivel_dias = tempo_disponivel_dias
        
    def classificar_hierarquia(self):
        """Avalia quem provavelmente deve tomar essa decisão."""
        if self.impacto_financeiro > 100000 and self.tempo_disponivel_dias > 30:
            return "📈 ESTRATÉGICA (Alta Administração)"
        elif self.impacto_financeiro > 5000:
            return "📊 GERENCIAL (Gestores de Nível Médio)"
        else:
            return "👔 OPERACIONAL (Supervisores / Linha de Frente)"

    def nivel_estruturacao(self):
        """Avalia a estrutura da informação do problema."""
        if self.incerteza_percentual < 10:
            return "✅ Estruturada (Conhecemos bem todos os fatores)"
        elif self.incerteza_percentual < 50:
            return "⚠️ Semiestruturada (Conhecemos parte das tendências)"
        else:
            return "🌪️ Não Estruturada (Muitas pontas soltas / Alto Risco)"

    def simular_escalonamento(self):
        hierarquia = self.classificar_hierarquia()
        estrutura = self.nivel_estruturacao()
        print(f"💰 Impacto Projetado: R$ {self.impacto_financeiro}")
        print(f"⏱️ Tempo Hábil: {self.tempo_disponivel_dias} dias")
        time.sleep(1)
        print(f"\n🧠 VEREDITO DIAGNÓSTICO DO PROBLEMA:")
        print(f"➜ Escopo: {hierarquia}")
        print(f"➜ Dificuldade / Risco: {estrutura}")

# -------------------------------------------------------------
# 🎯 SIMULAÇÃO 1: Decisão Operacional do Dia a Dia 
# (Ex: Trocar o tipo de pó de café da linha de frete da empresa)
# -------------------------------------------------------------
print_cabecalho("Estudo de Caso 1: Troca de Café")
caso1 = DecisaoPO(impacto_financeiro=120, incerteza_percentual=5, tempo_disponivel_dias=2)
caso1.simular_escalonamento()


# -------------------------------------------------------------
# 🎯 SIMULAÇÃO 2: Decisão Estratégica (Mudar a fábrica para SP)
# -------------------------------------------------------------
print_cabecalho("Estudo de Caso 2: Expansão Nacional")
caso2 = DecisaoPO(impacto_financeiro=2000000, incerteza_percentual=60, tempo_disponivel_dias=90)
caso2.simular_escalonamento()

print("\n💡 INSIGHT PRÁTICO:")
print("A Pesquisa Operacional ensina que o primeiro passo NUNCA é usar a matemática cega.")
print("Sem diagnosticar QUEM decide e o GRAU DE INCERTEZA do cenário, qualquer resultado gerado é lixo de dados!")
