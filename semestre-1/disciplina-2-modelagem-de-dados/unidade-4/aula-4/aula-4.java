import java.sql.Connection;
import java.sql.DatabaseMetaData;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;

public class Aula4 {

    // Simula a URL de conexão com um banco de dados legado
    private static final String DB_URL = "jdbc:sqlite:biblioteca_legado.db";

    public static void main(String[] args) {
        criarBancoLegado();
        realizarEngenhariaReversa();
    }

    /**
     * Cria um banco de dados SQLite para simular um sistema legado.
     */
    private static void criarBancoLegado() {
        try (Connection conn = DriverManager.getConnection(DB_URL);
             var stmt = conn.createStatement()) {

            System.out.println("Criando o banco de dados 'biblioteca_legado.db'...");

            stmt.execute("CREATE TABLE IF NOT EXISTS livros_info (" +
                    "id_livro INTEGER PRIMARY KEY, " +
                    "nome_livro TEXT NOT NULL, " +
                    "nome_do_autor TEXT NOT NULL, " +
                    "ano_de_publ INTEGER)");

            stmt.execute("CREATE TABLE IF NOT EXISTS membros_dados (" +
                    "identif TEXT PRIMARY KEY, " +
                    "nome_membro TEXT NOT NULL)");

            stmt.execute("CREATE TABLE IF NOT EXISTS emprestimos_registros (" +
                    "id_transacao INTEGER PRIMARY KEY, " +
                    "livro_id INTEGER, " +
                    "membro_identificacao TEXT, " +
                    "data_emprestimo TEXT)");

            // Inserindo dados de exemplo
            stmt.execute("INSERT INTO livros_info VALUES (1, 'Java para Iniciantes', 'Jane Doe', 2022)");
            stmt.execute("INSERT INTO membros_dados VALUES ('MEMB123', 'Carlos Souza')");
            stmt.execute("INSERT INTO emprestimos_registros VALUES (101, 1, 'MEMB123', '2023-11-01')");

            System.out.println("Banco de dados criado com sucesso!");

        } catch (SQLException e) {
            System.err.println("Erro ao criar o banco de dados: " + e.getMessage());
        }
    }

    /**
     * Realiza o processo de engenharia reversa no banco de dados legado.
     */
    private static void realizarEngenhariaReversa() {
        System.out.println("\n--- Iniciando a Engenharia Reversa ---");
        try (Connection conn = DriverManager.getConnection(DB_URL)) {

            DatabaseMetaData metaData = conn.getMetaData();

            // Passo 1: Descobrir as tabelas
            System.out.println("\nPasso 1: Descobrindo as tabelas...");
            List<String> tabelas = new ArrayList<>();
            try (ResultSet rs = metaData.getTables(null, null, "%", new String[]{"TABLE"})) {
                while (rs.next()) {
                    tabelas.add(rs.getString("TABLE_NAME"));
                }
            }
            System.out.println("Tabelas encontradas: " + tabelas);

            // Passo 2: Analisar a estrutura de cada tabela
            System.out.println("\nPasso 2: Analisando a estrutura e colunas...");
            for (String tabela : tabelas) {
                System.out.println("\nDetalhes da tabela '" + tabela + "':");
                try (ResultSet rs = metaData.getColumns(null, null, tabela, null)) {
                    while (rs.next()) {
                        String nomeColuna = rs.getString("COLUMN_NAME");
                        String tipoColuna = rs.getString("TYPE_NAME");
                        System.out.println("  Coluna: " + nomeColuna + ", Tipo: " + tipoColuna);
                    }
                }
            }

            // Passo 3: Identificar chaves estrangeiras (simulando a lógica de negócio)
            System.out.println("\nPasso 3: Inferindo relacionamentos (Chaves Estrangeiras)...");
            System.out.println("-> A coluna 'livro_id' na tabela 'emprestimos_registros' provavelmente é uma chave estrangeira para 'id_livro' em 'livros_info'.");
            System.out.println("-> A coluna 'membro_identificacao' na tabela 'emprestimos_registros' provavelmente é uma chave estrangeira para 'identif' em 'membros_dados'.");

            // Passo 4: Geração do modelo conceitual (impressão de um resumo)
            System.out.println("\nPasso 4: Criando o novo modelo lógico (resumo):");
            System.out.println("  - Entidade Livro (id_livro, nome_livro, nome_do_autor, ano_de_publ)");
            System.out.println("  - Entidade Membro (identif, nome_membro)");
            System.out.println("  - Entidade Empréstimo (id_transacao, livro_id, membro_identificacao, data_emprestimo)");
            System.out.println("  - Relacionamento 1:N entre Livro e Empréstimo");
            System.out.println("  - Relacionamento 1:N entre Membro e Empréstimo");

        } catch (SQLException e) {
            System.err.println("Erro durante a engenharia reversa: " + e.getMessage());
        }
        System.out.println("\n--- Engenharia Reversa concluída. Novo modelo de dados definido. ---");
    }
}