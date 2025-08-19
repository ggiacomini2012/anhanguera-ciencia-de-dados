#!/bin/bash

# ==============================================================================
# SCRIPT PARA CRIAR ESTRUTURA DE AULAS
# ==============================================================================

# Defina o número de aulas que deseja criar
NUM_AULAS=5

# O primeiro argumento ($1) é o diretório de destino.
# Se nenhum argumento for fornecido, use o diretório atual ('.').
DESTINO=${1:-.}

# Loop para criar as pastas e arquivos para cada aula
for i in $(seq 1 $NUM_AULAS); do
  # Define o nome da pasta da aula
  DIRETORIO_AULA="$DESTINO/aula-$i"

  # Cria o diretório (e os pais, se necessário)
  mkdir -p "$DIRETORIO_AULA"
  
  # Cria o arquivo .py e o arquivo .md dentro da pasta
  touch "$DIRETORIO_AULA/aula-$i.py"
  touch "$DIRETORIO_AULA/explicacao.md"
done

echo "Estrutura de diretórios criada com sucesso em '$DESTINO' com $NUM_AULAS aulas."
echo "Para visualizar, use o comando 'tree' no diretório de destino."