// aula-1.js: Exemplificando Tipos de Dados na Arquitetura de Dados (Aula 1)
// Este script JavaScript demonstra os conceitos usando estruturas de dados JS.

console.log("--- Tipos de Dados em JavaScript para Arquitetura ---");

// --- 1. DADOS ESTRUTURADOS (Array de Objetos Rígidos) ---
// Representamos a "tabela" de clientes onde todas as entradas têm o mesmo esquema (colunas).
const clientesEstruturados = [
    {
        id_cliente: 1, 
        nome: "Mario de Souza", 
        cpf: "111.111.111-11", 
        satisfacao_estrelas: 5
    },
    {
        id_cliente: 2, 
        nome: "Anderson Inácio", 
        cpf: "222.222.222-22", 
        satisfacao_estrelas: 3
    }
];

console.log("\n--- 1. DADOS ESTRUTURADOS (Array de Clientes) ---");

// Cálculo simples em dados estruturados
const totalEstrelas = clientesEstruturados.reduce((soma, cliente) => soma + cliente.satisfacao_estrelas, 0);
const mediaSatisfacao = totalEstrelas / clientesEstruturados.length;

console.log(`Média de Satisfação: ${mediaSatisfacao.toFixed(2)} estrelas.`);
console.log(`Cliente 2: ${clientesEstruturados[1].nome}`);
console.log("-".repeat(50));


// --- 2. DADOS NÃO ESTRUTURADOS (Strings Longas e Referências) ---
// Em JS, isso é tipicamente o conteúdo de texto livre (chat, reviews) ou URLs/caminhos de mídia.
console.log("--- 2. DADOS NÃO ESTRUTURADOS (Textos e Mídia) ---");

const feedbackTextoLivre = `
    A cor do produto é incrível! Mas a documentação que veio junto é muito confusa, 
    o que me fez perder tempo. Vou postar um vídeo de unboxing no meu canal.
`;

const urlVideoUnboxing = "https://youtube.com/user123/unboxing_prod_x.mp4";

console.log(`Trecho do Feedback: "${feedbackTextoLivre.trim().substring(0, 70)}..."`);
console.log(`URL do Vídeo: ${urlVideoUnboxing}`);

// A análise exige Processamento de Linguagem Natural (NLP)
if (feedbackTextoLivre.includes("incrível")) {
    console.log("Análise Simples: Termo 'incrível' detectado (positivo).");
}
console.log("-".repeat(50));


// --- 3. DADOS PARCIALMENTE ESTRUTURADOS (O Poder do JSON/Objetos JS) ---
// O JavaScript lida nativamente com JSON, que é o formato ideal para dados flexíveis (NoSQL).
console.log("--- 3. DADOS PARCIALMENTE ESTRUTURADOS (JSON/Objetos) ---");

// Avaliação A: Completa com todos os campos
const avaliacaoA = {
    id_avaliacao: "rev_001",
    estrelas: 4, // Estruturado
    data_registro: new Date().toISOString(),
    comentario: "Excelente compra, chegou super rápido!", // Não Estruturado
    parametros_analise: { // Estrutura aninhada (flexibilidade)
        satisfacao: "alta",
        rapidez_entrega: true
    }
};

// Avaliação B: Faltando a data e o campo 'parametros_analise' (Flexibilidade NoSQL)
const avaliacaoB = {
    id_avaliacao: "rev_002",
    estrelas: 5,
    comentario: "Simplesmente perfeito! Não tenho o que reclamar."
    // O campo 'data_registro' está ausente, o que é aceito em JSON/NoSQL.
};

// Conversão para string JSON (para envio via API)
const jsonStringA = JSON.stringify(avaliacaoA, null, 2); 
console.log("\nJSON da Avaliação A (Flexível):");
console.log(jsonStringA);

// Demonstração da leitura: Acessando dados estruturados e verificando flexibilidade
console.log(`\nEstrelas da Avaliação A: ${avaliacaoA.estrelas}`);
// Verificando se um campo opcional existe
console.log(`Possui parâmetros de análise na B? ${!!avaliacaoB.parametros_analise ? 'Sim' : 'Não'}`);
console.log("-".repeat(50));