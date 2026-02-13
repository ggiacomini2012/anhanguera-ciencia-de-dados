// Nome do arquivo: aula-4.js
// Exemplo de Modelagem Lógica em JavaScript (Representação JSON/Estrutura de Objetos)
// As arrays representam as Tabelas e as chaves (Keys) dos objetos representam as Colunas.

// Tabela 1: EDITORA
// Chave Primária (PK): cod_editora
const EDITORA = [
    {
        cod_editora: 101,
        nome: "Atlas Publishing"
    },
    {
        cod_editora: 102,
        nome: "Tech Books Inc."
    }
];

// Tabela 2: CLIENTE
// Chave Primária (PK): cod_cliente
const CLIENTE = [
    {
        cod_cliente: 500,
        nome: "Mariana Silva",
        endereco: "Rua A, 123"
    }
];

// Tabela 3: LIVRO
// Chave Primária (PK): cod_livro
// Chave Estrangeira (FK): cod_editora_fk (referencia EDITORA)
const LIVRO = [
    {
        cod_livro: 1,
        titulo: "Aventura em Python",
        ano_publicacao: 2023,
        cod_editora_fk: 102 // FK para Tech Books Inc.
    },
    {
        cod_livro: 2,
        titulo: "SQL Avançado",
        ano_publicacao: 2022,
        cod_editora_fk: 102 // FK para Tech Books Inc.
    },
    {
        cod_livro: 3,
        titulo: "Modelagem de Dados",
        ano_publicacao: 2021,
        cod_editora_fk: 101 // FK para Atlas Publishing
    }
];

// Tabela 4: PEDIDO
// Chave Primária (PK): num_pedido
// Chave Estrangeira (FK): cod_cliente_fk (referencia CLIENTE)
const PEDIDO = [
    {
        num_pedido: 1000,
        data_pedido: "2024-10-01",
        valor_total: 150.00,
        cod_cliente_fk: 500 // FK para Mariana Silva
    }
];

// Tabela 5: ITENS_PEDIDO (Tabela Associativa)
// Resolve o relacionamento N:N entre PEDIDO e LIVRO.
// Chave Primária Composta (PK): (num_pedido_fk, cod_livro_fk)
const ITENS_PEDIDO = [
    {
        num_pedido_fk: 1000, // FK para Pedido 1000
        cod_livro_fk: 1,     // FK para Livro 1
        quantidade: 1,
        preco_unitario: 80.00
    },
    {
        num_pedido_fk: 1000, // FK para Pedido 1000
        cod_livro_fk: 3,     // FK para Livro 3
        quantidade: 1,
        preco_unitario: 70.00
    }
];

// Tabela 6: ESTOQUE
// Chave Primária (PK) / Chave Estrangeira (FK): cod_livro_fk (referencia LIVRO)
const ESTOQUE = [
    {
        cod_livro_fk: 1,
        quantidade_disponivel: 50
    },
    {
        cod_livro_fk: 2,
        quantidade_disponivel: 30
    }
];

// --- FUNÇÃO PARA DEMONSTRAR O RELACIONAMENTO (JOIN LÓGICO) ---
console.log("--- 🤝 Demonstração de Relacionamento (Livro N:1 Editora) 🤝 ---");

function buscarLivrosComNomeDaEditora() {
    return LIVRO.map(livro => {
        // Encontra a editora correspondente usando a Chave Estrangeira (FK)
        const editora = EDITORA.find(e => e.cod_editora === livro.cod_editora_fk);
        
        return {
            titulo: livro.titulo,
            ano: livro.ano_publicacao,
            editora: editora ? editora.nome : 'Editora Desconhecida'
        };
    });
}

const livrosComEditora = buscarLivrosComNomeDaEditora();
console.log(livrosComEditora);

console.log("\n--- 🛒 Detalhes de um Pedido (Resolvendo o N:N) 🛒 ---");

function detalharPedido(numPedido) {
    const pedido = PEDIDO.find(p => p.num_pedido === numPedido);
    if (!pedido) return "Pedido não encontrado.";

    // 1. Filtra os itens_pedido para o pedido específico
    const itens = ITENS_PEDIDO.filter(item => item.num_pedido_fk === numPedido);

    // 2. Para cada item, encontra o detalhe do Livro (Cod_livro é a FK)
    const detalhesItens = itens.map(item => {
        const livro = LIVRO.find(l => l.cod_livro === item.cod_livro_fk);
        return {
            titulo_livro: livro ? livro.titulo : 'Livro Removido',
            quantidade: item.quantidade,
            preco_unitario: item.preco_unitario
        };
    });

    return {
        num_pedido: pedido.num_pedido,
        data: pedido.data_pedido,
        cliente_cod: pedido.cod_cliente_fk,
        itens: detalhesItens
    };
}

const detalhesDoPedido1000 = detalharPedido(1000);
console.log(detalhesDoPedido1000);

console.log("\n*Este código demonstra como as Chaves Estrangeiras (FKs) são usadas em JavaScript para 'unir' ou 'relacionar' os dados, exatamente como um JOIN faria no Modelo Físico SQL.*");