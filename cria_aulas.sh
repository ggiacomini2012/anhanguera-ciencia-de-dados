#!/bin/bash

# ==============================================================================
# SCRIPT PARA CRIAR ESTRUTURA DE AULAS POR UNIDADE (Versão Interativa)
# ==============================================================================

# Defina o número de unidades e aulas
NUM_UNIDADES=4
NUM_AULAS_POR_UNIDADE=5

# O primeiro argumento ($1) é o diretório de destino.
DESTINO=${1:-.}

# Pergunta o nome da disciplina e lê a entrada do usuário
echo "Qual o nome da disciplina que você deseja criar?"
read NOME_DISCIPLINA

# Checa se o nome da disciplina foi fornecido
if [ -z "$NOME_DISCIPLINA" ]; then
  echo "Erro: O nome da disciplina não pode ser vazio."
  exit 1
fi

# Cria o diretório principal da disciplina
DIRETORIO_PRINCIPAL="$DESTINO/$NOME_DISCIPLINA"
mkdir -p "$DIRETORIO_PRINCIPAL"

# Loop para criar as pastas de cada unidade
for u in $(seq 1 $NUM_UNIDADES); do
  # Define o nome da pasta da unidade
  DIRETORIO_UNIDADE="$DIRETORIO_PRINCIPAL/unidade-$u"
  mkdir -p "$DIRETORIO_UNIDADE"

  # Loop aninhado para criar as pastas e arquivos de cada aula
  for a in $(seq 1 $NUM_AULAS_POR_UNIDADE); do
    DIRETORIO_AULA="$DIRETORIO_UNIDADE/aula-$a"
    mkdir -p "$DIRETORIO_AULA"
    
    # Cria os arquivos .py e .md dentro da pasta da aula
    touch "$DIRETORIO_AULA/aula-$a.py"
    touch "$DIRETORIO_AULA/explicacao.md"
  done
done

echo "Estrutura de diretórios criada com sucesso em '$DIRETORIO_PRINCIPAL'."