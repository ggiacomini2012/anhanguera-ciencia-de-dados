// aula-2.js

/**
 * Normalização de Dados em JavaScript: Um Guia Prático
 *
 * Este script demonstra como aplicar as três primeiras formas normais (1FN, 2FN e 3FN)
 * a um conjunto de dados não normalizado, usando arrays de objetos para simular tabelas
 * de banco de dados. O objetivo é transformar dados redundantes e inconsistentes
 * em um modelo mais limpo, eficiente e robusto.
 */

// --- Dados Iniciais (Tabela Não Normalizada) ---
console.log("--- 📝 Tabela Original (Não Normalizada) ---");

const funcionariosNaoNormalizados = [
  {
    matriculaFunc: "148-9",
    nome: "Jane Anne",
    idCargo: 191,
    descCargo: "Analista Contábil I",
    enderecoCompleto: "Rua das Flores, 101, Curitiba, Contabilidade",
    dataAdmissao: "15/01/2018",
  },
  {
    matriculaFunc: "721-4",
    nome: "Klaus Lins",
    idCargo: 323,
    descCargo: "Assistente de Produção II",
    enderecoCompleto: "Avenida Central, 50, São Paulo, Produção",
    dataAdmissao: "21/11/2017",
  },
  {
    matriculaFunc: "673-2",
    nome: "Sandra Costa",
    idCargo: 101,
    descCargo: "Auxiliar de DP",
    enderecoCompleto: "Praça da Matriz, 25, Santo André, RH",
    dataAdmissao: "03/04/2018",
  },
];

// Função auxiliar para impressão no console
function imprimirTabela(tabela, nome) {
  console.log(`\n✅ Tabela '${nome}':`);
  if (tabela.length === 0) {
    console.log("  (Vazia)");
    return;
  }
  const cabecalhos = Object.keys(tabela[0]);
  console.log(`| ${cabecalhos.join(" | ")} |`);
  console.log(`|${"---".repeat(cabecalhos.length + 1)}|`);
  tabela.forEach(linha => {
    const valores = cabecalhos.map(h => linha[h] || "");
    console.log(`| ${valores.join(" | ")} |`);
  });
}

imprimirTabela(funcionariosNaoNormalizados, "Funcionários Não Normalizados");

// --- Passo 1: Normalização para a Primeira Forma Normal (1FN) ---
console.log("\n--- 🚀 Aplicando a 1FN: Dados Atômicos ---");
/**
 * Problema: O campo 'enderecoCompleto' é não atômico e contém múltiplas informações.
 * Solução: Dividir este campo em colunas mais específicas.
 * Neste exemplo, vamos extrair a cidade e o departamento.
 */
const funcionarios1FN = [];
const cidadesSet = new Set();
const departamentosSet = new Set();

funcionariosNaoNormalizados.forEach(f => {
  // Simulação de extração de dados
  const partes = f.enderecoCompleto.split(", ");
  const cidade = partes[2];
  const departamento = partes[3];
  cidadesSet.add(cidade);
  departamentosSet.add(departamento);

  const novoFuncionario = {
    matriculaFunc: f.matriculaFunc,
    nome: f.nome,
    idCargo: f.idCargo,
    descCargo: f.descCargo,
    cidade: cidade,
    departamento: departamento,
    dataAdmissao: f.dataAdmissao,
  };
  funcionarios1FN.push(novoFuncionario);
});

imprimirTabela(funcionarios1FN, "Funcionários (em 1FN)");

// --- Passo 2: Normalização para a Segunda Forma Normal (2FN) ---
console.log("\n--- 📈 Aplicando a 2FN: Dependência Total ---");
/**
 * Problema: As colunas 'cidade' e 'departamento' dependem da chave primária 'matriculaFunc'
 * de forma parcial, pois são atributos que se repetem. A dependência não é total.
 * Solução: Criar tabelas separadas para Cidades e Departamentos, com suas próprias chaves primárias.
 */
const funcionarios2FN = [];
const tabelaCidades = Array.from(cidadesSet).map((cidade, index) => ({
  idCidade: index + 1,
  nomeCidade: cidade,
}));
const tabelaDepartamentos = Array.from(departamentosSet).map((depto, index) => ({
  idDepto: index + 1,
  nomeDepto: depto,
}));

// Remodelando a tabela de funcionários para referenciar as novas tabelas
funcionarios1FN.forEach(f => {
  const idCidade = tabelaCidades.find(c => c.nomeCidade === f.cidade).idCidade;
  const idDepto = tabelaDepartamentos.find(d => d.nomeDepto === f.departamento).idDepto;
  
  const novoFuncionario = {
    matriculaFunc: f.matriculaFunc,
    nome: f.nome,
    idCargo: f.idCargo,
    descCargo: f.descCargo,
    idCidade: idCidade,
    idDepto: idDepto,
    dataAdmissao: f.dataAdmissao,
  };
  funcionarios2FN.push(novoFuncionario);
});

imprimirTabela(funcionarios2FN, "Funcionários (em 2FN)");
imprimirTabela(tabelaCidades, "Cidades");
imprimirTabela(tabelaDepartamentos, "Departamentos");

// --- Passo 3: Normalização para a Terceira Forma Normal (3FN) ---
console.log("\n--- 🎯 Aplicando a 3FN: Eliminando Dependências Transitivas ---");
/**
 * Problema: A coluna 'descCargo' é transitivamente dependente da chave primária.
 * Ela depende do 'idCargo', que por sua vez depende da 'matriculaFunc'.
 * Solução: Mover a descrição do cargo para uma nova tabela.
 */
const tabelaCargos = new Map();
funcionariosNaoNormalizados.forEach(f => {
  tabelaCargos.set(f.idCargo, f.descCargo);
});

const cargos = Array.from(tabelaCargos, ([idCargo, descCargo]) => ({ idCargo, descCargo }));

const funcionarios3FN = funcionarios2FN.map(f => {
  // Remove a coluna 'descCargo' da tabela de funcionários
  const novoFuncionario = { ...f };
  delete novoFuncionario.descCargo;
  return novoFuncionario;
});

// As tabelas finais, normalizadas, são:
console.log("\n--- ✨ Estado Final: Tabelas Normalizadas ---");
imprimirTabela(funcionarios3FN, "Funcionários Normalizado");
imprimirTabela(cargos, "Cargos");
imprimirTabela(tabelaCidades, "Cidades");
imprimirTabela(tabelaDepartamentos, "Departamentos");

console.log("\n--- Fim do Processo de Normalização ---");