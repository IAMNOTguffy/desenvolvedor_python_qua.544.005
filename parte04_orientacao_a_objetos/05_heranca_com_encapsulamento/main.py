# Importa o módulo 'os' para podermos usar o comando de limpar o terminal
import os

# IMPORTAÇÃO: Traz as classes filhas 'PessoaFisica' e 'PessoaJuridica' do arquivo 'modulo.py'
from modulo import PessoaFisica,PessoaJuridica

def limpar():
    """
    Função simples para limpar a tela do terminal.
    Se for Windows usa 'cls', se for Mac/Linux usa 'clear'.
    """
    os.system("cls" if os.name == "nt" else "clear")

def main():
    # 1. INSTANCIAÇÃO: Cria os objetos 'usuario' e 'empresa' com as caixinhas limpas ("").
    usuario = PessoaFisica(nome="",cpf="",email="",telefone="")
    empresa = PessoaJuridica(razao_social="",nome_fantasia="",cnpj="",email="", telefone="",)

    limpar()

    # 2. CAPTURA DOS DADOS DO USUÁRIO (Pessoa Física)
    print(f"{'-'*20} Informe os dados do usuário {'-'*20}")
    
    # O input lê o teclado e o '=' tenta acionar o @setter da classe para guardar o dado.
    # 🚨 NOTA: Como no 'modulo.py' as propriedades de PessoaFisica ficaram desalinhadas (dentro do __init__),
    # o Python pode reclamar que '.nome' e '.cpf' não possuem um Setter válido aqui.
    usuario.nome = input("Informe o nome: ").strip().title()
    usuario.cpf = input("Informe o CPF").strip()
    usuario.email = input("Informe o email: ").strip().lower()
    usuario.telefone = input("Informe o telefone: ").strip()

    limpar()
    
    # 3. CAPTURA DOS DADOS DA EMPRESA (Pessoa Jurídica)
    print(f"{'-'*20} Infomre os dados da empresa{'-'*20}")
    empresa.razao_social = input("Informe a raz]ao social: ").strip()
    
    # 🚨 DETALHE: Aqui você digitou 'empresa.razao_fantasia', mas lá no construtor 
    # da classe o nome correto que você definiu foi 'nome_fantasia'.
    empresa.razao_fantasia = input("Informe o nome: ").strip()
    
    empresa.cnpj = input("Informe o CNPJ: ").strip()
    empresa.email = input("Informe o e-mail: ").strip().lower()
    empresa.telefone = input("Informe o telefone: ").strip()

    limpar()

    # 4. EXIBIÇÃO DOS RELATÓRIOS NA TELA
    # Aqui, em vez de chamar um método pronto (como 'exibir_dados'), você preferiu
    # acessar propriedade por propriedade usando os prints direto no arquivo main.
    print(f"{'-'*20} DADOS DO USUÁRIO {'-'*20}")
    print(f"Nome: {usuario.nome}")
    print(f"CPF: {usuario.cpf}")
    print(f"E-mail: {usuario.email}")
    print(f"Telefone: {usuario.telefone}")
    
    print(f"{'-'*20} DADOS DO EMPRESA {'-'*20}")
    print(f"Razão Social: {empresa.razao_social}")
    print(f"Nome da empresa: {empresa.nome_fantasia}") # Pede o 'nome_fantasia' que foi criado no __init__
    print(f"CNPJ: {empresa.cnpj}")
    print(f"E-mail: {empresa.email}")
    print(f"Telefone: {empresa.telefone}")

# Garante que o script só execute a função main() se você der Play diretamente nele.
if __name__ == "__main__":
    main()