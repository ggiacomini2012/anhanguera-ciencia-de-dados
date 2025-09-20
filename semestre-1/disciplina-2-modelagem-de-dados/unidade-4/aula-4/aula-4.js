// Este script Node.js simula o processo de engenharia reversa de um banco de dados
// usando um objeto JSON para representar a estrutura e os dados "legados".

// --- Simulação de um banco de dados "legado" ---
// Um objeto que representa a estrutura de um banco de dados sem documentação clara.
const dbLegado = {
    tabelas: {
        livros_info: [
            { id_livro: 1, nome_livro: 'Aventuras em JavaScript', nome_do_autor: 'Ana Maria', ano_de_publ: 2021 },
            { id_livro: 2, nome_livro: 'Node.js Descomplicado', nome_do_autor: 'John Smith', ano_de_publ: 2019 }
        ],
        membros_dados: [
            { identif: 'MEMB123', nome_membro: 'Carlos Souza' },
            { identif: 'MEMB456', nome_membro: 'Maria Oliveira' }
        ],
        emprestimos_registros: [
            { id_transacao: 101, livro_id: 1, membro_identificacao: 'MEMB123', data_emprestimo: '2023-10-25' },
            { id_transacao: 102, livro_id: 2, membro_identificacao: 'MEMB456', data_emprestimo: '2023-10-26' }
        ]
    }
};

console.log("--- Iniciando o processo de Engenharia Reversa ---");

// Passo 1: Coleta de informações - Listar as tabelas
const tabelas = Object.keys(dbLegado.tabelas);
console.log("\nPasso 1: Descobrindo as tabelas existentes...");
console.log("Tabelas encontradas:", tabelas);

// Passo 2: Análise do banco de dados - Inspecionar a estrutura de cada tabela
console.log("\nPasso 2: Analisando a estrutura das tabelas...");

tabelas.forEach(tabela => {
    console.log(`\nDetalhes da tabela '${tabela}':`);
    const dados = dbLegado.tabelas[tabela];
    if (dados.length > 0) {
        const colunas = Object.keys(dados[0]);
        console.log("  Colunas:", colunas.join(', '));

        // Analisar o tipo de dado do primeiro registro
        console.log("  Tipos de dados (inferidos do primeiro registro):");
        colunas.forEach(coluna => {
            const tipo = typeof dados[0][coluna];
            console.log(`    - ${coluna}: ${tipo}`);
        });
    } else {
        console.log("  Tabela vazia.");
    }
});

// Passo 3: Identificação de Relacionamentos (Lógica de Negócio)
// O analista precisa inferir que 'livro_id' se refere a 'id_livro' e 'membro_identificacao' a 'identif'
console.log("\nPasso 3: Inferindo relacionamentos e regras de negócio...");
console.log("-> A coluna 'livro_id' na tabela 'emprestimos_registros' parece ser a chave estrangeira para 'id_livro' em 'livros_info'.");
console.log("-> A coluna 'membro_identificacao' na tabela 'emprestimos_registros' parece ser a chave estrangeira para 'identif' em 'membros_dados'.");
console.log("Isso estabelece os relacionamentos entre os empréstimos, os livros e os membros.");

// Passo 4: Geração de um "modelo lógico" simplificado
console.log("\nPasso 4: Criando o novo modelo lógico (conceitual)...");
const novoModelo = {
    entidades: [
        { nome: 'Livro', atributos: ['livroId', 'titulo', 'autor', 'ano'] },
        { nome: 'Membro', atributos: ['membroId', 'nome'] },
        { nome: 'Emprestimo', atributos: ['emprestimoId', 'livroId', 'membroId', 'data'] }
    ],
    relacionamentos: [
        'Um Livro pode ter muitos Empréstimos (1:N)',
        'Um Membro pode ter muitos Empréstimos (1:N)'
    ]
};

console.log("Novo Modelo de Dados (JSON):", JSON.stringify(novoModelo, null, 2));

console.log("\n--- Engenharia Reversa concluída. Novo modelo de dados definido. ---");