"""
Cria um programa que faça as seguintes operações:
- Cadastra novo usuário
- Lista todos os usuários cadastrados
- Altera os dados de um usuário
- Exclui um usuário
- Grava os dados em um arquivo JSON
- Abre um arquivo JSON e lista os usuários
"""

import json
import os


def limpar_terminal():
    os.system("cls" if os.name == "nt" else "clear")


usuarios = []

while True:
    print("\n1 - Cadastrar novo usuário")
    print("2 - Listar todos os usuários")
    print("3 - Alterar dados de um usuário")
    print("4 - Excluir um usuário")
    print("5 - Gravar dados em JSON")
    print("6 - Abrir arquivo JSON")
    print("7 - Sair do programa")

    opcao = input("Digite a opção desejada: ").strip()

    match opcao:

        case "1":
            limpar_terminal()

            nome = input("Informe o nome: ").strip().title()

            try:
                idade = int(input("Informe a idade: "))
            except ValueError:
                print("Idade inválida!")
                continue

            email = input("Informe o e-mail: ").strip().lower()
            cpf = input("Informe o CPF: ").strip()
            telefone = input("Informe o telefone: ").strip()

            usuario = {
                "nome": nome,
                "idade": idade,
                "email": email,
                "cpf": cpf,
                "telefone": telefone
            }

            usuarios.append(usuario)

            print("Usuário cadastrado com sucesso!")
            input("Pressione ENTER para continuar...")
            limpar_terminal()

        case "2":
            limpar_terminal()

            if not usuarios:
                print("Nenhum usuário cadastrado!")
            else:
                for usuario in usuarios:
                    print("-" * 25)

                    for chave, valor in usuario.items():
                        print(f"{chave.capitalize()}: {valor}")

                print("-" * 25)

            input("Pressione ENTER para voltar ao menu...")
            limpar_terminal()

        case "3":
            limpar_terminal()

            if not usuarios:
                print("Nenhum usuário cadastrado!")
                continue

            # Lista os usuários
            for usuario in usuarios:
                print("-" * 25)
                print(f"Nome: {usuario['nome']}")
                print(f"CPF: {usuario['cpf']}")

            # Busca pelo CPF
            cpfbuscar = input("Digite o CPF do usuário que deseja alterar: ").strip()

            for usuario in usuarios:
                if usuario["cpf"] == cpfbuscar:

                    print("\nDados do usuário:")
                    for chave, valor in usuario.items():
                        print(f"{chave.capitalize()}: {valor}")

                    chave_escolhida = input("\nQual dado deseja alterar? ""(nome, idade, email, cpf, telefone): ").strip().lower()

                    if chave_escolhida in usuario:
                        novo_valor = input("Informe o novo valor: ").strip()

                        if chave_escolhida == "idade":
                            try:
                                novo_valor = int(novo_valor)
                            except ValueError:
                                print("A idade deve ser um número!")
                                break

                        elif chave_escolhida == "nome":
                            novo_valor = novo_valor.title()

                        elif chave_escolhida == "email":
                            novo_valor = novo_valor.lower()

                        usuario[chave_escolhida] = novo_valor

                        print("Dado alterado com sucesso!")

                    else:
                        print("Chave inválida!")

                    break

            else:
                print("Usuário não encontrado!")

            input("Pressione ENTER para continuar...")
            limpar_terminal()

        case "4":
            limpar_terminal()

            if not usuarios:
                print("Nenhum usuário cadastrado!")
                continue

            # Lista os usuários
            for usuario in usuarios:
                print("-" * 25)
                print(f"Nome: {usuario['nome']}")
                print(f"CPF: {usuario['cpf']}")

            # Busca o CPF
            buscar = input(
                "\nDigite o CPF do usuário que deseja excluir: ").strip()

            for usuario in usuarios:
                if usuario["cpf"] == buscar:
                    usuarios.remove(usuario)
                    print("Usuário excluído com sucesso!")
                    break
            else:
                print("Usuário não encontrado!")

            input("Pressione ENTER para continuar...")
            limpar_terminal()

        case "5":
            limpar_terminal()

            try:
                with open("usuarios.json", "w", encoding="utf-8") as arquivo:
                    json.dump(usuarios,arquivo,ensure_ascii=False,indent=4)

                print("Dados gravados com sucesso!")

            except OSError:
                print("Erro ao gravar o arquivo!")

            input("Pressione ENTER para continuar...")
            limpar_terminal()

        case "6":
            limpar_terminal()

            try:
                with open("usuarios.json", "r", encoding="utf-8") as arquivo:
                    usuarios = json.load(arquivo)

                print("Dados carregados com sucesso!")

                if not usuarios:
                    print("O arquivo não possui usuários.")
                else:
                    for usuario in usuarios:
                        print("-" * 25)

                        for chave, valor in usuario.items():
                            print(f"{chave.capitalize()}: {valor}")

                    print("-" * 25)

            except FileNotFoundError:
                print("O arquivo usuarios.json ainda não existe!")

            except json.JSONDecodeError:
                print("O arquivo JSON está vazio ou contém dados inválidos!")

            input("Pressione ENTER para continuar...")
            limpar_terminal()

        case "7":
            print("Encerrando o programa...")
            break

        case _:
            print("Opção inválida!")
            input("Pressione ENTER para continuar...")
            limpar_terminal()