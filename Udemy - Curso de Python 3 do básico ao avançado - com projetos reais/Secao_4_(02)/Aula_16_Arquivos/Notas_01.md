## Criando arquivos com Python + Context Manager with
- Manipulação de Arquivos em Python com `open()` e `with`
- O Python oferece suporte nativo para a **manipulação de arquivos**, permitindo a leitura, escrita e edição de documentos em diferentes formatos. 
- O caminho do Arquivo Completo: {CAMINHO DO ARQUIVO -> opção}
- Com `\\` Sempre.
``` py
caminho_arquivo = "C:\\Users\\kaiqu\\OneDrive\\Imagens\\Estudo-em-pythom\\Udemy - Curso de Python 3 do básico ao avançado - com projetos reais\\Secao_4_(02)\\Code\\Aula_53.py" # Caminho completo do arquivo. 

caminho_arquivo += 'Aula_53.txt' # Concatenarr.
```

## 0.1 Abrindo Arquivos com `open()` 
- A função `open()` é usada para abrir arquivos no Python.
- Sintaxe:  

```python
arquivo = open("meuarquivo.txt", "modo", encoding='utf8')
```
- `"meuarquivo.txt"` - Nome do arquivo.  
- `"modo"` - Define como o arquivo será manipulado (leitura, escrita, etc.).  

- Após abrir o arquivo, você pode realizar operações como leitura e escrita. Mas é importante **sempre fechar o arquivo** após o uso com `arquivo.close()`, ou usar `with open()`, que faz isso automaticamente.  

### Modos de Abertura (`open()`) 
| **Modo** | **Descrição** |
|---------|--------------|
| `r` | **Modo de leitura** (**read**). Retorna erro se o arquivo não existir. |
| `w` | **Modo de escrita** (**write**). Cria um novo arquivo ou sobrescreve um existente. |
| `x` | **Modo de criação** (**exclusive**). Retorna erro se o arquivo já existir. |
| `a` | **Modo de adição** (**append**). Adiciona conteúdo ao final do arquivo, sem apagá-lo. |
| `b` | **Modo binário** (**binary**), usado para arquivos como imagens e vídeos. |
| `t` | **Modo texto** (**text**). É o padrão se não for especificado. |
| `+` | **Leitura e escrita simultânea** no mesmo arquivo. |
                                   
+ Os modos podem ser combinados:    
- `"w+"` - Escrita e leitura, sobrescrevendo o arquivo.  
- `"a+"` - Adiciona e permite leitura sem apagar o conteúdo existente.  
- `+r` Leitura e Escrita (`read and write`) Abre o arquivo para leitura e escrita. 
---

## 0.2 Usando o Context Manager (`with open()`)
- Ao abrir arquivos sem `with`, precisamos fechar o arquivo manualmente com `close()`, o que pode causar erros se o fechamento for esquecido.  
```python
with open("exemplo.txt", "w", encoding='utf8') as arquivo:
    arquivo.write("Olá, mundo!\n")
```
- O `with open()` **garante** que o arquivo será fechado corretamente, mesmo se ocorrer um erro durante a execução.

---

## Métodos úteis do TextIOWrapper para Manipulação de Arquivos: 
- Podemos usar-los juntos com o uso do *+*.
### 0.1. Escrevendo em Arquivos (`write()`):
-  `write()` escreve **uma string** no arquivo.  
```python
with open("exemplo.txt", "w") as arquivo:
    arquivo.write("Linha 1\n")
    arquivo.write("Linha 2\n")
```
- Cada `write()` escreve no arquivo, mas não adiciona automaticamente quebras de linha (`\n`).  

---

### 0.2. Escrevendo Múltiplas Linhas (`writelines()`)
- `writelines()` permite escrever múltiplas linhas de uma vez.  
- Podemons colocar um iterável com os dados detro dele.
```python
linhas = ["Linha 1\n", "Linha 2\n", "Linha 3\n"]

with open("exemplo.txt", "w") as arquivo:
    arquivo.writelines(linhas)
```
- Diferente do `write()`, aqui é necessário adicionar `\n` manualmente para separar as linhas.  

---

### 0.3. Lendo Arquivos (`read()`)
-  `read()` lê **todo o conteúdo** do arquivo como uma única string.  
- 
```python
with open("exemplo.txt", "r") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)
```
- Se o arquivo for grande, `read()` pode consumir muita memória.  

---

### 0.4. Lendo Linha por Linha (`readline()` e `readlines()`)
- `readline()`: Lê apenas uma linha por vez. Tipo um next.
```python
with open("exemplo.txt", "r") as arquivo:
    print(arquivo.readline(), end='')  # Lê a primeira linha e remove espaços.
    print(arquivo.readline().strip())  # Lê a segunda linha e remove espaços. 
```
 
- `readlines()`: Retorna todas as linhas como uma lista.
```python
with open("exemplo.txt", "r") as arquivo:
    linhas = arquivo.readlines()
    print(linhas)
```

---

### 0.5. Movendo o Cursor (`seek()`)
-`seek()` **move o cursor de leitura para uma posição específica** dentro do arquivo.  

```python
with open("exemplo.txt", "r") as arquivo:
    print(arquivo.read(5))  # Lê os primeiros 5 caracteres
    arquivo.seek(0)  # Volta para o início do arquivo
    print(arquivo.read(5))  # Lê novamente os primeiros 5 caracteres
```
- Útil para **reler arquivos sem precisar reabri-los**.  

---

### 0.6. Adicionando Conteúdo ao Arquivo (`a` - Append)
- Se quisermos adicionar novas linhas **sem apagar o conteúdo existente**, usamos `"a"`.  

```python
with open("exemplo.txt", "a") as arquivo:
    arquivo.write("Nova linha adicionada.\n")
```
- `"a"` **sempre escreve no final do arquivo**, sem remover dados anteriores.  

---