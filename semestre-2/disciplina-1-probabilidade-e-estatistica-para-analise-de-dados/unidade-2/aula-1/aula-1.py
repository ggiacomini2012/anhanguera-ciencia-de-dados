import statistics

# 📊 1. Definindo o nosso conjunto de dados (Notas de alunos)
# Imagine que estas são as notas de um pequeno grupo de estudos.
notas = [70, 80, 90, 100, 85, 70]

print(f"--- 📝 DADOS DA AULA: {notas} ---\n")

# --- MÉDIA (O Equilíbrio) ---
# Soma de tudo dividida pela quantidade
media = sum(notas) / len(notas)
# Usando a biblioteca: statistics.mean(notas)
print(f"⚖️ MÉDIA: {media:.2f}")
print("Nota: A média tenta equilibrar todos os valores.\n")

# --- MEDIANA (O Centro) ---
# Primeiro precisamos ordenar: [70, 70, 80, 85, 90, 100]
# Como temos 6 elementos (par), a mediana será a média entre 80 e 85.
mediana = statistics.median(notas)
print(f"📍 MEDIANA: {mediana}")
print("Nota: Mesmo que alguém tirasse 0 ou 1000, o centro mudaria pouco.\n")

# --- MODA (O Popular) ---
# O valor que mais aparece. No nosso caso, o 70.
try:
    moda = statistics.mode(notas)
    print(f"👑 MODA: {moda}")
except statistics.StatisticsError:
    print("👑 MODA: Não há uma moda única (Amodal ou Multimodal).")
print("Nota: A moda indica o valor mais frequente no conjunto.\n")

# --- O EFEITO DO OUTLIER (VALOR EXTREMO) ---
# Vamos adicionar um aluno que tirou uma nota muito baixa (30)
notas_com_outlier = [70, 80, 90, 100, 85, 30]
nova_media = statistics.mean(notas_com_outlier)
nova_mediana = statistics.median(notas_com_outlier)

print("⚠️ ADICIONANDO UM OUTLIER (Nota 30):")
print(f"📉 Nova Média: {nova_media:.2f} (Caiu bastante!)")
print(f"📍 Nova Mediana: {nova_mediana:.2f} (Permaneceu estável!)")