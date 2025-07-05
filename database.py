import sqlite3

conn = sqlite3.connect("denuncias.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome_usuario TEXT NOT NULL,
    data_nascimento DATE NOT NULL,
    senha TEXT NOT NULL
)
               """)

conn.commit()
conn.close()

print("Banco de tabela criados")