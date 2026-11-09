
class Endereco:
    def __init__(self, cep, uf, bairro, logradouro, complemento, numero):
        self.__cep = cep
        self.__uf = uf
        self.__bairro = bairro
        self.__logradouro = logradouro
        self.__complemento = complemento
        self.__numero = numero
# TODO PEGAR DO REPOSITORIO DO PROFESSOR 09/11/2026
    # CEP
    @property
    def cep(self):
        return self.__cep

    @cep.setter
    def cep(self, cep):
        self.__cep = cep

    # UF
    @property
    def uf(self):
        return self.__uf

    @uf.setter
    def uf(self, uf):
        self.__uf = uf

    @property
    def bairro(self):
        return self.__bairro

    @bairro.setter
    def bairro(self, bairro):
        self.__bairro = bairro

    # Logradouro
    @property
    def logradouro(self):
        return self.__logradouro

    @logradouro.setter
    def logradouro(self, logradouro):
        self.__logradouro = logradouro

    # Complemento
    @property
    def complemento(self):
        return self.__complemento

    @complemento.setter
    def complemento(self, complemento):
        self.__complemento = complemento

    # Número
    @property
    def numero(self):
        return self.__numero

    @numero.setter
    def numero(self, numero):
        self.__numero = numero


class Pessoa:
    def __init__(self, nome, cpf, email, telefone, endereco):
        self.__nome = nome
        self.__cpf = cpf
        self.__email = email
        self.__telefone = telefone
        self.__endereco = endereco

    # Nome
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    # CPF
    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf

    # Email
    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email

    # Telefone
    @property
    def telefone(self):
        return self.__telefone

    @telefone.setter
    def telefone(self, telefone):
        self.__telefone = telefone

    # Endereço
    @property
    def endereco(self):
        return self.__endereco

    @endereco.setter
    def endereco(self, endereco):
        self.__endereco = endereco

    # Exibir dados
    def exibir_dados(self):
        print("\n========== DADOS DA PESSOA ==========")
        print(f"Nome: {self.nome}")
        print(f"CPF: {self.cpf}")
        print(f"E-mail: {self.email}")
        print(f"Telefone: {self.telefone}")

        print("\n========== ENDEREÇO ==========")
        print(f"CEP: {self.endereco.cep}")
        print(f"UF: {self.endereco.uf}")
        print(f"Bairro: {self.endereco.bairro}")
        print(f"Logradouro: {self.endereco.logradouro}")
        print(f"Complemento: {self.endereco.complemento}")
        print(f"Número: {self.endereco.numero}")
        print("=====================================")