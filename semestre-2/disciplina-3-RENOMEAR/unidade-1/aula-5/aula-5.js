// aula-5.js
// Exemplo em JavaScript (Node.js) da representação do Modelo Lógico Normalizado.
// Usamos objetos e arrays para simular as tabelas e suas relações (FK).

// ------------------------------------------
// 1. Entidades Normalizadas (Tabelas)
// O resultado da normalização: dados separados para evitar redundância.
// ------------------------------------------

// Simula a Tabela 'Aluno'
const Alunos = [
    { ID_Aluno: 101, Nome: "Maria da Silva", Data_Matricula: "2023-08-15" },
    { ID_Aluno: 102, Nome: "João de Souza", Data_Matricula: "2024-01-20" },
    // A informação do aluno é guardada apenas uma vez (Normalização)
];

// Simula a Tabela 'Livro'
const Livros = [
    { ISBN: '978-8575225409', Titulo: 'Banco de Dados Avançado', Ano_Publicacao: 2020 },
    { ISBN: '978-0131103627', Titulo: 'A Linguagem C', Ano_Publicacao: 1978 },
];

// Simula a Tabela 'Emprestimo' (Tabela de Relacionamento)
// Esta tabela conecta Aluno e Livro usando Chaves Estrangeiras (FKs).
const Emprestimos = [
    { 
        ID_Emprestimo: 1, 
        ID_Aluno_FK: 101,                   // Chave Estrangeira para Aluno
        ISBN_FK: '978-8575225409',          // Chave Estrangeira para Livro
        Data_Emprestimo: '2025-10-01', 
        Data_Devolucao_Prevista: '2025-10-15' 
    },
    { 
        ID_Emprestimo: 2, 
        ID_Aluno_FK: 102, 
        ISBN_FK: '978-0131103627', 
        Data_Emprestimo: '2025-10-02', 
        Data_Devolucao_Prevista: '2025-10-16' 
    },
];

// ------------------------------------------
// 2. Função de Consulta (Simulando um JOIN)
// Demonstra como a informação separada é recombinada.
// ------------------------------------------

/**
 * Simula uma consulta (JOIN) para listar empréstimos.
 */
function listarEmprestimos() {
    console.log("📋 Lista de Empréstimos (Simulação de JOIN no Modelo Lógico):");
    console.log("------------------------------------------");

    Emprestimos.forEach(emprestimo => {
        // Encontra o Aluno (JOIN Aluno ON Emprestimo.ID_Aluno_FK = Aluno.ID_Aluno)
        const aluno = Alunos.find(a => a.ID_Aluno === emprestimo.ID_Aluno_FK);
        
        // Encontra o Livro (JOIN Livro ON Emprestimo.ISBN_FK = Livro.ISBN)
        const livro = Livros.find(l => l.ISBN === emprestimo.ISBN_FK);

        if (aluno && livro) {
            console.log(
                `[ID: ${emprestimo.ID_Emprestimo}] ` +
                `Aluno: ${aluno.Nome} | ` +
                `Livro: ${livro.Titulo} | ` +
                `Data Empréstimo: ${emprestimo.Data_Emprestimo}`
            );
        } else {
            console.log(`⚠️ Erro de Integridade: Empréstimo ${emprestimo.ID_Emprestimo} aponta para dados ausentes.`);
        }
    });

    console.log("------------------------------------------");
    console.log("✔️ Modelo Lógico (Entidades e Relacionamentos) exemplificado com sucesso.");
}

// ------------------------------------------
// 3. Execução
// ------------------------------------------
listarEmprestimos();

// Para rodar o arquivo, salve-o como aula-5.js e execute no terminal com Node.js: node aula-5.js