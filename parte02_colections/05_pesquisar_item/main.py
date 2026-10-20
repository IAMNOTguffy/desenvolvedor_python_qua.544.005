# LISTA

cidades = [

    "Taguatinga",
    "Plano Piloto",
    "Gama",
    "Samabia",
    "Santa Maria",
    "Taguatinga",
    "Planaltina",
    "Plano Piloto",
    "Brazlandia",
    "Plano Piloto",

]


# usuario informa o item a ser pesquisado

item = input("Informe a cidade a ser pesquisada:  ").strip().title()

# verifica quantas vezes o termo foi encontrado

print(f"{item} foi encontrado {cidades.count(item)} vezes na lista.")

                                                           