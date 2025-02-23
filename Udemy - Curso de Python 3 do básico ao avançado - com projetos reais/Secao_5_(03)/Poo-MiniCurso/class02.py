class Loja:
    def __init__(self, nome, endereco, produtos=[]):
        self.__nome = nome
        self.__endereco = endereco
        self.__produtos = produtos

    def get_nome(self):
        return self.__nome

    def get_endereco(self) -> dict:
        return {"endereco": self.__endereco}

    def qtd_produtos(self):
        return len(self.__produtos)

    def exibe_produtos(self):
        for produto in self.__produtos:
            print(produto)

    def adiciona_produto(self, produto):
        self.__produtos.append(produto)

    def __str__(self) -> str:
        return "Loja: " + self.__nome


class Produto:
    def __init__(self, nome, codigo, preco, quantidade, loja=None):
        """Cria uma instância de Produto."""
        self.__nome = nome
        self.__codigo = codigo
        self.__preco = preco
        self.__quantidade = quantidade
        self.__loja = loja

    def adiciona_loja(self, loja: Loja):
        self.__loja = loja

    def get_loja(self):
        return self.__loja

    def __str__(self) -> str:
        return "Produto: " + self.__nome


loja = Loja("Loja1", "Rua tal no3")
endereco = loja.get_endereco()
type(endereco)
produto = Produto("produto1", 1, 30.00, 5)
print(produto)

produto.adiciona_loja(loja)
print(produto.get_loja().get_endereco())
loja.qtd_produtos()

loja.adiciona_produto(produto)
loja.qtd_produtos()
loja.exibe_produtos()

class Petshop(Loja):
    def __init__(self, nome, endereco, tipo_racao=[], produtos=[]):
        super().__init__(nome, endereco, produtos)
        self.__tipo_racao = tipo_racao

    def adiciona_produto(self, tipo_racao):
        self.__tipo_racao.append(tipo_racao)

    def exibe_produtos_racoes(self):
        for racao in self.__tipo_racao:
            print(racao)

    def get_tipo_racao(self):
        return self.__tipo_racao


petshop = Petshop('MyPet', "Novo Endereço Petshop")

print(petshop.qtd_produtos())  # Saída esperada: 0

petshop.adiciona_produto("Pedrigi")

petshop.exibe_produtos_racoes()  # Saída esperada: Pedrigi
