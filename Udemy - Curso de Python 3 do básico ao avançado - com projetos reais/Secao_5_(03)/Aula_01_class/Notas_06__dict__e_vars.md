## `__dict__` e `vars()` para Atributos de Instância
- Todo objeto que tem atributos de instância armazena esses atributos em um dicionário interno chamado **`__dict__`**. - Esse dicionário mantém os valores atribuídos ao objeto em forma de **chave-valor**.

```python
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

# Criando um objeto da classe Pessoa
p1 = Pessoa("Ana", 25)

# Mostrando o dicionário interno do objeto
print(p1.__dict__)  # Saída: {'nome': 'Ana', 'idade': 25}
```
---

- A função **`vars(obj)`** retorna exatamente o dicionário `__dict__` do objeto.
- Salvar os dados ou desempacota-los. 
- ``**expandir``: expande os dados da estrutura.