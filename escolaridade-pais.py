import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# Configurações iniciais
plt.rcParams['figure.figsize'] = (10, 6)
plt.style.use('ggplot')

# Caminhos dos arquivos
arq10_path = os.path.join('dados', 'microdados2023_arq10.txt')
arq11_path = os.path.join('dados', 'microdados2023_arq11.txt')

# Carregar dados
df_pai = pd.read_csv(arq10_path, sep=';', encoding='utf-8', usecols=['NU_ANO', 'CO_CURSO', 'QE_I04'])
df_mae = pd.read_csv(arq11_path, sep=';', encoding='utf-8', usecols=['NU_ANO', 'CO_CURSO', 'QE_I05'])

# Renomear colunas para padronizar
df_pai.rename(columns={'QE_I04': 'ESCOLARIDADE'}, inplace=True)
df_mae.rename(columns={'QE_I05': 'ESCOLARIDADE'}, inplace=True)

# Adicionar coluna de identificação
df_pai['TIPO'] = 'Pai'
df_mae['TIPO'] = 'Mãe'

# Combinar os dois dataframes
df = pd.concat([df_pai, df_mae], ignore_index=True)

# Mapeamento das categorias
mapa_escolaridade = {
    'A': 'Nenhuma',
    'B': 'Fundamental (1º ao 5º ano)',
    'C': 'Fundamental (6º ao 9º ano)',
    'D': 'Ensino Médio',
    'E': 'Superior - Graduação',
    'F': 'Pós-graduação'
}

# Aplicar mapeamento
df['ESCOLARIDADE_DESC'] = df['ESCOLARIDADE'].map(mapa_escolaridade)

# Contagem por tipo e escolaridade
contagem = df.groupby(['TIPO', 'ESCOLARIDADE_DESC']).size().unstack(fill_value=0)

# Plotar gráfico de barras agrupadas
ax = contagem.T.plot(kind='bar', figsize=(12, 7), width=0.8)

plt.title('Comparação da Escolaridade dos Pais e Mães dos Alunos (2023)', fontsize=16, weight='bold')
plt.xlabel('Nível de Escolaridade', fontsize=12)
plt.ylabel('Número de Respostas', fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.legend(title='Tipo', fontsize=11)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()

# Mostrar valores nas barras
for container in ax.containers:
    ax.bar_label(container, label_type='edge', fontsize=9, padding=3)

plt.show()