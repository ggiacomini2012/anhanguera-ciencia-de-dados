# S2-D5-U3-A2 | Problema de Transporte — Método Canto Noroeste + Teste de Otimalidade
# Disciplina: Otimização e Pesquisa Operacional
# Resolve o problema clássico de transporte com 3 fontes e 4 destinos

from scipy.optimize import linprog

print("=" * 60)
print("🚚 PROBLEMA DE TRANSPORTE — S2-D5-U3-A2")
print("=" * 60)

# ── Dados do problema ──────────────────────────────────────────
fornecimento = [10_000, 15_000, 5_000]
demanda      = [8_000, 4_000, 7_000, 11_000]
custos = [
    [13, 8,  9, 12],
    [12, 9, 10, 14],
    [ 8, 8,  9,  6],
]

print("\n📦 Fornecimento:")
for i, f in enumerate(fornecimento, 1):
    print(f"   F{i} = {f:,} unidades")

print("\n🏪 Demanda:")
for j, d in enumerate(demanda, 1):
    print(f"   D{j} = {d:,} unidades")

equilibrado = sum(fornecimento) == sum(demanda)
print(f"\n⚖️  Total: {sum(fornecimento):,} | {'✅ EQUILIBRADO' if equilibrado else '❌ DESEQUILIBRADO'}")

# ── Método do Canto Noroeste (solução inicial) ─────────────────
print("\n" + "=" * 60)
print("📐 MÉTODO DO CANTO NOROESTE — Solução Inicial")
print("=" * 60)

n_f, n_d = len(fornecimento), len(demanda)
oferta = fornecimento.copy()
demanda_r = demanda.copy()
sol = [[0] * n_d for _ in range(n_f)]

i, j = 0, 0
while i < n_f and j < n_d:
    qtd = min(oferta[i], demanda_r[j])
    sol[i][j] = qtd
    oferta[i] -= qtd
    demanda_r[j] -= qtd
    if oferta[i] == 0:
        i += 1
    else:
        j += 1

header = "        " + "  ".join(f"  D{j+1}  " for j in range(n_d)) + "  Fornec."
print(f"\n{header}")
for i in range(n_f):
    linha = f"   F{i+1}  " + "  ".join(f"{sol[i][j]:6,}" for j in range(n_d))
    print(linha + f"  {fornecimento[i]:,}")
print("   Dem. " + "  ".join(f"{demanda[j]:6,}" for j in range(n_d)))

custo_ini = sum(custos[i][j] * sol[i][j] for i in range(n_f) for j in range(n_d))
print(f"\n💰 Custo da solução inicial (Canto Noroeste): R$ {custo_ini:,.0f}")

# ── Solução ótima via scipy.linprog ────────────────────────────
print("\n" + "=" * 60)
print("🔍 SOLUÇÃO ÓTIMA — Programação Linear (scipy HiGHS)")
print("=" * 60)

c = [custos[i][j] for i in range(n_f) for j in range(n_d)]
A_eq, b_eq = [], []

for i in range(n_f):
    row = [0] * (n_f * n_d)
    for j in range(n_d):
        row[i * n_d + j] = 1
    A_eq.append(row); b_eq.append(fornecimento[i])

for j in range(n_d):
    row = [0] * (n_f * n_d)
    for i in range(n_f):
        row[i * n_d + j] = 1
    A_eq.append(row); b_eq.append(demanda[j])

res = linprog(c, A_eq=A_eq, b_eq=b_eq, bounds=[(0, None)] * (n_f * n_d), method='highs')

if res.success:
    x = res.x.reshape(n_f, n_d)
    print(f"\n{header}")
    for i in range(n_f):
        linha = f"   F{i+1}  " + "  ".join(f"{x[i][j]:6,.0f}" for j in range(n_d))
        print(linha + f"  {fornecimento[i]:,}")
    print("   Dem. " + "  ".join(f"{demanda[j]:6,}" for j in range(n_d)))
    print(f"\n🏆 Custo mínimo ótimo:    R$ {res.fun:,.0f}")
    print(f"📉 Economia vs. inicial: R$ {custo_ini - res.fun:,.0f}")

# ── Exercício da aula (3x3) ────────────────────────────────────
print("\n" + "=" * 60)
print("📝 EXERCÍCIO — Fornecedores de Peças (3 origens x 3 destinos)")
print("=" * 60)

origens = ["Osasco", "Campinas", "S.Sebastião"]
destinos = ["São Paulo", "Rio de Janeiro", "Curitiba"]
forn_ex = [100, 140, 160]
dem_ex  = [120, 130, 150]
custos_ex = [[12, 22, 30], [18, 24, 32], [22, 15, 34]]

c_ex = [custos_ex[i][j] for i in range(3) for j in range(3)]
A_ex, b_ex = [], []
for i in range(3):
    row = [0]*9
    for j in range(3): row[i*3+j] = 1
    A_ex.append(row); b_ex.append(forn_ex[i])
for j in range(3):
    row = [0]*9
    for i in range(3): row[i*3+j] = 1
    A_ex.append(row); b_ex.append(dem_ex[j])

res_ex = linprog(c_ex, A_eq=A_ex, b_eq=b_ex, bounds=[(0,None)]*9, method='highs')

if res_ex.success:
    x_ex = res_ex.x.reshape(3, 3)
    print(f"\n   {'Origem':<15}" + "".join(f"{d:<17}" for d in destinos) + "Fornec.")
    for i in range(3):
        linha = f"   {origens[i]:<15}" + "".join(f"{x_ex[i][j]:>10,.0f}       " for j in range(3))
        print(linha + str(forn_ex[i]))
    print(f"\n🏆 Custo mínimo exercício: R$ {res_ex.fun:,.0f}")

print("\n" + "=" * 60)
print("💡 INSIGHT PRÁTICO:")
print("   O Problema de Transporte é PL com estrutura especial.")
print("   Canto Noroeste → ponto de partida rápido (sem custos).")
print("   Teste de otimalidade (multiplicadores u/v) detecta se")
print("   ainda há rotas com custo negativo para melhorar.")
print("   Na prática: scipy/PuLP resolvem em milissegundos. 🚀")
print("=" * 60)
