
---
## Exercício com Abstração, Herança, Encapsulamento e Polimorfismo
Sistema bancário simples, que envolve clientes, contas e um banco. A ideia principal é que o cliente tenha uma conta (poupança ou corrente) e possa realizar saques e depósitos. Contas correntes possuem um limite extra.

`````` md
Conta (ABC)
    ContaCorrente
    ContaPoupanca

Pessoa (ABC)
    Cliente
        Cliente -> Conta

Banco
    Banco -> Cliente
    Banco -> Conta
``````

### Dicas:

1. **Criar a classe Cliente que herda da classe Pessoa (Herança):**
    - A classe `Pessoa` possui atributos como nome e idade, com seus respectivos getters.
    - A classe `Cliente` tem uma conta associada (agregação das classes `ContaCorrente` ou `ContaPoupanca`).

2. **Criar as classes `ContaPoupanca` e `ContaCorrente` que herdam de `Conta`:**
    - A classe `ContaCorrente` deve ter um limite extra.
    - Ambas as classes de conta (Corrente e Poupança) devem ter os seguintes atributos: agência, número da conta e saldo.
    - As classes de conta devem ter um método para depósito.
    - A classe `Conta` (superclasse) deve possuir o método `sacar` como abstrato (usando Abstração e Polimorfismo), sendo implementado pelas subclasses.

3. **Criar a classe Banco para AGREGAR as classes de clientes e de contas:**
    - A classe `Banco` será responsável por gerenciar clientes e contas (agregação).
    - O Banco realiza a autenticação dos clientes e das contas de acordo com:
      - O banco possui contas e clientes.
      - Verifica se a agência pertence ao banco.
      - Verifica se o cliente é do banco.
      - Verifica se a conta pertence ao banco.
    - Só será possível realizar um saque se o cliente passar na autenticação do banco.
    - O Banco autentica por meio de um método específico.

---

