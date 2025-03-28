# Validação em Python
- Há métodos muito práticos para verificar o conteúdo de uma string.

| Método       | Retorna `True` quando...                                               |
|--------------|------------------------------------------------------------------------|
| `Comando.isdigit()`  | A string contém apenas dígitos (0-9).                                  |
| `Comando.isnumeric()`| A string contém caracteres numéricos, incluindo símbolos numéricos.    |
| `Comando.isalpha()`  | A string contém apenas letras (sem espaços, números ou símbolos).      |
| `Comando.isalnum()`  | A string contém apenas letras e/ou números (sem espaços ou símbolos).  |

1. isdigit(): Verifica se uma string contém apenas dígitos.
    - Sintaxe: `string.isdigit()`

2. isdecimal(): Verifica se uma string contém apenas caracteres decimais.
    - Sintaxe: `string.isdecimal()`

3. isidentifier(): Verifica se uma string é um identificador válido em Python.
    - Sintaxe: `string.isidentifier()`

4. isspace(): Verifica se a string contém apenas espaços em branco.
    - Sintaxe: `string.isspace()`

5. islower(): Verifica se todos os caracteres na string estão em minúsculas.
    - Sintaxe: `string.islower()`

6. isupper(): Verifica se todos os caracteres na string estão em maiúsculas.
    - Sintaxe: `string.isupper()`



7. `isinstance()` 
- Usado para verificar se um objeto pertence a uma determinada classe ou a uma tupla de classes. Se ele é do tipo determinado pelo usuário.

- Sintaxe
```python
isinstance(obj, classinfo)
```
- `obj`: O objeto que você deseja verificar.
- `classinfo`: Pode ser uma única classe ou uma tupla de classes ou uma tipagem.

```python
x = 10
print(isinstance(x, int))  # Saída: True
print(isinstance(x, float))  # Saída: False
```
