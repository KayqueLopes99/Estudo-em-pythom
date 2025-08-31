import re
from datetime import date

def errorMessage(text: str) -> None:
    print(f"\033[91m{text}\033[m")

def successMessage(text: str) -> None:
    print(f"\033[92m{text}\033[m")

def validaCpf(cpf: str) -> str | bool:
    cpf = cpf.replace(".", "").replace("-", "").replace(" ", "")
    
    if not cpf.isdigit() or len(cpf) != 11:
        print("\033[91mO CPF deve ter exatamente 11 dígitos e conter apenas números.\033[m")
        return False
    
    if cpf == (cpf[0] * 11):
        print("\033[91mFormato inválido! CPF não pode ter todos os números iguais.\033[m")
        return False

    listaCom9DigitosCpf: list[int] = []
    contadorRegressivo1: int = 10
    for digito in cpf[:9]:
        listaCom9DigitosCpf.append(int(digito) * contadorRegressivo1)
        contadorRegressivo1 -= 1
    
    somaValores1: int = sum(listaCom9DigitosCpf)
    resultadoPrimeiroDigito: int = (somaValores1 * 10) % 11
    resultadoPrimeiroDigito = resultadoPrimeiroDigito if resultadoPrimeiroDigito <= 9 else 0

    listaCom10DigitosCpf: list[int] = []
    contadorRegressivo2: int = 11
    for digito in cpf[:10]:  
        listaCom10DigitosCpf.append(int(digito) * contadorRegressivo2)
        contadorRegressivo2 -= 1
    
    somaValores2: int = sum(listaCom10DigitosCpf)
    resultadoSegundoDigito: int = (somaValores2 * 10) % 11
    resultadoSegundoDigito = resultadoSegundoDigito if resultadoSegundoDigito <= 9 else 0

    if resultadoPrimeiroDigito == int(cpf[9]) and resultadoSegundoDigito == int(cpf[10]):
        cpfPadronizado: str = f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:11]}"
        print(f"\033[92mSucesso! CPF: {cpfPadronizado} é válido.\033[m")
        return cpfPadronizado
    else:
        print("\033[91mErro! CPF inválido.\033[m")
        return False


def validateString(name: str, text: str) -> str | None:
    if not name.replace(" ", "").isalpha():
        errorMessage(text)
        return None
    return name.title()


def validateDateOfBirth(day: int, month: int, year: int) -> bool:
    try:
        birthDate: date = date(year, month, day)
        if not (1900 <= year <= 2025):
            errorMessage("Invalid year!")
            return False
        return True
    except ValueError:
        errorMessage("Invalid date! Check day or month.")
        return False

def validateEmail(email: str) -> str | None:
    emailPattern: str = r'^[a-zA-Z0-9_.+-]+@(gmail\.com|hotmail\.com|outlook\.com|yahoo\.com)$'
    if re.match(emailPattern, email):
        successMessage("Email is valid!")
        return email
    else:
        errorMessage("Email is not valid.")
        return None

def validateCpf(cpf: str) -> bool | str:
    return validaCpf(cpf) 

def validateIntegerOption(variable) -> int | None:
    if isinstance(variable, int) or (isinstance(variable, str) and variable.isdigit()):
        varInt: int = int(variable)
        if 1 <= varInt <= 7:
            return varInt
        else:
            errorMessage("Selected option is not in the range [1-7].")
    else:
        errorMessage("The selected option must be an integer.")
    return None

def validateInteger(variable) -> int | None:
    if isinstance(variable, int):
        return variable
    elif isinstance(variable, str) and variable.isdigit():
        return int(variable)
    else:
        errorMessage("Please enter a valid integer number.")
        return None


def validateFloat(variable) -> float | None:
    try:
        return float(variable)
    except ValueError:
        errorMessage("Please enter a valid number (float).")
        return None