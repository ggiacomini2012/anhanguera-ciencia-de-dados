# ✨ Guia Minimalista para Conventional Commits

Conventional Commits é uma convenção simples para padronizar as mensagens dos seus commits. Isso torna o histórico do projeto mais claro e fácil de ler.

---

### **A Estrutura Básica:**

`tipo(escopo): descrição concisa`

* **`tipo`**: O que seu commit faz.
* **`(escopo)`**: Opcional, onde a mudança ocorreu (ex: `login`, `api`).
* **`descrição`**: A mensagem principal.

---

### **Tipos Essenciais:**

* **`feat`**: Adiciona uma nova funcionalidade. ✨
* **`fix`**: Corrige um bug. 🐛
* **`docs`**: Apenas mudanças na documentação. 📝
* **`style`**: Formatação de código, sem mudança na lógica. 🎨
* **`refactor`**: Reestruturação de código que não adiciona funcionalidade nem corrige bugs. ♻️
* **`test`**: Adiciona ou corrige testes. 🧪
* **`chore`**: Tarefas de rotina ou manutenção. 🧹

---

### **Mudanças Que Quebram Algo:**

Para indicar uma **mudança drástica** (quebra a compatibilidade com versões anteriores), adicione um `!` após o tipo.

`feat!: nova_função_que_quebra_a_api` 💥