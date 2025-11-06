
## 1. O Conceito Fundamental: O Que é um Vetor?

Quando descrevemos o mundo, usamos dois tipos de grandezas:

* **⭐ Grandezas Escalares**
    São aquelas que precisam apenas de um valor (módulo) e uma unidade para serem completamente descritas.
    * **Exemplos:** Temperatura ($25^\circ\text{C}$), Massa ($70 \text{ kg}$), Tempo ($5$ segundos).
    * **Analogia:** É como falar que você comprou 5 maçãs 🍎. O número 5 é suficiente.

* **⚡ Grandezas Vetoriais**
    São aquelas que, além do módulo (o valor), precisam de **direção** e **sentido** para fazerem sentido.
    * **Exemplos:** Força, Velocidade, Aceleração.
    * **Analogia:** É como dar um soco! Você precisa saber o quão forte (módulo), para onde (direção, ex: horizontal) e em que parte do caminho (sentido, ex: para a esquerda).

> 💡 **Metáfora do GPS:** Um escalar diz que você precisa andar $10 \text{ km}$. Um vetor diz que você precisa andar $10 \text{ km}$ para o Norte!

Um vetor é, graficamente, uma flecha que possui:

* **Módulo:** O comprimento da flecha ($|\vec{A}|$).
* **Direção:** A linha sobre a qual o vetor age (ex: horizontal, vertical, $45^\circ$).
* **Sentido:** A orientação da flecha (ex: para cima, para a direita).

## 2. Módulo, Componentes e Direção (Onde o Bicho Pega!)

### 2.1. O Módulo (Tamanho do Vetor)

No plano Cartesiano (2D), se um vetor $\vec{A}$ tem componentes $(A_x, A_y)$, seu módulo é dado pelo famoso Teorema de Pitágoras 🏛️:

$$|\vec{A}| = \sqrt{A_x^2 + A_y^2}$$

### 2.2. Decomposição de Vetores (As Componentes)

Decompor um vetor é como "projetar" sua ação nos eixos $x$ e $y$. Se o vetor $\vec{A}$ forma um ângulo $\theta$ com o eixo $x$ positivo:

* **Componente X (Adjacente):**
    $$A_x = |\vec{A}| \cos(\theta)$$

* **Componente Y (Oposto):**
    $$A_y = |\vec{A}| \sin(\theta)$$

> ⚠️ **ATENÇÃO (Regra de Ouro):** O seu material nos avisa que esta associação ($\cos \rightarrow x$, $\sin \rightarrow y$) só é verdadeira se o ângulo $\theta$ for medido em relação ao eixo $x$. Se o ângulo for medido em relação ao eixo $y$, você deve pensar: qual componente é adjacente (usa $\cos$) e qual é oposta (usa $\sin$) ao ângulo? Não decore, compreenda o triângulo! 🧠

### 2.3. A Direção (O Ângulo)

A direção (ângulo $\theta$) do vetor é dada pela função tangente inversa (arco tangente) da razão entre as componentes $y$ e $x$:

$$\theta = \arctan\left(\frac{A_y}{A_x}\right)$$

> 🚨 **Cuidado com a Calculadora:** O seu material também nos alerta que a função $\arctan$ geralmente retorna ângulos entre $-90^\circ$ e $+90^\circ$ ($1^\circ$ e $4^\circ$ quadrantes).
>
> * Se o seu vetor estiver no **2º ou 3º Quadrante** (onde $A_x$ é negativo), você precisa **somar $180^\circ$** ao resultado da calculadora!

---

## 3. As Operações com Vetores (Adição e Subtração)

A grande diferença entre vetores e escalares reside nas suas operações.

### 3.1. Adição (Soma de Vetores)

**Regra:** $\vec{A} + \vec{B} = \vec{C}$ é diferente de $A + B = C$! A soma vetorial deve ser feita com cuidado.

* **Método Geométrico (Gráfico):**
    1.  **Regra do Paralelogramo:** Os vetores $\vec{A}$ e $\vec{B}$ partem do mesmo ponto. O vetor soma $\vec{C}$ é a diagonal do paralelogramo formado.
    2.  **Regra do Polígono (Ponta-a-Cauda):** Coloque a cauda de $\vec{B}$ na ponta de $\vec{A}$. O vetor soma $\vec{C}$ vai da cauda de $\vec{A}$ até a ponta de $\vec{B}$.

* **Método Algébrico (Componentes): O mais seguro e preciso!**
    1.  Decomponha todos os vetores nas suas componentes $x$ e $y$.
    2.  Some as componentes separadamente:
        $$C_x = A_x + B_x$$
        $$C_y = A_y + B_y$$
    3.  A resultante $\vec{C}$ é $(C_x, C_y)$. Calcule o módulo e a direção de $\vec{C}$ usando as fórmulas da Seção 2.

### 3.2. Subtração e Multiplicação por Escalar

* **Subtração:** Subtrair $\vec{B}$ de $\vec{A}$ é o mesmo que somar $\vec{A}$ com o vetor oposto a $\vec{B}$ (que tem o mesmo módulo e direção de $\vec{B}$, mas sentido contrário).
    $$\vec{A} - \vec{B} = \vec{A} + (-\vec{B})$$

