"""
**Exercício: Verificação de Elementos em uma Lista** 📝
"""

food_list = ["maçã", "banana", "laranja", "abacaxi", "uva", "pera", "cenoura", "tomate"]

food = input("Informe o nome do item para verificar: ")

if food in food_list:
    print(f"\033[92mA comida {(food)} está na Lista!\033[m")
else:
    print(f"\033[91mA comida {(food)} não está na Lista!\033[m")
