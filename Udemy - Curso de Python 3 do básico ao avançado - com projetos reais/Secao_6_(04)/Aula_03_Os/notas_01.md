## `os` – Módulo para interação com o sistema operacional
- **Acesse funcionalidades do sistema operacional** como manipular pastas, arquivos, permissões, variáveis de ambiente
> Sintaxe:

```python
import os
```

---

## 1. `os.path` – Trabalhando com caminhos de arquivos
- Evita erros ao montar caminhos de arquivos e facilita verificar arquivos/diretórios. 

- Principais funções para interagir com o S.O:

```python
# Junta partes de um caminho conforme o sistema operacional
caminho = os.path.join('pasta', 'subpasta', 'arquivo.txt')

# Verifica se o caminho existe
existe = os.path.exists(caminho)

# Caminho absoluto
abs_path = os.path.abspath('arquivo.txt')

# Verifica se é um arquivo
eh_arquivo = os.path.isfile('dados.txt')

# Verifica se é um diretório
eh_diretorio = os.path.isdir('pasta/')
```


> Exemplos do os.path:

> os.path.join: junta strings em um único caminho. Desse modo,

> os.path.join('pasta1', 'pasta2', 'arquivo.txt') retornaria 'pasta1\pasta2\arquivo.txt' no Windows.

> os.path.split: divide um caminho uma tupla (diretório, arquivo).
- Por exemplo, os.path.split('/home/user/arquivo.txt') retornaria ('/home/user', 'arquivo.txt').

> os.path.exists: verifica se um caminho especificado existe.

> os.path só trabalha com caminhos de arquivos e não faz nenhuma operação de entrada/saída (I/O) com arquivos em si.


## 2. `os.listdir()` – Listar arquivos/pastas
- Retorna **todos os arquivos e diretórios dentro de uma pasta**.
- Exemplo:

```python
# Lista o conteúdo da pasta atual
print(os.listdir('.'))

# Lista o conteúdo de uma pasta específica
print(os.listdir('meus_documentos'))
```

---

## 3. `os.system()` – Executar comandos do terminal
- Usa comandos do **sistema operacional** dentro do Python. Pode limpar a tela, executar um programa, rodar scripts etc.


```python
# Limpa a tela no Windows (cmd antigo)
os.system('cls')

# Limpa a tela no Linux, macOS ou PowerShell
os.system('clear')

# Abre o Bloco de Notas (Windows)
os.system('notepad')

# Lista arquivos (como "ls" no Linux/macOS ou "dir" no Windows)
os.system('dir')  # Windows
os.system('ls')   # Linux/macOS
```

## 4. Limpando a tela com `os.system()`

```python
import os

def limpar_tela():
    if os.name == 'nt':
        os.system('cls')  # Windows (cmd antigo)
    else:
        os.system('clear')  # Linux / macOS / PowerShell

print("Antes de limpar...")
input("Pressione Enter para continuar...")
limpar_tela()
print("Tela limpa!")
```

