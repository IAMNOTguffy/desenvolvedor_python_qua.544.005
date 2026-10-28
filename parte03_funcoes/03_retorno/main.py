# bilbioteca
import os


# funções 
def limpar():
    os.system("cls" if os.name == "nt" else "clear")

def boas_vindas(nome):
    return f"{nome}, seja bem vindo!"

# algoritmo principal
limpar()
nome = input("Digite o seu nome: ").strip().title()
print(boas_vindas(nome))

