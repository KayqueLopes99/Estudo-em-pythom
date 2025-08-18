"""
### **Exercício: Sistema de Acesso 🔐**  

"""

print("\033[38;5;136m------- Sistema de Acesso -------\033[m")

name = input("Usuário: ")
key = input("Senha: ")

if name == "admin" and key == "1234":
    print("\033[92mAcesso permitido!\033[m")
elif name == "sair" or key == "sair":
    print("Encerrando o sistema...")
else:
    print("\033[91mAcesso Negado: Nome de usuário ou senha incorretos..!\033[m")
print("\n")
print("\033[38;5;136m------- Teste de Saldo -------\033[m")
saldo = 1000
saque = 250
limite = 200
conta_especial = True


if (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque):
    print("\033[92mSaque permitido!\033[m")

