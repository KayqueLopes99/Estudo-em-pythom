# Exercício Python 099: Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

# Empacotamento
def maior(* maior_ate_agr):
 cont = 0
 maior = 0

 for valor in maior_ate_agr:
  
  if cont == 0:
     maior = valor
  else:
   if valor > maior:
    maior = valor
  cont +=1
 print(f"O maior valor dos números{M,F,G,H,J} corresponde ao valor: {maior}")
print("-"*20)
while True:
 resposta = int(input("\033[36mDeseja Começar?\n(1-sim)\n(0-não)\nResposta: \033[m"))
 
 if resposta == 1:
  M = int(input("\033[35mValor do 1º número: \033[m"))
  F = int(input("\033[35mValor de 2º número: \033[m"))
  G = int(input("\033[35mValor de 3º número: \033[m"))
  H = int(input("\033[35mValor de 4º número: \033[m"))
  J = int(input("\033[35mValor de 5º número: \033[m"))
  maior(M,F,G,H,J)
  
 elif resposta == 0:
  print("\033[91m Saindo...\033[m")
  break
print("-"*20)


