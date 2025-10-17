#!/bin/bash

# 1. Pega o nome completo do diretório atual (ex: "aula-3")
DIRETORIO_ATUAL=$(basename "$PWD")

# 2. Extrai o número do nome do diretório (ex: "3")
# Usa 'grep' com lookbehind (ou 'sed' para maior compatibilidade)
# Vamos usar 'sed' para extrair o número após "aula-"
NUMERO=$(echo "$DIRETORIO_ATUAL" | sed 's/aula-\([0-9]*\)/\1/')

# Verifica se a extração foi bem-sucedida e se é um diretório 'aula-X'
if [[ ! "$DIRETORIO_ATUAL" =~ ^aula-[0-9]+$ ]]; then
    echo "Erro: Este script deve ser executado em um diretório com o formato 'aula-X', onde X é um número."
    exit 1
fi

if [ -z "$NUMERO" ]; then
    echo "Erro: Não foi possível extrair o número do nome do diretório ($DIRETORIO_ATUAL)."
    exit 1
fi

# 3. Define o prefixo dos arquivos (ex: "aula-3")
PREFIXO="$DIRETORIO_ATUAL"

# 4. Cria os arquivos usando o comando 'touch'
echo "Criando arquivos em: $PWD"
echo "Prefix: $PREFIXO"

touch "${PREFIXO}.js"
touch "${PREFIXO}.sql"
touch "${PREFIXO}.java"

echo "Arquivos criados com sucesso:"
ls "${PREFIXO}."*