# TODO: atividade 02 
# crie um programa em que o usuário informe uma única vez o nome e a idade e em seguida, o programa exibe uma lista de filmes do cinema e suas respectivas salas e classificações indicativas. O usuário deve escolher a sala do filme desejado. Se tiver a idade mínima o programa imprime o ingresso e encerra. Senão o programa impede a entrada do usuário e retorna a lista para que o mesmo posssa escolher outro flme.

#import a biblioteca
import os

# limpa terminal
os.system("cls" if os.name == "nt" else "clear")

#Dado do Usuario
nome=input("Digite seu mome: ").strip().title()
idade=float(input("Digite sua idade: "))

# loop para exibir a lista de filmes

while True :

    # menu de filmes 
    print(f"{'-'*20} CINECLUBE {'-'*20}")
    print("Lista de filmes disponíveis: ")
    print("1. Deadpool e Wolverine - Sala 1 - 18 anos")
    print("2. Chainsawman - Sala 2 - 16 anos")
    print("3. Harry Potter - Sala 3 - 14 anos")
    print("4. Homem-Aranha - Sala 4 - 12 anos")
    print("5. Moana - Sala 5 - Livre")

    operador = input("Digite a opção desejada").strip()

    match operador:
        case "1":
            if idade >= 18:
                 print(f"{nome} você pode entrar na sala é assistir Wolverine")
                 break
            else:
                print(f"Desculpe, {nome} você nao tem a idade necessaria, Porfavor Escolha outro Filme")
            
        case "2":
            if idade >= 16:
                print(f"{nome} Continue para Sala 2, para Assistir Chainsawman")
                break
            else:
                print(f"{nome} desculpa voce tem a idade necessaria, Porfavor Escolha outro Filme")
              
        case "3":
            if idade >= 14:
                print(f"{nome} Continue para a Sala 3, para assistir Harry Potter")
                break
            else:
                print(f"Desculpe {nome} você não tem a idade necessaria, Porfavor Escolha outro Filme")
              
        case "4":
            if idade >= 12:
                print(f"{nome} Continue para a Sala 4, para assistir Homem-Aranha")
                break
            else: 
                print(f"Desculpe {nome} voce nao tem a idade necessaria, Porfavor Escolha outro Filme")
               
        case "5":
            print("Continue Para a Sala 5, para assistir Moana")
            break
        case _: 
            print("Digite um Filme Valido")
            continue

      



        