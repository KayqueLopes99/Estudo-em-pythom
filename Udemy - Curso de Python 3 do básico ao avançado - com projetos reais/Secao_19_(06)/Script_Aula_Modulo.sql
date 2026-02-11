DROP SCHEMA public CASCADE;
CREATE SCHEMA public;
-- DDL: Comando em tabelas. 
-- ';' - Fim.
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100)NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password_hash VARCHAR(100) NOT NULL,
	created_at TIMESTAMP DEFAULT NOW()

);

CREATE TABLE IF NOT EXISTS profiles (
    id SERIAL PRIMARY KEY,
    bio VARCHAR(100) NOT NULL,
    description VARCHAR(100) NOT NULL,
    user_id INTEGER NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id)
);


CREATE TABLE IF NOT EXISTS roles (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS users_roles (
    role_id INTEGER,
    user_id INTEGER,
    FOREIGN KEY (user_id) REFERENCES users(id),
	FOREIGN KEY (role_id) REFERENCES roles(id)
);

-- SQL INSERT
-- Ordem não importa, contanto que você alinhe.
INSERT INTO users 
(first_name, last_name, email, password_hash, created_at)
VALUES
('Tanner','Mayo','vitae.diam@consectetueripsum.ca','QLN12HIN3RL','2021-07-25 22:12:26'),
('Brittany','Stewart','nibh.sit@nunc.edu','ROM35HMM4SA','2020-08-22 13:41:06'),
('Ferris','Hall','neque.Morbi@porttitorscelerisqueneque.edu','YTU15GQR9HT','2020-02-28 05:52:36'),
('Jacob','Manning','risus.at@sociis.edu','EQS93HLI6QZ','2021-04-22 06:01:30'),
('Keelie','Petersen','Nulla@lobortis.org','ZHE87TSO6DA','2021-07-10 20:51:19'),
('Benjamin','Daniels','nec@dolor.org','CNW39GMH4NZ','2021-01-30 22:33:14'),
('Aspen','Cain','Nullam.ut@primisinfaucibus.com','ZFC58TUT0MB','2020-06-12 14:52:39'),
('Oprah','Reeves','nisi.nibh.lacinia@mattissemper.net','LYD20HWD3UN','2020-03-05 13:41:49'),
('Lynn','Hendricks','neque.tellus.imperdiet@dolor.net','CRA59DIT0TW','2020-04-12 15:26:28'),
('Wayne','Walters','torquent.per.conubia@Utsagittislobortis.co.uk','BVD19AUV2JO','2020-10-04 03:36:24');

-- SQL SELECT
SELECT * FROM users;

SELECT id, first_name, last_name, email FROM users;

SELECT
    first_name AS nome,
    last_name AS sobrenome,
    email AS "e-mail"
FROM users;

-- Evitando colisão de atributos entre tabelas com name.atribute
SELECT users.first_name, users.email
FROM users;

-- WHERE - FILTRO 
SELECT * FROM users WHERE email = 'joao@email.com';

-- Operadores: = < <= > >= (<> ou !=)
-- AND e OR
SELECT * FROM users WHERE id > 1;

-- Seleção: SELECT 
SELECT * FROM users WHERE created_at >= '2021-01-01'  AND id > 3;

-- BETWEEN filtra valores dentro de um intervalo, incluindo o valor inicial e o final.
-- Seleciona um range.
SELECT * FROM users WHERE created_at BETWEEN '2020-01-01' AND '2020-12-31';

SELECT * FROM users WHERE id BETWEEN 1 AND 5;

-- SELECT IN
-- IN: Usado para selecionar registros cujo valor esteja dentro de uma lista de valores especificados.
SELECT * FROM users WHERE id IN (1, 3, 5);

-- SELECT LIKE
-- LIKE é usado no SELECT para buscar registros por padrão de texto, e não por valor exato.
-- Todos usuários com a letra "A"
-- Antes%Depois
SELECT * FROM users WHERE first_name LIKE 'A%';

-- SELECT ORDER
-- ORDER BY é usado no SELECT para ordenar os resultados de uma consulta.
-- ASC = do menor para o maior
-- DESC = do maior para o menor
-- Ordem crescente
SELECT * FROM users ORDER BY created_at ASC;

-- Ordem decrescente
SELECT * FROM users ORDER BY created_at DESC;

-- LIMIT e OFFSET são usados no SELECT para controlar a quantidade
-- de registros retornados e a partir de onde a consulta começa.
-- Limit: limita a qtd de valores.
-- ofset: ignora valores / desloca os valores a serem exibidos.
SELECT * FROM users ORDER BY id LIMIT 5 OFFSET 5;

-- INSERT com SELECT é usado para inserir dados em uma tabela
-- a partir do 
-- resultado de um SELECT, sem escrever valores manualmente.

-- Insere na tabela users_roles todos os usuários
-- criados a partir de 2021, associando cada um ao
-- papel de id = 1.
INSERT INTO profiles (bio, description, user_id)
SELECT
  CONCAT('Bio de ', first_name),
  CONCAT('Descrição de ', first_name),
  id
FROM users;

SELECT * FROM profiles;


-- DELETE: usado para remover registros de uma tabela
DELETE FROM profiles WHERE user_id = 5;

DELETE FROM users WHERE id = 5;

-- UPDATE: usado para alterar dados existentes em uma tabela.
UPDATE users SET first_name = 'Carlos' WHERE id = 3;

-- SELECT de mais de uma tabela
-- Join: junção.
SELECT
  u.first_name,
  u.email,
  p.bio,
  p.description
FROM users u
JOIN profiles p ON p.user_id = u.id;

-- INNER JOIN é usado para retornar apenas os registros 
-- que existem nas duas tabelas ao mesmo tempo.

SELECT
  u.first_name,
  p.bio
FROM users u
INNER JOIN profiles p ON p.user_id = u.id;

-- LEFT JOIN retorna todos os registros da tabela
-- da esquerda e os correspondentes da direita
-- (ou NULL se não houver)
SELECT
  u.first_name,
  p.bio
FROM users u
LEFT JOIN profiles p ON p.user_id = u.id;

-- RIGHT JOIN retorna todos os registros da tabela
-- da direita e os correspondentes da esquerda 
-- (ou NULL se não houver)
SELECT
  u.first_name,
  p.bio
FROM users u
RIGHT JOIN profiles p ON p.user_id = u.id;


-- RANDOM gera número aleatório e 
-- ROUND arredonda o valor para um número inteiro
SELECT ROUND(RANDOM() * 100) AS numero_aleatorio;

-- INSERT de dados para a tabela roles
INSERT INTO roles (name)
VALUES ('POST'), ('GET'), ('PUT'), ('DELETE');

-- INSERT de dados para a tabela users_roles
INSERT INTO users_roles (user_id, role_id)
SELECT u.id, r.id
FROM users u
JOIN roles r ON r.name = 'POST';

-- INSERT IGNORE no PostgreSQL é feito com ON 
-- CONFLICT DO NOTHING para ignorar duplicados
-- sem gerar erro
INSERT INTO roles (name)
VALUES ('POST')
ON CONFLICT (name) DO NOTHING;

-- SELECT com vários JOINs
SELECT u.id AS uid, u.first_name, p.bio, r.name AS role_name
FROM users AS u
LEFT JOIN profiles AS p ON u.id = p.user_id
INNER JOIN users_roles AS ur ON u.id = ur.user_id
INNER JOIN roles AS r ON ur.role_id = r.id
ORDER BY Uid ASC;

-- UPDATE com vários JOINs
-- UPDATE com JOIN no PostgreSQL usando FROM para atualizar dados relacionados
UPDATE profiles p
SET bio = CONCAT(p.bio, ' atualizado')
FROM users u
WHERE p.user_id = u.id
  AND u.first_name = 'Lynn';

-- DELETE com JOINs
-- DELETE com JOIN no PostgreSQL remove registros usando relação entre tabelas
DELETE FROM profiles p
USING users u
WHERE p.user_id = u.id
  AND u.first_name = 'Lynn';

-- GROUP BY agrupa registros para aplicar
-- funções de agregação como COUNT, SUM ou AVG
SELECT role_id, COUNT(*) AS total_usuarios
FROM users_roles
GROUP BY role_id;

-- Funções de agregação:
-- Agregação é o processo de resumir vários registros em um único resultado
-- usando funções como COUNT, SUM, AVG, MIN ou MAX.
-- COUNT conta quantos usuários existem por ano de criação
SELECT EXTRACT(YEAR FROM created_at) AS ano, COUNT(*) AS total
FROM users
GROUP BY ano;

-- MAX retorna a data mais recente de criação por ano
SELECT EXTRACT(YEAR FROM created_at) AS ano, MAX(created_at) AS mais_recente
FROM users
GROUP BY ano;

-- MIN retorna a data mais antiga de criação por ano
SELECT EXTRACT(YEAR FROM created_at) AS ano, MIN(created_at) AS mais_antiga
FROM users
GROUP BY ano;

-- AVG calcula a média de id dos usuários por ano
SELECT EXTRACT(YEAR FROM created_at) AS ano, AVG(id) AS media_id
FROM users
GROUP BY ano;

-- SUM soma os ids dos usuários agrupados por ano
SELECT EXTRACT(YEAR FROM created_at) AS ano, SUM(id) AS soma_ids
FROM users
GROUP BY ano;


-- 1) Insere 5 novos usuários
INSERT INTO users (first_name, last_name, email, password_hash, created_at)
VALUES
('Ana','Silva','ana@email.com','HASH1',NOW()),
('Bruno','Souza','bruno@email.com','HASH2',NOW()),
('Carla','Lima','carla@email.com','HASH3',NOW()),
('Diego','Rocha','diego@email.com','HASH4',NOW()),
('Elisa','Martins','elisa@email.com','HASH5',NOW());

