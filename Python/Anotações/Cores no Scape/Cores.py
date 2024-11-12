
print('\033[7;40mBranco\033[m')
print('\033[1;41mVermelho\033[m')
print('\033[1;42mVerde\033[m')
print('\033[1;43mAmarelo\033[m')
print('\033[1;44mAzul\033[m')
print('\033[1;45mRoxo\033[m')
print('\033[1;46mAzul Claro\033[m')
print('\033[1;47mCinza\033[m')

Cores = int(input("Informe a Cor segundo a numeração: "))

if Cores == 1:
    print("\033[30mEscolheu\033[m")
elif Cores == 2:
    print("\033[31mEscolheu\033[m")
elif Cores == 3:
    print("\033[32mEscolheu\033[m")
elif Cores == 4:
    print("\033[33mEscolheu\033[m")
elif Cores == 5:
    print("\033[34mEscolheu\033[m")
elif Cores == 6:
    print("\033[35mEscolheu\033[m")
elif Cores == 7:
    print("\033[36mEscolheu\033[m")
else:
    print("\033[37mEscolheu\033[m")
