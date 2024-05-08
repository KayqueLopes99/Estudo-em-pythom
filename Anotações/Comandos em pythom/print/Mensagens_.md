## Impressão de texto na tela em Python PRINT
- O PRINT() é usado para escrever e imprimir uma mensagem na tela, aqui não temos o printf.
- Tanto para caractere quanto para números.
- Sintaxe:
print('mensagem')
- Formatação não importa.
- \n pular linha.
``` python 
# Pode ser
print("Estou aprendendo pythom!\n")
# Ou
print('Estou aprendendo pythom!\n')

# Não é necessário o \n, mas você pode usar assim. No entendo se você coloca.
print("Olá\n","mundo!")
# Ou
# O print abaixo com o restante da mensagem ele já pula a linha para você!!!
print("Ola")
print("mundo!")

. Imprimir o valor de uma variável:
```python
## Temos isso tanto para caractere, quanto para número.
mensagem = "Olá, mundo!"
print(mensagem)
# Ou
numero = 10
print(numero)
```
# Temos como colocar as operações no print():
. Operação imprimida
print("5 + 2")
. Resultado do cálculo
print(5  + 2) ou print (7)
. Juntar números 
print('7'+'4') #saída será 74

# A , e o + tem seus momentos especiais 
. Em número + número 
print('7'+'4') #saída será 74
. Em caractere + número = ERRO
print("Kayque" + 5)
. Em caractere , número = CERTO
print("Kayque" , 5)

# Print para textos longos:
- Para imprimir textos longos em Python, você pode usar aspas triplas para criar uma string de várias linhas. 
```python
texto = """
Este é um texto longo.
Você pode adicionar quantas linhas quiser.
Basta manter tudo entre as aspas triplas.
"""

print(texto)
```

