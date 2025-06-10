## O comando match
- Definição: O comando `match` é uma estrutura de controle que permite comparar uma variável com diferentes padrões, semelhante ao `switch` em outras linguagens.
- Sintaxe:
```python
match variavel:
    case padrao1:
        # bloco de código executado se variavel corresponder a padrao1
    case padrao2:
        # bloco de código executado se variavel corresponder a padrao2
    case _:
        # bloco de código executado se nenhuma das condições anteriores for satisfeita
```
- O `case _` é um coringa que captura qualquer valor que não corresponda aos padrões anteriores, funcionando como um `default` no `switch`.

- Exemplo:
```python
def verificar_numero(numero):
    match numero:
        case 1:
            return "Você escolheu o número um."
        case 2:
            return "Você escolheu o número dois."
        case 3:
            return "Você escolheu o número três."
        case _:
            return "Número não reconhecido."

# Testando a função
print(verificar_numero(1))  # Saída: Você escolheu o número um.
print(verificar_numero(4))  # Saída: Número não reconhecido.
```