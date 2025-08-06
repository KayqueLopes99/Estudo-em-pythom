import random

# Funções principais:

# random.seed(valor)
#   Inicializa o gerador de random (por isso "números pseudoaleatórios")
# random.seed(0)

# random.randrange(início, fim, passo)
#   Gera um número inteiro aleatório dentro de um intervalo específico
r_range = random.randrange(10, 20, 2)
# print(r_range)

# random.randint(início, fim)
#   Gera um número inteiro aleatório dentro de um intervalo (sem passo)
# 20 - 1 = até o 19
r_int = random.randint(10, 20)
# print(r_int)

# random.uniform(início, fim)
#   Gera um número flutuante aleatório dentro de um intervalo (sem passo)
r_uniform = random.uniform(10, 20)
# print(r_uniform)

# random.shuffle(sequencia_mutável)
#   Embaralha a lista original
nomes = ['Luiz', 'Maria', 'Helena', 'Joana']
# random.shuffle(nomes)
# print(nomes)

# random.sample(iterável, k=N)
#   Escolhe elementos do iterável e retorna outro iterável (não repete)
novos_nomes = random.sample(nomes, k=3)
# print(nomes)
# print(novos_nomes)

# random.choices(iterável, k=N)
#   Escolhe elementos do iterável e retorna outro iterável (pode repetir valores)
novos_nomes = random.choices(nomes, k=3)
print(nomes)
print(novos_nomes)

# random.choice(iterável)
#   Escolhe um elemento do iterável
print(random.choice(nomes))


# GERANDO SENHA.
# import secrets

# import string as s
# from secrets import SystemRandom as Sr

# print(''.join(Sr().choices(s.ascii_letters + s.digits + s.punctuation, k=64)))
# python -c "import string as s;from secrets import SystemRandom as Sr; print(''.join(Sr().choices(s.ascii_letters + s.punctuation + s.digits,k=12)))"