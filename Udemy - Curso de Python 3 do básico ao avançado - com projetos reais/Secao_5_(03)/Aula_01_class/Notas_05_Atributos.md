## Atributos de classe
- De forma geral podemos dizer que os atributos são os “dados” de cada objeto. Eles armazenam as informações que caracterizam aquele objeto. Por exemplo, em uma classe Carro, podemos ter atributos como cor e modelo, que guardam informações específicas de cada instância (objeto) dessa classe.

- Os **atributos de classe** são variáveis definidas dentro da classe, mas fora dos métodos. Eles são compartilhados por todas as instâncias (objetos) da classe.

- Contexto: Uma constante dentro do escopo da classe que será compartilhada em todo local.
- **Alterar um atributo de classe afeta todas as instâncias, mas modificar um atributo de instância só muda aquele objeto.**
- A utilização do self nesta constante pode gerar erros.  

## Obs:
- **Atributos de Classe**: pertencem à classe e são iguais para todos os objetos.
- **Atributos de Instância**: pertencem a um objeto específico, podendo ter valores diferentes para cada um.


```python
class Carro:
    # Atributo de classe (compartilhado por todos os carros)
    rodas = 4  

    def __init__(self, cor, modelo):
        # A tributos de instância (podem ser diferentes paracada carro)
        self.cor = cor
        self.modelo = modelo

# Criando dois objetos da classe Carro
carro1 = Carro("Vermelho", "Sedan")
carro2 = Carro("Azul", "SUV")

print(carro1.rodas)  # Saída: 4
print(carro2.rodas)  # Saída: 4

print(carro1.cor)  # Saída: Vermelho
print(carro2.cor)  # Saída: Azul
```

```python
Carro.rodas = 6  # Mudando o valor do atributo de classe

print(carro1.rodas)  # Saída: 6
print(carro2.rodas)  # Saída: 6
```
+ **Se alterarmos `rodas` apenas em um objeto, ele cria um atributo de instância novo e não muda a classe:**
```python
carro1.rodas = 8  # Agora, só carro1 tem 8 rodas
print(carro1.rodas)  # Saída: 8
print(carro2.rodas)  # Saída: 6
```

