# biblioteca

import os



# lista de usuarios vazia

usuarios = []


# limpa terminal 

os.system("cls" if os.name == "nt" else "clear")

# loop
while True:
    # menu
    print("1 - Cadastrar Usuario")
    print("2 - Exibir a lista de usuarios")
    print("3 - Sair do programa")
    opcao = input("Opção desejada> ").strip()
    # verifica opção escolhida
    match opcao: 
        case "1":
            # cria novo dicionario
            usuario = {}

            # inserir os dados do usaurio
            usuario['nome'] = input("Informe o nome: ").strip().title()
            usuario['idade'] = int(input("Informe a idade: "))
            usuario['email'] = input("Informe o seu email: ").strip().lower()
            usuario['cpf'] = input("Informe o CPF: ").strip()

            # adiciona o usuario na lista
            usuario.append(usuario)

            # usuario cadastrado com sucesso!!
            print(f"{usuario.get('nome')} cadastrado com sucesso!!")
            continue
        
        case "2":
            for usuario in usuarios:
                for chave, valor in usuario.items():
                    print(f"{chave.capitalize()}: {valor}")
                    print(f"{'-'*40}")
                    continue
        case "3":
            break
        case _:
           pass