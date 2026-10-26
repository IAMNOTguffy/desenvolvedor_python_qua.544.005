# Lista
frutas = [
    "Maça",
    "Pera",
    "Maracuja",
    "Morango",
    "Manga",
    "Melancia",
    "Goiaba"
]

while True:
    for n, fruta in enumerate(frutas):
        print(f"Índice {n}: {fruta}")

    # Menu
    print("1 - Excluir Fruta")
    print("2 - Encerrar Programa")
    opcao = input("Opção desejada: ").strip()

    # Verifica opção
    match opcao:
        case "1":
            indice = int(input("Informe o índice a ser excluído: "))
            del(frutas[indice]) # exclui indice selecionado
            print("Fruta excluída com sucesso!")
            continue
        case "2":
            break
        case _:
            print("Opção inválida.")
            continue

