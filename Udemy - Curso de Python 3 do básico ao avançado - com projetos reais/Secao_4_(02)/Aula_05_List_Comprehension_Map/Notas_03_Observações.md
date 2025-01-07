## List comprehension com mais de um for
- Podemos fazer um for dentro de outro.

```py
lista = []
for x in range(3):
    for y in range(3):
        lista.append((x, y))


lista_01 = [
    (x, y)
    for x in range(3)
    for y in range(3)
]

print(lista_01)
```


## Duuvidas:
- Atribuição de uma lista a outra variavel, as duas apontam para o mesmo local na memória. Isso implica que se um muda a outra muda também. 
- `copy()`

```py

## Duvida - Sintaxe:
numbers = [1, 2, 3, 4, 5]
new_number = [number for number in numbers]
# print(new_number)

## Duvida - Utilização: Realizar operções.
new_number_division = [number / 2 for number in numbers] # Mapeando
new_number_multiplication = [number * 2 for number in numbers] # Mapeando
new_number_potenciacion = [number ** 2 for number in numbers] # Mapeando

print(f"{new_number_division}\n{new_number_multiplication}\n{new_number_potenciacion}")

## Dúvida - Condicionais (filter)
numbers_03 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_number_03 = [number for number in numbers_03 if number > 5]
impares = [number for number in numbers_03 if number % 2 != 0]
pares = [number for number in numbers_03 if number % 2 == 0]

other_if = [number if number != 6 else 600 for number in pares]
print(f"{new_number_03}\n{impares}\n{pares}\n{other_if}")

## Dúvida - Linhas e colunas - for aninhado
rows_and_columns = [
    (x, y)
    for x in range(1, 11) 
    for y in range(1, 6) 
    if x != 2]

print(rows_and_columns)

## Dúvida - string

string = 'José Kayque Lima Lopes'
number_of_letters = 5

new_string = [string[indice:indice + number_of_letters
] for indice in range(0, len(string), number_of_letters
)]

print(new_string)
```
