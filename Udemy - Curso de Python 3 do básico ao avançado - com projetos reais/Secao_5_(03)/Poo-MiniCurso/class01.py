class MinhaClasse:
   def __init__(self, nome, descricao):
      self.__nome = nome
      self.descricao = descricao
   def get_nome(self):
      return self.__nome
   def set_nome(self, valor):
      self.__nome = valor
   def new_function(self):
      return "OK"
classe = MinhaClasse("classe1", "Minha primeira classe")

antigo = classe.get_nome()
classe.set_nome("Novo Nome")
novo = classe.get_nome()
print(antigo, " - ", novo)

valor = classe.new_function()
print(valor)