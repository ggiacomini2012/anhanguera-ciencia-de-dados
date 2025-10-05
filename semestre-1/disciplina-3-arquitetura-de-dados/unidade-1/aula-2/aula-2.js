// aula-2.js
// Simulação da Arquitetura de Três Camadas (ANSI/SPARC) e uso de Linguagens de Dados em JavaScript (Node.js)

// =========================================================================
// 1. CAMADA INTERNA (FÍSICA): O SGBD e os Dados Brutos
// =========================================================================

/**
 * Simula a Camada Interna (Física) / SGBD.
 * Armazena os dados brutos e executa comandos DDL/DML.
 */
class SGBDCamadaInterna {
    constructor() {
        // Simula o armazenamento físico em objetos JS (como tabelas no SQL)
        this.dadosFisicos = {};
        console.log("✅ Camada Interna: SGBD (simulado) inicializado.");
    }

    // DDL (Data Definition Language): Criação de Estrutura
    executarDDL(comandoSQL) {
        if (comandoSQL.toUpperCase().startsWith('CREATE TABLE')) {
            const tabela = comandoSQL.split(' ')[2];
            this.dadosFisicos[tabela] = []; // Cria um array vazio para a 'tabela'
            console.log(`   ⚙️ DDL Executado: Tabela '${tabela}' criada.`);
            return true;
        }
        return false;
    }

    // DML (Data Manipulation Language): Inserção e Consulta de Dados
    executarDML(comandoSQL, dados = null) {
        const partes = comandoSQL.toUpperCase().split(' ');
        const comando = partes[0];
        const tabela = partes[2];

        if (comando === 'INSERT' && tabela && dados) {
            if (this.dadosFisicos[tabela]) {
                this.dadosFisicos[tabela].push(dados);
                console.log(`   ➕ DML Executado: Registro inserido em '${tabela}'.`);
                return true;
            }
        } else if (comando === 'SELECT' && tabela) {
            console.log(`   🔍 DML Executado: Buscando dados brutos em '${tabela}'.`);
            // Retorna uma cópia para evitar alteração direta nos dados físicos
            return [...(this.dadosFisicos[tabela] || [])];
        }
        return false;
    }
}

// =========================================================================
// 2. CAMADA CONCEITUAL (LÓGICA): Regras de Negócio
// =========================================================================

/**
 * Simula a Camada Conceitual (Lógica).
 * Define as regras de negócio e usa a Camada Interna.
 */
class CamadaConceitualRegras {
    constructor(sgbd) {
        this.sgbd = sgbd;
        // Assegura que as estruturas existam (Modelo ER / DDL)
        this.sgbd.executarDDL("CREATE TABLE Funcionarios");
        this.sgbd.executarDDL("CREATE TABLE Despesas");
        console.log("🧠 Camada Conceitual: Regras de negócio definidas (Modelo ER).");
    }

    // Função que representa uma regra de negócio e usa DML
    registrarFuncionario(id, nome, departamento, salario) {
        const dados = { id, nome, departamento, salario };
        this.sgbd.executarDML("INSERT INTO Funcionarios", dados);
    }

    // Função de consulta centralizada para a Camada Externa
    obterTodosFuncionarios() {
        return this.sgbd.executarDML("SELECT * FROM Funcionarios");
    }
}

// =========================================================================
// 3. CAMADA EXTERNA (VISÃO): Apresentação Personalizada (Views)
// =========================================================================

/**
 * Simula a Camada Externa (Visão do Usuário).
 * Cria 'Views' personalizadas, resolvendo o problema da empresa.
 */
class CamadaExternaViews {
    constructor(conceitual) {
        this.conceitual = conceitual;
        console.log("🖥️ Camada Externa: Interfaces/APIs prontas para gerar 'Views'.");
    }

    // Simula a 'View' de um departamento específico (RH)
    viewRH() {
        console.log("\n=> VIEW RH (Acesso Personalizado: Nome e Salário)");
        const dadosBrutos = this.conceitual.obterTodosFuncionarios();
        // Filtra e projeta a informação para a VIEW RH (apenas nome e salário)
        return dadosBrutos.map(f => ({
            nome: f.nome,
            salario: f.salario
        }));
    }

    // Simula a 'View' de outro departamento (Operacional)
    viewOperacional() {
        console.log("\n=> VIEW OPERACIONAL (Acesso Personalizado: Sem Salário)");
        const dadosBrutos = this.conceitual.obterTodosFuncionarios();
        // Filtra e projeta a informação para a VIEW Operacional (sem dados sensíveis)
        return dadosBrutos.map(f => ({
            id: f.id,
            nome: f.nome,
            departamento: f.departamento
        })).filter(f => f.departamento !== 'RH'); // Ex: Não precisa ver o RH
    }
}


// =========================================================================
// EXECUÇÃO E DEMONSTRAÇÃO
// =========================================================================
console.log("=================================================================");
console.log("  Início da Simulação JS: Arquitetura de Três Camadas");
console.log("=================================================================");

// 1. Inicialização das Camadas
const sgbd = new SGBDCamadaInterna(); // FÍSICA
const regras = new CamadaConceitualRegras(sgbd); // CONCEITUAL
const views = new CamadaExternaViews(regras); // EXTERNA

console.log("\n--- Processamento de Dados (Camada Conceitual) ---");
// 2. Inserção de Dados (DML)
regras.registrarFuncionario(1, "Ana", "RH", 6200.00);
regras.registrarFuncionario(2, "Beto", "Vendas", 4500.00);
regras.registrarFuncionario(3, "Cintia", "Marketing", 5100.00);

// 3. Consulta de Dados (Camada Externa) - A Solução do Problema
console.log("\n--- Acesso Personalizado: Mitigando Ineficiência Operacional ---");

// Consulta 1: O time de RH solicita a View deles
const dadosRH = views.viewRH();
console.log("\nDados exibidos para o RH:");
console.log(dadosRH); 
/* [ 
  { nome: 'Ana', salario: 6200 }, 
  { nome: 'Beto', salario: 4500 }, 
  { nome: 'Cintia', salario: 5100 } 
]
*/

// Consulta 2: O time de Vendas/Marketing solicita a View Operacional
const dadosOperacionais = views.viewOperacional();
console.log("\nDados exibidos para Vendas/Marketing:");
console.log(dadosOperacionais);
/* [ 
  { id: 2, nome: 'Beto', departamento: 'Vendas' },
  { id: 3, nome: 'Cintia', departamento: 'Marketing' } 
] 
*/

console.log("\n--- Resolução do Problema da Empresa ---");
console.log("A Camada Externa (Views) garante que o RH veja salários (necessidade),");
console.log("enquanto o Operacional vê apenas o necessário (nome, depto),");
console.log("resolvendo a ineficiência de personalização de dados mencionada.");