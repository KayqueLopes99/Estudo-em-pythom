# B) Escreva um código que receba um número de segundos e converta este número em horas, minutos e segundos. Escreva também um código que faça o contrário.
numero = int(input('Informe um Número de Segundos: '))

minutos = numero // 60
segundos = numero % 60
horas = minutos // 60
minutos %= 60
print("Segundos: {}\nMinutos: {}\nHoras: {}\n".format(segundos, minutos, horas))
