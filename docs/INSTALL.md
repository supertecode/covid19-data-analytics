# Guia de Instalação

## Pré-requisitos

- Python 3.7 ou superior
- pip (gerenciador de pacotes do Python)
- Git (opcional, para clonar o repositório)

## Passos de Instalação

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/covid19-data-analytics.git
cd covid19-data-analytics
```

### 2. Crie um ambiente virtual

```bash
# No Windows
python -m venv venv
venv\Scripts\activate

# No macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Verifique a instalação

```bash
python -c "import pandas; print(pandas.__version__)"
```

## Usando Jupyter Notebook

Para abrir e executar os notebooks:

```bash
jupyter notebook notebooks/projeto.ipynb
```

Ou use o Jupyter Lab:

```bash
jupyter lab notebooks/projeto.ipynb
```

## Estrutura de Diretórios

Após a instalação, você terá:

```
covid19-data-analytics/
├── data/                 # Dados brutos e processados
├── notebooks/            # Jupyter notebooks com análises
├── src/                  # Código Python modular
├── docs/                 # Documentação
├── results/              # Resultados e visualizações
├── requirements.txt      # Dependências do projeto
└── README.md            # Este arquivo
```

## Solução de Problemas

### Erro: "No module named pandas"

Certifique-se de que o ambiente virtual está ativado e as dependências foram instaladas.

### Erro ao executar notebook

- Verifique se o caminho dos arquivos está correto
- Certifique-se de que o arquivo CSV está em `data/`

### Versão incorreta do Python

```bash
python --version  # Verificar versão
```

## Próximos Passos

- Leia o [README.md](../README.md) para entender o projeto
- Explore os notebooks em `notebooks/`
- Consulte a documentação em `docs/`
