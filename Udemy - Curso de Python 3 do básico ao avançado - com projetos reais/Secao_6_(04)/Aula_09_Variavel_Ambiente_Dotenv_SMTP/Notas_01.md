### Como usar variáveis de ambiente

- Para definir variáveis de ambiente:
    - **Windows PowerShell:**  
        `$env:VARIAVEL="VALOR"`  
        `dir env:`
    - **Linux e Mac:**  
        `export NOME_VARIAVEL="VALOR"`  
        `echo $VARIAVEL`
- Para obter o valor das variáveis de ambiente:
    - `os.getenv('VARIAVEL')`
    - `os.environ['VARIAVEL']`
- Para configurar variáveis de ambiente em Python:
    - `os.environ['VARIAVEL'] = 'valor'`
- Usando python-dotenv e o arquivo `.env`:
    - Instale: `pip install python-dotenv`
    - Importe e carregue:  
        ```python
        from dotenv import load_dotenv
        load_dotenv()
        ```
    - Documentação: [python-dotenv](https://pypi.org/project/python-dotenv/)
    - **OBS:** Sempre crie um `.env-example`

#### Exemplo de código

```python
import os
from dotenv import load_dotenv
load_dotenv()
CAMINHO_ARQUIVO = os.getenv('CAMINHO_ARQUIVO', 'aula_13.txt')
if not CAMINHO_ARQUIVO:
        raise ValueError('CAMINHO_ARQUIVO não está definido no .env')
with open(CAMINHO_ARQUIVO, 'r') as arquivo:
        texto = arquivo.read()
        print(texto)
```

- Crie um arquivo `.env-example`
- Promove segurança contra vazamento de dados sensíveis
- Nunca envie o arquivo `.env` para repositórios públicos
- O arquivo `.env` pode conter dados do banco

---

## Explicação

python-dotenv é uma biblioteca Python que permite usar arquivos de configuração para armazenar e acessar variáveis de ambiente de forma fácil e segura.

As variáveis de ambiente são valores usados no código que podem variar conforme o ambiente (produção, desenvolvimento, etc).

Para usar o python-dotenv:
1. Instale com pip:  
     `pip install python-dotenv`
2. Crie um arquivo `.env` na raiz do projeto:

     ``` python
     # .env
     VARIAVEL_DE_AMBIENTE_1=valor
     VARIAVEL_DE_AMBIENTE_2=valor
     VARIAVEL_DE_AMBIENTE_3=valor
     ```

3. No código, acesse as variáveis:

     ```python
     import os
     valor_da_variavel_1 = os.getenv("VARIAVEL_DE_AMBIENTE_1")
     ```

python-dotenv lê o arquivo `.env` e adiciona as variáveis ao ambiente do sistema operacional, tornando-as disponíveis via `os.getenv()`.

Isso evita expor senhas ou informações confidenciais no código ou em repositórios compartilhados. Adicione o arquivo `.env` ao `.gitignore` e crie um `.env-example` com valores fictícios.

Também é útil para armazenar configurações específicas de cada ambiente (desenvolvimento, teste, produção).

Doc: [https://pypi.org/project/python-dotenv/](https://pypi.org/project/python-dotenv/)