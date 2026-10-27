# TODO: parte 02/ atividade 01

# bibliotecas 
import os
import json
# lista
"""
Cria um programa que faça as seguintes operações:
- Cadastra novo usuário
- Lista todos os usuários cadastrados
- Altera os dados de um usuário
- Exclui um usuário
- Grava os dados em um arquivo JSON
- Abre um arquivo JSON e lista os usuários
"""
# lista
usuarios = []
# limpa terminal
os.system("cls" if os.name == "nt" else "clear")
# loop
while True: # todo programa que termina com 2 pontos e inicio de forma
    # menu
    print("1 - Cadastrar novo usuário")
    print("2 - Listar usuarios cadastrados")
    print("3 -Alterar dados do usuário")
    print("4 - Excluir um usuário")
    print("5 - Gravar todos os usuarios em .json")
    print("6 - Abrir arquivo.json")
    print("7 - Sair do programa")
    opcao = input("Opção desejada: ").strip()
    os.system("cls" if os.name == "nt" else "clear")
    match opcao:
        case "1":
             # inicializar um novo dicionario
                usuario = {}

            # informa os dados
                usuario['nome'] = input("Infomre o nome: ").strip().title()
                usuario['email'] = input("Infomre o e-mail: ").strip().lower()
                usuario['telefone'] = input("Infomre o telefone: ").strip()
                usuario['cpf'] = input("Infomre o CPF: ").strip()

             # adiciona novo usuario na lista
                usuarios.append(usuario)
                os.system("cls" if os.name == "nt" else "clear")
                print(f"Dados de {usuario.get('nome')} cadastrado com sucesso.")

                continue
        case "2":
            if usuarios:
                for i, usuario in enumerate(usuarios): # em cada intem da minha lista vou executar um print esse codigo fala
                    print(f"ID: {i}") # é o indice
                    for chave, valor in usuario.items():
                        print(f"{chave.capitalize()}: {valor}.")
                    print(f"{'-'*40}")
            else:
                print("Não foram encontrados usuários cadastrados.")        
            continue
        case "3":
            try:
                indice = int(input("Informe o ID do usuário a ser alterado: "))
                for chave, valor in usuarios[indice].items():
                    print(f"{chave.capitalize()}: {valor}.")
                chave = input("Qual chave deseja alterar o valor? ").strip().lower()
                usuarios[indice][chave] = input("Infomre o novo valor: ").strip()
                os.system("cls" if os.name == "nt" else "clear")
                print(f"{usuario[indice][chave]} de {usuarios[indice].get('nome')} alterado com sucesso!")
                continue
            except Exception as e: #exeto e mostra uma mensagem de exeção
                print(f"Não foi possivel atualizar os dados. {e}.")
        case "4":
            try:
                indice = int(input("Infomre o ID a ser excluido: "))
                del usuarios[indice]
                os.system("cls" if os.name == "nt" else "clear")
                print("Usuario excluido com sucesso!")
                continue
            except Exception as e:
                print(f"Não foi possível excluir. {e}")
        case "5":
                arquivos = input("Informe o nome do arquivo: ").strip()
                with open(f"{arquivos}.json","w",encoding="utf-8") as f:
                    json.dump(usuarios, f) #dump é o comando de gravar
                    os.system("cls" if os.name == "nt" else "clear")
                    print("Dados gravados com sucesso!")
                continue
        case "6":
            try:
                 arquivo = input("Informe o arquivo que deseja abrir: ").strip()
                 with open(f"{arquivo}.json","r",encoding="utf-8") as f:
                    usuarios = json.load(f) # é ultilizado para quando o sistema abrir, abrir com os dados dos usuarios da lista ja preenchida
                    os.system("cls" if os.name == "nt" else "clear")
            except Exception as e:
                 print(f"Não foi possível abrir o arquivo. {e}.")
        case "7":
            break
        case _:
            print("Opção invalida.")
            continue

