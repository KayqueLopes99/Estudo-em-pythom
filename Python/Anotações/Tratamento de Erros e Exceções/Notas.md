# Tratamento de Erros e Exceções 
- Nessa aula, vamos ver como o Python permite tratar erros e criar respostas a essas exceções. Aprenda como usar a estrutura try except no Python de uma forma simples.

## Teoria:
- Erro: Sintaxe_Error, Sintaxe do Código.
- Exceção: Value_Error, Valor digitado pelo usuário.
- Exemplos: Tipos, Valores não existentes em uma estrutura(IndexError), nos módulos não existentes. 
+ Exception = Exceção

## try e except

- Os comandos `try` e `except` são usados em Python para capturar e tratar exceções (erros) que podem ocorrer durante a execução de um programa.

### Sintaxe Básica

```python
try:
    # Código que pode gerar uma exceção - Operação
except TipoDeErro:
    # Código a ser executado se a exceção especificada ocorrer Falhou
# ...

else:
    # Code
finally:
    # Code

```

### Explicação

1. **Bloco `try`**: Contém o código que será executado. Se uma exceção ocorrer dentro do bloco `try`, o Python pulará para o bloco `except` correspondente.
2. **Bloco `except`**: Define o que deve acontecer caso uma exceção ocorra no bloco `try`. Podemos especificar o tipo de exceção que queremos capturar ou deixá-lo genérico para capturar qualquer exceção.

### Exemplo Básico

```python
try:
    numero = int(input("Digite um número: "))
    resultado = 10 / numero
except ValueError:
    print("Erro: Você deve digitar um número válido.")
except ZeroDivisionError:
    print("Erro: Divisão por zero não é permitida.")
```

### Blocos `else` e `finally`

- **`else`**: Executa o código caso não ocorra nenhuma exceção no bloco `try`.
- **`finally`**: Executa o código sempre, independente de uma exceção ocorrer ou não.

```python
try:
    numero = int(input("Digite um número: "))
    resultado = 10 / numero
except ValueError:
    print("Erro: Você deve digitar um número válido.")
except ZeroDivisionError:
    print("Erro: Divisão por zero não é permitida.")
else:
    print("Resultado:", resultado)
finally:
    print("Fim do programa.")
```
### Uso do as e __class__
- Para ver o erro no terminal.
- `Pratica.py`