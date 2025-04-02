"""
### **Exercício: Gerenciador de Pontuação** 🎮  
"""

print("\033[38;5;136m------- Gerenciador de Pontuação -------\033[m")

initial_score = input("Informe a Pontuação inicial do Jogador(a): ")
win = input("Quantos pontos você ganhou? ")
lose = input("Quantos pontos você perdeu? ")

if initial_score.isdigit() and win.isdigit() and lose.isdigit():  
    initial_score = int(initial_score)
    win = int(win)
    lose = int(lose)
    initial_score += win
    initial_score -= lose
    print("Bônus aplicado!")
    initial_score *= 2

    if lose > 30:
        initial_score /= 2
    
    print(f"Pontuação Final do Jogador: {initial_score:.0f}")
    
   
else:
    print("\033[91mErro: Digite apenas números inteiros.\033[m")



