"""
Pacote de análise de dados de COVID-19
"""

from .data_processing import (
    load_covid_data,
    clean_numeric_columns,
    process_covid_data,
    get_top_countries,
    get_basic_statistics
)

__version__ = '1.0.0'
__author__ = 'João Augusto, Murilo Emanoel'

__all__ = [
    'load_covid_data',
    'clean_numeric_columns',
    'process_covid_data',
    'get_top_countries',
    'get_basic_statistics'
]
