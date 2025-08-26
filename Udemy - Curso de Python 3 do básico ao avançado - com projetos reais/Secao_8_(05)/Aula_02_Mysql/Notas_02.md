## MySql:
- PyMySql: é um pacote para consultas.
> USO DO MYSQL WOORBREACH E O MYSQL SEVER.
> COMANDOS SQL LOCALIZADOS NO OUTRO REPOSITÓRIO.

## Comandos em PyMySQL

## `with connection:`
O bloco `with connection:` garante que a conexão com o banco de dados será **aberta e fechada corretamente** ao final do bloco, mesmo que ocorra algum erro dentro dele.  
É equivalente a abrir a conexão manualmente e depois chamá-la de `connection.close()`, mas de forma mais segura e limpa.

Exemplo:
```python
with connection:
    # tudo dentro desse bloco usa a conexão
    pass
````

---

## `with connection.cursor() as cursor:`

Este comando cria um **cursor**, que é o objeto usado para **executar comandos SQL** (SELECT, INSERT, UPDATE, DELETE).
O `with` garante que o cursor será fechado automaticamente ao final do bloco, evitando vazamentos de recursos.

Exemplo:

```python
with connection.cursor() as cursor:
    cursor.execute("SELECT * FROM cliente")
    resultados = cursor.fetchall()
```

---

## `cursor.execute(sql)`

Usado para **executar qualquer comando SQL** passado como string.
Pode ser usado para consultas (`SELECT`) ou alterações (`INSERT`, `UPDATE`, `DELETE`).

Exemplo:

```python
sql = "INSERT INTO cliente (nome, email) VALUES (%s, %s)"
valores = ("João Silva", "joao@email.com")
cursor.execute(sql, valores)
```

---

## `connection.commit()`

Usado para **confirmar alterações** feitas no banco de dados.
É necessário para comandos que modificam dados (`INSERT`, `UPDATE`, `DELETE`).
Se não for chamado, as alterações **não serão salvas**.

Exemplo:

```python
cursor.execute("DELETE FROM cliente WHERE id=10")
connection.commit()  # confirma a exclusão
```

---

**Resumo rápido:**

* `with connection:` → garante que a conexão será fechada corretamente.
* `with connection.cursor() as cursor:` → cria e fecha automaticamente o cursor.
* `cursor.execute(sql)` → executa a query SQL.
* `connection.commit()` → salva as alterações no banco (obrigatório para INSERT/UPDATE/DELETE).

```

