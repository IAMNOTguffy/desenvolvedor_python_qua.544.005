# Importa o módulo 'os', que serve para interagir com o sistema operacional (como limpar a tela)
import os

# IMPORTAÇÃO: Busca no arquivo 'model.py' as duas classes filhas que você criou lá
from model import PessoaFisica, PessoaJuridica


def limpar():
    """
    Esta função limpa o terminal para deixar a experiência visual mais bonita.
    Se o sistema for Windows (nt), usa 'cls'. Se for Mac/Linux, usa 'clear'.
    """
    os.system("cls" if os.name == "nt" else "clear")

def main():
    # 1. INSTANCIANDO AS CLASSES (Criando os objetos em branco)
    # Você cria o objeto 'usuario' (Pessoa Física) e o objeto 'empresa' (Pessoa Jurídica).
    # Passar as strings vazias "" serve apenas para criar as "caixinhas" limpas na memória.
    usuario = PessoaFisica(nome="",cpf="",email="",telefone="",endereco="")
    empresa = PessoaJuridica(cnpj="",razao_social="",nome_fantasia="",email="",telefone="",endereco="")

    # 2. CAPTURA DE DADOS DO USUÁRIO (Pessoa Física)
    limpar() # Limpa a tela antes de começar as perguntas do usuário
    print(f"{'-'*20} Informe os dados do usuário {'-'*20}\n")
    
    # O input lê o que o usuário digita e o '=' guarda o dado direto na caixinha do objeto 'usuario'.
    usuario.nome = input("Informe o nome: ").strip().title()
    usuario.cpf = input("Informe o CPF: ").strip()
    usuario.email = input("Informe o e-mail: ").strip().lower()
    usuario.telefone = input("Informe o telefone: ").strip()
    usuario.endereco = input("Informe o endereço: ").strip()

    # 3. CAPTURA DE DADOS DA EMPRESA (Pessoa Jurídica)
    limpar() # Limpa a tela para sumir com as perguntas anteriores e focar apenas na empresa
    print(f"{'-'*20} Informe os dados da empresa {'-'*20}")
    
    # O input lê os dados da empresa e o '=' guarda tudo nas caixinhas do objeto 'empresa'.
    empresa.razao_social = input("Informe a razão social: ").strip()
    empresa.nome_fantasia = input("Informe o nome: ").strip().title()
    empresa.cnpj = input("Informe o CNPJ: ").strip()
    empresa.email = input("Informe o e-mail: ").strip().lower()
    empresa.telefone = input("Informe o telefone: ").strip()
    empresa.endereco = input("Informe o endereço: ").strip()

    # 4. EXIBIÇÃO DOS RESULTADOS FINAIS
    limpar() # Limpa a tela uma última vez para mostrar os relatórios organizados
    
    # Chama o método de exibir dados da Pessoa Física. 
    # Lembra do model? Ele vai mostrar o Nome, CPF e depois chamará o super() para mostrar e-mail/tel/end.
    usuario.exibir_dados()
    
    # Chama o método de exibir dados da Empresa.
    # Ele vai mostrar a Razão Social, Nome Fantasia, CNPJ e depois o super() para mostrar e-mail/tel/end.
    empresa.exibir_dados()


# REGRA DE INICIALIZAÇÃO: Garante que o programa só vai começar a rodar se você der 'Play' direto neste arquivo main.py