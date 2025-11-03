# 📐 Vetores e Segmentos Orientados

## 🚀 Ponto de Partida

Vetores são entidades matemáticas que representam grandezas que têm magnitude (tamanho) e direção. Eles são como "setas" matemáticas usadas em física, informática e engenharia para descrever movimento, força e muito mais.

Pense em um vetor como uma **receita de navegação** 🗺️. Ele não diz apenas *onde* você está (como um ponto), mas *para onde* ir (direção) e *quão longe* ir (magnitude).

Vetores e segmentos orientados estão intimamente relacionados, pois um segmento orientado (um pedaço de reta com um início e um fim) pode ser representado por um vetor.

### O Desafio do Prisma

A respeito da relação entre vetores e segmentos orientados, considere o exemplo a seguir.

Na **Figura 1** está reproduzido um prisma reto de base retangular com vértices A, B, C, D, E, F, G e H:

*[Figura 1 | Prisma reto de base retangular]*

A partir dessa figura, classifique as seguintes afirmações como verdadeiras (V) ou falsas (F):

( ) Os vetores
( ) Os vetores
( ) Os vetores

Para responder a essas afirmativas, são necessários alguns conhecimentos a respeito de segmentos orientados e vetores.

Vamos começar? Bons estudos!

---

## 📍 Ponto, Reta e Plano

Esses são os blocos de construção da geometria! São conceitos primitivos, o que significa que os aceitamos sem uma definição formal.

* **Ponto (A, B, C...)**: Representa uma localização exata no espaço. Não tem dimensão (sem largura, altura ou profundidade). Pense no "pin" 📍 de um mapa digital.
* **Reta (r, s, t...)**: Uma coleção infinita de pontos em linha reta, que se estende para sempre em ambas as direções. Tem uma dimensão (comprimento).
* **Plano ($\alpha$, $\beta$, $\gamma$...)**: Uma superfície plana bidimensional que se estende infinitamente em todas as direções. Pense na superfície de uma mesa infinita.

*[Figura 2 | Ponto, reta e plano]*

## 📏 Segmento e Segmento Orientado

**Segmento** é qualquer trecho de uma reta delimitado por dois pontos, $A$ e $B$, por exemplo.

Quando damos um "sentido" a esse segmento, ele se torna um **segmento orientado**. Podemos ir:
1.  De $A$ (origem) para $B$ (extremidade): $\vec{AB}$
2.  De $B$ (origem) para $A$ (extremidade): $\vec{BA}$

*[Figura 3 | Segmentos orientados: (a) de A para B; (b) de B para A]*

Todo segmento orientado tem três componentes:

1.  **Módulo (Magnitude)**: O comprimento ou "tamanho" do segmento, ou seja, a distância entre $A$ e $B$. É sempre um valor positivo.
2.  **Direção**: A "inclinação" da reta onde o segmento está. Retas paralelas têm a mesma direção.
3.  **Sentido**: Para onde a "seta" aponta. Em uma mesma direção (ex: a BR-101), você pode ter dois sentidos (ir para o norte ou ir para o sul).

**Exemplo do Avião ✈️:**
Observe o segmento $\vec{AB}$ que representa a decolagem de um avião.
* **Módulo**: A distância que o avião percorreu.
* **Direção**: A trajetória da decolagem.
* **Sentido**: De $A$ (pista) para $B$ (céu).

*[Figura 4 | Decolagem]*

---

## 🧭 Tipos de Segmentos Orientados

### 1. Segmento Nulo
É um segmento onde a origem e a extremidade são o mesmo ponto (ex: $\vec{AA}$). Seu módulo é zero.

### 2. Segmentos Opostos
Dois segmentos são opostos se têm o mesmo módulo, mesma direção, mas **sentidos contrários**.
* $\vec{AB}$ e $\vec{BA}$ são o exemplo clássico.

*[Figura 5 | Segmentos orientados: (a) de mesma direção; (b) opostos]*

### 3. Segmentos Equipolentes (O mais importante!)
Dois segmentos orientados, $\vec{AB}$ e $ \vec{CD} $, são **equipolentes** se eles têm:
* Mesmo **módulo** (mesmo comprimento)
* Mesma **direção** (são paralelos)
* Mesmo **sentido** (apontam para o mesmo lado)

> **Analogia:** Pense em segmentos equipolentes como uma **instrução de movimento idêntica**.
>
> Se você e seu amigo estão em lugares diferentes da sala, e ambos dão "dois passos para frente", vocês executaram segmentos equipolentes. Os pontos de partida (A e C) são diferentes, mas o deslocamento (o vetor) foi o mesmo.

