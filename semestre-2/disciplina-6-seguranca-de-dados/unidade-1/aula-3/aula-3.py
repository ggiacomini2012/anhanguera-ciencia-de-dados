# Aula 3 - Modelagem para Tomada de Decisão em Pesquisa Operacional
# s2 - d5 - u1 - a3
# Disciplina: Otimização e Pesquisa Operacional

import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

print("=" * 60)
print("   🧠 MODELAGEM PARA TOMADA DE DECISÃO — PO")
print("=" * 60)

# -----------------------------------------------------------
# CONTEXTO: Uma fábrica de móveis produz Mesas e Cadeiras.
# Precisamos construir um modelo matemático de decisão para
# maximizar o lucro respeitando as restrições de produção.
# -----------------------------------------------------------

# ============================================================
# 1. VARIÁVEIS DE DECISÃO
# ============================================================
print("\n📌 1. VARIÁVEIS DE DECISÃO (o que queremos determinar):")
print("-" * 60)
print("  x1 = quantidade de Mesas a produzir (variável contínua)")
print("  x2 = quantidade de Cadeiras a produzir (variável contínua)")
print("  Restrição de não-negatividade: x1 >= 0, x2 >= 0")

# ============================================================
# 2. PARÂMETROS DO PROBLEMA (valores conhecidos)
# ============================================================
lucro_mesa      = 300   # R$ lucro por mesa
lucro_cadeira   = 150   # R$ lucro por cadeira

horas_mesa      = 4     # horas de mão-de-obra por mesa
horas_cadeira   = 2     # horas de mão-de-obra por cadeira
horas_total     = 120   # horas disponíveis na semana

madeira_mesa    = 6     # kg de madeira por mesa
madeira_cadeira = 3     # kg de madeira por cadeira
madeira_total   = 200   # kg de madeira disponíveis

print("\n📦 2. PARÂMETROS (valores conhecidos do problema):")
print("-" * 60)
print(f"  Lucro por Mesa:     R$ {lucro_mesa}")
print(f"  Lucro por Cadeira:  R$ {lucro_cadeira}")
print(f"  Horas disponíveis:  {horas_total}h/semana")
print(f"  Madeira disponível: {madeira_total} kg")

# ============================================================
# 3. FUNÇÃO OBJETIVO (o que queremos maximizar)
# ============================================================
print("\n🎯 3. FUNÇÃO OBJETIVO:")
print("-" * 60)
print("  Maximizar Z = 300·x1 + 150·x2")
print("  (maximizar o lucro total da produção semanal)")

# ============================================================
# 4. RESTRIÇÕES
# ============================================================
print("\n🔒 4. RESTRIÇÕES DO MODELO:")
print("-" * 60)
print("  [Mão-de-obra]  4·x1 + 2·x2 <= 120")
print("  [Madeira]      6·x1 + 3·x2 <= 200")
print("  [Não-negat.]   x1 >= 0, x2 >= 0")

# ============================================================
# 5. SIMULAÇÃO DE SOLUÇÕES CANDIDATAS
# ============================================================
print("\n🔍 5. AVALIANDO COMBINAÇÕES DE PRODUÇÃO:")
print("-" * 60)
print(f"  {'Mesas':>6} {'Cadeiras':>9} {'Lucro':>12} {'Mão-obra':>10} {'Madeira':>9} {'Viável?':>8}")
print("-" * 60)

melhores = []
for x1 in range(0, 35, 5):       # mesas: 0 a 30
    for x2 in range(0, 65, 5):   # cadeiras: 0 a 60
        uso_horas   = horas_mesa * x1 + horas_cadeira * x2
        uso_madeira = madeira_mesa * x1 + madeira_cadeira * x2
        viavel = uso_horas <= horas_total and uso_madeira <= madeira_total
        lucro = lucro_mesa * x1 + lucro_cadeira * x2
        if viavel:
            melhores.append((lucro, x1, x2, uso_horas, uso_madeira))

melhores.sort(reverse=True)
for lucro, x1, x2, h, m in melhores[:8]:
    print(f"  {x1:>6} {x2:>9} R${lucro:>9,.0f} {h:>8}h {m:>8}kg    ✅")

# ============================================================
# 6. SOLUÇÃO ÓTIMA
# ============================================================
lucro_opt, x1_opt, x2_opt, h_opt, m_opt = melhores[0]
print("\n🏆 6. SOLUÇÃO ÓTIMA (maior lucro viável):")
print("-" * 60)
print(f"  Mesas a produzir:    {x1_opt} unidades")
print(f"  Cadeiras a produzir: {x2_opt} unidades")
print(f"  💰 Lucro máximo:     R$ {lucro_opt:,.0f}")
print(f"  ⏱️  Horas utilizadas:  {h_opt}h de {horas_total}h")
print(f"  🪵  Madeira utilizada: {m_opt}kg de {madeira_total}kg")

# ============================================================
# 7. TIPOS DE VARIÁVEIS — COMPARATIVO
# ============================================================
print("\n📐 7. TIPOS DE VARIÁVEIS DE DECISÃO:")
print("-" * 60)
tipos = [
    ("Contínua",  "Qtd. de litros de combustível a comprar",   "Qualquer valor real >= 0"),
    ("Discreta",  "Nº de funcionários por turno",              "Inteiro >= 0"),
    ("Binária",   "Abrir ou não uma nova filial",              "0 (não) ou 1 (sim)"),
]
for tipo, exemplo, dominio in tipos:
    print(f"  🔹 {tipo:<10} | Ex: {exemplo}")
    print(f"             | Domínio: {dominio}")

# ============================================================
# 8. FASES DA PESQUISA OPERACIONAL
# ============================================================
print("\n🔄 8. FASES DO ESTUDO EM PESQUISA OPERACIONAL:")
print("-" * 60)
fases = [
    ("a", "Definição do Problema",        "Objetivos, limitações e relações com outros sistemas"),
    ("b", "Construção do Modelo Matem.",  "Equações da função objetivo e restrições"),
    ("c", "Solução do Modelo",            "Técnicas como Simplex, branch-and-bound"),
    ("d", "Validação do Modelo",          "Verificar se o modelo representa o sistema real"),
    ("e", "Implementação dos Resultados", "Aplicação controlada e monitorada da solução"),
    ("f", "Avaliação Final",              "Confirmar se o objetivo foi alcançado"),
]
for letra, fase, desc in fases:
    print(f"  ({letra}) {fase}")
    print(f"       → {desc}")

print("\n" + "=" * 60)
print("  ✅ Modelo construído: da realidade à decisão ótima!")
print("=" * 60)
