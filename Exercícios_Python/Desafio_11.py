# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua áres
# e a quantitadade de tinta necessária para tinta-la. Sabendo que cada litro de tinta, pinta uma área de 2,^2.

largura = float(input('Informe a largura da parede: '))
altura = float(input('Informe a altura da parede: '))

area = largura * altura

print("Largura: {:.2f}".format(largura))
print("Altura: {:.2f}".format(altura))
print('A área da parede é: {:.2f} metros quadrados'.format(area))

litro_tinta = (area)/2

print('A quantidade de tinta necessaria: {:.2f} litros'.format(litro_tinta))