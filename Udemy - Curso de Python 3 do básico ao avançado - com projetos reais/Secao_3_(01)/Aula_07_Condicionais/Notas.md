## Introdução aos blocos de código + if / elif / else (condicionais)
# Condições (Parte 1)
- São blocos de comandos separados que seguem um caminho que o usuário escolhe.
- Facilitar ou complicar, segundo a condição.
- if = se.
- elif = se não se.
- else = se não.
- Usadas para controle de fluxo condicional.
- Se a condição for verdadeira, o bloco de código sob o `if` é executado. Se a condição for falsa, o bloco de código sob o `else` é executado.
- A ideia: `Você Executa ou não esse código.`
- Podemos aninhar as condições(Uma condição com outras dentro dela).
- Sintaxe:

```python
if condição:
    # bloco de código executado se a condição for verdadeira
else:
    # bloco de código executado se a condição for falsa
```

- `elif` É usada em uma estrutura de controle de fluxo `if` para verificar múltiplas condições em sequência.
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

##  if, elif e else: entendendo o fluxo do interpretador em condicionais
- Podemos atribuir True ou False para exibir ou não uma bloco de código, segundo as condições.
- Se uma condição é executada a outra associada como elif e else não será. 
- Checar varíaveis.
- Vai checando cada condição.
- Se quiser varías condições separadas coloca-se somente `if`.
- É possível adicionar um if dentro de outro fazendo várias condições aninhadas.

## O Debugger do VS Code e o interpretador do Python lendo os códigos
> Código -> seleciona a linha do breakpoint -> Executar e depurar -> Avançar ou Voltar. 

## Operação ternária com Python (if e else de uma linha)
- Condicional de uma linha.
-  Operação ternária (condicional de uma linha) <valor> if <codição> else <outro valor>

``` python
condicao = 10 == 11 # Condição. 
#                       True          False
#                    Vice versa dependendo do código. 
variavel = 'Valor' if condicao else 'Outro Valor'
print(variavel)


digito = 9 # > 9 = 0
novo_digito = digito if digito <= 9 else 0
novo_digito = 0 if digito > 9 else digito
print(novo_digito)


print('Valor' if False else 'Outro valor' if False else 'Fim')
```