import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME = 'dataBase.sqlite3'
DB_FILE = ROOT_DIR / DB_NAME
TABLE_NAME = "customers"

# ==========================
# CONEXÃO
# ==========================
connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

# ==========================
# CREATE TABLE
# ==========================
cursor.execute(
    f'''
    CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        weight REAL
    )
    '''
)
connection.commit()

# ==========================
# INSERT
# ==========================

# Insert direto (vários registros fixos)
cursor.execute(
    f'''
    INSERT INTO {TABLE_NAME} (name, weight) VALUES
    ('Alice', 55.0),
    ('Bob', 70.5),
    ('Carol', 62.3),
    ('David', 80.2),
    ('Eve', 58.7)
    '''
)
connection.commit()

# Insert com placeholder "?"
sql = f"INSERT INTO {TABLE_NAME} (name, weight) VALUES (?, ?)"
cursor.execute(sql, ('kayque', 55))
connection.commit()

# Insert múltiplo com executemany
cursor.executemany(sql, [
    ('rian', 56),
    ('isa', 56)
])
connection.commit()

# Insert com dicionário (placeholders nomeados)
sql2 = f"INSERT INTO {TABLE_NAME} (name, weight) VALUES (:nameKey, :weightKey)"
cursor.execute(sql2, {'nameKey': 'kaio1', 'weightKey': 60})
cursor.executemany(sql2, [
    {'nameKey': 'kaio2', 'weightKey': 60}
])
connection.commit()

# ==========================
# UPDATE
# ==========================
cursor.execute(
    f'''
    UPDATE {TABLE_NAME} 
    SET name="QUALQUER", weight = 67
    WHERE id = 3
    '''
)
connection.commit()

# ==========================
# DELETE
# ==========================

# Delete por id
idValue = 1
cursor.execute(f"DELETE FROM {TABLE_NAME} WHERE id = ?", (idValue,))
connection.commit()

# Delete toda a tabela (mantém IDs)
# cursor.execute(f"DELETE FROM {TABLE_NAME}")

# Resetar IDs também
# cursor.execute(f"DELETE FROM {TABLE_NAME}")
# cursor.execute(f"DELETE FROM sqlite_sequence WHERE name='{TABLE_NAME}'")
# connection.commit()

# ==========================
# SELECT
# ==========================

# Todos os registros
cursor.execute(f"SELECT * FROM {TABLE_NAME}")
rows = cursor.fetchall()
for row in rows:
    _id, name, weight = row
    print(_id, name, weight)

# Um registro (primeiro encontrado)
row = cursor.fetchone()
print("Primeiro registro:", row)

# Buscar por ID
idValue = 2
cursor.execute(f"SELECT * FROM {TABLE_NAME} WHERE id = ?", (idValue,))
row = cursor.fetchone()
print("Resultado por id:", row)

# Buscar por nome
cursor.execute(f"SELECT * FROM {TABLE_NAME} WHERE name = ?", ('Alice',))
rows = cursor.fetchall()
print("Resultado por nome:", rows)

# Selecionar só algumas colunas
cursor.execute(f"SELECT name, weight FROM {TABLE_NAME}")
rows = cursor.fetchall()
print("Somente nome e peso:", rows)

# ==========================
# ENCERRANDO CONEXÃO
# ==========================
cursor.close()
connection.close()
