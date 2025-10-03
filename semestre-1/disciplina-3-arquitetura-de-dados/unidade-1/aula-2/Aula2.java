// Aula2.java
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;

/**
 * Classe principal para demonstrar a Arquitetura de Três Camadas (ANSI/SPARC).
 */
public class Aula2 {

    public static void main(String[] args) {
        System.out.println("=================================================================");
        System.out.println("  Início da Simulação Java: Arquitetura de Três Camadas");
        System.out.println("=================================================================");

        // 1. Inicialização das Camadas (Bottom-up)
        SGBDCamadaInterna sgbd = new SGBDCamadaInterna();         // Camada Interna (Física)
        CamadaConceitualRegras regras = new CamadaConceitualRegras(sgbd); // Camada Conceitual (Lógica)
        CamadaExternaViews views = new CamadaExternaViews(regras);        // Camada Externa (Visão)

        System.out.println("\n--- Processamento de Dados (Camada Conceitual) ---");
        // 2. Inserção de Dados (DML) via Camada Conceitual
        regras.registrarFuncionario(1, "Daniela", "RH", 6500.00);
        regras.registrarFuncionario(2, "Eduardo", "Financeiro", 7200.00);
        regras.registrarFuncionario(3, "Felipe", "Financeiro", 7100.00);
        regras.registrarFuncionario(4, "Giovana", "Vendas", 4900.00);


        // 3. Consulta de Dados (Camada Externa) - A Solução
        System.out.println("\n--- Acesso Personalizado: Mitigando Ineficiência Operacional ---");

        // Visão do Financeiro (necessita de dados de Salário)
        System.out.println("\n=> VIEW FINANCEIRO (Acesso a Salários)");
        List<Map<String, Object>> dadosFinanceiro = views.viewFinanceiro();
        dadosFinanceiro.forEach(d -> System.out.println("  Financeiro Vê: Nome: " + d.get("nome") + ", Salário: " + d.get("salario")));

        // Visão de Vendas (NÃO pode ver salários, apenas dados operacionais)
        System.out.println("\n=> VIEW VENDAS (Acesso Operacional Sem Salário)");
        List<Map<String, Object>> dadosVendas = views.viewVendasSimples();
        dadosVendas.forEach(d -> System.out.println("  Vendas Vê: Nome: " + d.get("nome") + ", Depto: " + d.get("departamento")));
        
        System.out.println("\n--- Resolução do Problema da Empresa ---");
        System.out.println("As Views (Camada Externa) resolvem a dificuldade de personalização de dados,");
        System.out.println("entregando informações customizadas a cada departamento.");
    }
}

// =========================================================================
// 1. CLASSE CAMADA INTERNA (FÍSICA): O SGBD
// =========================================================================

class SGBDCamadaInterna {
    // Simula o armazenamento físico: um Mapa de 'tabelas' (String) para 'registros' (List<Map>)
    private Map<String, List<Map<String, Object>>> dadosFisicos;

    public SGBDCamadaInterna() {
        this.dadosFisicos = new HashMap<>();
        System.out.println("✅ Camada Interna: SGBD (HashMap) inicializado. Base para DDL/DML.");
    }

    // Simulação de DDL (CREATE TABLE)
    public void executarDDL(String tabela) {
        if (!dadosFisicos.containsKey(tabela)) {
            dadosFisicos.put(tabela, new ArrayList<>());
            System.out.println("   ⚙️ DDL Executado: Tabela '" + tabela + "' criada.");
        }
    }

    // Simulação de DML (INSERT)
    public void executarInsert(String tabela, Map<String, Object> registro) {
        if (dadosFisicos.containsKey(tabela)) {
            dadosFisicos.get(tabela).add(registro);
            System.out.println("   ➕ DML Executado: Registro inserido em '" + tabela + "'.");
        }
    }

    // Simulação de DML (SELECT)
    public List<Map<String, Object>> executarSelect(String tabela) {
        System.out.println("   🔍 DML Executado: Buscando dados brutos em '" + tabela + "'.");
        // Retorna uma cópia para proteger os dados físicos (Desacoplamento)
        return new ArrayList<>(dadosFisicos.getOrDefault(tabela, new ArrayList<>()));
    }
}

// =========================================================================
// 2. CLASSE CAMADA CONCEITUAL (LÓGICA): Regras de Negócio
// =========================================================================

class CamadaConceitualRegras {
    private SGBDCamadaInterna sgbd;

    public CamadaConceitualRegras(SGBDCamadaInterna sgbd) {
        this.sgbd = sgbd;
        // DDL necessário (Garante a estrutura lógica no SGBD físico)
        this.sgbd.executarDDL("Funcionarios"); 
        System.out.println("🧠 Camada Conceitual: Regras de negócio definidas (Modelo ER).");
    }

    // Regra de Negócio que utiliza DML para inserção
    public void registrarFuncionario(int id, String nome, String departamento, double salario) {
        Map<String, Object> dados = new HashMap<>();
        dados.put("id", id);
        dados.put("nome", nome);
        dados.put("departamento", departamento);
        dados.put("salario", salario);
        // Usa o SGBD para persistir os dados
        this.sgbd.executarInsert("Funcionarios", dados);
    }

    // Função de consulta centralizada (API de dados brutos para a Camada Externa)
    public List<Map<String, Object>> obterTodosFuncionarios() {
        return this.sgbd.executarSelect("Funcionarios");
    }
}

// =========================================================================
// 3. CLASSE CAMADA EXTERNA (VISÃO): Views Personalizadas
// =========================================================================

class CamadaExternaViews {
    private CamadaConceitualRegras conceitual;

    public CamadaExternaViews(CamadaConceitualRegras conceitual) {
        this.conceitual = conceitual;
        System.out.println("🖥️ Camada Externa: Interfaces prontas para gerar 'Views'.");
    }

    /**
     * View para o Departamento Financeiro (acesso a dados sensíveis como salário).
     */
    public List<Map<String, Object>> viewFinanceiro() {
        // Pede os dados brutos para a Camada Conceitual
        List<Map<String, Object>> dadosBrutos = this.conceitual.obterTodosFuncionarios();

        // Filtra para o departamento e projeta (seleciona) apenas nome e salário
        return dadosBrutos.stream()
                .filter(d -> "Financeiro".equals(d.get("departamento")))
                .map(d -> {
                    Map<String, Object> viewData = new HashMap<>();
                    viewData.put("nome", d.get("nome"));
                    viewData.put("salario", d.get("salario"));
                    return viewData;
                })
                .collect(Collectors.toList());
    }

    /**
     * View para o Departamento de Vendas (apenas dados operacionais, sem salário).
     */
    public List<Map<String, Object>> viewVendasSimples() {
        // Pede os dados brutos para a Camada Conceitual
        List<Map<String, Object>> dadosBrutos = this.conceitual.obterTodosFuncionarios();

        // Filtra para o departamento e projeta (seleciona) nome e departamento
        return dadosBrutos.stream()
                .filter(d -> "Vendas".equals(d.get("departamento")))
                .map(d -> {
                    Map<String, Object> viewData = new HashMap<>();
                    viewData.put("nome", d.get("nome"));
                    viewData.put("departamento", d.get("departamento"));
                    return viewData;
                })
                .collect(Collectors.toList());
    }
}