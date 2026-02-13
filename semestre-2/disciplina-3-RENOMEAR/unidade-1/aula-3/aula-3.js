// O JavaScript será usado para simular a comunicação entre Cliente e Servidor
// na arquitetura de banco de dados distribuída em Nuvem.

// --- 1. O Servidor na Nuvem (Back-end) ---
// Simulado por um objeto em memória, representando o Banco de Dados Centralizado (Cloud DB)
const cloudInventoryDB = {
    'SKU-100': { nome: 'Camiseta Básica', estoque: 500, preco: 49.90 },
    'SKU-201': { nome: 'Calça Jeans Premium', estoque: 250, preco: 199.90 },
    'SKU-302': { nome: 'Tênis Esportivo', estoque: 800, preco: 249.90 },
};

/**
 * Simula o Servidor de Banco de Dados Cliente-Servidor.
 * Recebe a solicitação do Cliente e processa a lógica de negócio.
 * @param {string} sku - O ID do produto.
 * @returns {object} O status e os dados do inventário.
 */
function getServerInventory(sku) {
    console.log(`\n[SERVIDOR]: Recebida solicitação de inventário para SKU: ${sku}`);
    
    // Simula o tempo de processamento/consulta ao DB em Nuvem (latency)
    // new Promise(resolve => setTimeout(resolve, 100)); 

    const item = cloudInventoryDB[sku];
    
    if (item) {
        // Resposta do Servidor: Retorna o dataset (Estoque e Nome)
        return {
            status: 200,
            data: { 
                nome: item.nome, 
                estoque: item.estoque, 
                preco: item.preco 
            }
        };
    } else {
        // Resposta de Erro do Servidor
        return {
            status: 404,
            message: `Produto SKU ${sku} não encontrado.`
        };
    }
}

/**
 * Simula a transação de venda, garantindo a atomicidade e consistência.
 * @param {string} sku - O ID do produto.
 * @param {number} quantidade - Quantidade a ser vendida.
 * @param {string} cliente - Identificação do cliente (Loja/E-commerce).
 * @returns {object} Status da transação.
 */
function processServerTransaction(sku, quantidade, cliente) {
    console.log(`\n[SERVIDOR]: Recebida transação de ${cliente} para vender ${quantidade} de ${sku}`);
    
    const item = cloudInventoryDB[sku];
    
    if (!item) {
        return { status: 404, message: 'Produto não existe.' };
    }
    
    let novoEstoque = item.estoque;

    // 1. Verificação de Consistência e Isolamento (Regras de Negócio)
    if (novoEstoque >= quantidade) {
        // 2. Atomicidade: A transação é efetuada
        novoEstoque -= quantidade;
        
        // Simula a escrita/commit no Banco de Dados Central (Durabilidade)
        cloudInventoryDB[sku].estoque = novoEstoque;
        
        return { 
            status: 200, 
            message: `Venda de ${quantidade} de ${item.nome} efetuada por ${cliente}.`,
            novoEstoque: novoEstoque
        };
    } else {
        // Simula o Rollback implícito: A transação não é efetuada
        return { 
            status: 400, 
            message: `Estoque insuficiente para ${cliente}. Disponível: ${novoEstoque}.` 
        };
    }
}

// --- 2. Os Clientes (Front-ends) ---

/**
 * Simula o Cliente (Navegador/App PDV da Loja) fazendo uma requisição ao Servidor.
 * @param {string} sku - O ID do produto.
 * @param {string} nomeCliente - O nome do cliente (Loja-SP ou E-commerce).
 */
function clienteConsultaInventario(sku, nomeCliente) {
    console.log(`\n[CLIENTE ${nomeCliente}]: Requisição GET para verificar estoque do SKU ${sku}...`);
    
    const response = getServerInventory(sku);

    if (response.status === 200) {
        console.log(`[CLIENTE ${nomeCliente}]: ✅ Resposta Recebida.`);
        console.log(`   Produto: ${response.data.nome}`);
        console.log(`   Estoque Global Atual: ${response.data.estoque}`);
    } else {
        console.log(`[CLIENTE ${nomeCliente}]: ❌ Erro: ${response.message}`);
    }
    return response.data ? response.data.estoque : 0;
}

/**
 * Simula o Cliente fazendo um pedido de compra (Transação no sistema distribuído).
 */
function clienteRealizaCompra(sku, quantidade, nomeCliente) {
    console.log(`\n[CLIENTE ${nomeCliente}]: Requisição POST para comprar ${quantidade} de ${sku}...`);
    
    const response = processServerTransaction(sku, quantidade, nomeCliente);

    if (response.status === 200) {
        console.log(`[CLIENTE ${nomeCliente}]: ✅ Compra SUCESSO! ${response.message}`);
        console.log(`   Novo estoque no Servidor: ${response.novoEstoque}`);
    } else {
        console.log(`[CLIENTE ${nomeCliente}]: ⛔ Compra FALHOU: ${response.message}`);
    }
}

// ----------------- Fluxo de Simulação em JavaScript -----------------

console.log("========================================================================");
console.log("    SIMULAÇÃO JS: ARQUITETURA CLIENTE-SERVIDOR E DISTRIBUÍDA (NUVEM)    ");
console.log("========================================================================");

// 1. Cliente E-commerce consulta o estoque global antes de exibir a página.
const estoqueInicial = clienteConsultaInventario('SKU-201', 'E-commerce');

// 2. Clientes Distribuídos (Loja-SP e Loja-RJ) fazem vendas simultâneas.
// O Cliente/Loja faz a requisição, e o Servidor (Nuvel) garante a integridade.
clienteRealizaCompra('SKU-201', 5, 'Loja-SP - PDV');
clienteRealizaCompra('SKU-201', 20, 'E-commerce - Pedido');

// 3. Um terceiro Cliente (Loja-RJ) tenta uma grande venda após as anteriores.
// O servidor verifica o estoque atualizado (sincronizado em tempo real).
clienteRealizaCompra('SKU-201', 230, 'Loja-RJ - Venda Grande'); // Deve falhar, estoque em 225 (250 - 5 - 20)

// 4. E-commerce consulta o estoque novamente (Reflexo da sincronização).
clienteConsultaInventario('SKU-201', 'E-commerce');

console.log("\n========================================================================");
console.log("  O JS demonstra como o Cliente (Navegador/App) faz a Requisição e o");
console.log("  Servidor (Nuvel/Back-end) processa a Lógica e sincroniza o dado.");
console.log("========================================================================");