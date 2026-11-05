# MODULO
# superClasse
class Pessoa:
    """
    Esta é a Classe-Pai. Ela foi criada para guardar o que é comum (email e telefone).
    """
    def __init__(self,email,telefone):
        # 🚨 ATENÇÃO: Aqui o código guarda o dado 'email' dentro de uma caixinha chamada '__nome'
        # e guarda o dado 'telefone' dentro de uma caixinha chamada '__email'.
        self.__nome = email
        self.__email = telefone

    # metodo de acesso

    @property
    def email(self):
        # Quando alguém pede o .email, o código devolve a caixinha '__email' (que guarda o telefone)
        return self.__email

    @email.setter
    def email(self,email):
        self.__email = email

    @property
    def telefone(self):
        # 🚨 CUIDADO: Este getter tenta devolver 'self.__telefone', mas essa caixinha 
        # não foi criada lá em cima no __init__ (o programa vai dar erro aqui se for chamado)
        return self.__telefone
    
    @telefone.setter
    def telefone(self,telefone):
        self.__telefone = telefone

# subclasses
class PessoaFisica(Pessoa):
    """
    Classe-Filha que herda de Pessoa e adiciona Nome e CPF.
    """
    def __init__(self,nome,cpf,email,telefone):
        self.__nome = nome
        self.__cpf = cpf
        # Passa os dados para o Pai resolver usando o super()
        super().__init__(email=email,telefone=telefone)

        # 🚨 NOTA RELEVANTE: As propriedades abaixo foram recuadas para DENTRO do __init__.
        # No Python, as @property devem ficar fora do __init__, alinhadas com o 'def __init__'.
        @property
        def nome(self_):
            return self.__nome

        @nome.setter
        def nome(self,nome):
            self.__nome = nome

        @property
        def cpf(self):
            return self.__cpf

        @cpf.setter
        def cpf(self,cpf):
            self.__cpf = cpf

class PessoaJuridica(Pessoa):
    """
    Classe-Filha que herda de Pessoa e adiciona dados de Empresa.
    """
    def __init__(self,razao_social,nome_fantasia,cnpj,email,telefone):
        self.__razao_social = razao_social
        self.__nome_fantasia = nome_fantasia
        self.__cnpj = cnpj
        # Passa e-mail e telefone para a classe-pai gerenciar
        super().__init__(email=email,telefone=telefone)

    # Aqui as @property foram colocadas no lugar certo (fora do __init__)
    @property
    def razao_social(self):
        return self.__razao_social

    @razao_social.setter
    def razao_social(self,razao_social):
        self.__razao_social = razao_social

    @property
    def nome_fantasia(self):
        return self.__nome_fantasia
