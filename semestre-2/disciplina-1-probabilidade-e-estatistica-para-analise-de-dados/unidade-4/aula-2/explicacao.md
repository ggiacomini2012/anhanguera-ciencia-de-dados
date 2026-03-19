# 📝 Significância Estatística — Métodos Fisher e Neyman-Pearson

## 💡 O que de fato importa?

1. **Significância estatística** responde a pergunta: *"esse resultado é real ou só coincidência?"* — ela mede a probabilidade de você ter observado aquilo por puro acaso.
2. **Método de Fisher** usa o **valor p**: se `p < 0,05`, o resultado é improvável sob a hipótese nula (H0) e você a rejeita. Simples assim.
3. **Método de Neyman-Pearson** vai além e exige que você controle dois tipos de erro antes de decidir: **Erro Tipo I (α)** — rejeitar H0 quando ela era verdadeira (falso positivo) — e **Erro Tipo II (β)** — deixar passar H0 quando ela era falsa (falso negativo).

---

## 🚀 Na prática

### Fisher — "p menor que 0,05? Rejeita!"
```python
from scipy import stats
import numpy as np

grupo_A = np.random.normal(5.5, 1, 100)
grupo_B = np.random.normal(5.0, 1, 100)

_, p = stats.ttest_ind(grupo_A, grupo_B)
print(f"Valor p: {p:.4f}")  # Ex: 0.0000 → rejeita H0
```
> Se `p < 0.05`: os grupos são estatisticamente diferentes.

### Neyman-Pearson — "compara com o valor crítico"
```python
alpha = 0.05
valor_critico = stats.t.ppf(1 - alpha / 2, df=198)  # ~1.97

t_stat, _ = stats.ttest_ind(grupo_A, grupo_B)

if abs(t_stat) > valor_critico:
    print("Rejeita H0 — decisão formal com controle de erro Tipo I")
```
> Aqui você planeja o experimento controlando **α** (falso positivo) e **β** (falso negativo).

---

## 🧠 Dica de Ouro

> O **valor p não é a probabilidade de H0 ser verdadeira** — é a probabilidade de *ver esses dados (ou algo mais extremo) assumindo que H0 já é verdadeira*. Parece sutil, mas essa confusão derruba muita gente em prova!
>
> Resumão dos erros:
> | Situação real \ Decisão | Rejeita H0 | Não rejeita H0 |
> |-------------------------|------------|----------------|
> | H0 verdadeira           | ❌ Erro Tipo I (α) | ✅ Correto |
> | H0 falsa                | ✅ Correto (Poder) | ❌ Erro Tipo II (β) |
