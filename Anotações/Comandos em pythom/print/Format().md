## Formatação da saída de dados:
- Existem várias maneiras de formatar a saída do print em Python. 
. método ".format()", já com sintaxe:

```python
print('O candidato (a): {} tem {} votos.'.format(nome, votos))
```
Neste exemplo, {} é um espaço reservado que será substituído pelos argumentos no .format().
O primeiro {} será substituído por nome e o segundo {} será substituído por votos.

## Centralização e enfeites:
# Questão dos espaços e alinhamento 
nome = input("Qual seu nome: \n") 
print("Prazer {:20}!!!".format(nome))

# Alinhamento para direita.
nome1 = input("Qual seu nome: \n") 
print("Prazer {:>20}!!!".format(nome1))

# Alinhamento para esquerda.
nome2 = input("Qual seu nome: \n") 
print("Prazer {:<20}!!!".format(nome2))

# Alinhamento centralizado.
nome3 = input("Qual seu nome: \n") 
print("Prazer {:^20}!!!".format(nome3))

# Alinhamento centralizado com = + - no efeito.
nome3 = input("Qual seu nome: \n") 
print("Prazer {:+^20}!!!".format(nome3))


## END = ''

. O valor padrão de `end` é `'\n'`, que é o caractere de nova linha.
- Exemplo e sintaxe:
```python
print("Olá, ", end='')
print("mundo!")
```
- Resultado
```
Olá, 
mundo!
```
