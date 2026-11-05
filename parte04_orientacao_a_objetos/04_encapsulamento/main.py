# IMPORTAÇÃO: Busca o arquivo 'model.py' que contém a classe básica 'Pessoa' para usá-la aqui
from model import Pessoa


def main():
    """
    Função principal que serve como o roteiro de execução do programa.
    """
    # 1. INSTANCIAÇÃO: Cria o objeto chamado 'usuario' usando o molde da classe 'Pessoa'.
    # Passamos strings vazias "" e o número 0 para abrir espaço na memória (criar as caixinhas limpas).
    usuario = Pessoa(nome="",idade=0,cpf="",telefone="",email="")

    # 2. ENTRADA E TRATAMENTO DE DADOS:
    # O input captura o texto digitado pelo usuário. 
    # O operador '=' joga esse valor direto para dentro do atributo correspondente do objeto 'usuario'.
    
    # .strip() remove espaços extras nas pontas e .title() deixa as primeiras letras em maiúsculo.
    usuario.nome = input("Informe o nome: ").strip().title()
    
    # int() é obrigatório para converter o texto do input em um número inteiro real na memória.
    usuario.idade = int(input("Informe a idade: "))
    
    # .strip() limpa espaços indesejados que o usuário possa digitar no CPF ou Telefone.
    usuario.cpf = input("Informe o CPF: ").strip()
    usuario.telefone = input("Informe o telefone: ").strip()
    
    # .lower() garante que todo o e-mail fique salvo em letras minúsculas.
    usuario.email = input("Informe o e-mail: ").strip().lower()

    # 3. EXIBIÇÃO DIRETAMENTE NO MAIN:
    # Diferente dos outros códigos onde a classe tinha uma função pronta para se exibir,
    # aqui você está acessando as caixinhas de dados do 'usuario' uma por uma e usando o print comum.
    print(f"Nome: {usuario.nome}")
    print(f"Idade: {usuario.idade} anos")
    print(f"CPF: {usuario.cpf}")
    print(f"Telefone: {usuario.telefone}")
    print(f"E-mail: {usuario.email}")


# REGRA DE INICIALIZAÇÃO: O Python só executa a função main() se este arquivo for o que recebeu o 'Play' direto no terminal.
if __name__ == "__main__":
    main()