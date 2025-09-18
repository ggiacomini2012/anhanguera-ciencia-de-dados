// aula-2.java

import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.HashMap;
import java.util.Set;
import java.util.HashSet;
import java.util.stream.Collectors;

/**
 * Normalização de Dados em Java
 *
 * Este programa demonstra o processo de normalização de um conjunto de dados.
 * Ele simula a aplicação das três primeiras formas normais (1FN, 2FN e 3FN)
 * em uma 'tabela' de funcionários, transformando-a em um modelo relacional
 * mais eficiente e sem redundâncias.
 */
public class aula2 {

    // Classe interna para simular o modelo de dados de um funcionário antes da normalização
    static class FuncionarioNaoNormalizado {
        public String matriculaFunc;
        public String nome;
        public int idCargo;
        public String descCargo;
        public String enderecoCompleto; // Exemplo de campo não atômico
        public String dataAdmissao;

        public FuncionarioNaoNormalizado(String matriculaFunc, String nome, int idCargo, String descCargo, String enderecoCompleto, String dataAdmissao) {
            this.matriculaFunc = matriculaFunc;
            this.nome = nome;
            this.idCargo = idCargo;
            this.descCargo = descCargo;
            this.enderecoCompleto = enderecoCompleto;
            this.dataAdmissao = dataAdmissao;
        }

        @Override
        public String toString() {
            return String.format("| %s | %s | %d | %s | %s | %s |",
                matriculaFunc, nome, idCargo, descCargo, enderecoCompleto, dataAdmissao);
        }
    }

    // Classe para representar a tabela de funcionários após a 3FN
    static class Funcionario {
        public String matriculaFunc;
        public String nome;
        public int idCargo; // Chave estrangeira
        public int idCidade; // Chave estrangeira
        public String dataAdmissao;

        public Funcionario(String matriculaFunc, String nome, int idCargo, int idCidade, String dataAdmissao) {
            this.matriculaFunc = matriculaFunc;
            this.nome = nome;
            this.idCargo = idCargo;
            this.idCidade = idCidade;
            this.dataAdmissao = dataAdmissao;
        }
        
        @Override
        public String toString() {
            return String.format("| %s | %s | %d | %d | %s |",
                matriculaFunc, nome, idCargo, idCidade, dataAdmissao);
        }
    }
    
    // Classe para a tabela de cargos
    static class Cargo {
        public int idCargo;
        public String descricao;

        public Cargo(int idCargo, String descricao) {
            this.idCargo = idCargo;
            this.descricao = descricao;
        }

        @Override
        public String toString() {
            return String.format("| %d | %s |", idCargo, descricao);
        }
    }

    // Classe para a tabela de cidades
    static class Cidade {
        public int idCidade;
        public String nome;

        public Cidade(int idCidade, String nome) {
            this.idCidade = idCidade;
            this.nome = nome;
        }

        @Override
        public String toString() {
            return String.format("| %d | %s |", idCidade, nome);
        }
    }
    
    // Método auxiliar para imprimir tabelas no console
    public static <T> void imprimirTabela(String nome, List<T> tabela) {
        System.out.println("\n✅ Tabela '" + nome + "':");
        if (tabela.isEmpty()) {
            System.out.println("  (Vazia)");
            return;
        }
        
        // Impressão do cabeçalho
        if (tabela.get(0) instanceof FuncionarioNaoNormalizado) {
            System.out.println("| matriculaFunc | nome | idCargo | descCargo | enderecoCompleto | dataAdmissao |");
        } else if (tabela.get(0) instanceof Funcionario) {
            System.out.println("| matriculaFunc | nome | idCargo | idCidade | dataAdmissao |");
        } else if (tabela.get(0) instanceof Cargo) {
            System.out.println("| idCargo | descricao |");
        } else if (tabela.get(0) instanceof Cidade) {
            System.out.println("| idCidade | nome |");
        }
        
        System.out.println("----------------------------------------------------------------------");
        
        // Impressão das linhas
        for (T item : tabela) {
            System.out.println(item.toString());
        }
    }

