class Carinho:
    def __init__(self):
        self._produtos = []

    def total(self):
        return sum(mercadoria.preco for mercadoria in self._produtos)
    
    def inserir_produtos(self, *produtos):
        for produto in produtos:
            self._produtos.append(produto)

    def listar_produtos(self):

        print("-"*15)
        for produto in self._produtos:
            print(produto.nome, produto.preco)
        print("-"*15)


class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco


# Agregação
carrinho = Carinho()
p1, p2, p3 = Produto("Café", 5.50), Produto("Frutas", 10.50), Produto("Chá", 2.50)
carrinho.inserir_produtos(p1, p2, p3)
carrinho.listar_produtos()
print(carrinho.total())