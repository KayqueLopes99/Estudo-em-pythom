# Condições (Parte 1)
- São blocos de comandos separados que seguem um caminho que o usuário escolhe.
- Facilitar ou complicar, segundo a condição.

## IF e ELSE
- Usadas para controle de fluxo condicional.
- Se a condição for verdadeira, o bloco de código sob o `if` é executado. Se a condição for falsa, o bloco de código sob o `else` é executado.

- Sintaxe:

```python
if condição:
    # bloco de código executado se a condição for verdadeira
else:
    # bloco de código executado se a condição for falsa
```

- Exemplo:

```python
idade = 20
if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")
```
## Indentação
- Linhas dentro da condicional.
-Consistência: A convenção padrão é usar 4 espaços para cada nível de indentação.

```python
for i in range(5):  # Início do loop for
    if i % 2 == 0:  # Início do if
        print(f"{i} é par.")  # Esta linha está duplamente indentada
    else:
        print(f"{i} é ímpar.")  # Esta linha também está duplamente indentada
```

## ELIF
-  É usada em uma estrutura de controle de fluxo `if` para verificar múltiplas condições em sequência.
- Sintaxe:

```python
if condição1:
    # bloco de código executado se condição1 for verdadeira
elif condição2:
    # bloco de código executado se condição1 for falsa e condição2 for verdadeira
else:
    # bloco de código executado se todas as condições anteriores forem falsas
```

- Pode ter quantos blocos elif quiser em uma estrutura `if`.

```python
idade = 20
if idade < 13:
    print("Criança")
elif idade < 18:
    print("Adolescente")
elif idade < 60:
    print("Adulto")
else:
    print("Idoso")
```
## Condições simplificada:
- Colocar códigos em uma mesma linha
``` python
 idade = int(input('Digite sua idade: '))
status = 'menor' if idade < 18 else 'maior'
print('Você é {status} de idade')

```