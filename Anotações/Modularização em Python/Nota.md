# Módulos e Pacotes
- Nessa aula, vamos continuar nossos estudos de funções em Python, aprendendo como criar módulos em Python e reutilizar nossos códigos em outros projetos. Vamos aprender também como agrupar vários módulos em um pacote, ampliando ainda mais a modularização em grandes projetos em Python.

## Modularização:
+ Arquivos Grandes únicos com necessidade de partição das funcionalidades. 
+ Foco:
- DIVIDIR UM PROGRAMA GRANDE.
- AUMENTAR A LEGIBILIDADE.
- FACILITAR A MANUTEÇÃO.

### Teoria:
- Em Python, **módulos** são arquivos que contêm definições e instruções em Python (funções, classes, variáveis, etc.) que podem ser reutilizados em outros scripts ou programas.

    ```python
    import modulo
    # Ou
    from modulo import funções
    ## Essa segunda maneira é um risco, pois pode haver conflito com os demais módulos existentes.
    modulo.Nome_da_Função()
    ```

    ```python
    # arquivo: meu_modulo.py
    def saudacao(nome):
        return f"Olá, {nome}!"

    # Em outro arquivo:
    import meu_modulo
    print(meu_modulo.saudacao("José"))  # Saída: Olá, José!
    ```
### Estrutura de Módulos e Pacotes

- **Módulos** são arquivos `.py` individuais.

+ Uso:

    ```python
    from meu_pacote import modulo1
    ```
- O ideal é import meu_pacote nesta questão.
## Temos um exemplo no diretório Modulos. 

## Vantagens:
> Organização.
> Manutenção.
> Ocultação.
> Reutilização em outros arquivos. 


## Pacotes:
- **Pacotes** são diretórios que contêm vários módulos. Um pacote é identificado pela presença de um arquivo `__init__.py` dentro da pasta. Esse arquivo pode estar vazio ou conter código de inicialização para o pacote.

- Separar as funções por assunto. 
- Um pacote com varias funções separadas por ações no projeto.
+ Estrutura de exemplo de um pacote:

    ```
    meu_pacote/
    ├── __init__.py
    ├── modulo1.py
    └── modulo2.py

    meu_pacote/
    ├── __init__.py
    ├── pasta_cor
    └── pasta_calculos
    ```


