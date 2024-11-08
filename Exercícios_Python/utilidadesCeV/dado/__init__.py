def leiaDinheiro(msg):
    while True:
        numero = input(msg).replace(',', '.')

        if numero.replace('.', '').isdigit():  # trannsformar o . ou , em vazio
            return float(numero)  
        else:
            print("\033[91mErro! Por favor, digite um número inteiro válido.\033[m") 
    