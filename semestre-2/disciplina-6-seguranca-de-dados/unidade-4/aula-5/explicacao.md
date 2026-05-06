# S2-D5-U4-A5: Arquitetura e Simulação no Software Arena

## 🎯 Objetivos de Aprendizagem
Compreender os componentes básicos da arquitetura do software Arena, focando em entidades, atributos e a construção de fluxogramas lógicos (Basic Process).

---

## 🏛️ Conceitos Fundamentais

### 1. Entidades vs. Atributos
*   **Entidades:** São os objetos dinâmicos que "trafegam" pelo sistema (ex: clientes, produtos, peças). Elas são criadas, processadas e destruídas (saída do sistema).
*   **Atributos:** São propriedades específicas de cada entidade (ex: idade do cliente, prioridade, tempo de processamento). O atributo define o comportamento da entidade dentro do fluxo.

### 2. Módulos de Fluxograma (Basic Process)
A simulação no Arena baseia-se na tríade fundamental:
*   **CREATE:** Ponto de entrada das entidades no sistema.
*   **PROCESS:** Local onde ocorre a atividade, consumo de tempo e recursos.
*   **DISPOSE:** Ponto de saída e finalização do ciclo de vida da entidade.
*   **DECIDE:** Módulo de lógica condicional (decisão) que direciona entidades para diferentes caminhos com base em atributos ou probabilidades.

---

## 🛒 Estudo de Caso: Filas de um Supermercado

### Cenário
Um mercado em São Paulo possui três tipos de filas de caixa:
1.  **Prioritário:** Para idosos (> 60 anos).
2.  **Até 15 itens:** Para compras rápidas.
3.  **Normal:** Demais clientes.

### Lógica do Fluxograma (Algoritmo de Decisão)
O processo segue uma cascata de decisões (Módulos DECIDE):

1.  **Início (CREATE):** Chegada do Cliente.
2.  **Decisão 1 (É Idoso?):** 
    *   **Sim:** Direciona para o **Caixa Prioritário**.
    *   **Não:** Encaminha para a próxima análise.
3.  **Decisão 2 (Tem até 15 itens?):**
    *   **Sim:** Direciona para o **Caixa Rápido**.
    *   **Não:** Direciona para o **Caixa Normal**.
4.  **Finalização (DISPOSE):** Todos os caixas convergem para a saída do sistema.

---

## 💡 Reflexão
*   **Importância da Simulação:** Permite prever gargalos e testar mudanças sem custos reais ou riscos operacionais.
*   **Vantagens:** Identificação de ociosidade, otimização de recursos (caixas/atendentes) e melhoria na experiência do cliente (redução de tempo de espera).
