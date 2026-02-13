// aula-1.js

/**
 * Representa a tabela original, não normalizada,
 * do formulário de registro de jogos de um clube de futebol.
 * Esta tabela contém redundâncias e violações das Formas Normais.
 */
const tabelaOriginal = [
  {
    NumeroJogo: 101,
    DataPartida: '2023-10-25',
    LocalJogo: 'Estádio Municipal',
    CidadeLocal: 'Santa Catarina',
    NomeOponente: 'Time A',
    CodigoJogador: 'J001',
    NomeJogador: 'João Silva',
    PosicaoJogador: 'Atacante',
    GolsMarcados: 2,
  },
  {
    NumeroJogo: 102,
    DataPartida: '2023-11-02',
    LocalJogo: 'Arena Olímpica',
    CidadeLocal: 'Rio de Janeiro',
    NomeOponente: 'Time B',
    CodigoJogador: 'J002',
    NomeJogador: 'Maria Santos',
    PosicaoJogador: 'Meio-campo',
    GolsMarcados: 1,
  },
  {
    NumeroJogo: 103,
    DataPartida: '2023-11-10',
    LocalJogo: 'Estádio Municipal',
    CidadeLocal: 'Santa Catarina',
    NomeOponente: 'Time C',
    CodigoJogador: 'J001',
    NomeJogador: 'João Silva',
    PosicaoJogador: 'Atacante',
    GolsMarcados: 0,
  },
  {
    NumeroJogo: 104,
    DataPartida: '2023-11-18',
    LocalJogo: 'Estádio do Morumbi',
    CidadeLocal: 'São Paulo',
    NomeOponente: 'Time D',
    CodigoJogador: 'J003',
    NomeJogador: 'Pedro Rocha',
    PosicaoJogador: 'Defensor',
    GolsMarcados: 3,
  },
  {
    NumeroJogo: 105,
    DataPartida: '2023-11-25',
    LocalJogo: 'Arena Olímpica',
    CidadeLocal: 'Rio de Janeiro',
    NomeOponente: 'Time E',
    CodigoJogador: 'J002',
    NomeJogador: 'Maria Santos',
    PosicaoJogador: 'Meio-campo',
    GolsMarcados: 1,
  },
];

/**
 * Remove duplicatas de um array de objetos com base em uma chave específica.
 * @param {Array<Object>} array O array de objetos.
 * @param {string} key A chave para verificar a unicidade.
 * @returns {Array<Object>} Um novo array sem duplicatas.
 */
const removerDuplicatasPorChave = (array, key) => {
  const chavesVistas = new Set();
  return array.filter((item) => {
    const chave = item[key];
    if (chavesVistas.has(chave)) {
      return false;
    }
    chavesVistas.add(chave);
    return true;
  });
};

/**
 * Simula a normalização para a Segunda Forma Normal (2FN).
 * Separa a tabela original em tabelas menores para eliminar dependências parciais.
 * @param {Array<Object>} dados A tabela de entrada (já em 1FN).
 * @returns {Object} Um objeto contendo as tabelas normalizadas (jogos, jogadores, atuacoes).
 */
