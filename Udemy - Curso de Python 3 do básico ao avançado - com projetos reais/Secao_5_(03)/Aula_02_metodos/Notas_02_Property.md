##  **@property** - um getter no modo Pythônico
### **@property - O Jeito Pythônico de Gerenciar Atributos**
+ **Getter**  
- Um método para **acessar/ler/obter** o valor de um atributo.
+ Modo Pythônico: Refere-se às práticas idiomáticas do Python.

+ **@property**: propriedade do objeto. 
- Um decorador que transforma um método em uma **propriedade do objeto**, permitindo que ele seja acessado como se fosse um atributo comum.  
- *Exemplo prático:* Um método `valor` vira `objeto.valor` (sem parênteses!).

---
## **Usar?**  

1. **Controle de Acesso (Getter)**  
   - Ler atributos com validações ou cálculos dinâmicos  
   - Exemplo: Calcular idade a partir da data de nascimento.

2. **Preservação do Código Cliente**  
   - Evita quebras em códigos existentes que acessam atributos diretamente.  
   - Permite adicionar lógica sem alterar a interface pública da classe.

3. **Habilitar Setters/Deleters**  
   - Permite criar métodos associados com `@propriedade.setter` e `@propriedade.deleter` para controle de modificações/remoções.

4. **Ações Transparentes**  
   - Executar ações secundárias ao acessar um atributo.

## **Código Cliente: 
- Se você alterar a estrutura interna de uma classe sem propriedades, todo código que acessa atributos diretamente precisará ser reescrito. O `@property` elimina esse problema!
- É o código que usa seu código. 

---

Aqui está sua explicação aprimorada para maior clareza e fluidez:  

---

### `@property` + `@setter` - Getter e Setter no modo Pythônico 
- **`@property`**: Decorador que transforma um método de classe em um **atributo somente leitura**, permitindo acessá-lo como um atributo normal, sem precisar chamá-lo como uma função.  

- **Getter**: Método que retorna o valor de um atributo.

- **Setter**: Método que permite modificar o valor de um atributo.  
  - Definido acima da função com `@nome_da_property.setter`.  
  - Exige um **novo valor** como entrada para atualizar o **valor armazenado**.  
  - Pode ser usado para restringir valores inválidos ou aplicar validações.  
  - Temos que salvar ele é algum local.

- Se um atributo for apenas **`@property`** (getter), **não pode ser modificado diretamente**. Para permitir modificações, é necessário definir um **setter**. 

- Atributos que começam com um ou dois underlines (`_atributo`, `__atributo`) são considerados **privados** e **não devem ser acessados diretamente** fora da classe.

#### **Exemplo Prático**
```python
class Produto:
    def __init__(self, preco):
        self._preco = preco  # Atributo "protegido"

    @property
    def preco(self):

        """Getter(obtendo valor do atributo): Retorna preço com desconto de 10%"""
        return self._preco * 0.9

    @preco.setter
    def preco(self, novo_valor):
        """Setter(modifica o valor do atributo): Valida novo preço"""
        if novo_valor > 0:
            self._preco = novo_valor
        else:
            raise ValueError("Preço inválido")

# Código Cliente (não quebra!)
produto = Produto(100)
print(produto.preco)  # 90.0 (usa o getter)
produto.preco = 200   # Usa o setter
```