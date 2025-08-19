
# 🗺️ Explorando a Teoria dos Grafos 🗺️

**A teoria dos grafos é como um mapa de conexões! 📍 Ela nos ajuda a entender como diferentes coisas se ligam.**

### 🟢 Vértices (Nós) e Arestas (Conexões) 🟡

**Imagine seus amigos e as amizades entre eles. 🧑‍🤝‍🧑**

**Os ****VÉRTICES** são as pessoas.

> **João, Maria, Pedro, Ana**

**As ****ARESTAS** são as amizades.

> **João e Maria são amigos.**

**Exemplo:** Um grupo de amigos em uma rede social.

```
👩‍🦱 --- 🧑‍🦱 --- 👩‍🦳
  |    /   |
  |  /     |
  🧓 --- 👴

```

**Neste grafo, cada emoji é um ****vértice** e as linhas são as  **arestas** **.**

### 🤝 Grafo Não Direcionado 🤝

**Em um grafo ** **não direcionado** **, as conexões são de mão dupla! 🔄 Se você está conectado a alguém, essa pessoa também está conectada a você. Pense em uma rua onde você pode ir e voltar.**

**Exemplo:** Amigos que se seguem mutuamente no Instagram.

> 👨‍💻 <---> 👩‍💻
>
> Se A segue B, então B segue A.

### ➡️ Grafo Direcionado ⬅️

**Aqui, as conexões têm uma direção específica. ➡️ Pense em seguir alguém no Twitter: você pode seguir uma pessoa, mas ela não precisa te seguir de volta.**

**Exemplo:** A rota de um carro 🚗

```
🏡 A -> 🏢 B -> 🛍️ C
(Casa)    (Trabalho)  (Shopping)

```

**Você pode ir de **`<span class="selected">A</span>` para `<span class="selected">B</span>`, mas não necessariamente de `<span class="selected">B</span>` para `<span class="selected">A</span>`. A seta ➡️ mostra o sentido.

### 🛤️ Caminhos e Ciclos 🔄

* **Caminho:** É uma sequência de vértices e arestas para ir de um ponto a outro.
  > 🏃‍♀️ A -> B -> C
  >
  > Isso é um caminho!
  >
* **Ciclo:** É um caminho que começa e termina no mesmo vértice, sem repetir arestas.
  > 🚴‍♂️ A -> B -> C -> A
  >
  > Isso é um ciclo! O caminho forma um laço.
  >

### 💰 Grafo Ponderado (Com Custos) 💰

**Em um grafo ponderado, cada aresta tem um "peso" ou "custo". 💸 Esse custo pode ser tempo, distância, dinheiro, etc.**

**Exemplo:** O custo para ir de uma cidade a outra.

```
   R$50
🏙️ A --------> 🏙️ B
   |  \       / |
   |   \ R$70 /  |
R$120|    \   /  | R$60
   |     \ /   |
   |      V    |
   |   🏙️ C   |
   +-----------+

```

**A aresta de **`<span class="selected">A</span>` para `<span class="selected">C</span>` custa R**120**,**e**n**q**u**an**t**o**d**e**‘**A**‘**p**a**r**a**‘**B**‘**c**u**s**t**a**R**50. Você pode usar isso para encontrar o caminho mais barato.

### 🗓️ Grafo Topológico 🗓️

**Este tipo de grafo é usado para tarefas que dependem de outras. É ** **acíclico** **, ou seja, não tem ciclos! 🚫 Isso garante que você não terá uma dependência infinita.**

**Exemplo:** A rotina da manhã ☕

> **Despertar ⏰ -> Tomar café ☕ -> Se vestir 👕 -> Sair de casa 🚪**

**Cada passo só pode ser feito após o anterior. Não é possível "sair de casa" antes de "se vestir".**
