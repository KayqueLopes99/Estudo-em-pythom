#  Manipulação de dados textuais OBS:
- s.find(subtexto, ini, fim) Procura subtexto em s começando da posição ini até a posição fim.
- Retorna −1, se o subtexto não for encontrado.
```PYTHON

nome_completo = input('Informe seu nome completo: ')
sobrenome = input('Informe seu sobrenome: ')
pos = nome_completo.find(sobrenome)
if pos != -1:
 print('Seu sobrenome começa na posição ', pos)
else:
 print('Sobrenome não encontrado')
n = float(input('Informe um número: '))
print('{n:.8f}'.format(n=n))
```