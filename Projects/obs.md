## IMPLEMENTAT: Impressão do saldo com o limite.
## inativar conta
```
    print("\n--- Digite seu endereço ---")
    logradouro = input("Logradouro (Ex: Rua das Flores): ").title()
    numero = input("Número: ")
    bairro = input("Bairro: ").title()
    cidade = input("Cidade: ").title()
    estado = input("Sigla do Estado (Ex: SP): ").upper()
    address = f"{logradouro}, {numero} - {bairro} - {cidade}/{estado}"
```
## Variavel extrato? s/n?
``` py
def menu():
    print("-"*42)
    print("\033[38;5;136m===== Welcome to FinTechOne Bank! =====\033[38;5;136m")
    print("\033[38;5;136m===== Menu Options =====\033[38;5;136m")
    print("\033[38;5;21m[1] - Register.\033[m")
    print("\033[38;5;21m[2] - View data registers.\033[m")
    print("\033[38;5;21m[3] - List clients.\033[m")

    print("\033[38;5;21m[4] - Check data Account and statement.\033[m") 
    print("\033[38;5;21m[5] - Withdraw.\033[m")
    print("\033[38;5;21m[6] - Deposit.\033[m")
    print("\033[38;5;21m[7] - Exit banking system.\033[m")
    print("-"*42)
```
## CamelCase
<!-- 

    def validate_float(self, variable) -> float | None:
        """Validate a general float"""
        try:
            return float(variable)
        except ValueError:
            error_message("Please enter a valid number (float).")
            return None -->