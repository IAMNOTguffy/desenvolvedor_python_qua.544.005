# biblioteca
import os

# dicionario
usuario = {
    'nome': "Fulano de Tal",
    'idade': 18,
    'email': "fulano@gmail.com"
}

# usuario informa o nome da nova chave
nova_chave = input("Informe o nome da nova chave:  ").strip().lower()
# usuario informa o valor da nova chave
usuario[nova_chave] = input("Informe o valor da nova chave:  ").strip()

# exibe o dicionario
for chave, valor in usuario.items():
    print(f"{chave.capitalize()}: {valor}.")


# limpa terminal
os.system("cls" if os.name == "nt" else "clear")

# loop
for chave, valor in usuario.items():
        print(f"{chave}: {valor}")
      