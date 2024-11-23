# Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

Contagem = ('Nought ', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen', 'Twenty')


numero = -1

while True:
    print('='*30)
    print('\033[33mDigite um número de 0 - 20:\033[m')
    print('21 - Sair')
    numero = int(input('Informe o Número: '))
    if 0 <= numero <= 20:
        print(f'O número {numero} em Extenso é {Contagem[numero]}')

    elif numero == 21:
        print('Saindo do Programa...')
        break
    else:
        print("Informe Um Número Válido.")