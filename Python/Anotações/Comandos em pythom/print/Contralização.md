## Centralização em Printf
- Usando f-strings com símbolos personalizados:
Exemplo:
- *:^60*
```Python 
print(f'{"ACME INC.":^60}')

```

print(f'{"ACME INC.":^60}')
- Isso centraliza o texto “ACME INC.” em um campo de 60 caracteres3.

### Outro Exemplo:
- centralização de números.
```Python 
lista1 = list()
lista2 = list()
lista3 = list()
lista_Oficial = []
for i in range(3):
    numero1 = int(input(f"Informe um número para posição [{0},{i}]: "))
    lista1.append(numero1)
    
for i in range(3):
    numero2 = int(input(f"Informe um número para posição [{1},{i}]: "))
    lista2.append(numero2)
for i in range(3):
    numero3 = int(input(f"Informe um número para posição [{2},{i}]: "))
    lista3.append(numero3)

lista_Oficial.append(lista1)
lista_Oficial.append(lista2)
lista_Oficial.append(lista3)
# Nessa parte.
for linha in range(0,3):
    for coluna in range(0,3):
      print(f"[{lista_Oficial[linha][coluna]:^5}]", end='')# Centraliza um cinco casas decimais.
    print()

```
# :<10
- Alinhamento a direita.
# :>5
- Alinhamento a esquerda.