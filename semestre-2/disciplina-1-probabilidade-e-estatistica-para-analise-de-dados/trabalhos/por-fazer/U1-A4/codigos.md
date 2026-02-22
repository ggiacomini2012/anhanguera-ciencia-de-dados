# ---------------------------------------------------------
# PROJETO: PROBABILIDADE E ESTATÍSTICA PARA ANÁLISE DE DADOS
# OBJETIVO: ANALISAR DADOS DE ACIDENTES RODOVIÁRIOS (2024)
# ---------------------------------------------------------

# 1. Carregar as bibliotecas necessárias [cite: 31, 33, 36]
library(dplyr)
library(ggplot2)

# 2. Carregar o conjunto de dados [cite: 27, 28, 29]
# Usando o link oficial do repositório do projeto
url <- "https://raw.githubusercontent.com/AndersonSalata/projeto-integrado-ciencia-de-dados/main/datatran2024.csv"
dados <- read.csv(url, sep=";", fill=TRUE, check.names = FALSE)

# 3. Exploração inicial dos dados [cite: 30]
str(dados)
summary(dados)

# 4. Questão 1: Estado com maior número de acidentes [cite: 46]
ranking_estados <- dados %>%
  group_by(uf) %>%
  summarise(total = n()) %>%
  arrange(desc(total))

print("Ranking de acidentes por UF:")
print(ranking_estados)

# 5. Questão 2: Probabilidade de acidentes em condições climáticas claras [cite: 34, 47]
# Tratamento de encoding para identificar "Céu Claro"
termo_claro <- unique(dados$condicao_metereologica)[1] 
clima_claro <- sum(dados$condicao_metereologica == termo_claro, na.rm = TRUE)
total_acidentes <- nrow(dados)

prob_clima <- (clima_claro / total_acidentes) * 100

cat("Total de acidentes:", total_acidentes, "\n")
cat("Acidentes em clima claro:", clima_claro, "\n")
cat("A probabilidade é de:", round(prob_clima, 2), "%\n")

# 6. Questão 3: Influência da Fase do Dia nos acidentes (Gráfico) [cite: 36, 48]
ggplot(dados, aes(x = fase_dia, fill = fase_dia)) +
  geom_bar() +
  labs(
    title = "Distribuição de Acidentes por Fase do Dia",
    x = "Fase do Dia",
    y = "Quantidade de Ocorrências",
    fill = "Legenda"
  ) +
  theme_minimal()

# 7. Questão 4: Principais causas de acidentes (Insights) [cite: 49]
principais_causas <- dados %>%
  group_by(causa_acidente) %>%
  summarise(total = n()) %>%
  arrange(desc(total)) %>%
  head(5)

print("As 5 principais causas de acidentes:")
print(principais_causas)