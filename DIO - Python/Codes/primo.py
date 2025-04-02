"""
### **Exercício: Verificação de Número Primo**  

Crie uma **função em Python** que verifica se um número é primo.  

#### **Requisitos:**  
1. O programa deve solicitar um número inteiro positivo ao usuário.  
2. A função deve retornar **True** se o número for primo e **False** caso contrário.  
3. O programa deve exibir uma mensagem informando se o número é primo ou não.  

#### **Exemplo de Entrada e Saída:**  
```
Digite um número: 7
7 é um número primo!
```
```
Digite um número: 10
10 não é um número primo.
```

💡 **Dica:** Um número é primo se for maior que 1 e **divisível apenas por 1 e por ele mesmo**.  

Tente resolver! Se precisar de ajuda, estou aqui. 🚀
"""

from math import sqrt

def is_prime_number(num):
    if num < 2:
        return f"O Número {num} não é primo"
    
    for i in range(2, (int(sqrt(num)) + 1)): 
        if num % i == 0:
            return f"O Número {num} não é primo"

    return f"O Número {num} é primo"

print("\033[38;5;136m------- Números Primos -------\033[m")

num = input("Informe um algarismo para verificar se ele é um número primo: ")

if num.isdigit():
    num = int(num)
    print(is_prime_number(num))
else:
    print("\033[91mErro: Digite apenas números inteiros.\033[m")

print("\033[38;5;136m------- Carros -------\033[m")

def save_car(model, year, mark, plate):
    return f"Carro: {model}/{year}/{mark}/{plate}"

print(save_car("Modelo: Palio", "Ano: 2004", "Marca: Fiat", "Placa: 2345671"))