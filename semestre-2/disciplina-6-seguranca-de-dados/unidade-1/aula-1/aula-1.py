# Aula 1 - Pesquisa Operacional: Seu Contexto Histórico e o Processo de Modelagem
# s2 - d5 - u1 - a1
# Disciplina: Otimização e Pesquisa Operacional

import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

print("=" * 55)
print("   🔍 PESQUISA OPERACIONAL - SIMULADOR DE DECISÃO")
print("=" * 55)

# -----------------------------------------------------------
# CONTEXTO: Uma indústria de eletrônicos precisa alocar seu
# orçamento de produção entre 3 linhas de produtos.
# O objetivo da PO: maximizar o lucro dentro das restrições.
# -----------------------------------------------------------

# Dados dos produtos
produtos = {
    "Smartphone": {
        "lucro_unitario": 350,       # R$ de lucro por unidade
        "horas_maquina": 2.5,        # horas de máquina por unidade
        "custo_material": 400,       # R$ em material por unidade
    },
    "Tablet": {
        "lucro_unitario": 500,
        "horas_maquina": 4.0,
        "custo_material": 600,
    },
    "Notebook": {
        "lucro_unitario": 800,
        "horas_maquina": 6.0,
        "custo_material": 900,
    },
}

# Restrições da fábrica
horas_maquina_disponiveis = 120   # horas/semana
orcamento_material = 25000        # R$ disponíveis para materiais

print("\n📊 ANÁLISE DE OPÇÕES DE PRODUÇÃO:")
print("-" * 55)
print(f"{'Produto':<12} {'Lucro/un':>10} {'Hrs/un':>8} {'Custo/un':>10} {'Eficiência':>12}")
print("-" * 55)

resultados = []
for nome, dados in produtos.items():
    # Eficiência = Lucro por hora de máquina (quanto cada hora GERA)
    eficiencia = dados["lucro_unitario"] / dados["horas_maquina"]

    # Quantas unidades podemos fazer MAX pelo tempo disponível?
    max_por_tempo = int(horas_maquina_disponiveis / dados["horas_maquina"])

    # Quantas podemos fazer MAX pelo orçamento?
    max_por_orcamento = int(orcamento_material / dados["custo_material"])

    # A restrição mais restritiva define o limite real (gargalo)
    max_producao = min(max_por_tempo, max_por_orcamento)
    lucro_max = max_producao * dados["lucro_unitario"]

    resultados.append({
        "nome": nome,
        "eficiencia": eficiencia,
        "max_producao": max_producao,
        "lucro_max": lucro_max,
        "gargalo": "⏱️ Tempo" if max_por_tempo < max_por_orcamento else "💰 Orçamento",
    })

    print(f"{nome:<12} R${dados['lucro_unitario']:>7} {dados['horas_maquina']:>7}h R${dados['custo_material']:>7} R${eficiencia:>8.2f}/h")

# Ranking por eficiência (lógica greedy simples — base do pensamento PO)
resultados_ordenados = sorted(resultados, key=lambda x: x["eficiencia"], reverse=True)

print("\n🏆 RANKING DE EFICIÊNCIA (Lucro por Hora de Máquina):")
print("-" * 55)
for i, r in enumerate(resultados_ordenados, 1):
    print(f"  {i}° lugar: {r['nome']:<12} | Gargalo: {r['gargalo']} | Lucro máx: R$ {r['lucro_max']:,.0f}")

print("\n📌 INSIGHT DE PESQUISA OPERACIONAL:")
print("-" * 55)
melhor = resultados_ordenados[0]
print(f"  O produto mais EFICIENTE é o '{melhor['nome']}'.")
print(f"  Cada hora de máquina gasta nele gera maior retorno em lucro.")
print(f"  Num cenário com recursos escassos, PO recomendaria priorizar este")
print(f"  produto — a não ser que outras restrições (contratos, demanda)")
print(f"  imponham limites adicionais. Isso é o PROCESSO DE MODELAGEM na prática.")

print("\n📚 LINHA DO TEMPO DO SIMPLEX:")
print("-" * 55)
timeline = [
    (1947, "George Dantzig inventa o Algoritmo Simplex no Pentágono"),
    (1952, "1ª aplicação civil: otimização na produção de gasolina"),
    (1954, "1° software comercial de Prog. Linear (Rand Corporation)"),
    (1973, "Nobel para Leontief (modelo que inspirou Dantzig)"),
    (1975, "Nobel para Kantorovich e Koopmans (alocação ótima)"),
]
for ano, evento in timeline:
    print(f"  {ano} → {evento}")

print("\n" + "=" * 55)
print("  ✅ PO: Intuição + Modelo = Decisão Robusta")
print("=" * 55)
