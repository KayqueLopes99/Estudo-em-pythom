## Base de Dados com Python (SQLite)
* Abrir uma conexão e manipular dados.
* **SQLite**: tem os poderes do SQL, mas é um pouco diferente.
* Não suporta muitas conexões em sites.
* Salva dados em **um arquivo único de conexão**.
* Comandos estão no código em Python.
> sempre fazer o commit
---

## Comandos e Operações Principais no SQLite (com Python)
### 1. **INSERT** (inserir dados)

```python
sql = "INSERT INTO tabela (coluna1, coluna2) VALUES (?, ?)"
cursor.execute(sql, (valor1, valor2))
conn.commit()
```

* **Subcomandos**:
  * `INSERT INTO tabela DEFAULT VALUES;` → insere valores padrão.
  * `INSERT OR REPLACE INTO tabela ...` → substitui se já existir.
---

### 2. **SELECT** (consultar dados)
```python
sql = "SELECT coluna1, coluna2 FROM tabela WHERE coluna1 = ?"
cursor.execute(sql, (valor,))
resultados = cursor.fetchall()
```
* **Subcomandos**:
  * `SELECT * FROM tabela` → retorna todas as colunas.
  * `WHERE` → filtra resultados.
  * `ORDER BY coluna ASC|DESC` → ordena.
  * `LIMIT n` → limita a quantidade.

---
### 3. **UPDATE** (atualizar dados)

```python
sql = "UPDATE tabela SET coluna1 = ? WHERE id = ?"
cursor.execute(sql, (novo_valor, id))
conn.commit()
```
* **Subcomandos**:
  * `SET coluna = valor` → define o que vai mudar.
  * `WHERE` → garante que só atualize registros específicos.
---

### 4. **DELETE** (apagar dados)
```python
sql = "DELETE FROM tabela WHERE id = ?"
cursor.execute(sql, (id,))
conn.commit()
```
* **Subcomandos**:

  * `DELETE FROM tabela` → remove todos os dados (não reseta IDs).
  * `DELETE FROM tabela WHERE condição` → remove só os filtrados.
- Para resetar IDs (autoincremento):
```python
cursor.execute("DELETE FROM tabela")
cursor.execute("DELETE FROM sqlite_sequence WHERE name='tabela'")
conn.commit()
```
---
## Usando Placeholders para Maior Segurança (Bindings) no SQLite
* Não mande comandos diretos para o SQL.
* O usuário fornece os dados, você separa **comandos SQL** de **valores recebidos**.
* Evita **SQL Injection**.
Exemplo:
```python
sql = "INSERT INTO tabela (name, weight) VALUES (?, ?)"
cursor.execute(sql, (nome, peso))
```
> tuplas, listas e dicionários.

---

## Tipos de Dados no SQLite

| Tipo        | Descrição                                          |
| ----------- | -------------------------------------------------- |
| **NULL**    | Valor nulo (sem valor).                            |
| **INTEGER** | Número inteiro (pode ser grande).                  |
| **REAL**    | Número com ponto flutuante (decimal).              |
| **TEXT**    | Texto (strings).                                   |
| **BLOB**    | Armazena dados binários (imagens, arquivos, etc.). |

---
