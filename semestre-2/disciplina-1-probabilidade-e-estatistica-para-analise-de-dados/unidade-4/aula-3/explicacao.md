# 📝 Testes de Hipóteses — Z, t de Student e Qui-quadrado

## 💡 O que de fato importa?

1. **Todo teste de hipóteses** parte de duas perguntas: *"os dados mostram algo real?"* (H1) ou *"isso é ruído aleatório?"* (H0). O teste escolhido depende do tipo de dado e do que você sabe sobre a população.
2. **Teste Z** quando você tem amostra grande (n > 30) e conhece a variância da população. **Teste t de Student** quando a amostra é pequena ou a variância é desconhecida. **Qui-quadrado** quando as variáveis são categóricas.
3. **Intervalos de confiança** e testes de hipóteses andam juntos: se o IC de 95% não contém o valor da H0, você rejeita H0 ao nível de significância de 5%.

---

## 🚀 Na prática

### Quando usar cada teste?
| Situação | Teste |
|----------|-------|
| Contínua + n > 30 + variância conhecida | Teste Z |
| Contínua + n < 30 **ou** variância desconhecida | Teste t de Student |
| Variáveis categóricas (associação) | Qui-quadrado |

### Teste Z — impacto de campanha de marketing
```python
from scipy import stats
import numpy as np

media_pop, media_amostra, desvio_pop, n = 0.05, 0.07, 0.02, 50
z = (media_amostra - media_pop) / (desvio_pop / np.sqrt(n))
p = 2 * (1 - stats.norm.cdf(abs(z)))
print(f"Z={z:.2f}, p={p:.2e}")  # Z=7.07, p~0 → rejeita H0
```

### Teste t — comparar duas campanhas
```python
vendas_A = [150, 160, 145, 170, 155, 165, 140, 175, 150, 160]
vendas_B = [180, 175, 165, 160, 170, 185, 175, 180, 165, 170]
t, p = stats.ttest_ind(vendas_A, vendas_B)
print(f"t={t:.3f}, p={p:.4f}")  # p < 0.05 → B vende mais
```

### Qui-quadrado — gênero vs. produto preferido
```python
tabela = [[50, 30], [20, 40]]  # Masc/Fem × Produto A/B
chi2, p, df, _ = stats.chi2_contingency(tabela)
print(f"χ²={chi2:.3f}, p={p:.4f}")  # p < 0.05 → associação existe
```

---

## 🧠 Dica de Ouro

> ⚡ **Teste t de Welch vs. teste t clássico**: por padrão, o `stats.ttest_ind()` do scipy usa Welch (não assume variâncias iguais entre grupos), que é mais seguro e robusto. Use sempre ele — é o equivalente ao `t.test()` do R.
>
> 📊 **Qui-quadrado com frequências pequenas?** Ative a correção de Yates (`correction=True`) ou use o teste exato de Fisher quando alguma célula tem frequência esperada < 5.
