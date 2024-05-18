import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sqlite3

# Conectar ao banco de dados SQLite
db_file = 'database.sqlite'
conn = sqlite3.connect(db_file)

# Carregar os dados da tabela 'Player_Attributes' para um DataFrame
query = "SELECT * FROM Player_Attributes"
df = pd.read_sql_query(query, conn)

# Fechar a conexão com o banco de dados
conn.close()

# Mostrar as primeiras linhas do dataset
print(df.head())

# Estatísticas descritivas do dataset
print(df.describe())

# Escolher colunas relevantes para a análise
# Você pode ajustar essas colunas conforme necessário
colunas_relevantes = ['overall_rating', 'potential', 'crossing', 'finishing', 'heading_accuracy', 'short_passing', 'volleys', 'dribbling', 'curve', 'free_kick_accuracy', 'long_passing', 'ball_control', 'acceleration', 'sprint_speed', 'agility', 'reactions', 'balance', 'shot_power', 'jumping', 'stamina', 'strength', 'long_shots', 'aggression', 'interceptions', 'positioning', 'vision', 'penalties', 'marking', 'standing_tackle', 'sliding_tackle', 'gk_diving', 'gk_handling', 'gk_kicking', 'gk_positioning', 'gk_reflexes']

# Filtrar apenas as colunas relevantes
df_relevant = df[colunas_relevantes]

# Mostrar as primeiras linhas do dataset filtrado
print(df_relevant.head())

# Estatísticas descritivas do dataset filtrado
print(df_relevant.describe())

# Distribuição da avaliação geral dos jogadores
plt.figure(figsize=(10, 6))
sns.histplot(df_relevant['overall_rating'], kde=True)
plt.title('Distribuição da Avaliação Geral dos Jogadores')
plt.xlabel('Avaliação Geral')
plt.ylabel('Frequência')
plt.show()

# Gráfico de dispersão entre avaliação geral e potencial
plt.figure(figsize=(10, 6))
sns.scatterplot(x='overall_rating', y='potential', data=df_relevant)
plt.title('Avaliação Geral vs Potencial')
plt.xlabel('Avaliação Geral')
plt.ylabel('Potencial')
plt.show()

# Análise de correlação
correlation = df_relevant.corr()
plt.figure(figsize=(12, 8))
sns.heatmap(correlation, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Matriz de Correlação')
plt.show()
