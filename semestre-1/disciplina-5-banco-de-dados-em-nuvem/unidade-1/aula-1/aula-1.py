"""
exemplo_cloud_db.py

Este script ilustra, de forma simples, alguns conceitos da aula:

- Diferença entre infraestrutura local (on-premise) e banco de dados em nuvem.
- Escalabilidade / elasticidade: a nuvem cresce e encolhe conforme a demanda.
- Impacto de picos de uso nos custos.

Obs.: Os valores de custo são APENAS ilustrativos, não representam preços reais.
"""

from dataclasses import dataclass
from typing import List, Dict


# ==========================
# Modelos de infraestrutura
# ==========================

@dataclass
class OnPremiseDB:
    """
    Simula um banco de dados local (servidor próprio).
    - custo_inicial: compra de hardware, licenças, etc.
    - custo_mensal_manutencao: energia, equipe de TI, refrigeração, etc.
    - capacidade_max_conexoes: limite "fixo" de conexões simultâneas suportadas.
    """
    custo_inicial: float
    custo_mensal_manutencao: float
    capacidade_max_conexoes: int

    def custo_total(self, meses: int) -> float:
        return self.custo_inicial + self.custo_mensal_manutencao * meses

    def suporta_carga(self, conexoes_simultaneas: int) -> bool:
        return conexoes_simultaneas <= self.capacidade_max_conexoes


@dataclass
class CloudDB:
    """
    Simula um banco de dados em nuvem (modelo pay-as-you-go).
    - custo_base_mensal: plano mínimo ou custos fixos.
    - custo_por_conexao_extra: quanto custa, por mês, cada "unidade" de capacidade (por ex. vCPU, conexão, etc.).
    - capacidade_incluida: capacidade básica já inclusa no plano.
    A ideia é: se você precisar de mais capacidade, paga a mais, mas não precisa comprar servidor novo.
    """
    custo_base_mensal: float
    custo_por_conexao_extra: float
    capacidade_incluida: int

    def custo_mensal_para_carga(self, conexoes_simultaneas: int) -> float:
        if conexoes_simultaneas <= self.capacidade_incluida:
            return self.custo_base_mensal

        extras = conexoes_simultaneas - self.capacidade_incluida
        return self.custo_base_mensal + extras * self.custo_por_conexao_extra

    def suporta_carga(self, conexoes_simultaneas: int) -> bool:
        # Na nuvem assumimos que sempre é possível aumentar a capacidade,
        # desde que você esteja disposto a pagar por isso.
        return True


# ==========================
# Funções de simulação
# ==========================

def simular_cenario(
    on_premise: OnPremiseDB,
    cloud: CloudDB,
    meses: int,
    cargas_mensais: List[int],
) -> Dict[str, float]:
    """
    Recebe:
      - on_premise: instancia de OnPremiseDB
      - cloud: instância de CloudDB
      - meses: quantos meses simular
      - cargas_mensais: lista com o número de conexões simultâneas em cada mês

    Retorna um dicionário com estatísticas de custo.
    """

    # Garantia: se a lista de cargas for menor que a quantidade de meses,
    # repete o último valor.
    if len(cargas_mensais) < meses:
        cargas_mensais = cargas_mensais + [cargas_mensais[-1]] * (meses - len(cargas_mensais))

    # Custo on-premise é simples: custo inicial + manutenção mensal fixa
    custo_total_on_prem = on_premise.custo_total(meses)

    # Na nuvem, calculamos mês a mês dependendo da carga
    custos_mensais_cloud = []
    for carga in cargas_mensais[:meses]:
        custo_mes = cloud.custo_mensal_para_carga(carga)
        custos_mensais_cloud.append(custo_mes)

    custo_total_cloud = sum(custos_mensais_cloud)

    # Contar quantas vezes a infraestrutura local não aguenta a carga
    meses_sobrecarga_on_prem = sum(
        1 for carga in cargas_mensais[:meses] if not on_premise.suporta_carga(carga)
    )

    resultado = {
        "custo_total_on_premise": custo_total_on_prem,
        "custo_total_cloud": custo_total_cloud,
        "meses_sobrecarga_on_premise": meses_sobrecarga_on_prem,
    }

    return resultado


