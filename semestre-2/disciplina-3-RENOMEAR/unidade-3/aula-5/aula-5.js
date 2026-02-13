/**
 * Arquivo: aula-5.js
 * Tema: Arquitetura de Dados Corporativos, ETL, Modelagem Dimensional e Análise OLAP
 *
 * Simulação do Processo de Transformação e Análise de Dados de Vendas
 * para o Data Warehouse, focando em JavaScript.
 */

// ==============================================================================
// 1. CARGA (L) - Dados Simulados no DW (Modelagem Dimensional Simples)
//    (Estes dados representam a Tabela Fato 'Vendas' após o processo ETL)
// ==============================================================================
const dadosDW = [
    { id_transacao: 101, id_produto: 1001, uf: 'SP', valor_liquido: 1350.45, data: '2024-10-15' },
    { id_transacao: 102, id_produto: 1002, uf: 'RJ', valor_liquido: 45.00, data: '2024-10-16' },
    { id_transacao: 103, id_produto: 1003, uf: 'SP', valor_liquido: 180.89, data: '2024-10-16' },
    { id_transacao: 104, id_produto: 1004, uf: 'MG', valor_liquido: 405.00, data: '2024-10-17' },
    { id_transacao: 105, id_produto: 1002, uf: 'RJ', valor_liquido: 45.00, data: '2024-10-17' },
    { id_transacao: 106, id_produto: 1001, uf: 'SP', valor_liquido: 1350.45, data: '2024-10-18' },
];

// Tabela Dimensão Produto (Dimensão)
const dimProduto = {
    1001: { nome: 'Notebook X', categoria: 'Eletrônicos' },
    1002: { nome: 'MousePad', categoria: 'Acessórios' },
    1003: { nome: 'Fone Pro', categoria: 'Áudio' },
    1004: { nome: 'Teclado Mec', categoria: 'Periféricos' },
};

console.log("--- 1. Dados Carregados (Data Warehouse) ---");
console.log(`Total de Transações: ${dadosDW.length}`);

// ==============================================================================
// 2. SIMULAÇÃO DE OLAP (Online Analytical Processing)
//    Realizando consultas agregadas (Slice/Dice) usando JS
// ==============================================================================

/**
 * Função que simula a agregação de dados em um "Cubo OLAP".
 * Agrega o valor líquido das vendas por uma dimensão específica (ex: UF, Categoria).
 * @param {Array} data - A tabela Fato (dadosDW).
 * @param {string} dimensionKey - A chave da dimensão para agrupar (ex: 'uf').
 * @returns {Object} Um objeto com os totais agrupados.
 */
function aggregateByDimension(data, dimensionKey) {
    const aggregation = {};

    data.forEach(fato => {
        let key = fato[dimensionKey];

        // Se a dimensão for o produto (id_produto), usamos a dimensão externa para buscar a Categoria
        if (dimensionKey === 'categoria') {
            const produtoInfo = dimProduto[fato.id_produto];
            key = produtoInfo ? produtoInfo.categoria : 'Desconhecido';
        }

        // Soma o valor líquido (o "Fato" numérico)
        if (!aggregation[key]) {
            aggregation[key] = 0;
        }
        aggregation[key] += fato.valor_liquido;
    });

    // Formata os resultados
    return Object.keys(aggregation).map(key => ({
        [dimensionKey]: key,
        total_vendas_liquidas: aggregation[key].toFixed(2) // 2 casas decimais
    }));
}


// AÇÃO 1: Análise por Localização (Dimensão UF)
const analisePorUF = aggregateByDimension(dadosDW, 'uf');
console.log("\n--- 2.1. Análise OLAP: Vendas por Localização (UF) ---");
console.table(analisePorUF);

// AÇÃO 2: Análise por Categoria de Produto (Drill-down na Dimensão Produto)
const analisePorCategoria = aggregateByDimension(dadosDW, 'categoria');
console.log("\n--- 2.2. Análise OLAP: Vendas por Categoria de Produto ---");
console.table(analisePorCategoria);


// ==============================================================================
// 3. METADADOS - Uso e Consulta
// ==============================================================================

// Simulação de Metadados de Negócio (Descrição do Fato principal)
const metadadoVendas = {
    nome: "valor_liquido",
    tipo: "Métrica (Fato)",
    origem: "Calculado em ETL (Valor Bruto - Impostos)",
    definicao_negocio: "Receita final da empresa por transação, fundamental para o cálculo de Margem de Lucro."
};

console.log("\n--- 3. Consulta de Metadado de Negócio ---");
console.log(`Métrica: ${metadadoVendas.nome}`);
console.log(`Definição: ${metadadoVendas.definicao_negocio}`);


console.log("\n✅ Simulação de Carga e Análise OLAP em JavaScript concluída.");