def primo(n):
        cont = 0
        for i in range(1, n+1):
                if(n%i == 0):
                        cont = cont + 1
        return cont == 2
  
cont = 0
maximo = 20000
for n in range(2, maximo + 1):
        if(primo(n)):
                cont = cont + 1
print(f'O número de primos no intervalo é {cont}')