# biblioteca
import os


# limpa terminal
os.system("cls" if os.name == "nt" else "clear")


# loop 
while True:
    #MENU
    print("1 - Gravar nobo arquivo")
    print("2 - Abrir e ler arquivo")
    print("3 - Sair do programa")
    opcao =input("Opção desejada: ")
    os.system("cls" if os.name == "nt" else "clear")

    # verifica a opção 
    match opcao:
        case "1":
            # infomra o texto a ser gravado
            novo_texto = input("Digite aqui o seu texto:  ")
            # informa o nome do arquivo
            novo_arquivo = input("Digite aqui o nome do arquivo:  ").strip()

            # grava o novo arquivo
            with open(f"15_gravando_arquivos/{novo_arquivo}.txt","w", encoding="utf-8") as f: # WITH OPEN inicia o bloco a ser gravado!!! # "w" significa gravar!!!  #ENCODING = tira as caracterias, 
                f.write(novo_texto)
                continue
        case "2":
            abrir_arquivo = input("Infomre o nome do .txt que deseja abrir:").strip()
            with open(f"15_gravando_arquivos/{abrir_arquivo}.txt","r", encoding="utf-8") as f: # R = significa "reading" abrir que o sistema indetifica como ler o programa
             texto = f.read()
                # exibe o arquivo na tela
            print(texto)

            
        case "3":
            print("Programa finalizado com sucesso!")
            
            break
            
        case _:
            print("Opção invalida")
            continue