# 🛠️ Turbinando o Modelo: Atribuições, Estatísticas e Animação

Agora que já sabemos o básico do Arena, vamos aprender a dar "inteligência" e "beleza" ao nosso modelo. Nesta aula, focamos em como personalizar as entidades e como coletar dados sérios para análise. 📈

---

## 🏷️ Módulo ASSIGN: O Crachá da Entidade

Imagine que o Arena é uma fábrica de camisetas. O bloco **CREATE** cria a camiseta branca básica. Mas e se quisermos camisetas azuis e vermelhas? 👕

É aqui que entra o **ASSIGN**. Ele funciona como uma etiqueta que você cola na entidade assim que ela nasce. Com ele, você define:
- **Atributos:** Informações únicas (ex: "Tamanho: G").
- **Imagens:** Como ela aparece na tela (ex: trocar o desenho de um carro por uma moto).
- **Variáveis:** Valores globais que afetam todo o sistema.

> **Regra de Ouro:** O ASSIGN geralmente vem logo após o CREATE. É a primeira coisa que acontece!

---

## 📝 Módulo RECORD: O Caderno do Auditor

De nada adianta simular se você não souber o que aconteceu no final. O **RECORD** é o módulo que "anota" os dados toda vez que alguém passa por ele. 📔

Ele pode registrar:
- **Count:** "Já passaram 50 pessoas por aqui". ✅
- **Time Interval:** "O João demorou 15 minutos desde que entrou até agora". ⏳
- **Time Between:** "O intervalo entre o último cliente e este foi de 2 minutos". ⏱️

Os dados do RECORD vão direto para o **Relatório Final**, que é o que você apresenta para o seu chefe para provar que sua solução funciona.

---

## 🎥 Animação: Estática vs. Dinâmica

A simulação não precisa ser apenas números; ela pode ser visual para facilitar o entendimento de quem não é técnico.

### 🖼️ Imagens Estáticas (Arena Symbol Factory)
São as decorações do cenário. Uma árvore, uma parede, um balcão. Elas **não mudam**. Se você colocou uma planta lá, ela continuará sendo uma planta o tempo todo. 🌳

### 🏃 Imagens Dinâmicas (Recursos)
Essas são as "vivas". Elas mudam de acordo com o estado do sistema:
- **Idle (Ocioso):** O atendente está sentado esperando (imagem A). 😴
- **Busy (Ocupado):** O atendente está trabalhando freneticamente (imagem B). 👨‍💻

Isso ajuda a identificar gargalos só de olhar para a tela! Se o desenho está sempre em "Ocupado", você tem um problema de fila ali.

---

## 🧱 Template Basic Process: A Base de Tudo

Este conjunto de módulos é o coração do Arena. Ele simplifica a modelagem porque:
1.  **Não exige programação complexa:** Você conecta blocos lógicos.
2.  **É visual:** Você entende o fluxo de movimento das entidades.
3.  **É flexível:** Permite modelar desde uma fila de banco até uma linha de montagem da Boeing.

---

> [!IMPORTANT]
> **Dica de Data Science:** Atributos definidos no **ASSIGN** podem ser usados mais tarde para criar regras de decisão. Por exemplo: "Se a camiseta for Vermelha (Atributo), mande para a máquina de estampa X; se for Azul, mande para a Y". Isso é o que chamamos de lógica condicional! 🧠
