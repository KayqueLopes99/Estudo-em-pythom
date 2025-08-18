print("\033[38;5;136m------- Sistema de Formatação str -------\033[m")

string = input("Informe uma palavra: ")
print(string.upper())
print(string.lower())
print(string.title())

print(string.strip())
print(string.lstrip())
print(string.rstrip())
print(string.center(len(string) * 2, "="))
print("-".join(string))