-- 2) Insere 5 perfis para os últimos 5 usuários inseridos
INSERT INTO profiles (bio, description, user_id)
SELECT 
  CONCAT('Bio de ', first_name),
  CONCAT('Descrição de ', first_name),
  id
FROM users
ORDER BY id DESC
LIMIT 5;


-- 3) Insere permissões (roles) para os usuários inseridos associando à role USER
INSERT INTO users_roles (user_id, role_id)
SELECT u.id, r.id
FROM users u
JOIN roles r ON r.name = 'USER'
ORDER BY u.id DESC
LIMIT 5;

-- 4) Selecione os últimos 5 usuários por ordem decrescente 
SELECT * FROM users u ORDER BY u.id DESC LIMIT 5;

-- 5) Atualize o último usuário inserido
UPDATE users SET first_name = 'Wayne atualizado!' 
WHERE id = (SELECT id FROM users u ORDER BY u.id DESC LIMIT 1);

SELECT * FROM users u ORDER BY u.id DESC LIMIT 1;


-- 6) Remova uma permissão de algum usuário
-- Remove uma permissão (role) de um usuário específico
DELETE FROM users_roles
WHERE user_id = 1
  AND role_id = 1;

-- 7) Remova um usuário que tem a permissão "PUT"
DELETE FROM users u
USING users_roles ur, roles r
WHERE u.id = ur.user_id
  AND ur.role_id = r.id
  AND r.name = 'PUT';

-- 8) Seleciona apenas usuários que possuem perfil e permissão (INNER JOIN obrigatório)
SELECT u.id, u.first_name, p.bio, r.name AS role
FROM users u
INNER JOIN profiles p ON p.user_id = u.id
INNER JOIN users_roles ur ON ur.user_id = u.id
INNER JOIN roles r ON r.id = ur.role_id;



-- 9) Seleciona todos os usuários mesmo que não tenham perfil ou permissão (LEFT JOIN opcional)
SELECT u.id, u.first_name, p.bio, r.name AS role
FROM users u
LEFT JOIN profiles p ON p.user_id = u.id
LEFT JOIN users_roles ur ON ur.user_id = u.id
LEFT JOIN roles r ON r.id = ur.role_id;