    public static void main(String[] args) {
        
        // --- Dados Iniciais (Tabela Não Normalizada) ---
        System.out.println("--- 📝 Tabela Original (Não Normalizada) ---");
        List<FuncionarioNaoNormalizado> tabelaNaoNormalizada = new ArrayList<>();
        tabelaNaoNormalizada.add(new FuncionarioNaoNormalizado("148-9", "Jane Anne", 191, "Analista Contábil I", "Rua das Flores, 101, Curitiba, Contabilidade", "15/01/2018"));
        tabelaNaoNormalizada.add(new FuncionarioNaoNormalizado("721-4", "Klaus Lins", 323, "Assistente de Produção II", "Avenida Central, 50, São Paulo, Produção", "21/11/2017"));
        tabelaNaoNormalizada.add(new FuncionarioNaoNormalizado("673-2", "Sandra Costa", 101, "Auxiliar de DP", "Praça da Matriz, 25, Santo André, RH", "03/04/2018"));
        
        imprimirTabela("Funcionários Não Normalizados", tabelaNaoNormalizada);

        // --- Passo 1: Normalização para a Primeira Forma Normal (1FN) ---
        System.out.println("\n--- 🚀 Aplicando a 1FN: Dados Atômicos ---");
        /*
         * Problema: O campo 'enderecoCompleto' não é atômico.
         * Solução: Separar a cidade e o departamento em campos próprios.
         * Neste exemplo, também faremos a migração para tabelas separadas.
         */
        Map<String, Integer> cidadesMap = new HashMap<>();
        List<Cidade> tabelaCidades = new ArrayList<>();
        int cidadeIdCounter = 1;

        Map<String, Integer> departamentosMap = new HashMap<>();
        List<Cargo> tabelaCargos = new ArrayList<>(); // Usaremos para a 2FN/3FN

        List<FuncionarioNaoNormalizado> tabela1FN = new ArrayList<>();
        
        for (FuncionarioNaoNormalizado f : tabelaNaoNormalizada) {
            // Extração da cidade
            String[] partesEndereco = f.enderecoCompleto.split(", ");
            String cidadeNome = partesEndereco[2];
            
            if (!cidadesMap.containsKey(cidadeNome)) {
                cidadesMap.put(cidadeNome, cidadeIdCounter);
                tabelaCidades.add(new Cidade(cidadeIdCounter, cidadeNome));
                cidadeIdCounter++;
            }
        }
        
        // O resultado da 1FN será a separação das tabelas
        imprimirTabela("Cidades (em 1FN)", tabelaCidades);
        // A tabela de funcionários ainda não está completamente normalizada, mas o campo foi tratado.
        
        // --- Passo 2 & 3: Normalização para a Segunda e Terceira Forma Normal (2FN e 3FN) ---
        System.out.println("\n--- 📈🎯 Aplicando a 2FN e 3FN: Dependência Total e Eliminação de Transitividade ---");
        /*
         * Problema: Os campos 'descCargo' e 'enderecoCompleto' dependem de outras colunas, não da chave primária.
         * Solução: Criar tabelas separadas para Cargos e Departamentos.
         */
        
        // Criando a tabela de Cargos (3FN)
        for (FuncionarioNaoNormalizado f : tabelaNaoNormalizada) {
            if (tabelaCargos.stream().noneMatch(c -> c.idCargo == f.idCargo)) {
                tabelaCargos.add(new Cargo(f.idCargo, f.descCargo));
            }
        }
        
        // Agora, construímos a tabela final de funcionários, sem redundâncias
        List<Funcionario> tabelaFuncionariosNormalizada = new ArrayList<>();
        for (FuncionarioNaoNormalizado f : tabelaNaoNormalizada) {
            String[] partesEndereco = f.enderecoCompleto.split(", ");
            String cidadeNome = partesEndereco[2];
            int idCidade = cidadesMap.get(cidadeNome);
            
            tabelaFuncionariosNormalizada.add(new Funcionario(f.matriculaFunc, f.nome, f.idCargo, idCidade, f.dataAdmissao));
        }

        // --- Estado Final: Tabelas Normalizadas ---
        System.out.println("\n--- ✨ Estado Final: Tabelas Normalizadas ---");
        imprimirTabela("Funcionários Normalizado", tabelaFuncionariosNormalizada);
        imprimirTabela("Cargos", tabelaCargos);
        imprimirTabela("Cidades", tabelaCidades);
        
        System.out.println("\n--- Fim do Processo de Normalização ---");
    }
}