*[Figura 6 | Segmentos equipolentes]*

**Exemplo Rápido (Figura 7):**
*[Figura 7 | Segmentos]*

* **$ \vec{AB} $ e $\vec{CD}$ são segmentos opostos?**
    * Sim. Têm mesmo módulo, mesma direção, mas sentidos opostos.
* **$ \vec{AB} $ e $\vec{MN}$ são segmentos de módulos iguais, direção e sentidos diferentes?**
    * Não. Têm módulos e sentidos diferentes, mas a *mesma direção* (são paralelos).
* **$ \vec{MN} $ e $\vec{EF}$ são segmentos de mesmo módulo, direção e sentido?**
    * Não. São completamente diferentes.
* **$ \vec{GH} $ e $\vec{OP}$ são segmentos equipolentes?**
    * Sim. Têm mesmo módulo, mesma direção e mesmo sentido.

---

## 🛰️ Vetor

Aqui está a grande ideia:

> Um **vetor** é o conjunto de TODOS os segmentos orientados que são equipolentes entre si.

Enquanto $\vec{AB}$ é um segmento específico que começa em A e termina em B, o **vetor** $\vec{v} = \vec{AB}$ representa a *ideia* desse deslocamento (módulo, direção e sentido), podendo ser aplicado em qualquer lugar.

Por isso, na Figura 6, $\vec{AB}$ e $\vec{CD}$ são **representantes** do mesmo vetor $\vec{v}$.

Denominamos vetor $\vec{v}$ ao conjunto de todos os segmentos orientados equipolentes a um segmento orientado $\vec{AB}$.

### Casos Particulares
* **Vetor Nulo ($\vec{0}$)**: Representado por um segmento nulo (como $\vec{AA}$).
* **Vetores Paralelos ($\vec{u}$ // $\vec{v}$)**: Têm a mesma direção. O ângulo entre eles é 0° (mesmo sentido) ou 180° (sentidos opostos).
* **Vetores Perpendiculares**: O ângulo entre eles é de 90°.

---

## 🔍 Diferença entre Vetor e Segmento de Reta Orientado

* Um **segmento orientado** é "preso". Ele tem um ponto inicial e um ponto final fixos no espaço. $\vec{AB}$ começa *exatamente* em A.
* Um **vetor** é "livre". É um conceito abstrato que define magnitude e direção. Ele pode ser "desenhado" (representado) começando em qualquer ponto.

Em resumo, o segmento orientado é *uma* representação física e específica, enquanto o vetor é a *ideia* matemática geral por trás dessa representação.

---

## ✍️ Vamos Exercitar?

Vamos retomar ao exemplo do começo da nossa aula.

*[Figura 1 | Prisma reto de base retangular]*

Vamos refazer a figura mostrando os vetores necessários para a resolução do exercício.

**Tabela 1 | Alguns vetores do prisma**
| Vetor | Origem | Extremidade |
| :--- | :--- | :--- |
| $\vec{AB}$ | A | B |
| $\vec{AD}$ | A | D |
| $\vec{BC}$ | B | C |
| $\vec{DH}$ | D | H |
| $\vec{FG}$ | F | G |
| $\vec{GH}$ | G | H |

*[Figura 8 | Prisma reto de base retangular com vetores destacados]*

A partir da Figura 8, podemos analisar as afirmações (que agora podemos responder!):

1.  **"Os vetores $\vec{AB}$ e $\vec{GH}$ têm a mesma direção, mas sentidos contrários."**
    * $\vec{AB}$ (A $\rightarrow$ B) e $\vec{GH}$ (G $\rightarrow$ H) são paralelos e apontam para o mesmo lado.
    * **Conclusão:** Eles têm mesma direção e *mesmo* sentido. A afirmação é **FALSA**.

2.  **"Os vetores $\vec{FG}$ e $\vec{AD}$ são de mesmo sentido."**
    * $\vec{FG}$ (F $\rightarrow$ G) e $\vec{AD}$ (A $\rightarrow$ D) são paralelos e apontam para o mesmo lado.
    * **Conclusão:** Eles têm mesma direção e mesmo sentido. A afirmação é **VERDADEIRA**.

3.  **"Os vetores $\vec{DH}$ e $\vec{BC}$ não têm a mesma direção."**
    * $\vec{DH}$ (D $\rightarrow$ H) é uma aresta vertical.
    * $\vec{BC}$ (B $\rightarrow$ C) é uma aresta de "profundidade" (horizontal).
    * **Conclusão:** Eles não são paralelos, logo, não têm a mesma direção. A afirmação é **VERDADEIRA**.