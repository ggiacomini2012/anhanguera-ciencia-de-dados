# 🚚 Problema de Transporte — Como Distribuir com o Menor Custo?

## 🎯 O que é o Problema de Transporte?

Imagina que você trabalha numa empresa de bebidas. Você tem **3 fábricas** espalhadas pelo Brasil e **4 armazéns** em cidades diferentes. Cada fábrica produz uma quantidade fixa por mês, e cada armazém precisa de uma quantidade específica. O desafio: **como enviar os produtos gastando o mínimo possível em frete?**

Isso é exatamente o **Problema de Transporte** — um tipo especial de Programação Linear onde você quer minimizar o custo total de distribuição, respeitando a capacidade de quem produz e a necessidade de quem consome.

---

## 📦 Ingredientes do Problema

Todo problema de transporte tem três elementos:

| Elemento | O que é | Exemplo |
|---|---|---|
| **Fontes (origens)** | Quem fornece | F1=10.000, F2=15.000, F3=5.000 unidades |
| **Destinos** | Quem consome | D1=8.000, D2=4.000, D3=7.000, D4=11.000 |
| **Custos** | Preço por unidade transportada de i para j | R$13/un de F1→D1 |

A condição de **equilíbrio** é fundamental: `soma do fornecimento = soma da demanda`. Se não estiver equilibrado, cria-se uma fonte ou destino fictício com custo zero.

---

## 🗺️ Como Montar o Modelo Matemático

As **variáveis de decisão** são simples: `xij` = quantidade transportada da fonte `i` para o destino `j`.

A **função objetivo** minimiza o custo total:
```
Min Z = Σ Cij * xij
```

As **restrições** garantem que:
- Cada fonte não ultrapasse sua capacidade: `x11 + x12 + x13 + x14 = 10.000`
- Cada destino tenha sua demanda atendida: `x11 + x21 + x31 = 8.000`
- Todas as quantidades sejam não-negativas: `xij ≥ 0`

---

## 📐 Método do Canto Noroeste — O Ponto de Partida

O Canto Noroeste é como preencher uma tabela começando do **canto superior esquerdo** (noroeste) e indo em zigue-zague:

1. Aloque o máximo possível na célula (F1, D1)
2. Se a fonte esgotou → desça uma linha
3. Se o destino foi atendido → avance uma coluna
4. Repita até preencher tudo

**Analogia:** é como servir comida num buffet — você começa pela primeira fila, serve até acabar o prato ou o cliente estar satisfeito, e vai para o próximo.

⚠️ O Canto Noroeste **ignora os custos** — serve só para ter uma solução inicial válida, não necessariamente barata. No exemplo da aula, o custo inicial foi **R$ 328.000**.

---

## 🔍 Teste de Otimalidade — Dá para Melhorar?

Depois da solução inicial, usamos o **método dos multiplicadores** (variáveis u e v) para checar se existe alguma rota não usada que reduziria o custo:

- Para cada rota **em uso**: `Cij - ui - vj = 0`
- Para cada rota **fora de uso**: calcula `Pij = Cij - ui - vj`

Se todos os `Pij ≥ 0` → solução ótima! ✅  
Se algum `Pij < 0` → ainda dá para melhorar. Entra a variável com maior valor negativo.

**Analogia:** é como revisar sua playlist de músicas. Você tem uma ordem tocando. O teste pergunta: "existe alguma música que, se eu colocar agora, melhora o conjunto?" Se sim, você troca. Repete até não ter mais troca que melhore.

---

## 🔄 Circuito de Compensação

Quando uma nova variável entra na base, você precisa ajustar as outras para não violar as restrições. Isso é feito pelo **circuito de compensação**: um caminho em "L" ou "U" que adiciona e subtrai `q` alternadamente até fechar o equilíbrio.

O valor de `q` é o **menor dos valores nos vértices negativos** do circuito — isso garante que nenhuma variável fique negativa.

---

## 💻 Na Prática com Python

Na vida real, ninguém resolve isso à mão para problemas grandes. O `scipy.optimize.linprog` resolve em milissegundos usando o algoritmo HiGHS (variante do Simplex):

```python
from scipy.optimize import linprog

# Custos como vetor (linha por linha da matriz)
c = [13, 8, 9, 12, 12, 9, 10, 14, 8, 8, 9, 6]

# Restrições de igualdade (fornecimento + demanda)
resultado = linprog(c, A_eq=A_eq, b_eq=b_eq, bounds=[(0, None)]*12)
print(resultado.fun)  # Custo mínimo
```

---

## 🎓 Conclusão — Por que isso importa em Data Science?

O Problema de Transporte aparece em várias situações reais:

- 🛒 **E-commerce:** qual CD (centro de distribuição) atende cada pedido com menor frete?
- 🏥 **Saúde pública:** como distribuir vacinas entre municípios minimizando custo logístico?
- ☁️ **Cloud computing:** qual servidor processa qual workload para minimizar latência e custo?
- 📦 **Supply chain:** otimizar fluxo de estoque entre fábricas, atacadistas e varejistas

A estrutura especial do problema (matriz de oferta/demanda) permite resolver de forma mais eficiente que o Simplex geral — e entender isso te diferencia na hora de modelar problemas reais de otimização logística.
