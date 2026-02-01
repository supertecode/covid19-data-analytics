"""
Módulo para processamento e tratamento de dados de COVID-19.

Este módulo contém funções para:
- Carregamento de dados
- Limpeza e transformação de dados
- Tratamento de valores ausentes
- Análise exploratória básica
"""

import pandas as pd
import numpy as np
from typing import Tuple


def load_covid_data(filepath: str) -> pd.DataFrame:
    """
    Carrega dados de COVID-19 de um arquivo CSV.
    
    Args:
        filepath: Caminho para o arquivo CSV
        
    Returns:
        DataFrame com dados carregados
        
    Example:
        >>> df = load_covid_data('data/covid_worldwide.csv')
    """
    return pd.read_csv(filepath)


def clean_numeric_columns(df: pd.DataFrame, columns: list) -> pd.DataFrame:
    """
    Remove separadores de milhares e converte colunas para formato numérico.
    
    Args:
        df: DataFrame com dados
        columns: Lista de nomes das colunas a converter
        
    Returns:
        DataFrame com colunas limpas
    """
    df = df.copy()
    for col in columns:
        if col in df.columns:
            df[col] = df[col].astype(str).str.replace(',', '')
            df[col] = pd.to_numeric(df[col], errors='coerce')
    return df


def process_covid_data(filepath: str) -> pd.DataFrame:
    """
    Pipeline completo de processamento de dados de COVID-19.
    
    Realiza:
    1. Carregamento dos dados
    2. Limpeza de valores numéricos
    3. Remoção de dados ausentes
    4. Remoção de colunas desnecessárias
    
    Args:
        filepath: Caminho para o arquivo CSV
        
    Returns:
        DataFrame processado e limpo
    """
    # Carregar dados
    df = load_covid_data(filepath)
    
    # Colunas numéricas para limpeza
    numeric_columns = [
        'Total Cases', 'Total Deaths', 'Total Recovered', 
        'Active Cases', 'Total Test', 'Population'
    ]
    
    # Limpar colunas numéricas
    df = clean_numeric_columns(df, numeric_columns)
    
    # Remover linhas com valores ausentes
    df = df.dropna(how='any', axis=0)
    
    # Remover colunas desnecessárias
    columns_to_drop = [
        'Serial Number', 'Total Recovered', 'Total Test', 'Population'
    ]
    df = df.drop([col for col in columns_to_drop if col in df.columns], axis=1)
    
    return df


def get_top_countries(df: pd.DataFrame, column: str, n: int = 10) -> pd.DataFrame:
    """
    Retorna os top N países por uma métrica específica.
    
    Args:
        df: DataFrame com dados de COVID-19
        column: Nome da coluna para ordenação
        n: Número de países a retornar (padrão: 10)
        
    Returns:
        DataFrame com top N países
    """
    return df.nlargest(n, column)[['Country', column]].reset_index(drop=True)


def get_basic_statistics(df: pd.DataFrame) -> dict:
    """
    Calcula estatísticas básicas dos dados.
    
    Args:
        df: DataFrame com dados
        
    Returns:
        Dicionário com estatísticas (média, mediana, desvio padrão, etc)
    """
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    
    stats = {}
    for col in numeric_cols:
        stats[col] = {
            'media': df[col].mean(),
            'mediana': df[col].median(),
            'desvio_padrao': df[col].std(),
            'minimo': df[col].min(),
            'maximo': df[col].max(),
            'q1': df[col].quantile(0.25),
            'q3': df[col].quantile(0.75)
        }
    
    return stats
