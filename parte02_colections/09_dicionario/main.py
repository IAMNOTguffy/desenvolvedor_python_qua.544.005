
# Dicionário
usuario = {
    'nome': "Ekure",
    'idade': 23,
    'altura': 1.80,
    'email': "ekure@gmail.com",
    'cpf': "123.456.789.10",
    'telefone': "(61) 940028922"
}

# Exibir um valor específico
print(f"Nome: {usuario['nome']}")
print(f"E-mail: {usuario.get('email')}")

# Com laço de repetição
for chave, valor in usuario.items():
    print(f"{chave.capitalize()}: {valor}.")