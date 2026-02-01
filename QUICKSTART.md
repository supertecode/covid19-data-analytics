#!/bin/bash

# Quick Start Guide for covid19-data-analytics

# ==============================================

# 1. INSTALAÇÃO

# ==============================================

echo "📦 Instalando dependências..."
python -m venv venv

# Windows

venv\Scripts\activate

# macOS/Linux

# source venv/bin/activate

pip install -r requirements.txt

# ==============================================

# 2. EXPLORAR DADOS

# ==============================================

echo "📊 Abrindo Jupyter Notebook..."
jupyter notebook notebooks/projeto.ipynb

# ==============================================

# 3. USAR O MÓDULO PYTHON

# ==============================================

python << 'EOF'
from src.data_processing import process_covid_data, get_top_countries

# Processar dados

df = process_covid_data('data/covid_worldwide.csv')

# Top 10 países com mais casos

print("Top 10 países com mais casos:")
print(get_top_countries(df, 'Total Cases', n=10))

# Top 10 países com mais mortes

print("\nTop 10 países com mais mortes:")
print(get_top_countries(df, 'Total Deaths', n=10))
EOF

# ==============================================

# 4. COMANDOS ÚTEIS

# ==============================================

# Ver estatísticas básicas

python -c "from src.data_processing import load_covid_data; df = load_covid_data('data/covid_worldwide.csv'); print(df.describe())"

# Listar colunas

python -c "from src.data_processing import load_covid_data; df = load_covid_data('data/covid_worldwide.csv'); print(df.columns.tolist())"

# Contar linhas

python -c "from src.data_processing import load_covid_data; df = load_covid_data('data/covid_worldwide.csv'); print(f'Total de países: {len(df)}')"
