// Arquivo: aula-1.js
// Aula 1: Introdução à Arquitetura de Dados em JavaScript - Refinando Dados para Sabedoria

/**
 * Representa os dados brutos de transações (O Petróleo Bruto).
 * Em um cenário real de e-commerce, isso viria de um banco de dados transacional (Esquema Físico).
 */
const rawData = [
    { transacaoId: 1001, clienteId: "C001", produtoCor: "azul", valor: 150.00, data: "2023-09-01" },
    { transacaoId: 1002, clienteId: "C002", produtoCor: "verde", valor: 50.00, data: "2023-09-01" },
    { transacaoId: 1003, clienteId: "C001", produtoCor: "verde", valor: 200.00, data: "2023-09-02" },
    { transacaoId: 1004, clienteId: "C003", produtoCor: "azul", valor: 80.00, data: "2023-09-02" },
    { transacaoId: 1005, clienteId: "C002", produtoCor: "vermelho", valor: 120.00, data: "2023-09-03" },
];

console.log("--- 1. DADOS (Data) Brutos ---");
console.log("Fatos isolados e sem agregação (5 registros).");
console.table(rawData);
console.log("=".repeat(50) + "\n");

// --- 2. INFORMAÇÃO (Information): Agregação e Contexto ---

/**
 * Função de Arquitetura de Dados: Refina dados brutos em Informação.
 * Agrupa transações por cliente para calcular o total gasto e o ticket médio.
 */
function refinarParaInformacao(dados) {
    // Uso do reduce para agrupar e somar valores - simula um processo ETL/ELT
    const infoMap = dados.reduce((acc, transacao) => {
        const id = transacao.clienteId;
        if (!acc[id]) {
            acc[id] = { totalGasto: 0, numCompras: 0, clienteId: id };
        }
        acc[id].totalGasto += transacao.valor;
        acc[id].numCompras += 1;
        return acc;
    }, {});

    // Adiciona o contexto do Ticket Médio
    const informacao = Object.values(infoMap).map(item => ({
        ...item,
        ticketMedio: item.totalGasto / item.numCompras
    }));

    return informacao;
}

const informacaoContextualizada = refinarParaInformacao(rawData);

console.log("--- 2. INFORMAÇÃO (Information) Contextualizada ---");
console.log("Dados transformados em contexto de Cliente (Total Gasto, Ticket Médio).");
console.table(informacaoContextualizada);
console.log("=".repeat(50) + "\n");

// --- 3. CONHECIMENTO (Knowledge): Padrões e Relações ---

/**
 * Função de Análise: Gera Conhecimento a partir do cruzamento de Informações.
 * Procura um padrão de compra cruzada (AZUL seguido por VERDE).
 */
function gerarConhecimento(dados) {
    const clientesComAzul = new Set();
    const clientesComVerde = new Set();
    
    // Separa os IDs dos clientes que compraram as cores
    dados.forEach(t => {
        if (t.produtoCor === 'azul') clientesComAzul.add(t.clienteId);
        if (t.produtoCor === 'verde') clientesComVerde.add(t.clienteId);
    });

    // Encontra a interseção de clientes que compraram AMBAS as cores
    const clientesComAmbos = [...clientesComAzul].filter(id => clientesComVerde.has(id));

    if (clientesComAmbos.length > 0) {
        return `PADRÃO ENCONTRADO (Conhecimento): Os clientes [${clientesComAmbos.join(', ')}] compraram produtos AZUIS e VERDES. Isso é um forte indicador para 'Cross-selling'.`;
    } else {
        return "Nenhum padrão de compra AZUL/VERDE significativo encontrado neste lote.";
    }
}

const conhecimentoGerado = gerarConhecimento(rawData);

console.log("--- 3. CONHECIMENTO (Knowledge) - Padrão Descoberto ---");
console.log(conhecimentoGerado);
console.log("=".repeat(50) + "\n");

// --- 4. SABEDORIA (Wisdom): Decisão e Ação Estratégica ---

/**
 * Função de Decisão Estratégica (Sabedoria).
 * Transforma o Conhecimento em uma Ação tática de e-commerce.
 */
function aplicarSabedoria(conhecimento, informacao) {
    let acoesEstrategicas = [];
    
    // Ação 1: Baseada no Padrão de Cross-selling
    if (conhecimento.includes('AZUIS e VERDES')) {
        acoesEstrategicas.push("✅ AÇÃO 1 (Sabedoria): Lançar uma campanha de e-mail marketing oferecendo 10% de desconto em produtos VERDES para clientes que compraram AZUL nos últimos 30 dias. (Ação do Ciclo OODA)");
    }
    
    // Ação 2: Baseada em Alta Informação (Ticket Médio Elevado)
    const clientesDeAltoValor = informacao.filter(c => c.ticketMedio >= 150.00).map(c => c.clienteId);
    if (clientesDeAltoValor.length > 0) {
         acoesEstrategicas.push(`✅ AÇÃO 2 (Sabedoria): Iniciar o processo de migração dos clientes [${clientesDeAltoValor.join(', ')}] para o 'Programa de Fidelidade Platinum' para aumentar a retenção de alto valor.`);
    }

    return acoesEstrategicas.join('\n');
}

const sabedoriaEstrategica = aplicarSabedoria(conhecimentoGerado, informacaoContextualizada);

console.log("--- 4. SABEDORIA (Wisdom) - Direcional Estratégico ---");
console.log("O Arquiteto de Dados transforma insights em ações de negócio:");
console.log(sabedoriaEstrategica);
console.log("\n" + "=".repeat(50) + "\n");

// O JavaScript demonstrou como a Arquitetura de Dados (as funções de processamento)
// transforma dados brutos em valor estratégico de forma programática.