const normalizarPara2FN = (dados) => {
  console.log('\n--- Normalização para 2ª Forma Normal (2FN) ---');

  // A chave primária é a combinação de {NumeroJogo, CodigoJogador}.
  // 'NomeJogador' e 'PosicaoJogador' dependem apenas de 'CodigoJogador'. (Dependência Parcial)
  // 'LocalJogo' e 'CidadeLocal' dependem apenas de 'NumeroJogo'. (Dependência Parcial)

  // Tabela JOGOS: Retira as dependências parciais de NumeroJogo.
  const tabelaJogos = removerDuplicatasPorChave(
    dados.map(({ NumeroJogo, DataPartida, LocalJogo, CidadeLocal, NomeOponente }) => ({
      NumeroJogo,
      DataPartida,
      LocalJogo,
      CidadeLocal,
      NomeOponente,
    })),
    'NumeroJogo'
  );

  // Tabela JOGADORES: Retira as dependências parciais de CodigoJogador.
  const tabelaJogadores = removerDuplicatasPorChave(
    dados.map(({ CodigoJogador, NomeJogador, PosicaoJogador }) => ({
      CodigoJogador,
      NomeJogador,
      PosicaoJogador,
    })),
    'CodigoJogador'
  );

  // Tabela ATUACOES: Tabela de ligação que mantém a chave composta e os dados dependentes da chave inteira.
  const tabelaAtuacoes = dados.map(({ NumeroJogo, CodigoJogador, GolsMarcados }) => ({
    NumeroJogo,
    CodigoJogador,
    GolsMarcados,
  }));

  console.log('Tabela JOGOS (separada para 2FN):\n', tabelaJogos);
  console.log('\nTabela JOGADORES (separada para 2FN):\n', tabelaJogadores);
  console.log('\nTabela ATUACOES (tabela de ligação):\n', tabelaAtuacoes);

  return { tabelaJogos, tabelaJogadores, tabelaAtuacoes };
};

/**
 * Simula a normalização para a Terceira Forma Normal (3FN).
 * Separa a tabela de jogos para remover dependências transitivas.
 * @param {Array<Object>} tabelaJogos A tabela de jogos de entrada.
 * @returns {Object} Um objeto contendo as tabelas normalizadas (localizacoes, jogosNormalizada).
 */
const normalizarPara3FN = (tabelaJogos) => {
  console.log('\n--- Normalização para 3ª Forma Normal (3FN) ---');

  // Na tabela 'tabelaJogos', 'CidadeLocal' depende de 'LocalJogo', que não é a chave primária.
  // Isso é uma dependência transitiva.

  // Tabela LOCALIZACOES: Retira a dependência transitiva.
  const tabelaLocalizacoes = removerDuplicatasPorChave(
    tabelaJogos.map(({ LocalJogo, CidadeLocal }) => ({
      LocalJogo,
      CidadeLocal,
    })),
    'LocalJogo'
  );

  // Tabela JOGOS NORMALIZADA: Retira o campo 'CidadeLocal', agora referenciado pela nova tabela.
  const tabelaJogosNormalizada = tabelaJogos.map(
    ({ NumeroJogo, DataPartida, LocalJogo, NomeOponente }) => ({
      NumeroJogo,
      DataPartida,
      LocalJogo,
      NomeOponente,
    })
  );

  console.log('Tabela LOCALIZACOES (separada para 3FN):\n', tabelaLocalizacoes);
  console.log('\nTabela JOGOS_NORMALIZADA (com a dependência removida):\n', tabelaJogosNormalizada);

  return { tabelaLocalizacoes, tabelaJogosNormalizada };
};

// --- Execução do processo de Normalização ---
console.log('--------------------------------------------------');
console.log('    EXEMPLO DE NORMALIZAÇÃO DE DADOS EM JAVASCRIPT    ');
console.log('--------------------------------------------------');
console.log('\n[Tabela Original - Formulário do Clube]\n', tabelaOriginal);

// 1ª Forma Normal: A tabela já está em 1FN.
console.log('\n--- Normalização para 1ª Forma Normal (1FN) ---');
console.log('A tabela original já atende à 1FN, pois não há valores repetidos ou listas em uma única célula.');

// 2ª Forma Normal
const { tabelaJogos, tabelaJogadores, tabelaAtuacoes } = normalizarPara2FN(tabelaOriginal);

// 3ª Forma Normal
const { tabelaLocalizacoes, tabelaJogosNormalizada } = normalizarPara3FN(tabelaJogos);

console.log('\n--------------------------------------------------');
console.log('          PROCESSO DE NORMALIZAÇÃO FINALIZADO       ');
console.log('--------------------------------------------------');
console.log('As tabelas agora estão organizadas e prontas para um banco de dados relacional.');