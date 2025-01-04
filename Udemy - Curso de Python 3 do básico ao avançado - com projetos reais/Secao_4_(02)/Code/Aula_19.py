"""
Exercício
Crie uma função que encontra o primeiro duplicado considerando o segundo
número como a duplicação. Retorne a duplicação considerada.
Requisitos:
    A ordem do número duplicado é considerada a partir da segunda
    ocorrência do número, ou seja, o número duplicado em si.
    Exemplo:
        [1, 2, 3, ->3<-, 2, 1] -> 1, 2 e 3 são duplicados (retorne 3)
        [1, 2, 3, 4, 5, 6] -> Retorne -1 (não tem duplicados)
        [1, 4, 9, 8, ->9<-, 4, 8] (retorne 9)
    Se não encontrar duplicados na lista, retorne -1

-> Explicação:

Dada uma lista de números, o objetivo é percorrê-la do primeiro ao último elemento e identificar o primeiro número que aparece pela segunda vez. À medida que percorremos a lista, armazenamos os números já encontrados. Quando encontramos um número que já apareceu anteriormente, ele é considerado a primeira duplicação e deve ser retornado.  

### Exemplo:  
Lista: `[1, 4, 9, 8, ->9<-, 4, 8]`  
Passo a passo da análise:  
1. O primeiro número é `1` → não tem.
2. O segundo número é `4` → ainda não apareceu antes.  
3. O terceiro número é `9` → ainda não apareceu antes.  
4. O quarto número é `8` → ainda não apareceu antes.  
5. O quinto número é `9` → já apareceu antes (segunda ocorrência). **Retornamos 9**.  

Assim, o primeiro número que se repete na lista, considerando sua segunda ocorrência como critério, é `9`.

"""
lista_de_listas_de_inteiros = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],
    [1, 3, 2, 2, 8, 6, 5, 9, 6, 7],
    [3, 8, 2, 8, 6, 7, 7, 3, 1, 9],
    [4, 8, 8, 8, 5, 1, 10, 3, 1, 7],
    [1, 3, 7, 2, 2, 1, 5, 1, 9, 9],
    [10, 2, 2, 1, 3, 5, 10, 5, 10, 1],
    [1, 6, 1, 5, 1, 1, 1, 4, 7, 3],
    [1, 3, 7, 1, 10, 5, 9, 2, 5, 7],
    [4, 7, 6, 5, 2, 9, 2, 1, 2, 1],
    [5, 3, 1, 8, 5, 7, 1, 8, 8, 7],
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
]

def funcao_encontra_primeiro_duplicado(lista_de_listas):
    resultados = []
    for sublistas in lista_de_listas: # percorrer a lista
       numeros_vistos = set() # cria um set a cada momento
       primeiro_duplicado = -1 # caso não encontre

       for numero in sublistas: # percorrer as sublisttas
           if numero in numeros_vistos: # se o numero estiver no set()
              primeiro_duplicado = numero # Temos uma segundaocorrencia do duplicado
              break
           
           # Se não está no set()
           numeros_vistos.add(numero) 

       # Vai adicionando na lista os resultados
       resultados.append(primeiro_duplicado)


    return resultados


# Executando a função e exibindo os resultados
resultados = funcao_encontra_primeiro_duplicado(lista_de_listas_de_inteiros)
print(resultados)
        

    


           
