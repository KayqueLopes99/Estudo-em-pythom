## Uma introdução às f-strings (formatação de strings)
- São uma maneira de formatar strings que é mais concisa e fácil de ler do que os métodos anteriores.
- As f-strings são uma ferramenta poderosa e flexível que torna a formatação de strings em Python muito mais intuitiva e legível.
- Acesso na string: `string[indice]`
``
+12345
-54321
``
- Sintaxe:

```python
nome = "Mundo"
mensagem = f"Olá, {nome}!"
print(mensagem)  # Saída: Olá, Mundo!
```

```python
x = 10
y = 5
resultado = f"A soma de {x} e {y} é {x + y}"
print(resultado)  # Saída: A soma de 10 e 5 é 15
```

``` python
nome = 'Kayque Lopes'
altura = 1.65
peso = 59
imc = peso / (altura * altura) 

linha_1 = f"Nome: {nome} Altura: {altura} Peso: {peso} IMC: {imc:.2f}"
print(linha_1)

print(f"Nome: {nome} Altura: {altura} Peso: {peso} IMC: {imc:.2f}")
```

### Ajuste nas casas Decimais:
- Sintaxe: `f"{variavel_float:.numero_de_casas_para_aparecerf(f -> float)}"`
``` python
dinheiro = 123.45555
print(f'{dinheiro:.2f}') # Saída 123.45
```

## Formatação de strings com o método format
- Existem várias maneiras de formatar a saída do print em Python. 
- Método `.format()`, já com sintaxe:
- A primeira chave é o primeiro valor colocado dentro do format.
- O começo de contagens começa no zero dos índices.
```python
print('O candidato (a): {} tem {} votos.'.format(nome, votos))
```

- Neste exemplo, {} é um espaço reservado que será substituído pelos argumentos no .format().
- O primeiro {} será substituído por nome e o segundo {} será substituído por votos.

- Parâmetro Nomeado: 
- Nomear coisas nas chamadas ou criação das funções no seus parâmetros. 
- Deve nomear todos da da varíavel para frente. 

``` python
# Parâmetros Nomeados.
# Com índices 0,1,2,3 = Ordem de varíaveis. 
string = 'a= {nome1} b= {nome2} c= {nome3} d= {idade1:.2f}' 

# Deve nomear todos
format = string.format(
    nome1=a , nome2=b, nome3=c, idade1=d
)
print(format)
```

## Centralização e enfeites:
### Questão dos espaços e alinhamento 
nome = input("Qual seu nome: \n") 
print("Prazer {:20}!!!".format(nome))

### Alinhamento para direita.
nome1 = input("Qual seu nome: \n") 
print("Prazer {:>20}!!!".format(nome1))

### Alinhamento para esquerda.
nome2 = input("Qual seu nome: \n") 
print("Prazer {:<20}!!!".format(nome2))

### Alinhamento centralizado.
nome3 = input("Qual seu nome: \n") 
print("Prazer {:^20}!!!".format(nome3))

### Alinhamento centralizado com = + - no efeito.
nome3 = input("Qual seu nome: \n") 
print("Prazer {:+^20}!!!".format(nome3))


### Podemos fazer operações no própio format
``` python
num = int(input("Digite um número para ver a sua tabuada: "))
print("{} x 1 = {}".format(num, num*1))
```


# Interpolação de string com % em Python:
- A interpolação de string com % em Python é uma formatação de string antiga.
```
Interpolação básica de strings
s - string
d e i - int
f - float
x e X - Hexadecimal (ABCDEF0123456789)
```

```` python
nome = 'Kayque'
preco = 1000.8888
variavel = '%s, o preco total foi %f' % (nome, preco)
print(variavel)

print('O haxadecimal de %d é %04x' % (15, 15))
# 000f - 4 casas.

````

- OBS:
- Placeholders: é um texto temporário exibido em um campo de entrada, fornecendo uma dica ou exemplo sobre o que o usuário deve digitar.

## Formatação de strings com f-strings
- Formatação básica de strings
+ s - string
+ d - int
+ f - float
+ .<número de dígitos>f
+ x ou X - Hexadecimal
- :(Caractere)(><^)(quantidade)
- :'>' - Esquerda
- :< - Direita
- :^ - Centro
- Força o número a aparecer antes dos zeros
- Sinal - + ou - (Mostrar o sinal)
- Ex.: 0>-100,.1f
- Conversion flags - !r !s !a 