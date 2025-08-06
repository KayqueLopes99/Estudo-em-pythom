## random: Gerador de Números Pseudoaleatórios

> **Obs.:** Números pseudoaleatórios parecem ser aleatórios, mas na verdade não são. Portanto, este módulo **não deve ser usado para segurança ou uso criptográfico**.  
> O motivo é que, com a mesma entrada e o mesmo algoritmo, a saída pode ser previsível.  
> [Documentação](https://docs.python.org/pt-br/3/library/random.html)

```python
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
```


## Secrets > **Obs.:** O módulo `secrets` é usado para gerar números aleatórios de forma segura, ideal para uso criptográfico.
```python
import secrets
randon = secrets.SystemRandom()

# random.randrange(início, fim, passo)
r_range = randon.randrange(10, 20, 2)
# random.randint(início, fim)
r_int = randon.randint(10, 20)
# random.uniform(início, fim)
r_uniform = randon.uniform(10, 20)
# random.shuffle(sequencia_mutável)
nomes = ['Luiz', 'Maria', 'Helena', 'Joana']
randon.shuffle(nomes)
# random.sample(iterável, k=N)
novos_nomes = randon.sample(nomes, k=3)
# random.choices(iterável, k=N)
novos_nomes = randon.choices(nomes, k=3)
# random.choice(iterável)
print(nomes)
print(random.choice(nomes))
# random.choice(iterável)
#   Escolhe um elemento do iterável
print(randon.choice(nomes))
```
