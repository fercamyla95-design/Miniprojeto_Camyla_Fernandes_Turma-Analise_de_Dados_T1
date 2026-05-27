# MINI PROJETO - ANÁLISE EXPLORATÓRIA DE DADOS
# Autor: Camyla Karin Fernandes
# Turma: Analise_de_Dados_T1

import pandas as pd  
import numpy as np  

# 1. CARREGAMENTO, LEITURA, EXIBIR INFORMAÇOES DE DADOS

print("\n--- Carregando base de dados ---")
df = pd.read_csv("BaseVarejo.csv", sep=";")
print(df.head())

print("\nQuantidade de linhas e colunas:")
print(df.shape)

print("\nTipo de dados:")
print(df.dtypes)

print("\nNome de colunas:")
print(df.columns)

# 2. Verificação de valores 
print("\n--- Verificando valores nos dados ---")

# Nulos
print("\nValores nulos por coluna:")
print(df.isnull().sum())

# Duplicata 
duplicados = df.duplicated().sum()
print(f"\nQuantidade de duplicatas: {duplicados}")

# Categorias vazias
if "Categoria" in df.columns:
    categorias_vazias = (df["Categoria"] == "").sum()
    print(f"\nCategorias vazias: {categorias_vazias}")

# 3. Limpeza de Dados 
print("\n--- Limpeza dos dados ---")

# Remover duplicatas 
df = df.drop_duplicates()

# Tratamento de categorias vazias 
if "Categoria" in df.columns:
    df["Categoria"] = df["Categoria"].replace("", "Sem Categoria")

# Preenchimento de nulos :
# Colunas categoria (Texto) -> preenchido como "Não informado";
# Colunas numéricas -> preencimento com a mediana.
for coluna in df.columns:
    if df[coluna].dtype == "object":
        df[coluna] = df[coluna].fillna("Não Informado")
    else:
        df[coluna] = df[coluna].fillna(df[coluna].median())

# Conversão de data
if "DATA" in df.columns:
    df["DATA"] = pd.to_datetime(df["DATA"], errors="coerce")

# Verificar datas invalidas
datas_invalidas = df["DATA"].isnull().sum()
print(f"\nDatas invalidas encontradas: {datas_invalidas}")

# 4. Estatística Descritiva
print("\n--- Estatistica ---")

coluna_filhos = "CL_FHL"
if coluna_filhos in df.columns:
    print("\nResumo estatisticas:")
    print(df[coluna_filhos].describe())

    print("\nMédia:")
    print(df[coluna_filhos].mean())

    print("\nMediana:")
    print(df[coluna_filhos].median())

    print("\nModa:")
    print(df[coluna_filhos].mode())

    print("\nDesvio Padrão:")
    print(df[coluna_filhos].std())

    print("\nValor máximo:")
    print(df[coluna_filhos].max())

    print("\nValor minímo:")
    print(df[coluna_filhos].min())


# 5. Agrupamento

