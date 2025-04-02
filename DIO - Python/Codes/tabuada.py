
print("\033[38;5;136m------- Simulação da Tabuada -------\033[m")

num = input("Informe um algarismo para visualizar sua Tabuada: ")

if num.isdigit():
    num = int(num)
    print("-"*15)
    for nums in range(1,11):
        result = num * nums
        print(f"{num} x {nums} = {result}")
        nums += 1
    print("-"*15)

else:
    print("\033[91mErro: Digite apenas números inteiros.\033[m")



print("\033[38;5;136m------- Percorrer strings -------\033[m")

word = input("Informe uma palavra: ")
VOWELS = 'AEIOU'
print("-"*15)  
for letter in word:
    if letter.upper() in VOWELS:
        print(f"{letter}", end=' ')
print("-"*15)  


print("\033[38;5;136m------- Menu com while-------\033[m")
while True:
    option = int(input("[1] - Sacar \n[2] - Extrato \n[10] - Sair: "))

    if option == 1:
        print("Saque")
    elif option == 2:
        print("Extrato")
    elif option == 10:
        print("Saindo")
        break
    else:
        print("Opção invalida")
    

