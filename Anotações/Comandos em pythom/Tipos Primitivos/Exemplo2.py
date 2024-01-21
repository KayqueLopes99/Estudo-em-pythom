# Código sintetíco
print('Bem vindo a pokedex python! ')
print('Vamos inserir os dados do usuario')
nome = (str(input('Digite seu nome de treinador:\n')))
nomep = (str(input('Digite seu nome do seu pokemon:\n')))
numero = (int(input('Digite o numero do seu pokemon:\n')))
peso = (float(input('Digite o peso do seu pokemon:\n')))

print("Dados:\nNome: {}\nPokemon: {}\nNumero: {}\nPeso: {}\n".format(nome, nomep, numero, peso))


resposta = input('Digite sim para cadastrar ou nao para excluir: ')
is_true = resposta.lower() == 'sim' # Para caracteres minusculos.

