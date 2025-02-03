## Modos de abertura de arquivo e encoding com with open
### Modos de Abertura (`open()`) 
| **Modo** | **Descrição** |
|---------|--------------|
| `r` | **Modo de leitura** (**read**). Retorna erro se o arquivo não existir. |
| `w` | **Modo de escrita** (**write**). Cria um novo arquivo ou sobrescreve um existente. |
| `x` | **Modo de criação** (**exclusive**). Retorna erro se o arquivo já existir. |
| `a` | **Modo de adição** (**append**). Adiciona conteúdo ao final do arquivo, sem apagá-lo. |
| `b` | **Modo binário** (**binary**), usado para arquivos como imagens e vídeos. |
| `t` | **Modo texto** (**text**). É o padrão se não for especificado. |
| `+` | **Leitura e escrita simultânea** no mesmo arquivo. |
                                   
+ Os modos podem ser combinados:    
- `"w+"` - Escrita e leitura, sobrescrevendo o arquivo.  
- `"a+"` - Adiciona e permite leitura sem apagar o conteúdo existente.  
- `+r` Leitura e Escrita (`read and write`) Abre o arquivo para leitura e escrita. 

- O modo `w` ele apaga tudo que estava no arquivo antes e escreve tudo denovo. 
- O modo `a` começa no final do arquivo não deletando.
### O encoding com with open:
- Os caracteres com acentos e especiais podem ficar distorcidos.
- Para os caracteres especiais sejam interpretados corretamente, evitando erros de decodificação.

### Explicação:
- `encoding="utf-8"`: Padrão mais comum, suporta a maioria dos caracteres.

### Exemplo de leitura de arquivo com encoding:

```python
# Lendo um arquivo UTF-8
with open("exemplo.txt", "r", encoding="utf-8") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)
```
```python
# Escrevendo um arquivo com UTF-8
with open("saida.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write("Olá, mundo!")
```

