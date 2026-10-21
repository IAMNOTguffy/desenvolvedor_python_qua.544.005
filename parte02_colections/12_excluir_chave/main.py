# dicionario
usuario = {
    'nome': "Joao Melo",
    'idade': 16,
    'email': "Joao@gmail.com",
    'telefone': "(61) 9875234-4132",
    'endereço': "Curral"
}

# exibe a lista original
for chave, valor in usuario.items():
    print(f"{chave}: {valor}")

# informa a chave a ser deletada
chave_escolhida = input("Informe a chave a exluir: ").strip().lower()

# deleta a chave
del usuario[chave_escolhida]

# re-exibe o novo dicionario 
for chave, valor in usuario.items():
    print(f"{chave}: {valor}")