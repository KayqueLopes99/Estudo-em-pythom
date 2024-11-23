teste = list()
teste.append("Kay")
teste.append(19)
galera = list()
# A partir desse momentos as listas estão ligadas se alterar uma coisa em uma a outra também vai alterar.
'''
galera.append(teste)
teste[0] = "Maria"
teste[1] = 20
galera.append(teste)
print(galera)
saida: [['Maria', 20], ['Maria', 20]]
'''

galera.append(teste[:])
teste[0] = "Maria"
teste[1] = 20
galera.append(teste[:])
print(galera)