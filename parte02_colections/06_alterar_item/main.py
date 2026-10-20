# bibliotecas
import os
# exibe a lista original

os.system("cls" if os.name == "nt" else "clear" )

# lista 
nomes = ["Naruto", "Hinata", "Sakura", "Shikamaru" "Sasuke", "Madara", "Obito",]



# loop 
while True:

# exibe a forma indice a ser alterada

    for n, nome in enumerate (nomes):
        print(f"(Indice {n}: {nome}")

    # menu
    print("1 - Alterar item da lista")
    print("2 - Finaliar")
    opcao = input("Opção desejada:  ").strip() # informa opção desejada

    # verifica a opção escohlida
    match opcao:
        case "1":
            # inofrma indice a ser alterado
            indice = int(input("Informe o indicce a ser açterado: "))
            # informa novo valor
            nomesindice = input ("Informe novo nome:  ").strip().title()
            os.sytem("cls" if os.name == "nt" else "Clear")
            print("Item da lista alerado com sucesso!")
            continue    

        case "2":
            os.sytstem("cls" if os.name == "nt" else "clear")

                # exibe a nova lista

            for n. nome in enumerate(nomes):
                    print(f"indicae {n: {nome}}")
                    break
            
        case "_":
            print("Opção invalida")
            continue
        
