// Exemplo de Armazenamento de Dados em Java: Conexão JDBC e Comandos SQL
// Demonstra a interação robusta de um sistema corporativo (Java) com o SQL,
// um cenário comum ao se conectar a serviços como SQL Server ou SQL Azure.

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

public class Aula3 {

    // URL de Conexão: Simulação de um banco de dados SQLite (como o SQL Azure ou MySQL gerenciado)
    // Para Azure, a URL seria: "jdbc:sqlserver://<serverName>.database.windows.net:1433;databaseName=..."
    private static final String JDBC_URL = "jdbc:sqlite:auladb.db";
    
    // NOTA: Para rodar este código, você precisará do driver JDBC do SQLite (sqlite-jdbc).

    public static void main(String[] args) {
        Connection conn = null;

        try {
            // 1. Conexão (Iniciando a comunicação com o Castelo SQL)
            // Simula o login na plataforma Azure/serviço SQL.
            conn = DriverManager.getConnection(JDBC_URL);
            System.out.println("✅ Conexão JDBC estabelecida com sucesso.");
            conn.setAutoCommit(false); // Inicia o conceito de Transação (DTL)

            // 2. DDL (Data Definition Language) - Criação da Estrutura
            criarTabela(conn);

            // 3. DML (Data Manipulation Language) - Inserção de Dados
            inserirProjetos(conn);

            // 4. DTL (Data Transaction Language) - Confirmação
            conn.commit();
            System.out.println("✅ Transação confirmada (COMMIT). Dados salvos permanentemente.");

            // 5. DML (Data Manipulation Language) - Consulta e Análise
            consultarProjetosAzure(conn);
            
        } catch (SQLException e) {
            System.err.println("❌ Erro SQL detectado: " + e.getMessage());
            // 6. DTL (Reversão em caso de erro)
            if (conn != null) {
                try {
                    conn.rollback();
                    System.out.println("↩️ Transação desfeita (ROLLBACK) devido ao erro.");
                } catch (SQLException ex) {
                    System.err.println("Erro ao reverter: " + ex.getMessage());
                }
            }
        } finally {
            // 7. Finalização (Fechando a conexão com a Nuvem)
            if (conn != null) {
                try {
                    conn.close();
                    System.out.println("\n✅ Conexão SQL encerrada.");
                } catch (SQLException e) {
                    System.err.println("Erro ao fechar a conexão: " + e.getMessage());
                }
            }
        }
    }

    // Método que executa o DDL (CREATE TABLE)
    private static void criarTabela(Connection conn) throws SQLException {
        String sqlDDL = """
            CREATE TABLE IF NOT EXISTS Projetos_Nuvem (
                id INTEGER PRIMARY KEY,
                nome_projeto TEXT NOT NULL,
                plataforma_nuvem TEXT NOT NULL,
                modelo_servico TEXT,
                custo_mensal REAL
            );
        """;
        try (Statement stmt = conn.createStatement()) {
            stmt.execute(sqlDDL);
            System.out.println("\n📋 DDL executado: Tabela 'Projetos_Nuvem' criada ou verificada.");
        }
    }

    // Método que executa o DML (INSERT)
    private static void inserirProjetos(Connection conn) throws SQLException {
        String sqlDML = "INSERT INTO Projetos_Nuvem (nome_projeto, plataforma_nuvem, modelo_servico, custo_mensal) VALUES (?, ?, ?, ?)";
        
        try (PreparedStatement pstmt = conn.prepareStatement(sqlDML)) {
            
            // Inserção 1 (Azure PaaS)
            pstmt.setString(1, "Data Warehouse Central");
            pstmt.setString(2, "Azure");
            pstmt.setString(3, "PaaS");
            pstmt.setDouble(4, 300.50);
            pstmt.executeUpdate();

            // Inserção 2 (GCP IaaS)
            pstmt.setString(1, "Máquinas Virtuais de Teste");
            pstmt.setString(2, "GCP");
            pstmt.setString(3, "IaaS");
            pstmt.setDouble(4, 75.20);
            pstmt.executeUpdate();

            System.out.println("\n➕ DML executado: 2 novos registros inseridos.");
        }
    }

    // Método que executa o DML (SELECT) e funções agregadas
    private static void consultarProjetosAzure(Connection conn) throws SQLException {
        String sqlSelect = "SELECT nome_projeto, modelo_servico, custo_mensal FROM Projetos_Nuvem WHERE plataforma_nuvem = 'Azure'";
        
        try (Statement stmt = conn.createStatement();
             ResultSet rs = stmt.executeQuery(sqlSelect)) {
            
            System.out.println("\n-- Executando DML: Consultando Projetos na Azure (SELECT com WHERE)");
            
            double custoTotalAzure = 0;
            int contador = 0;

            while (rs.next()) {
                String nome = rs.getString("nome_projeto");
                String modelo = rs.getString("modelo_servico");
                double custo = rs.getDouble("custo_mensal");
                
                System.out.println("  - Projeto: " + nome + ", Modelo: " + modelo + ", Custo: R$ " + custo);
                
                custoTotalAzure += custo; // Simula Função Agregada (SUM)
                contador++; // Simula Função Agregada (COUNT)
            }
            
            // Cálculo da média
            double custoMedio = contador > 0 ? custoTotalAzure / contador : 0; // Simula Função Agregada (AVG)

            System.out.println("\n📊 Análise (Funções Agregadas):");
            System.out.println("  - Total de Projetos Azure (COUNT): " + contador);
            System.out.println("  - Custo Total Azure (SUM): R$ " + String.format("%.2f", custoTotalAzure));
            System.out.println("  - Custo Médio Azure (AVG): R$ " + String.format("%.2f", custoMedio));
        }
    }
}