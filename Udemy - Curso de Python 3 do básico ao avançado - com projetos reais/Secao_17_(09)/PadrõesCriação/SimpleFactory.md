## Simple Factory
> Conceito de factory: refere-se a uma classe ou método que é responsável por criar objetos. 

- Na programação POO, o termo factory (fábrica) refere-se a uma classe ou método que é responsável por criar objetos.

- Vantagens:
    Permitem criar um sistema com baixo acoplamento entre classes porque
    ocultam as classes que criam os objetos do código cliente.

    Facilitam a adição de novas classes ao código, porque o cliente não
    conhece e nem utiliza a implementação da classe (utiliza a factory).

    Podem facilitar o processo de "cache" ou criação de "singletons" porque a
    fábrica pode retornar um objeto já criado para o cliente, ao invés de criar
    novos objetos sempre que o cliente precisar.

- Desvantagens:
    Podem introduzir muitas classes no código

> Vamos ver 2 tipos de Factory da GoF: Factory method e Abstract Factory

- Simple Factory <- Uma espécie de Factory Method parametrizado
- Simple Factory pode não ser considerado um padrão de projeto por si só
- Simple Factory pode quebrar princípios do SOLID

Obs da imagem: - Product: interface.

---
![](image/image_01.png)

---
