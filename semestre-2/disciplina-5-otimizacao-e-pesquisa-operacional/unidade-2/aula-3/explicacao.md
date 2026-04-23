# Programação Linear: O Método Simplex (S2-D5-U2-A3)

O método Simplex, criado por George B. Dantzig em 1947, é a "ferramenta definitiva" para resolver problemas de Programação Linear (PL), especialmente quando temos mais de 2 ou 3 variáveis, onde o método gráfico se torna impossível.

## 🧭 Analogia: O Explorador de Vértices
Imagine que a região de soluções possíveis é um polígono (como uma sala com várias quinas). O método gráfico tenta olhar a sala inteira de cima. O **Simplex** é como um explorador que:
1. Começa em uma quina (geralmente a origem).
2. Olha para as quinas vizinhas e pergunta: "Se eu for para lá, meu lucro aumenta?".
3. Caminha para a melhor quina vizinha.
4. Repete o processo até que todas as quinas vizinhas sejam piores. Quando isso acontece, ele encontrou o pico (ponto ótimo).

---

## 🛠️ Conceitos Fundamentais

### 1. Variáveis de Folga (Slack)
Na vida real, nem sempre usamos 100% dos recursos. As variáveis de folga transformam **inequações** ($\le$) em **equações** ($=$).
- Se a restrição é $x_1 + x_2 \le 6$, adicionamos $x_3$ para que vire $x_1 + x_2 + x_3 = 6$.
- $x_3$ representa o que "sobrou" do recurso.

### 2. Variáveis Básicas vs. Não Básicas
- **Não Básicas (VNB):** Variáveis que "estão de fora" da solução atual (valor = 0). No início, costumam ser as variáveis de decisão.
- **Básicas (VB):** Variáveis que compõem a solução atual. No início, costumam ser as variáveis de folga (já que não produzimos nada, a folga é total).

### 3. A Forma Tabular (Tableau)
É o "painel de controle" do Simplex. Através de operações matemáticas (Eliminação de Gauss-Jordan), trocamos quem entra e quem sai da base para melhorar o valor de $Z$.

---

## 📈 Exemplo Prático da Aula

**Problema:**
- Max $Z = 3x_1 + 2x_2$
- Sujeito a:
  - $x_1 + x_2 \le 6$
  - $5x_1 + 2x_2 \le 20$

**Passos do Simplex:**
1. **Início:** Partimos de $(0, 0)$. Lucro $Z = 0$.
2. **Iteração 1:** $x_1$ entra na base (é quem dá mais lucro por unidade). $x_4$ sai.
3. **Iteração 2:** $x_2$ entra na base para melhorar ainda mais. $x_3$ sai.
4. **Fim:** Chegamos ao ponto ótimo onde $x_1 = 2,67$ e $x_2 = 3,33$, com lucro total $Z = 14,67$.

---

> [!TIP]
> O Simplex é eficiente porque ele não testa todos os pontos dentro da área, apenas os vértices (quinas), pois matematicamente o valor ótimo **sempre** estará em um vértice ou em uma aresta entre dois vértices ótimos.

---
*Referência: Fávero e Belfiore (2013); Hillier e Lieberman (2013).*
