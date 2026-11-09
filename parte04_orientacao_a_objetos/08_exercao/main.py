
import os

from model import Pessoa, Endereco


def limpar():
    os.system("cls" if os.name == "nt" else "clear")

# TODO PEGAR DO REPOSITORIO DO PROFESSOR 09/11/2026
def main():

    limpar()

    # Criando objeto Endereco
    endereco = Endereco(
        cep="",
        uf="",
        cidade="",
        bairro="",
        logradouro="",
        complemento="",
        numero=""
    )

    # Criando objeto Pessoa
    usuario = Pessoa(
        nome="",
        cpf="",
        email="",
        telefone="",
        endereco=endereco
    )

    # Entrada de dados da pessoa
    print("========== CADASTRO DE PESSOA ==========")

    usuario.nome = input("Informe o nome: ").strip().title()
    usuario.cpf = input("Informe o CPF: ").strip()
    usuario.email = input("Informe o email: ").strip().lower()
    usuario.telefone = input("Informe o telefone: ").strip()

    # Entrada de dados do endereço
    print("\n========== CADASTRO DE ENDEREÇO ==========")

    endereco.cep = input("Informe o CEP: ").strip()
    endereco.uf = input("Informe a UF: ").strip().upper()
    endereco.cidade = input("Informe a cidade: ").strip().title()
    endereco.bairro = input("Informe o bairro: ").strip().title()
    endereco.logradouro = input("Informe o logradouro: ").strip().title()
    endereco.complemento = input("Informe o complemento: ").strip()
    endereco.numero = input("Informe o número: ").strip()

    # Saída de dados
    limpar()
    usuario.exibir_dados()


if __name__ == "__main__":
    main()
