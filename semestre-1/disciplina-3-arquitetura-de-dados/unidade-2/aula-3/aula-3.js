// aula-3.js
// Exemplo de Armazenamento de Dados e Nuvem em JavaScript (Node.js)
// Simula a estrutura relacional de uma tabela SQL e o acesso assíncrono a dados na nuvem.

// --------------------------------------------------------------------------------------
// 1. Simulação da Estrutura SQL (DDL e Dados DML)
// --------------------------------------------------------------------------------------

// Estrutura da "Tabela" (Similar ao DDL)
const DDL_TABELA = "Projetos_Nuvem (id, nome_projeto, plataforma_nuvem, modelo_servico, custo_mensal)";

// Dados de Manipulação (Similar ao DML INSERT)
const dadosProjetos = [
    { id: 1, nome_projeto: 'Data Lake', plataforma_nuvem: 'Azure', modelo_servico: 'PaaS', custo_mensal: 150.00 },
    { id: 2, nome_projeto: 'Website Institucional', plataforma_nuvem: 'AWS', modelo_servico: 'IaaS', custo_mensal: 45.50 },
    { id: 3, nome_projeto: 'Email Corporativo', plataforma_nuvem: 'GCP', modelo_servico: 'SaaS', custo_mensal: 25.00 },
    { id: 4, nome_projeto: 'Análise de Logs', plataforma_nuvem: 'Azure', modelo_servico: 'PaaS', custo_mensal: 89.90 },
    { id: 5, nome_projeto: 'Serviço de IA', plataforma_nuvem: 'Azure', modelo_servico: 'SaaS', custo_mensal: 210.00 }
];

console.log(`📋 Estrutura de Dados (DDL Simulado): ${DDL_TABELA}`);
console.log(`➕ Total de ${dadosProjetos.length} registros inseridos na simulação.`);

// --------------------------------------------------------------------------------------
// 2. Simulação de Consulta SQL (DML SELECT)
// --------------------------------------------------------------------------------------

/**
 * Simula uma consulta (SELECT) com um predicado (WHERE).
 * @param {string} plataforma - O valor para o filtro (ex: 'Azure').
 * @returns {Array} Lista de projetos filtrados.
 */
function consultarProjetosPorPlataforma(plataforma) {
    console.log(`\n-- Executando DML: Consultando WHERE plataforma_nuvem = '${plataforma}'`);
    return dadosProjetos.filter(projeto => projeto.plataforma_nuvem === plataforma);
}

// --------------------------------------------------------------------------------------
// 3. Funções Agregadas (Simulando SUM, AVG, COUNT)
// --------------------------------------------------------------------------------------

function analisarCustos(projetos) {
    const total = projetos.length;
    
    // Função Agregada SUM
    const somaCustos = projetos.reduce((total, projeto) => total + projeto.custo_mensal, 0);

    // Função Agregada AVG
    const mediaCustos = total > 0 ? somaCustos / total : 0;

    console.log("📊 Análise de Custos para os projetos filtrados:");
    console.log(`  - Número Total de Projetos (COUNT): ${total}`);
    console.log(`  - Custo Mensal Total (SUM): R$ ${somaCustos.toFixed(2)}`);
    console.log(`  - Custo Mensal Médio (AVG): R$ ${mediaCustos.toFixed(2)}`);
}

// --------------------------------------------------------------------------------------
// 4. Conceito de Nuvem: Acesso Assíncrono
// --------------------------------------------------------------------------------------

/**
 * Simula o acesso a um serviço de armazenamento em nuvem (ex: um endpoint REST na Azure).
 * O uso de 'async/await' e 'Promise' reflete a natureza de rede e latência da nuvem.
 */
async function acessarServicoDeNuvem(plataforma) {
    console.log(`\n-- ☁️ Tentando conexão assíncrona ao serviço de Nuvem (${plataforma})...`);
    
    // Simula a latência de rede com um atraso de 1 segundo (1000ms)
    await new Promise(resolve => setTimeout(resolve, 1000)); 

    if (plataforma === 'Azure') {
        const projetosAzure = consultarProjetosPorPlataforma('Azure');
        
        console.log("✅ Conexão bem-sucedida! Dados do Azure recebidos:");
        projetosAzure.forEach(p => console.log(`  - Projeto: ${p.nome_projeto}, Modelo: ${p.modelo_servico}`));
        
        analisarCustos(projetosAzure);
    } else {
        console.log("❌ Falha na conexão ou plataforma não suportada. (Analogia DCL/Permissões)");
    }
}


// --------------------------------------------------------------------------------------
// INÍCIO DA EXECUÇÃO
// --------------------------------------------------------------------------------------
acessarServicoDeNuvem('Azure');