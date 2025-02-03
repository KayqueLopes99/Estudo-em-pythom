## os.remove, os.unlink e os.rename - apagando, renomeando e movendo arquivos
### 0.1 `os.remove()` e `os.unlink()`  
- Ambas são usadas para excluir arquivos no sistema.
- Sintaxe:
```python
import os
os.remove("caminho/do/arquivo")
# ou
os.unlink("caminho/do/arquivo")
```

### 0.2️ `os.rename()` 
- Usado para renomear ou mover arquivos e diretórios.

- Sintaxe:
```python
import os
os.rename("caminho/antigo", "caminho/novo")
```
- Se `caminho/novo` for um nome diferente no mesmo diretório, o arquivo será **renomeado**.
- Se `caminho/novo` for um diretório diferente, o arquivo será **movido**.

```python
import os

arquivo_antigo = "dados.txt"
arquivo_novo = "dados_renomeado.txt"

if os.path.exists(arquivo_antigo):
    os.rename(arquivo_antigo, arquivo_novo)
    print("Arquivo renomeado com sucesso!")
else:
    print("Arquivo não encontrado!")
```