// --- 1. SIMULANDO A EXTRAÇÃO (ODS Bruto) ---
// Dados de vendas transacionais com inconsistências (Ex: regiões não padronizadas).
console.log("1. EXTRAÇÃO: Capturando dados brutos (ODS)");

const dadosODS = [
    { id: 101, data: '2025-09-01', regiao: 'sudeste', produto: 'TV 50', valorBruto: 2500.50, qtd: 1 },
    { id: 102, data: '2025-09-01', regiao: 'Sudeste', produto: 'FONE Bluetooth', valorBruto: 150.00, qtd: 2 },
    { id: 103, data: '2025-09-02', regiao: 'NORTE', produto: 'TV 50', valorBruto: 2500.50, qtd: 1 },
    { id: 104, data: '2025-09-02', regiao: 'Norte', produto: 'FONE Bluetooth', valorBruto: 150.00, qtd: 3 },
    { id: 105, data: '2025-09-03', regiao: 'SUL', produto: 'TV 50', valorBruto: 2500.50, qtd: 1 },
    { id: 106, data: '2025-09-03', regiao: 'sul', produto: 'FONE Bluetooth', valorBruto: 150.00, qtd: 4 },
];

console.log(`Total de Transações no ODS: ${dadosODS.length}`);
console.log('--------------------------------------------------');


// --- 2. ETAPA DE TRANSFORMAÇÃO (T) - Preparação para o DW ---

console.log("2. TRANSFORMAÇÃO: Limpeza, Padronização e Enriquecimento");

// Função T1: Padroniza o texto (primeira letra maiúscula) e calcula a Receita Total
const transformarDados = (dados) => {
    return dados.map(item => {
        // Padronização da Região (Limpeza de Dados)
        const regiaoPadronizada = item.regiao.charAt(0).toUpperCase() + item.regiao.slice(1).toLowerCase();
        
        // Cálculo de Métrica (Enriquecimento)
        const receitaTotal = item.valorBruto * item.qtd;

        // Retorna o objeto limpo e enriquecido (Pronto para o DW)
        return {
            data: item.data,
            regiao: regiaoPadronizada,
            produto: item.produto,
            quantidade: item.qtd,
            receita: receitaTotal.toFixed(2) // Formatado para 2 casas decimais
        };
    });
};

const dadosDW = transformarDados(dadosODS);

console.log("Dados Transformados (Pronto para DW):\n", dadosDW);
console.log('--------------------------------------------------');

// --- 3. SIMULANDO CONSULTA/RELATÓRIO (Agregação com JavaScript) ---
// Implementação do GROUP BY e SUM (como faríamos com SQL)

console.log("3. CONSULTA ANALÍTICA: Agregação (Simulando SQL GROUP BY)");

const agregadorReceitaPorRegiao = (dados) => {
    // Usamos 'reduce' para iterar e agrupar os dados
    const agregacao = dados.reduce((acumulador, item) => {
        const regiao = item.regiao;
        const receita = parseFloat(item.receita);

        // Se a região já existe no acumulador, adiciona a receita
        if (acumulador[regiao]) {
            acumulador[regiao] += receita;
        } else {
            // Se a região for nova, inicializa com a receita atual
            acumulador[regiao] = receita;
        }
        return acumulador;
    }, {}); // O objeto inicial de agregação

    // Converte o objeto de volta para um array para fácil visualização em relatório
    return Object.keys(agregacao).map(regiao => ({
        regiao: regiao,
        receita_total: `R$ ${agregacao[regiao].toFixed(2)}`
    }));
};

const relatorioReceita = agregadorReceitaPorRegiao(dadosDW);

console.log("\nInsight para Relatório: Receita Total por Região (Simulação GROUP BY):");
console.table(relatorioReceita);

// --- 4. CONCLUSÃO PARA TOMADA DE DECISÃO ---
console.log('--------------------------------------------------');
console.log("Decisão Acionável:");
if (relatorioReceita.length > 0) {
    // Busca a região de maior receita para direcionar investimentos
    let maiorReceita = relatorioReceita.reduce((prev, current) => 
        (parseFloat(prev.receita_total.replace('R$ ', '').replace(',', '')) > parseFloat(current.receita_total.replace('R$ ', '').replace(',', ''))) ? prev : current
    );
    console.log(`A região com maior performance é ${maiorReceita.regiao}. Estratégia: Analisar campanhas de sucesso nesta região e replicá-las nas demais.`);
} else {
    console.log("Nenhum dado processado para análise.");
}