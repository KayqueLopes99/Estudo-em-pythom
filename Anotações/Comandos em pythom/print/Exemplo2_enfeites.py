# Questão dos espaços e alinhamento 
nome = input("Qual seu nome: \n") 
print("Prazer {:20}!!!".format(nome))

# Alinhamento para direita.
nome1 = input("Qual seu nome: \n") 
print("Prazer {:>20}!!!".format(nome1))

# Alinhamento para esquerda.
nome2 = input("Qual seu nome: \n") 
print("Prazer {:<20}!!!".format(nome2))

# Alinhamento centralizado.
nome3 = input("Qual seu nome: \n") 
print("Prazer {:^20}!!!".format(nome3))

# Alinhamento centralizado com = + - no efeito.
nome3 = input("Qual seu nome: \n") 
print("Prazer {:+^20}!!!".format(nome3))