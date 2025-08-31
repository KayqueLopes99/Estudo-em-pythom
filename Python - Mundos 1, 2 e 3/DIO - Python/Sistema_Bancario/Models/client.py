from datetime import date
import Utils.tratatives as tratative
import re

def registerDateOfBirth() -> str:
    fmt: str = "%d/%m/%Y"
    
    while True:
        print("Enter your date of birth (dd/mm/yyyy):")
        day: int  | None  = tratative.validateInteger(input("Enter the day: "))
        
        if day is None:
            print("\033[91mInvalid day. Try again.\033[m")
            continue
        
        month: int | None = tratative.validateInteger(input("Enter the month: "))
        
        if month is None:
            print("\033[91mInvalid month. Try again.\033[m")
            continue
            
            
        year: int  | None = tratative.validateInteger(input("Enter the year: "))

        if year is None:
            print("\033[91mInvalid year. Try again.\033[m")
            continue
        
        if not tratative.validateDateOfBirth(day, month, year):
                print("\033[91mInvalid date. Try again.\033[m")
                continue
        
        
        try:
            dateNormal = date(year, month, day)
            formatted_date = dateNormal.strftime(fmt)
            print("\033[92mDate successfully registered!\033[m")
            return formatted_date
        except ValueError:
            print("\033[91mInvalid date. Try again.\033[m")


def registerClient(usersList) -> dict[str]  | None:
    print("=" * 30)
    print("\033[38;5;21m--- = = = > Register < = = = ---\033[m")
    print("=" * 30)
    
    while True:
        nameInput: str = input("Enter your full name: ")
        name: str | None = tratative.validateString(nameInput, "Invalid name! Please enter letters only.")
        if name:
            break

    while True:
        cpfInput: str = input("Enter your CPF (numbers only): ")
        cpf: str = tratative.validateCpf(cpfInput)
        cpfCleaned: str = re.sub(r'\D', '', cpfInput) if cpf else ""
        if cpfCleaned:
            cpfExists: bool = False
            for user in usersList:
                if user['cpf'] == cpfCleaned:
                    cpfExists = True
                    break            
            if cpfExists:
                return None
            break

    
 
    cpfClean = cpf.replace('.', '').replace('-', '')
    dateOfBirth: str = registerDateOfBirth()

    while True:
        emailInput: str = input("Enter your email: ")
        email: str = tratative.validateEmail(emailInput)
        if email:
            break
        
    
    
    while True:
        print("\033[38;5;21m--- Enter your address ---\033[m")
        streetInput: str = input("Street (e.g., Flower Street): ")
        street: str | None = tratative.validateString(streetInput, "Invalid street name! Please enter letters only.")
    
        numberInput: int = input("Number: ")
        number: int = tratative.validateInteger(numberInput)
        str(number)
        
        neighborhoodInput: str = input("Neighborhood: ")
        
        neighborhood: str | None = tratative.validateString(neighborhoodInput, "Invalid neighborhood! Please enter letters only.")
        
        
        
        cityInput: str = input("City: ")
        city: str | None = tratative.validateString(cityInput, "Invalid city name! Please enter letters only.")
        stateInput: str = input("State abbreviation (e.g., NY): ")
        state: str | None = tratative.validateString(stateInput, "Invalid state! Please enter letters only.")
        address: str = f"{street}, {number} - {neighborhood} - {city}/{state}"

        if street and number and neighborhood and city and state:
            break
        else:
            print("\033[91mInvalid address. Please fill in all fields.\033[m")
    
    newUser = {
        "name": name,
        "dateOfBirth": dateOfBirth,
        "cpf": cpfClean,
        "email": email,
        "address": address,
    }
    
    tratative.successMessage("User successfully registered!")
    return newUser


def listClients(usersList) -> None:
    print("=" * 35)
    print("\033[38;5;21m--- = = = > Client List < = = = ---\033[m")
    print("=" * 35)
    if not usersList:
        print("\033[93mNo clients registered.\033[m")
        return
    
    for i, user in enumerate(usersList, 1):
        print(f"{i}: \033[1;38;5;46mName: {user['name']}\033[m | \033[1;38;5;46mCPF: {user['cpf']}\033[m | \033[1;38;5;46mEmail: {user['email']}\033[m")


def listDataClient(cpf: str, usersList) -> None:
    userFound = False
    for user in usersList:
        if user['cpf'] == cpf:
            print("\n" + "=" * 40)
            print("\033[38;5;136m======= Client Data =======\033[m")
            print(f"\033[1;38;5;46mName: {user['name']}\033[m")
            print(f"\033[1;38;5;46mDate of Birth: {user['dateOfBirth']}\033[m")
            print(f"\033[1;38;5;46mCPF: {user['cpf']}\033[m")
            print(f"\033[1;38;5;46mEmail: {user['email']}\033[m")
            print(f"\033[1;38;5;46mAddress: {user['address']}\033[m")
            print("=" * 40 + "\n")
            userFound = True
            break
    if not userFound:
        print("\033[91mError: Client not found.\033[m")