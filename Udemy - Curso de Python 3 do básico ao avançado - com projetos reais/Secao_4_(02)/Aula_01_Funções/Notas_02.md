## (Parte 1) *args para quantidade de argumentos não nomeados variáveis
## Empacotamento em Python
- **Empacotamento**:
   - O empacotamento permite agrupar vários valores em uma única variável (como uma lista ou tupla).
   - Você pode usar o operador `*` para empacotar valores em uma sequência.
   - Ele Cria Um Tupla em Caso de Print:
```python
def contador(* núm):
    print(núm)

contador(1,4,3,2,7)
```


   - Exemplo:
     ```python
     def minha_soma(*args):
         return sum(args)

     print(minha_soma(1, 2, 3, 4, 5))  # Saída: 15
     ```
- Acumulação - A cada iteração vai realizando uma operação atuaizando este acumulador.

## (Parte 2) *args para quantidade de argumentos não nomeados variáveis

```` py

# Lembre-te de desempacotamento
x, y, *resto = 1, 2, 3, 4
print(x, y, resto)


# def soma(x, y):
#     return x + y

# *ARGS - empacota o que se envia na função dentro de uma tupla.
def soma(*args):
    total = 0
    for numero in args:
        print('Total:', total, numero)
        total = total + numero
        print("Total:", total)
    return(total)

numeros01 = (1, 2, 3, 4, 5, 6, 7, 8)



# Desempacotando a tupla para enviar como parâmetros na função. 
somatoria_01 = soma(*numeros01)
print(somatoria_01)

numeros02 = (8, 9, 10, 11 ,12, 13)
somatoria_02 = sum(numeros02)
print(somatoria_02)
````