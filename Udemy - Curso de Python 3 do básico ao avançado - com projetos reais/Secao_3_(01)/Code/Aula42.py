# Qual letra apareceu mais vezes na frase? (Iterando strings com while)
frase = 'O python é uma linguagem de programação multiparadigma. Python foi criado por Guido van Rossum.'
# 'O' != 'o'. 

indice = 0  
maior_quantidade = 0 
letra_mais_frequente = '' 

while indice < len(frase):
    caractere_atual = frase[indice]  
    quantidade_atual = frase.count(caractere_atual)  

    # Se encontrar um espaço, pule e continue.
    if caractere_atual == ' ':
        indice += 1
        continue

    # Atualiza a letra mais frequente e sua quantidade caso encontre um valor maior.
    # Se tiver duas letras com a mesma qtd a primeira é considera
    if quantidade_atual > maior_quantidade:
        maior_quantidade = quantidade_atual
        letra_mais_frequente = caractere_atual

    indice += 1 

print(f"O caractere '{letra_mais_frequente}' apareceu {maior_quantidade} vezes na frase.")

