"""
Exercício com Abstração, Herança, Encapsulamento e Polimorfismo
Criar um sistema bancário (extremamente simples) que tem clientes, contas e
um banco. A ideia é que o cliente tenha uma conta (poupança ou corrente) e que
possa sacar/depositar nessa conta. Contas corrente tem um limite extra.

# - corrente limite extra - se voce chegar no zero empresta um limite extra
# - poupança chega no zero não pode mais


Conta (ABC)
    ContaCorrente
    ContaPoupanca

Pessoa (ABC)
    Cliente
        Cliente -> Conta

Banco
    Banco -> Cliente
    Banco -> Conta

Dicas:
1. Criar classe Cliente que herda da classe Pessoa (Herança)
    - Pessoa tem nome e idade (com getters)
    - Cliente TEM conta (Agregação da classe ContaCorrente ou ContaPoupanca)



2. Criar classes ContaPoupanca e ContaCorrente que herdam de Conta
    - ContaCorrente deve ter um limite extra
    - Contas têm agência, número da conta e saldo
    - Contas devem ter método para depósito
    - Conta (super classe) deve ter o método sacar abstrato (Abstração e
      polimorfismo - as subclasses que implementam o método sacar)


      

3. Criar classe Banco para AGREGAR classes de clientes e de contas (Agregação)
    - Banco será responsável autenticar o cliente e as contas da seguinte maneira:
      - Banco tem contas e clientes (Agregação)
      - Checar se a agência é daquele banco
      - Checar se o cliente é daquele banco
      - Checar se a conta é daquele banco
    - Só será possível sacar se passar na autenticação do banco (descrita acima)
    - Banco autentica por um método.

Etapas adicionais para aprofundar conceitos de Python:

Etapa 1: Conceitos básicos
- Praticar a criação de classes e objetos.
- Implementar métodos simples.

Etapa 2: Encapsulamento e propriedades
- Adicionar propriedades com @property e @setter para controlar o acesso a atributos privados.

Etapa 3: Métodos Mágicos
- Implementar métodos __str__ para facilitar a exibição de objetos.

Etapa 4: Manipulação de Exceções
- Adicionar exceções personalizadas para tratar erros como saldo insuficiente.

Etapa 5: Persistência de Dados
- Implementar uma funcionalidade simples para salvar e carregar dados em arquivos usando a biblioteca pickle.

Etapa 6: Testes
- Criar testes unitários usando unittest para garantir o correto funcionamento das classes e métodos.

"""

d = {"v": 1, "f":5}

d["v"] =  5


print(d)