from dataclasses import dataclass, asdict, astuple, field, fields

@dataclass(init=False)
class Pessoa:
    #nome: str
    #sobrenome: str

    def __init__(self, nome, sobrenome):
       self.nome = nome 
       self.sobrenome = sobrenome
       self.nome_completo = f"{self.nome} {self.sobrenome}"


    # Executado depois do init.
    def __post_init__(self):
       self.nome_completo = f"{self.nome} {self.sobrenome}"

    #@property
    # def nome_completo(self):
    #    return f"{self.nome} {self.sobrenome}"
    
    #@nome_completo.setter
    # def nome_completo(self, valor):
    #    nome, sobrenome = valor.title().split()
    #    self.nome = nome
    #   self.sobrenome = ' '.join(sobrenome)



if __name__ == '__main__':
  pessoa = Pessoa("José", "Kayque")
  #pessoa.nome_completo = 'Daniel Costa'
  print(pessoa)
  print(pessoa.nome_completo)
  


# Configurações do decorator dataclass frozen=True, order-True. 

#  asdict e astuple em dataclasses
@dataclass()
class Pessoa:
    nome: str
    sobrenome: str


if __name__ == '__main__':
  pessoa = Pessoa("José", "Kayque")
  #pessoa.nome_completo = 'Daniel Costa'
  print(asdict(pessoa))
  dicionario_data_class = asdict(pessoa)
  print(dicionario_data_class.keys())
  print(astuple(pessoa))
# Valores padrão, field e fields em dataclasses
@dataclass()
class Pessoa:
    nome: str = field(default="MISSING")
    sobrenome: str = 'Not sent'
    idade: int = 0
    enderecos: list[str] = field(default_factory=list)


if __name__ == '__main__':
  pessoa = Pessoa()
  print(pessoa)
  print(fields(pessoa))
  