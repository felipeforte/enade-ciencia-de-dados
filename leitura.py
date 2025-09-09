import os
import pandas as pd

# Entra na pasta dados
os.chdir('dados')

# Lista todos os arquivos que começam com 'microdados2023' e terminam com '.txt'
arquivos = [f for f in os.listdir() if f.startswith('microdados2023') and f.endswith('.txt')]
arquivos.sort()

# Lê todos os dataframes
dataframes = {}
for arquivo in arquivos:
    df = pd.read_csv(arquivo, sep=';')
    dataframes[arquivo] = df
    print(f"\n{arquivo}:")
    print(df.head())

print(f"\nTotal de arquivos lidos: {len(dataframes)}")