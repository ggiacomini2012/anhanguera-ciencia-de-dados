# 🧠 Aula 3: Modelagem para Tomada de Decisão em Pesquisa Operacional

## 🚀 Introdução: O que é um Modelo?

Imagine que você precisa decidir quantas mesas e cadeiras fabricar essa semana para lucrar o máximo possível, sem gastar mais madeira do que você tem no estoque. Você não precisa testar todas as combinações na prática — você cria um **modelo**.

Um **modelo** é uma representação simplificada do sistema real. Ele não precisa capturar cada detalhe do mundo real, apenas as variáveis e relações que realmente importam para a decisão que você quer tomar.

Na Pesquisa Operacional (PO), modelos são a principal ferramenta para transformar problemas complexos em decisões racionais e quantificáveis.

---

## 🗂️ Tipos de Modelos

Existem três grandes famílias de modelos:

### 🏗️ Modelos Físicos
São representações concretas e tangíveis do objeto real.
- **Exemplos:** maquetes de aviões usadas por engenheiros aeronáuticos, maquetes de prédios usadas por arquitetos.
- São ótimos para visualização, mas difíceis de otimizar matematicamente.

### 🗺️ Modelos Análogos
Usam um meio diferente para representar uma relação do mundo real.
- **Exemplos:** um mapa rodoviário (estradas viram traços no papel), o ponteiro do tanque de gasolina (combustível vira posição numa escala).
- São mais abstratos que os físicos, mas ainda não permitem cálculo direto.

### 📐 Modelos Matemáticos (ou Simbólicos)
São os mais utilizados em gestão e Pesquisa Operacional. As grandezas viram **variáveis** e as relações viram **equações**.
- **Exemplo:** `Lucro = 300·x1 + 150·x2`, onde `x1` e `x2` são quantidades de produtos.
- Permitem otimização, simulação e análise computacional.

> 💡 Modelos matemáticos que incluem variáveis de decisão são chamados de **modelos de decisão**. Eles sempre têm uma variável que mede a performance — o **objetivo**.

---

## 🧩 Os Três Elementos de um Modelo Matemático

Todo modelo de PO é composto por três partes fundamentais:

### 1️⃣ Variáveis de Decisão e Parâmetros

**Variáveis de decisão** são as incógnitas — o que o modelo vai determinar. Existem três tipos:

| Tipo | O que é | Exemplo |
|------|---------|---------|
| **Contínua** | Qualquer valor real não-negativo | Litros de combustível a comprar |
| **Discreta** | Valores inteiros (contagem) | Nº de funcionários por turno |
| **Binária** | 0 ou 1 (sim/não) | Abrir ou não uma nova filial |

**Parâmetros** são os valores já conhecidos do problema (dados fixos):
- Custo por unidade produzida
- Demanda mínima de um produto
- Capacidade máxima da fábrica

### 2️⃣ Função Objetivo

É a equação que mede o que você quer **maximizar** ou **minimizar**:

- **Maximizar:** lucro, receita, utilidade, retorno sobre investimento
- **Minimizar:** custo, risco, tempo, número de funcionários

Exemplo: `Maximizar Z = 300·x1 + 150·x2`

### 3️⃣ Restrições

São as limitações do sistema — equações ou inequações que as variáveis precisam respeitar:

```
4·x1 + 2·x2 <= 120   (limite de horas de mão-de-obra)
6·x1 + 3·x2 <= 200   (limite de matéria-prima disponível)
x1 >= 0, x2 >= 0     (não dá pra produzir quantidade negativa)
```

> 🎯 A solução ótima é o conjunto de valores das variáveis que respeita **todas** as restrições e maximiza (ou minimiza) a função objetivo.

---

## 🔄 As 6 Fases do Estudo em Pesquisa Operacional

Ter um modelo não basta — você precisa de um processo. A PO segue um ciclo estruturado:

```
Sistema Real → Definição → Modelo → Solução → Validação → Implementação → Avaliação
```

### (a) Definição do Problema
Antes de modelar, entenda o problema. Quais são os objetivos? Quais são as limitações técnicas? Como esse sistema se relaciona com outros?

### (b) Construção do Modelo Matemático
Traduza o problema em equações: defina variáveis, parâmetros, função objetivo e restrições.

### (c) Solução do Modelo
Use técnicas de PO para encontrar a solução ótima:
- **Simplex** → programação linear
- **Branch-and-bound** → programação inteira

### (d) Validação do Modelo
O modelo é válido se consegue prever o comportamento real do sistema com precisão aceitável. Se não, volta para a etapa de construção.

### (e) Implementação dos Resultados
Coloque a solução em prática. Monitorar é essencial — mudanças no ambiente real podem exigir revisões no modelo.

### (f) Avaliação Final
O objetivo foi alcançado? Se sim, ótimo. Se não, o ciclo recomeça.

---

## 🌍 Aplicação em Data Science

Em ciência de dados, você vai modelar decisões o tempo todo:

- **Modelos de regressão** → são modelos matemáticos que minimizam o erro (função objetivo = minimizar MSE)
- **Otimização de hiperparâmetros** → variáveis de decisão são os parâmetros do modelo; a função objetivo é a acurácia
- **Alocação de campanhas de marketing** → variáveis binárias (investir ou não em cada canal), função objetivo = maximizar conversão

A lógica é sempre a mesma: **identificar o que se quer otimizar**, **o que se pode controlar** e **quais são os limites**.

---

## ✅ Conclusão

Modelar é simplificar sem perder o essencial. Um bom modelo de decisão:
- Torna explícitos os objetivos de quem decide
- Identifica as variáveis relevantes e suas relações
- Respeita as restrições reais do sistema
- Pode ser resolvido no tempo disponível

Na prática profissional, você raramente vai resolver problemas "na intuição". Vai construir modelos — e a PO te dá o vocabulário e as ferramentas para fazer isso de forma rigorosa e eficiente.
