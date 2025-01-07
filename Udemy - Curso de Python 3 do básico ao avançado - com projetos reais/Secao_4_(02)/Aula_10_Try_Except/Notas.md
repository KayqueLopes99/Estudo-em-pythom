## 149. (Parte 1) try e except para tratar exceções
# Tratamento de Erros e Exceções 
- Nessa aula, vamos ver como o Python permite tratar erros e criar respostas a essas exceções. Aprenda como usar a estrutura try except no Python de uma forma simples.
- *Não se pode silenciar os erros*: Isto é tratar os erros sem especifica-los como por exemplo no except.
- Deve-se informar o erro no `except`.
- Classe: exception.
- Pode passar mais de uma excerção usando uma tupla: `except (exception_)01, exception_02, ...)` 
## Teoria:
- Erro: Sintaxe_Error, Sintaxe do Código.
- Exceção: Value_Error, Valor digitado pelo usuário.
- Exemplos: Tipos, Valores não existentes em uma estrutura(IndexError), nos módulos não existentes. 
+ Exception = Exceção

## try (Tente) e except (Se ouver erro ou excerção faça isso ...)
- Os comandos `try` e `except` são usados em Python para capturar e tratar exceções (erros) que podem ocorrer durante a execução de um programa.

### Sintaxe Básica

```python
try:
    # Código que pode gerar uma exceção - Operação
except TipoDeErro_class_exception:
    # Código a ser executado se a exceção especificada ocorrer Falhou
# ...
except Exception:
    # Tratar todos os demais erros. # Não é muito bom!?

except (TipoDeErro_class_exception_01, ...):
    # Podemos colocar mais de um error ou exceção.
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

## No Comando *as*
# As
- O comando `as`: **atribuir um apelido (alias)** a um item, tornando-o mais fácil de referenciar. 
- Como criar uam variavel. 
### Sintaxe
```python
Nome_do_Comando as alias_name_Apelido
```
### `as` em Blocos `try-except`
```python
try:
    resultado = 10 / 0
except ZeroDivisionError as e:
    print("Erro:", e)  # Mostra a descrição da exceção
```

- Neste caso, `e` contém informações sobre o erro que ocorreu, como mensagem de erro e tipo de exceção.

## Como ver a classe do erro:
- `variavel_do_erro.__class__.__name__)` *XError*. 

## try, except, else e finally + Built-in Exceptions
- Atenção nos regulamentos destes comandos.
- `https://docs.python.org/pt-br/3/library/exceptions.html#built-in-exceptions`
## raise - lançando exceções (erros)
- Isso significa que você pode interromper a execução do programa quando uma condição específica acontecer, indicando que há um erro.  

+ Sintaxe  
```python
raise TipoDeErro("Mensagem de erro")
```

