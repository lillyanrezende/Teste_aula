from datetime import date

def calcular_idade(ano_nascimento: int)-> int:
    ano_atual = date.today().year
    return ano_atual - ano_nascimento

print("Olá turma do Python!")
print("Tudo joia!")
nome: str = input("Qual é o seu nome? ")
print(f"Olá, {nome}!")
print("Vamos começar!")
animal: str = input("Qual seu animal favorito? ")
print(f"Eu tambem adoro {animal}!")


while True:
    try:
        ano_nascimento = int(input("Em que ano você nasceu? "))

        idade = calcular_idade(ano_nascimento)

        print(f"Você tem {idade} anos de idade!")

        if idade <= 10:
            print("És uma Criança")

        elif 11 <= idade <= 18:
            print("Já és um adolescente")

        elif 19 <= idade <= 64:
            print("És um Adulto")

        elif idade >= 65:
            print("És um idoso")

        repetir = input("\nDeseja introduzir outro ano de nascimento? (s/n): ").strip().lower()
        if repetir != "s":
            print("\nFoi bom falar com você! Até breve!")
            break
    except ValueError:
        print("Por favor, insira um ano de nascimento válido!")
