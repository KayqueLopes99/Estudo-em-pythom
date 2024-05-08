# Operadores lógicos 

## 1. and (e): 
- Retorna True se ambas as condições forem verdadeiras.
    ```python
    x = 5
    print(x > 3 and x < 10)  # Saída: True
    ```

## 2. or (ou): 
- Retorna True se pelo menos uma das condições for verdadeira.
    ```python
    x = 5
    print(x > 3 or x > 10)  # Saída: True
    ```

## 3. not (não): 
- Inverte o resultado, retorna False se o resultado for verdadeiro.
    ```python
    x = 5
    print(not(x > 3 and x < 10))  # Saída: False
    ```

````python
n1 = int(input('Informe um número: '))
n2 = int(input('Informe outro número: '))
p = (n1 > n2)
q = (n1 != n2)
r = not (p or q) and (not p)
print('p =', p)
print('q =', q)
print('r =', r)
````