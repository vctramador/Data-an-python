import sqlite3

# Conectar ao banco de dados SQLite
db_file = 'database.sqlite'
conn = sqlite3.connect(db_file)

# Listar todas as tabelas no banco de dados
cursor = conn.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
print("Tabelas no banco de dados:", tables)

# Fechar a conexão com o banco de dados
conn.close()
