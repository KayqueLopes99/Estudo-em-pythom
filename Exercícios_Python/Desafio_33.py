# Faça um programa que leia Três números e mostre qual é o maior e qual o menor.

a = int(input("Informe um algarismo: "))
b = int(input("Informe um algarismo: "))
c = int(input("Informe um algarismo: "))

if a <= b <= c:
    print("Ordem \nPrimeiro: {}\nSegundo: {}\nTerceiro {}\n".format(a, b, c))
elif a <= c <= b:
    print("Ordem \nPrimeiro: {}\nSegundo: {}\nTerceiro {}\n".format(a, c, b))
elif b <= a <= c:
    print("Ordem \nPrimeiro: {}\nSegundo: {}\nTerceiro {}\n".format(b, a, c))
elif b <= c <= a:
    print("Ordem \nPrimeiro: {}\nSegundo: {}\nTerceiro {}\n".format(b, c, a))
elif c <= a <= b:
    print("Ordem \nPrimeiro: {}\nSegundo: {}\nTerceiro {}\n".format(c, a, b))
else:
    print("Ordem \nPrimeiro: {}\nSegundo: {}\nTerceiro {}\n".format(c, b, a))
