# COVID-19 Data Analytics

> Análise de dados epidemiológicos da COVID-19 em nível mundial

[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Status: Projeto Acadêmico](https://img.shields.io/badge/status-academic%20project-lightgrey.svg)]()

---

## 📋 Sumário

- [Visão Geral](#visão-geral)
- [Questões de Pesquisa](#questões-de-pesquisa)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Instalação](#instalação)
- [Uso](#uso)
- [Dados](#dados)
- [Análises Realizadas](#análises-realizadas)
- [Requisitos](#requisitos)
- [Licença](#licença)

---

## 🎯 Visão Geral

Este projeto implementa uma análise exploratória completa de dados epidemiológicos da pandemia de COVID-19 em escala mundial. Desenvolvido como trabalho prático da disciplina **Tópicos em Programação 1**, o projeto demonstra boas práticas de ciência de dados, incluindo:

- **Limpeza e transformação de dados**: Remoção de inconsistências, tratamento de valores ausentes
- **Análise exploratória**: Estatísticas descritivas, visualizações e padrões
- **Resposta a questões de pesquisa**: Identificação de países mais afetados e tendências

A pandemia de COVID-19, causada pelo vírus SARS-CoV-2, representa um dos maiores desafios de saúde pública dos últimos tempos. Através da análise de dados, este projeto busca fornecer insights sobre o impacto global da doença.

---

## ❓ Questões de Pesquisa

Este projeto responde às seguintes questões:

1. **Quais são os top 10 países que mais registraram casos de COVID-19?**
   - Identificação dos países com maior número absoluto de casos confirmados

2. **Quais são os top 10 países que mais apresentaram casos de morte por COVID-19?**
   - Análise da mortalidade em diferentes regiões

3. **Onde os casos ainda são altos?**
   - Identificação de regiões com casos ativos elevados na data de coleta dos dados

---

## 📁 Estrutura do Projeto

```
covid19-data-analytics/
│
├── 📂 data/                      # Dados brutos e processados
│   └── covid_worldwide.csv       # Dataset de entrada
│
├── 📂 notebooks/                 # Jupyter Notebooks
│   └── projeto.ipynb             # Análise completa interativa
│
├── 📂 src/                       # Código Python modular
│   ├── __init__.py
│   └── data_processing.py        # Funções de processamento
│
├── 📂 docs/                      # Documentação
│   └── INSTALL.md               # Guia de instalação
│
├── 📂 results/                   # Resultados e saídas
│   ├── *.png                    # Visualizações
│   ├── *.csv                    # Dados processados
│   └── *.json                   # Resultados em JSON
│
├── .gitignore                   # Configuração do Git
├── requirements.txt             # Dependências do projeto
├── README.md                    # Este arquivo
├── CONTRIBUTING.md              # Guia de contribuição
└── LICENSE                      # Licença (MIT)
```

---

## ⚙️ Instalação

Para clonar e configurar o projeto em sua máquina:

### Pré-requisitos

- Python 3.7 ou superior
- pip (gerenciador de pacotes)
- Git (opcional)

### Passos

1. **Clone o repositório**

   ```bash
   git clone https://github.com/seu-usuario/covid19-data-analytics.git
   cd covid19-data-analytics
   ```

2. **Crie um ambiente virtual**

   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate

   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Instale as dependências**

   ```bash
   pip install -r requirements.txt
   ```

4. **Verifique a instalação**
   ```bash
   python -c "import pandas; print('✓ Pandas instalado')"
   ```

Para detalhes completos, consulte [INSTALL.md](docs/INSTALL.md).

---

## 🚀 Uso

### Executar o Notebook Interativo

```bash
jupyter notebook notebooks/projeto.ipynb
```

Ou com Jupyter Lab:

```bash
jupyter lab notebooks/projeto.ipynb
```

### Usar o Módulo de Processamento

```python
from src.data_processing import process_covid_data, get_top_countries

# Processar dados
df = process_covid_data('data/covid_worldwide.csv')

# Obter top 10 países com mais casos
top_cases = get_top_countries(df, 'Total Cases', n=10)
print(top_cases)

# Obter top 10 países com mais mortes
top_deaths = get_top_countries(df, 'Total Deaths', n=10)
print(top_deaths)
```

### Exemplos de Análises

```python
import pandas as pd
from src.data_processing import load_covid_data, clean_numeric_columns

# Carregar dados
df = load_covid_data('data/covid_worldwide.csv')

# Visualizar informações básicas
print(df.head())
print(df.shape)
print(df.info())

# Limpar colunas numéricas
numeric_cols = ['Total Cases', 'Total Deaths', 'Active Cases']
df = clean_numeric_columns(df, numeric_cols)

# Análises estatísticas
print(df.describe())
```

---

## 📊 Dados

### Fonte

- Dataset: `covid_worldwide.csv`
- Formato: CSV (valores separados por vírgula)

### Colunas

| Coluna          | Descrição                         | Tipo     |
| --------------- | --------------------------------- | -------- |
| Country         | Nome do país                      | String   |
| Total Cases     | Número total de casos confirmados | Numérico |
| Total Deaths    | Número total de mortes            | Numérico |
| Total Recovered | Número total de recuperados       | Numérico |
| Active Cases    | Número de casos ativos            | Numérico |
| Total Test      | Total de testes realizados        | Numérico |
| Population      | População do país                 | Numérico |

### Processamento

Os dados passam por um pipeline de limpeza que inclui:

1. Remoção de separadores de milhares
2. Conversão para tipos numéricos apropriados
3. Tratamento de valores ausentes
4. Remoção de colunas irrelevantes

---

## 📈 Análises Realizadas

### 1. Limpeza e Exploração de Dados

- Verificação de tipos de dados e inconsistências
- Tratamento de valores ausentes
- Remoção de colunas desnecessárias
- Análise estatística básica

### 2. Identificação de Padrões

- **Top 10 Países com Mais Casos**: Identificação dos países mais afetados
- **Top 10 Países com Mais Mortes**: Análise da mortalidade por país
- **Regiões com Casos Ativos Altos**: Análise de tendências

### 3. Estatísticas Descritivas

- Média, mediana, moda
- Desvio padrão
- Quartis (Q1, Q2, Q3)
- Valores mínimos e máximos

### 4. Visualizações

- Gráficos de barras dos top países
- Distribuições de casos e mortes
- Análises por região

---

## 📋 Requisitos

### Dependências Python

```
pandas>=1.3.0
numpy>=1.21.0
matplotlib>=3.4.0
seaborn>=0.11.0
jupyter>=1.0.0
jupyterlab>=3.0.0
scikit-learn>=0.24.0
```

### Sistema

- Python 3.7+
- 2GB RAM mínimo
- 500MB espaço em disco

---

## 🤝 Contribuindo

Contribuições são bem-vindas! Por favor, consulte [CONTRIBUTING.md](CONTRIBUTING.md) para:

- Como reportar bugs
- Como propor melhorias
- Padrões de código
- Processo de pull requests

---

Projeto desenvolvido como trabalho prático da disciplina **Tópicos em Programação 1**.

---

## 📚 Referências

- [OMS - Sobre COVID-19](https://www.who.int/health-topics/coronavirus)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [NumPy Documentation](https://numpy.org/doc/)
- [Matplotlib Documentation](https://matplotlib.org/)

---

## ❓ Perguntas e Suporte

- **Issues**: [GitHub Issues](https://github.com/seu-usuario/covid19-data-analytics/issues)
- **Email**: [seu-email@exemplo.com]

---

## 📅 Status do Projeto

- ✅ Análise exploratória completa
- ✅ Pipeline de processamento de dados
- ✅ Documentação
- 📋 Melhorias futuras:
  - Análises de série temporal
  - Machine Learning para previsões
  - Dashboard interativo

---

**Última atualização**: Fevereiro de 2026