def imprimir_relatorio(
    on_premise: OnPremiseDB,
    cloud: CloudDB,
    meses: int,
    cargas_mensais: List[int],
    titulo: str,
) -> None:
    """
    Executa a simulação e imprime resultados de forma amigável.
    """

    print("\n" + "=" * 70)
    print(titulo)
    print("=" * 70)

    print("\nConfiguração On-Premise:")
    print(f" - Custo inicial: R$ {on_premise.custo_inicial:,.2f}")
    print(f" - Custo mensal de manutenção: R$ {on_premise.custo_mensal_manutencao:,.2f}")
    print(f" - Capacidade máxima de conexões: {on_premise.capacidade_max_conexoes}")

    print("\nConfiguração Cloud:")
    print(f" - Custo base mensal: R$ {cloud.custo_base_mensal:,.2f}")
    print(f" - Custo por conexão extra (acima da capacidade incluída): R$ {cloud.custo_por_conexao_extra:,.2f}")
    print(f" - Capacidade incluída: {cloud.capacidade_incluida} conexões")

    resultado = simular_cenario(on_premise, cloud, meses, cargas_mensais)

    print("\nResumo da simulação:")
    print(f" - Período simulado: {meses} meses")
    print(f" - Cargas mensais simuladas (conexões simultâneas): {cargas_mensais[:meses]}")
    print(f" - Custo total On-Premise no período: R$ {resultado['custo_total_on_premise']:,.2f}")
    print(f" - Custo total Cloud no período:      R$ {resultado['custo_total_cloud']:,.2f}")
    print(f" - Meses em que On-Premise não suportou a carga: {resultado['meses_sobrecarga_on_premise']}")

    if resultado["custo_total_cloud"] < resultado["custo_total_on_premise"]:
        print("\n💡 Nesta simulação, a NUVEM foi mais econômica.")
    else:
        print("\n💡 Nesta simulação, a INFRAESTRUTURA LOCAL foi mais econômica.")

    if resultado["meses_sobrecarga_on_premise"] > 0:
        print(
            "⚠️ Atenção: houve meses em que o servidor local não aguentou a carga.\n"
            "   Isso pode significar indisponibilidade ou lentidão para os usuários."
        )
    else:
        print("✅ O servidor local suportou a carga em todos os meses simulados.")


# ==========================
# Função principal
# ==========================

def main():
    # Exemplo 1: carga estável (empresa pequena, crescimento previsível)
    on_premise_estavel = OnPremiseDB(
        custo_inicial=50000.0,             # compra de servidor + licenças
        custo_mensal_manutencao=3000.0,    # energia, equipe de TI, etc.
        capacidade_max_conexoes=200,       # até 200 conexões simultâneas
    )

    cloud_estavel = CloudDB(
        custo_base_mensal=2500.0,          # plano base na nuvem
        custo_por_conexao_extra=10.0,      # cada conexão extra é tarifada
        capacidade_incluida=100,           # 100 conexões já inclusas
    )

    cargas_estaveis = [80, 90, 100, 110, 95, 105, 120, 130, 110, 100, 90, 85]

    imprimir_relatorio(
        on_premise=on_premise_estavel,
        cloud=cloud_estavel,
        meses=12,
        cargas_mensais=cargas_estaveis,
        titulo="Cenário 1: Carga relativamente estável (startup em crescimento controlado)",
    )

    # Exemplo 2: carga com picos (startup que viraliza)
    on_premise_picos = OnPremiseDB(
        custo_inicial=80000.0,             # investe ainda mais em hardware para tentar aguentar picos
        custo_mensal_manutencao=3500.0,
        capacidade_max_conexoes=400,
    )

    cloud_picos = CloudDB(
        custo_base_mensal=3000.0,
        custo_por_conexao_extra=12.0,
        capacidade_incluida=150,
    )

    cargas_com_picos = [120, 140, 160, 180, 200, 800, 900, 400, 350, 300, 250, 200]

    imprimir_relatorio(
        on_premise=on_premise_picos,
        cloud=cloud_picos,
        meses=12,
        cargas_mensais=cargas_com_picos,
        titulo="Cenário 2: Carga com picos (aplicativo viraliza em alguns meses)",
    )


if __name__ == "__main__":
    main()
