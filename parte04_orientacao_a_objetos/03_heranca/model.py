# superclasse / classe-pai
class Pessoa:
    """
    Esta é a CLASSE-PAI (ou Superclasse). Ela guarda tudo o que é COMUM a qualquer tipo de pessoa.
    Tanto uma pessoa comum (Física) quanto uma empresa (Jurídica) têm e-mail, telefone e endereço.
    Para não ter que digitar essas variáveis duas vezes, nós as colocamos aqui no Pai.
    """
    def __init__(self,email,telefone,endereco):
        # O Pai cria e cuida dessas três caixinhas de dados comuns
        self.email = email
        self.telefone = telefone
        self.endereco = endereco

    # método da classe
    def exibir_dados(self):
        # Esta função do Pai sabe apenas mostrar os dados que o Pai possui
        print(f"E-mail: {self.email}")
        print(f"Telefone: {self.telefone}")
        print(f"Endereço: {self.endereco}")


# subclasses / classes-filha
class PessoaFisica(Pessoa):
    """
    Esta é uma CLASSE-FILHA (Subclasse). Ao colocar '(Pessoa)', ela herda tudo do Pai.
    A PessoaFisica é uma Pessoa, mas com características próprias: 'nome' e 'cpf'.
    """
    def __init__(self,nome,cpf,email,telefone,endereco):
        # 1. Primeiro ela pega os dados específicos dela e guarda nas suas próprias caixinhas:
        self.nome = nome
        self.cpf = cpf
        
        # 2. O COMANDO MÁGICO: super().__init__(...)
        # O 'super()' significa: "Chame o meu Pai". 
        # Esta linha repassa o e-mail, telefone e endereço para o construtor do Pai resolver e guardar lá.
        super().__init__(email=email,telefone=telefone,endereco=endereco)

    def exibir_dados(self):
        """
        POLIMORFISMO: A filha recria a função 'exibir_dados' para personalizá-la.
        """
        print(f"{'-'*20} DADOS DO USUÁRIO {'-'*20}")
        print(f"Nome: {self.nome}") # Mostra o dado específico da filha
        print(f"CPF: {self.cpf}")   # Mostra o dado específico da filha
        
        # O 'super().exibir_dados()' diz: "Pai, agora termine de mostrar o e-mail, telefone e endereço"
        super().exibir_dados()


class PessoaJuridica(Pessoa):
    """
    Esta é outra CLASSE-FILHA. Ela também herda tudo de Pessoa.
    Mas, por ser uma empresa, suas características próprias são 'cnpj', 'razao_social' e 'nome_fantasia'.
    """
    def __init__(self,cnpj,razao_social,nome_fantasia,email,telefone,endereco):
        # 1. Guarda os dados específicos de empresa:
        self.cnpj = cnpj
        self.razao_social = razao_social
        self.nome_fantasia = nome_fantasia
        
        # 2. Envia os dados comuns para o Pai cuidar, exatamente como a outra irmã fez:
        super().__init__(email=email,telefone=telefone,endereco=endereco)

    def exibir_dados(self):
        """
        A classe empresa também personaliza a exibição de dados com seu próprio estilo.
        """
        print(f"{'-'*20} DADOS DA EMPRESA {'-'*20}")
        print(f"Razão Social: {self.razao_social}")
        print(f"Nome da empresa: {self.nome_fantasia}")
        print(f"CNPJ: {self.cnpj}")
        
        # Chama a função do Pai para imprimir os dados de contato no final do bloco
        super().exibir_dados()