* **Multiplicação por Escalar:** Multiplicar um vetor $\vec{A}$ por um escalar $k$ resulta em um novo vetor $k\vec{A}$:
    * **Módulo:** $|k\vec{A}| = |k| |\vec{A}|$
    * **Direção:** Mantida.
    * **Sentido:** Mantido se $k>0$, Invertido se $k<0$.

## 4. Aplicação Prática: O Semáforo em Equilíbrio (Estática)

Vamos aplicar tudo o que aprendemos no problema do semáforo, que é um exemplo clássico de equilíbrio de forças (Primeira Lei de Newton: $\vec{F}_r = 0$).

### 4.1. Análise do Problema

* Um semáforo de peso $F_g = 122 \text{ N}$ está suspenso por três cabos.
* Cabos superiores: $\theta_1 = 37,0^\circ$ e $\theta_2 = 53,0^\circ$ (em relação à horizontal).
* Limite de Tensão (Cabo 1 e 2): $T_{max} = 100 \text{ N}$.
* **Pergunta:** O semáforo permanecerá pendurado (os cabos aguentam)?

### 4.2. Diagrama de Corpo Livre e Equilíbrio

No nó que une os três cabos (o ponto de aplicação das forças), temos:

* **Força Peso ($\vec{F}_g$):** Ação do cabo vertical, $T_3 = F_g = 122 \text{ N}$, aponta para baixo (eixo $-y$).
* **Tração 1 ($\vec{T}_1$):** Cabo esquerdo.
* **Tração 2 ($\vec{T}_2$):** Cabo direito.

O sistema está em Equilíbrio: A força resultante é zero ($\vec{F}_r = 0$).

$$\sum \vec{F}_x = 0 \quad \text{e} \quad \sum \vec{F}_y = 0$$

### 4.3. Decomposição das Trações

* **Vetor $\vec{T}_1$:** (Aponta para o quadrante 2)
    * $T_{1x} = -T_1 \cos(\theta_1)$ (Negativo pois aponta para a esquerda)
    * $T_{1y} = T_1 \sin(\theta_1)$
* **Vetor $\vec{T}_2$:** (Aponta para o quadrante 1)
    * $T_{2x} = T_2 \cos(\theta_2)$
    * $T_{2y} = T_2 \sin(\theta_2)$
* **Vetor $\vec{T}_3$ ($\vec{F}_g$):** (Apenas componente $y$)
    * $T_{3x} = 0$
    * $T_{3y} = -F_g$ (Negativo pois aponta para baixo)

### 4.4. Equações de Equilíbrio

1.  **Soma das Forças em X ($\sum F_x = 0$):**
    $$-T_1 \cos(\theta_1) + T_2 \cos(\theta_2) = 0$$
    $$T_2 = T_1 \frac{\cos(37^\circ)}{\cos(53^\circ)} \quad \text{(Equação I)}$$

2.  **Soma das Forças em Y ($\sum F_y = 0$):**
    $$T_1 \sin(\theta_1) + T_2 \sin(\theta_2) - F_g = 0$$
    $$T_1 \sin(37^\circ) + T_2 \sin(53^\circ) - 122 = 0 \quad \text{(Equação II)}$$

### 4.5. Solução (Cálculos Fornecidos)

Substituindo (I) em (II), encontramos $T_1$:

$$T_1 = \frac{F_g}{\sin(\theta_1) + \cos(\theta_1) \tan(\theta_2)}$$
$$T_1 = \frac{122}{\sin(37^\circ) + \cos(37^\circ) \tan(53^\circ)} \approx 73,4 \text{ N}$$

Usando $T_1$ na Equação I, encontramos $T_2$:

$$T_2 = T_1 \frac{\cos(37^\circ)}{\cos(53^\circ)}$$
$$T_2 = 73,4 \frac{\cos(37^\circ)}{\cos(53^\circ)} \approx 97,4 \text{ N}$$

### 4.6. Conclusão

Os valores das tensões são:

* $T_1 = 73,4 \text{ N}$
* $T_2 = 97,4 \text{ N}$

Como ambas as tensões ($73,4 \text{ N}$ e $97,4 \text{ N}$) são **menores** que o limite de $100 \text{ N}$, os cabos **NÃO** quebrarão. O semáforo permanecerá pendurado em equilíbrio! 🎉

---

## 5. Mapa Mental (Síntese do Conhecimento)

| Conceito | Descrição | Palavras-Chave |
| :--- | :--- | :--- |
| **Vetores vs. Escalares** | Vetor requer Módulo, Direção e Sentido. Escalar requer só Módulo. | Força, Velocidade, Massa, Tempo. |
| **Componentes** | Projeção do vetor nos eixos $x$ e $y$. **Sempre** pensar no **Triângulo Retângulo** ($\cos$/adjacente, $\sin$/oposto). | $A_x = A \cos\theta$, $A_y = A \sin\theta$. |
| **Módulo (Tamanho)** | Calculado via Teorema de Pitágoras. | $|A| = \sqrt{A_x^2 + A_y^2}$. |
| **Direção (Ângulo)** | Calculado via Arco Tangente. **Cuidado com o Quadrante!** | $\theta = \arctan(A_y/A_x)$. |
| **Soma Algébrica** | Soma as componentes separadamente: $\vec{C} = (A_x+B_x, A_y+B_y)$. | Resultante, Componentes, Somatório. |
| **Equilíbrio** | Condição onde a Força Resultante é nula em todas as direções ($\sum F_x = 0$ e $\sum F_y = 0$). | Estática, Força Peso, Tração. |

