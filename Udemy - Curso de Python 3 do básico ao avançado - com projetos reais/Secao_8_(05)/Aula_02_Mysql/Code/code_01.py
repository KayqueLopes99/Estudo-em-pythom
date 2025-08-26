import pymysql
import pymysql.cursors # -> Para cursor em  dicionario
# ==========================================================
# 1. CONEXÃO COM O BANCO DE DADOS (MySQL Workbench)
# ==========================================================
connection = pymysql.connect(
    host='127.0.0.1',  # ou 'localhost'
    port=3306,
    user='root',
    password='52746363kl',
    database='base_de_dados',
    cursorclass=pymysql.cursors.DictCursor # -> Para cursor em  dicionario
)

# Nome da tabela padrão
TABLE_NAME: str = "custumers"

# ==========================================================
# 2. ABRIR CONEXÃO USANDO CONTEXT MANAGER (with)
# ==========================================================
with connection:
    with connection.cursor() as cursor:
        print("Conexão estabelecida com sucesso!")

        # ==========================================================
        # 3. CRIAÇÃO DA TABELA (caso não exista)
        # ==========================================================
        sqlCreatTable = f'''
        CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
            id INT NOT NULL AUTO_INCREMENT,
            name VARCHAR(50) NOT NULL,
            age INT NOT NULL,
            PRIMARY KEY (id)
        )        
        '''
        cursor.execute(sqlCreatTable)

        # ATENÇÃO: Limpa a tabela inteira (use com cuidado)
        # cursor.execute(f'TRUNCATE TABLE {TABLE_NAME}') 
        # connection.commit()

        # ==========================================================
        # 4. CRUD - INSERÇÃO DE DADOS
        # ==========================================================

        # 4.1 Inserção usando dicionário (boa prática)
        sqlInsert = f'''
        INSERT INTO {TABLE_NAME}
        (name, age) 
        VALUES 
        (%(name_)s, %(age_)s)     
        '''
        # Aqui usamos placeholders com nomes (ex: name_, age_)
        # Isso permite passar dicionários para o execute.

        # Exemplo: inserindo UM registro
        data: dict = {
            'name_': "isim",
            "age_": 21,
        }
        cursor.execute(sqlInsert, data)
        connection.commit()  # Sempre necessário após INSERT/UPDATE/DELETE

        # 4.2 Inserção de vários registros de uma vez (executemany)
        data2 = (
            {'name_': "hy", "age_": 21},
            {'name_': "Mari", "age_": 21},
            {'name_': "let", "age_": 21},
            {'name_': "hugo", "age_": 21},
        )
        cursor.executemany(sqlInsert, data2)
        connection.commit()
        # ==========================================================
        # 5. SELECT (CONSULTA DE DADOS) - não necessita de commit()
        # =========================================================
        # Exemplo 1: Buscar de uma tabela qualquer (ex: cliente)
        sql = "SELECT * FROM cliente"
        cursor.execute(sql)
        resultados = cursor.fetchall()
        print("\nResultados da tabela 'cliente':")
        for row in resultados:
            print(row)

        # Exemplo 2: Buscar todos os dados da tabela criada
        sql = f"SELECT * FROM {TABLE_NAME}"
        cursor.execute(sql)
        resultados = cursor.fetchall()
        print(f"\nResultados da tabela '{TABLE_NAME}':")
        for row in resultados:
            print(row)
        
        # ==========================================================
        # SELECT COM SUBCOMANDOS NO PYTHON
        # ==========================================================
        # fetchall:; Ele pega todos os resultados da última query executada (SELECT).
        # Retorna uma lista de tuplas, onde cada tupla é uma linha da tabela.
        

        # 1. WHERE → filtra registros
        cursor.execute(f"SELECT * FROM {TABLE_NAME} WHERE age > 18;")
        print("WHERE age > 18:", cursor.fetchall())

        # 2. ORDER BY → ordena resultados
        cursor.execute(f"SELECT * FROM {TABLE_NAME} ORDER BY age DESC;")
        print("ORDER BY age DESC:", cursor.fetchall())

        # 3. LIMIT → limita resultados
        cursor.execute(f"SELECT * FROM {TABLE_NAME} LIMIT 3;")
        print("LIMIT 3:", cursor.fetchall())

        # 5. LIKE → busca por padrão
        cursor.execute(f"SELECT * FROM {TABLE_NAME} WHERE name LIKE 'M%';")
        print("LIKE 'M%':", cursor.fetchall())

        # 6. IN → valores dentro de uma lista
        cursor.execute(f"SELECT * FROM {TABLE_NAME} WHERE age IN (18, 21, 25);")
        print("IN (18,21,25):", cursor.fetchall())

        # 8. DISTINCT → remove duplicados
        cursor.execute(f"SELECT DISTINCT age FROM {TABLE_NAME};")
        print("DISTINCT ages:", cursor.fetchall())

        # 9. GROUP BY → agrupa
        cursor.execute(f"SELECT age, COUNT(*) AS qtd FROM {TABLE_NAME} GROUP BY age;")
        print("GROUP BY age:", cursor.fetchall())
        
        # BETWEEN usado no WHERE para verificar se um valor está dentro de um intervalo.
        sql = f"SELECT * FROM {TABLE_NAME} WHERE age BETWEEN 18 AND 25;"
        cursor.execute(sql)
        resultados = cursor.fetchall()

        print("Registros com age entre 18 e 25:")
        for row in resultados:
            print(row)

        # ==========================================================
        # 6. DELETE 
        # =========================================================     
        # NECESSITA DE WHERE
        sqlDelete: str = f'DELETE FROM {TABLE_NAME} WHERE id = 1'
        cursor.execute(sqlDelete)
        connection.commit()      
        
        sql = f"SELECT * FROM {TABLE_NAME}"
        cursor.execute(sql)
        resultados = cursor.fetchall()
        print(f"\nResultados da tabela '{TABLE_NAME}' PÓS DELETE:")
        for row in resultados:
            print(row)
        
        # ==========================================================
        # 7. UPDATE 
        # =========================================================     
        sqlUpdate: str = f'UPDATE {TABLE_NAME} SET name = %s, age = %s WHERE id = %s'
        cursor.execute(sqlUpdate, ('NEWNAME', 99, 4))
        connection.commit()     
        
        sql = f"SELECT * FROM {TABLE_NAME}"
        cursor.execute(sql)
        resultados = cursor.fetchall()
        print(f"\nResultados da tabela '{TABLE_NAME}' PÓS UPDATE:")
        for row in resultados:
            print(row)
        
        
        #  Trocando o cursor para retornar dicionários -
        # DictCursor | import | melhor para localização de dados
        print()    
        sql11 = f"SELECT * FROM {TABLE_NAME}"
        cursor.execute(sql11)
        for row in cursor.fetchall():
            print(row['name'])
            
            
        ## rowcount, rownumber e lastrowid para detalhes de consultas executadas
        ## -> Elementos afetados: cursor.rowcount (o ultimo)
        ## -> cursosr.lastrowid: ultimo id inserido
        ## -> cursor.rownumber: nuero da linha do cursor
        
        
        
        cursor.execute(f"TRUNCATE TABLE {TABLE_NAME};")
        connection.commit()
        print(f"Tabela '{TABLE_NAME}' limpa e AUTO_INCREMENT reiniciado!")


        

        # outro: cursores scroll -> voltar linhas anteriores ou posteriores.
        # outro: Para muitos dados SSDictCursor: pausas para continuidades futuras e seleção do necessário.

        # JOIN → junta tabelas (exemplo genérico)
        # Necessário ter outra tabela (ex: phones com coluna customer_id)
        # cursor.execute(f"""
        #     SELECT c.id, c.name, p.phone
        #     FROM {TABLE_NAME} c
        #     JOIN phones p ON c.id = p.customer_id;
        # """)
        # print("JOIN exemplo:", cursor.fetchall())
        # -> NÃO PERMITIR COMANDOS VIA INPUT: restringir.
        
        
        