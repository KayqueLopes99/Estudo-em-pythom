## `pathlib`
- Módulo que encapsula caminhos de sistema de arquivos como objetos. 
-`from pathlib import Path`

### `Path(__file__)`
* `__file__` é uma variável especial do Python que, quando um script é executado, contém o caminho completo do arquivo do script atual.
* `Path(__file__)` converte esse caminho (que é uma string) em um objeto `Path`.

### `parent`
- A propriedade `parent` de um objeto `Path` retorna um novo objeto `Path` que representa o diretório pai do caminho atual.

**Exemplo:**

```python
from pathlib import Path

# Caminho do script (ex: /home/kayque/projetos/meu_script.py)
script_path = Path('/home/kayque/projetos/meu_script.py')

# O diretório pai do script é '/home/kayque/projetos'
script_parent_dir = script_path.parent
print(f"Diretório pai do script: {script_parent_dir}")
# Saída: Diretório pai do script: /home/kayque/projetos
```

### `touch(exist_ok=True)`

- O método `touch()` de um objeto `Path` cria um arquivo vazio no caminho especificado. Se o arquivo já existir, ele atualiza o tempo de modificação do arquivo.

* `exist_ok=True`: Se o arquivo já existe, `touch()` não levantará um `FileExistsError`. Ele simplesmente atualizará o tempo de modificação, o que é o comportamento mais comum e desejável na maioria dos casos. Se `exist_ok` for `False` (padrão) e o arquivo existir, um erro será gerado.

**Exemplo:**

```python
from pathlib import Path
import time

# Criando um caminho para um arquivo temporário no mesmo diretório do script
temp_file = Path(__file__).parent / "temp_log.txt"

# Cria o arquivo se não existir, ou atualiza o timestamp se existir
print(f"Criando/tocando o arquivo: {temp_file}")
temp_file.touch(exist_ok=True)
print(f"Existe agora? {temp_file.exists()}")

# Espera um pouco e toca novamente para ver o timestamp mudar (se o arquivo existir)
time.sleep(1)
print(f"Tocando o arquivo novamente (timestamp será atualizado)...")
temp_file.touch(exist_ok=True)

# Lembre-se de limpar o arquivo temporário após o uso
# temp_file.unlink() # Descomente para deletar o arquivo
```

### `exists()`
- O método `exists()` de um objeto `Path` verifica se o caminho (arquivo ou diretório) existe no sistema de arquivos. Retorna `True` se existir, `False` caso contrário.

### `stat()` e `st_size > 0`
* `stat()`: O método `stat()` de um objeto `Path` retorna um objeto `os.stat_result` (o mesmo que `os.stat()`). Este objeto contém várias informações sobre o arquivo ou diretório, como tamanho, permissões, tempos de criação/modificação, etc. Se o caminho não existir, `stat()` levantará um `FileNotFoundError`.
* `st_size`: É um atributo do objeto retornado por `stat()` que representa o tamanho do arquivo em bytes.
* `st_size > 0`: Esta condição é comumente usada para verificar se um arquivo existe **e não está vazio**.

**Exemplo:**
```python
from pathlib import Path
class Arquivo:
  def __init__(self, arquivo_json = 'fluxo_de_dados.json'):
        self.caminho_json = Path(__file__).parent / arquivo_json
        self.caminho_json.touch(exist_ok=True)  # Cria o arquivo, se não existir
    
  def escrever(self, dados):
        try: 
            if self.caminho_json.exists() and self.caminho_json.stat().st_size > 0:
               with open(self.caminho_json, 'r', encoding='utf-8') as arquivo:
                 conteudo = json.load(arquivo)  # Lê os dados existentes no arquivo JSON
            else:
               conteudo = []

           ...
```