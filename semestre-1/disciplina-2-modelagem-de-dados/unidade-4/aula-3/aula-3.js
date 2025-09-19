// Exemplificando as Formas Normais de Boyce-Codd (FNBC) e 4FN com JavaScript

// =============================================================================
// Introdução
// =============================================================================
// A normalização não é apenas um conceito de banco de dados, mas uma filosofia
// de organização de dados que pode ser aplicada em qualquer contexto, incluindo
// a manipulação de objetos e arrays em JavaScript.

console.log("---");
console.log("Iniciando a demonstração de normalização em JavaScript...");
console.log("---");

// =============================================================================
// Exemplo 1: Forma Normal de Boyce-Codd (FNBC)
// =============================================================================
// A FNBC resolve anomalias onde um atributo não-chave determina outro atributo,
// mas esse determinante não é uma chave candidata. A solução é separar os dados.

console.log("### Exemplo da FNBC: O Caso do Aluno e do Professor ###");

// Cenário inicial: Dados aninhados ou em uma única estrutura que violam a FNBC.
// A informação do professor depende da sala, e a sala depende do professor.
// Isso gera uma dependência problemática.

const dadosAlunoAntesFNBC = [
  {
    nomeFilho: 'João',
    enderecoFilho: 'Rua A',
    dataNascimento: '10/01/2015',
    escola: {
      nomeEscola: 'Escola X',
      sala: {
        numeroSala: '101',
        nomeProfessor: 'Prof. Ana'
      }
    }
  },
  {
    nomeFilho: 'Maria',
    enderecoFilho: 'Rua B',
    dataNascimento: '15/05/2016',
    escola: {
      nomeEscola: 'Escola Y',
      sala: {
        numeroSala: '205',
        nomeProfessor: 'Prof. Carlos'
      }
    }
  },
  {
    nomeFilho: 'Pedro',
    enderecoFilho: 'Rua C',
    dataNascimento: '20/09/2017',
    escola: {
      nomeEscola: 'Escola X',
      sala: {
        numeroSala: '101',
        nomeProfessor: 'Prof. Ana'
      }
    }
  }
];

console.log("\nDados iniciais (violando a FNBC):");
console.log(JSON.stringify(dadosAlunoAntesFNBC, null, 2));

// Ação: Normalizar os dados, separando as entidades.
// A entidade "Filho" terá apenas o ID da sala.
// A entidade "Sala" conterá a relação entre sala e professor.

const alunosNormalizados = [
  { id: 1, nomeFilho: 'João', enderecoFilho: 'Rua A', dataNascimento: '10/01/2015', idSala: '101' },
  { id: 2, nomeFilho: 'Maria', enderecoFilho: 'Rua B', dataNascimento: '15/05/2016', idSala: '205' },
  { id: 3, nomeFilho: 'Pedro', enderecoFilho: 'Rua C', dataNascimento: '20/09/2017', idSala: '101' }
];

const salasNormalizadas = [
  { id: '101', nomeEscola: 'Escola X', nomeProfessor: 'Prof. Ana' },
  { id: '205', nomeEscola: 'Escola Y', nomeProfessor: 'Prof. Carlos' }
];

console.log("\nDados normalizados - Alunos (na FNBC):");
console.log(alunosNormalizados);

console.log("\nDados normalizados - Salas (na FNBC):");
console.log(salasNormalizadas);

console.log("\n--> Observação: Separamos a dependência. Agora, a alteração de um professor afeta apenas o objeto 'sala' correspondente, não exigindo a duplicação de dados em todos os registros de alunos.");
console.log("---");

// =============================================================================
// Exemplo 2: Quarta Forma Normal (4FN)
// =============================================================================
// A 4FN lida com dependências multivaloradas. Isso ocorre quando uma única tabela
// tenta conter mais de um "fato" multivalorado sobre a mesma entidade.

console.log("### Exemplo da 4FN: O Histórico de Compras ###");

// Cenário inicial: A tabela de compras mistura fornecedores, produtos e compradores.
// O mesmo fornecedor pode ter vários produtos e vários compradores.
// Isso cria repetição desnecessária.

const comprasAntes4FN = [
  { codFornecedor: 101, codProduto: 'BA3', codComprador: '01' },
  { codFornecedor: 102, codProduto: 'CJ10', codComprador: '05' },
  { codFornecedor: 110, codProduto: '88A', codComprador: '25' },
  { codFornecedor: 530, codProduto: 'BA3', codComprador: '01' },
  { codFornecedor: 101, codProduto: 'BA3', codComprador: '25' } // Aqui, a informação do produto 'BA3' para o fornecedor 101 se repete, mas para outro comprador.
];

console.log("\nDados iniciais (violando a 4FN):");
console.log(comprasAntes4FN);

// Ação: Normalizar os dados, dividindo a tabela em duas.
// Uma para a relação entre Fornecedor e Produto.
// Outra para a relação entre Fornecedor e Comprador.

const fornecedorProdutos = [
  { codFornecedor: 101, codProduto: 'BA3' },
  { codFornecedor: 102, codProduto: 'CJ10' },
  { codFornecedor: 110, codProduto: '88A' },
  { codFornecedor: 530, codProduto: 'BA3' }
];

const fornecedorCompradores = [
  { codFornecedor: 101, codComprador: '01' },
  { codFornecedor: 102, codComprador: '05' },
  { codFornecedor: 110, codComprador: '25' },
  { codFornecedor: 530, codComprador: '01' },
  { codFornecedor: 101, codComprador: '25' }
];

console.log("\nDados normalizados - Fornecedor e seus Produtos (na 4FN):");
console.log(fornecedorProdutos);

console.log("\nDados normalizados - Fornecedor e seus Compradores (na 4FN):");
console.log(fornecedorCompradores);

console.log("\n--> Observação: A separação dos dados elimina a redundância. Se um fornecedor começar a vender um novo produto, adicionamos apenas uma linha na tabela 'fornecedorProdutos', sem precisar repetir a informação do comprador.");
console.log("---");
console.log("Fim da demonstração. A normalização simplifica a estrutura e melhora a integridade dos dados, independentemente da linguagem!");