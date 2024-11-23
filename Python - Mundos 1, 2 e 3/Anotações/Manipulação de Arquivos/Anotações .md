- Em Python, a manipulação de arquivos é feita com o uso do comando `open()`, que abre o arquivo e retorna um objeto de arquivo. Através desse objeto, podemos realizar operações como leitura, escrita e adição de dados ao arquivo. 
- Além disso, o comando `close()` encerra o uso do arquivo para liberar recursos.

### Abertura de Arquivos com `open()`

A função `open()` em Python é usada para abrir arquivos, e ela possui dois parâmetros principais:
1. **Nome do arquivo**: O caminho do arquivo que você deseja abrir.
2. **Modo de abertura**: O modo define como o arquivo será aberto (leitura, escrita, etc.).

```python
file = open('nome_do_arquivo.txt', 'modo')
```

### Modos de Abertura de Arquivos

Aqui estão os modos principais de abertura de arquivos em Python:

| Modo | Significado                              | Descrição                                                                                                   |
|------|------------------------------------------|-------------------------------------------------------------------------------------------------------------|
| `'r'`| Leitura (`read`)                         | Abre o arquivo para leitura (padrão). O arquivo deve existir; caso contrário, ocorre um erro.               |
| `'w'`| Escrita (`write`)                        | Abre o arquivo para escrita, criando-o se ele não existir ou truncando-o (apagando seu conteúdo) se existir.|
| `'a'`| Anexação (`append`)                      | Abre o arquivo para anexar dados ao final. Cria o arquivo se ele não existir.                               |
| `'r+'`| Leitura e Escrita (`read and write`)    | Abre o arquivo para leitura e escrita. O arquivo deve existir.                                              |
| `'w+'`| Escrita e Leitura                       | Abre o arquivo para leitura e escrita, criando-o ou truncando-o se existir.                                 |
| `'a+'`| Anexação e Leitura                      | Abre o arquivo para anexação e leitura. Cria o arquivo se ele não existir.                                  |
| `'rb'`, `'wb'`, `'ab'` | Modos binários        | Como os modos acima, mas para arquivos binários.                                                           |

### Operações Básicas

#### 1. Lendo Dados com `read()`

O método `read()` lê o conteúdo inteiro do arquivo como uma string:

```python
file = open('nome_do_arquivo.txt', 'r')
conteudo = file.read()
print(conteudo)
file.close()
```

Para ler apenas uma quantidade específica de caracteres, você pode passar um valor como parâmetro para `read()`:

```python
conteudo_parcial = file.read(10)  # Lê os primeiros 10 caracteres
```

#### 2. Lendo Linha a Linha com `readline()` e `readlines()`

- **`readline()`**: Lê uma linha de cada vez, permitindo que você controle o fluxo de leitura:

    ```python
    with open('nome_do_arquivo.txt', 'r') as file:
        linha = file.readline()
        print(linha)
    ```
- Nome_read() é um pouco melhor para imprimir os dados.

- **`readlines()`**: Lê todas as linhas de uma vez e retorna uma lista de strings (cada linha é um item da lista):

    ```python
    with open('nome_do_arquivo.txt', 'r') as file:
        linhas = file.readlines()
        for linha in linhas:
            print(linha.strip())
    ```

#### 3. Escrevendo Dados com `write()`

O método `write()` grava uma string no arquivo:

```python
file = open('nome_do_arquivo.txt', 'w')
file.write("Exemplo de texto.")
file.close()
```

#### 4. Adicionando Dados com `append`

No modo `'a'` ou `'a+'`, podemos adicionar dados ao final do arquivo sem apagar o conteúdo existente:

```python
file = open('nome_do_arquivo.txt', 'a')
file.write("\nNovo conteúdo adicionado.")
file.close()
```

### Usando `with` para Gerenciar Arquivos

A instrução `with` em Python garante que o arquivo será fechado automaticamente após a execução do bloco, mesmo se ocorrer um erro:

```python
with open('nome_do_arquivo.txt', 'r') as file:
    conteudo = file.read()
    print(conteudo)
# Não precisa chamar close(), pois o arquivo é fechado automaticamente
```

### Modos Binários (`rb`, `wb`, `ab`)

Para manipular arquivos binários, como imagens ou arquivos executáveis, você pode usar os modos binários (`rb`, `wb`, `ab`). A leitura e escrita de arquivos binários é feita em bytes:

```python
with open('imagem.png', 'rb') as file:
    dados = file.read()
    print(dados[:10])  # Exibe os primeiros 10 bytes
```

### Exemplo Completo

Aqui está um exemplo completo que demonstra a abertura, leitura, escrita e fechamento de arquivos usando diferentes modos:

```python
# Criando ou substituindo o conteúdo do arquivo
with open('exemplo.txt', 'w') as file:
    file.write("Esta é uma linha de exemplo.")

# Lendo o conteúdo do arquivo
with open('exemplo.txt', 'r') as file:
    conteudo = file.read()
    print(conteudo)

# Adicionando conteúdo ao arquivo existente
with open('exemplo.txt', 'a') as file:
    file.write("\nMais uma linha adicionada.")

# Lendo o conteúdo atualizado
with open('exemplo.txt', 'r') as file:
    print(file.read())
```
