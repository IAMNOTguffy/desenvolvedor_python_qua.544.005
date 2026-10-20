# lista

frutas = [
    "Maça",
    "Pera",
    "Maracujaa",
    "Morango",
    "Manga",
    "Melancia",
    "Goiaba"
]

    





while True:

    for n, fruta in enumerate(frutas):
        print(f"Indice {n} {frutas}")

        # menu
        print("1 - Excluir item")
        print("2 - Encerrar programa")
        opcao = input("Opção desejada:  ").strip()

        # verifica opção
        
        match opcao:
            case "1":
                Indice = float(input("O indice a ser excluido:  "))
                del(fruta[Indice])
                print("Frutas excluidas com sucesso!")
                continue
            case "2":
                break
            case _:
                print("Opção inválida")
                continue

                


