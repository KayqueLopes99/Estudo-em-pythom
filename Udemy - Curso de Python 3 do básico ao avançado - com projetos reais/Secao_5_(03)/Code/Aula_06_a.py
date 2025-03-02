# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.

# Nesta parte A o arquivo salva os dados.
import json
CAMINHO = "C:\\Users\\kaiqu\\Music\\Estudo-em-pythom\\Udemy - Curso de Python 3 do básico ao avançado - com projetos reais\\Secao_5_(03)\\Code\\Aula_06.json"


class Poket_monsters:
    def __init__(self, name, num):
        self.name = name
        self.num = num
    def print(self):
        return f"O Pokémon {self.name} com o número da Pokedex {self.num}"
    

# Criando Instâncias
pokemon_1 = Poket_monsters("Bubasaur", 1)
pokemon_2 = Poket_monsters("Chamander", 4)
pokemon_3 = Poket_monsters("Squirtle", 7)

# Lista de pokémons convertida para dicionários
lista_pokemons = [p.__dict__ for p in [pokemon_1, pokemon_2, pokemon_3]]

def salvar_dados_dump():
  with open(CAMINHO, "w") as arquivo:
    json.dump(lista_pokemons, arquivo, indent=2, ensure_ascii=False) # ensure_ascii=False <- Acentos>
    print("Dados salvos com sucesso no arquivo.json!")

if __name__ == "__main__":
   salvar_dados_dump()
   