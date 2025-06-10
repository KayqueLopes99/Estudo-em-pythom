### Comandos da Biblioteca `re` 
- Definição: A biblioteca `re` em Python é usada para trabalhar com
* **Validação:** Verificar se uma string (como um e-mail, CPF, telefone) segue um formato específico.
* **Busca:** Encontrar ocorrências de um padrão dentro de um texto.
* **Substituição:** Substituir partes de um texto que correspondem a um padrão.
* **Extração:** Extrair informações específicas de um texto.

#### Validação de E-mails
```python
import re

# Regex padrão para e-mails
# Explicação detalhada abaixo
email_regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

def validar_email(email):
    if re.match(email_regex, email):
        return True
    return False

print(f"teste@exemplo.com: {validar_email('teste@exemplo.com')}")  # True
print(f"nome.sobrenome@sub.dominio.br: {validar_email('nome.sobrenome@sub.dominio.br')}")  # True
print(f"email@servidor.muito.longo: {validar_email('email@servidor.muito.longo')}") # True
```

**Explicação do Regex:** `r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"`

* `^`: Início da string. Garante que o padrão casa desde o começo.
* `[a-zA-Z0-9._%+-]+`: **Parte local (usuário)**
    * `[a-zA-Z0-9._%+-]`: Conjunto de caracteres permitidos: letras (maiúsculas/minúsculas), números, ponto, underscore, porcentagem, mais e hífen.
    * `+`: Indica que deve haver uma ou mais ocorrências desses caracteres.
* `@`: O caractere literal arroba.
* `[a-zA-Z0-9.-]+`: **Parte do domínio**
    * `[a-zA-Z0-9.-]`: Conjunto de caracteres permitidos: letras, números, ponto, hífen.
    * `+`: Uma ou mais ocorrências.
* `\.`: Um ponto literal. O `\` escapa o `.` para que ele não seja interpretado como "qualquer caractere".
* `[a-zA-Z]{2,}`: **Top Level Domain (TLD)**
    * `[a-zA-Z]`: Apenas letras.
    * `{2,}`: Duas ou mais ocorrências (ex: .com, .net, .br).
* `$`: Fim da string. Garante que o padrão casa até o final.



####  Extração de Números de Telefone - `(XX) XXXX-XXXX` ou `(XX) XXXXX-XXXX`.

```python
import re

texto = "Entre em contato pelo (11) 98765-4321 ou (21) 3456-7890."

# Regex para telefones: (DD) NNNN-NNNN ou (DD) NNNNN-NNNN
# r"\(\d{2}\)\s?\d{4,5}-\d{4}"
# Explicação:
# \( : parêntese de abertura literal
# \d{2} : dois dígitos (DDD)
# \) : parêntese de fechamento literal
# \s? : zero ou um espaço em branco (opcional)
# \d{4,5} : 4 ou 5 dígitos (primeira parte do número)
# - : hífen literal
# \d{4} : 4 dígitos (última parte do número)

telefones = re.findall(r"\(\d{2}\)\s?\d{4,5}-\d{4}", texto)
print(f"Telefones encontrados: {telefones}")
# Saída: Telefones encontrados: ['(11) 98765-4321', '(21) 3456-7890']
```


####  Extração de Datas no Formato DD/MM/AAAA

```python
import re

log_entry = "Erro em 05/06/2023. Sucesso em 20/01/2024."

# Regex para datas: DD/MM/AAAA
# r"\d{2}/\d{2}/\d{4}"
# Explicação:
# \d{2} : dois dígitos
# / : barra literal
# \d{4} : quatro dígitos

datas = re.findall(r"\d{2}/\d{2}/\d{4}", log_entry)
print(f"Datas encontradas: {datas}")
# Saída: Datas encontradas: ['05/06/2023', '20/01/2024']
```

