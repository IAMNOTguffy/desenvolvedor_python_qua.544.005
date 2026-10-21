# informa o nome de nova chave
# dicionario
import os
# limpa terminal

os.system("cls" if os.name == "nt" else "clear")

usuario = {
    'nome': "FULANO",
    'idade': 18,
    'email': "fulano@gmail.com",
    'telefone': "61-9991348",
}

# exibe o dicionario
for chave, valor in usuario.items():
    print(f"{chave.capitalize()}: {valor}.")

# limpa terminal


# informa o nome de nova chave

chave_escolhida = input("Informe o nome da chave que deseja alterar ou Enter para encerrar: ").strip().lower()
# verifica se a chave é valida
if chave_escolhida in chave: usuario[chave_escolhida]
input("Informe o novo valor: ").strip()

for chave, valor in usuario.items():
    print(f"{chave}: {valor}")







