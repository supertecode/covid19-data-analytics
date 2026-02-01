# Visão Geral da Estrutura do Projeto

## Organização dos Diretórios

Este documento descreve a organização do projeto `covid19-data-analytics` seguindo boas práticas de engenharia de software.

### 📁 Diretório `data/`

Contém os dados brutos e processados utilizados no projeto.

**Arquivos:**

- `covid_worldwide.csv` - Dataset original com dados de COVID-19 em todo mundo

**Boas Práticas:**

- Manter dados brutos separados de dados processados
- Documentar a fonte e data dos dados
- Usar versionamento para rastreabilidade

### 📁 Diretório `notebooks/`

Contém os Jupyter Notebooks com análises interativas.

**Arquivos:**

- `projeto.ipynb` - Notebook principal com análise completa de dados

**Estrutura Recomendada do Notebook:**

1. Importações
2. Carregamento de dados
3. Exploração inicial
4. Limpeza e tratamento
5. Análise exploratória
6. Resultados e conclusões

### 📁 Diretório `src/`

Contém código Python modular e reutilizável.

**Arquivos:**

- `__init__.py` - Torna o diretório um pacote Python
- `data_processing.py` - Funções para processamento de dados

**Padrão de Desenvolvimento:**

- Um módulo por responsabilidade
- Funções bem documentadas com docstrings
- Type hints para melhor legibilidade
- Testes unitários (quando aplicável)

### 📁 Diretório `docs/`

Contém documentação adicional do projeto.

**Arquivos:**

- `INSTALL.md` - Guia de instalação detalhado
- Outros: tutoriais, guias de uso, análises técnicas

### 📁 Diretório `results/`

Contém saídas, visualizações e resultados das análises.

**Subdiretórios Sugeridos:**

```
results/
├── figures/        # Imagens e gráficos (PNG, JPG)
├── data/           # Dados processados e exportados (CSV, JSON)
└── reports/        # Relatórios em PDF ou Markdown
```

### 📄 Arquivos Raiz

| Arquivo            | Descrição                         |
| ------------------ | --------------------------------- |
| `README.md`        | Documentação principal do projeto |
| `CONTRIBUTING.md`  | Guia de contribuição              |
| `requirements.txt` | Dependências Python               |
| `.gitignore`       | Configuração do Git               |
| `LICENSE`          | Licença do projeto                |

---

## 🔄 Fluxo de Trabalho Recomendado

```
1. Dados Brutos (data/)
         ↓
2. Exploração (notebooks/)
         ↓
3. Processamento (src/)
         ↓
4. Análises (notebooks/)
         ↓
5. Resultados (results/)
         ↓
6. Documentação (docs/)
```

---

## 📝 Convenções de Nomenclatura

### Arquivos Python

- Use `snake_case` para nomes de arquivos
- Exemplo: `data_processing.py`, `model_training.py`

### Funções e Variáveis

- Use `snake_case` para funções e variáveis
- Exemplo: `process_data()`, `top_countries`

### Classes

- Use `PascalCase` para classes
- Exemplo: `DataProcessor`, `CovidAnalyzer`

### Constantes

- Use `UPPER_SNAKE_CASE` para constantes
- Exemplo: `MAX_ROWS = 10000`

---

## ✅ Checklist de Qualidade

- [ ] Código segue PEP 8
- [ ] Funções têm docstrings
- [ ] Imports estão organizados
- [ ] Sem código duplicado
- [ ] Testes implementados
- [ ] README atualizado
- [ ] Dependências documentadas

---

## 🚀 Próximos Passos

1. Executar o notebook em `notebooks/projeto.ipynb`
2. Explorar os dados em `data/covid_worldwide.csv`
3. Usar funções de `src/data_processing.py` em suas análises
4. Documentar novas funcionalidades em `docs/`
5. Manter `results/` atualizado com seus achados

---

Para mais informações, consulte [README.md](../README.md).
