"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

entrada = input('Informe um Número Inteiro: ')
if entrada.isdigit():

    numero_inteiro = int(entrada)

    if numero_inteiro % 2 == 0:
        print(f"O número {numero_inteiro} é Par.")
    else:
        print(f"O número {numero_inteiro} é Ímpar.")
else:
    print("Isso não é um número inteiro.")



"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
# Podemos fazer co try e except ou...
try:
    horario = int(input("Informe a Hora em formato (0 - 23): "))

    if horario >= 0 and horario <= 11:
       print(f"Bom Dia são {horario}:00.")
    elif horario > 11 and horario <= 17:
       print(f"Boa Tarde são {horario}:00.")
    elif horario >= 18 and horario <= 23:
       print(f"Boa Noite são {horario}:00.")
    else:
       print(f"Não conheço está Hora.")
except:
    print("Isso não é um número inteiro.")




"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome_do_usuario = input("Informe seu primeiro nome: ")
tamanho_do_nome = len(nome_do_usuario)
if tamanho_do_nome > 1 and tamanho_do_nome != ' ':
   if tamanho_do_nome <= 4:
     print("Seu nome é curto.")
   elif tamanho_do_nome >= 5 and tamanho_do_nome <= 6:
     print("Seu nome é normal.")
   else:
     print("Seu nome é muito grande.")
else:
   print("Digite mais um letra e não precione enter.")