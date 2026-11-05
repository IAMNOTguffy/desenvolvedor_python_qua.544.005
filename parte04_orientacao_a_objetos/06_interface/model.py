# import abstração
from abc import ABC, abstractmethod # importa uma classe que ja existe na biblioteca python
# TODO  
# Abstractmethod obriga o programa a ter essa subclasse no programa (os requisistos)

# interface / classe abstrata
from abc import ABC, abstractmethod  # Importa as ferramentas para criar classes abstratas (o "contrato")

# 1. CRIANDO A INTERFACE (O CONTRATO)
class IConta(ABC):  # O (ABC) diz que esta classe é abstrata e serve como um modelo/esqueleto
    
    @abstractmethod  # Este decorador OBRIGA qualquer classe que herdar de IConta a criar o método 'consultar_conta'
    def consultar_conta(self): 
        pass  # O 'pass' serve apenas para preencher o espaço, já que a interface não executa código real
        
    @abstractmethod  # Obriga a classe filha a ter o método 'depositar'
    def depositar(self,valor):
        pass
        
    @abstractmethod  # Obriga a classe filha a ter o método 'sacar'
    def sacar(self,valor):
        pass


# 2. IMPLEMENTANDO A CLASSE REAL
class Conta(IConta):  # O (IConta) significa que a classe Conta HERDA e deve cumprir o contrato da IConta
    
    def __init__(self, titular, cpf, agencia, n_conta, saldo):
        # O __init__ é o CONSTRUTOR. Ele roda automaticamente quando você cria uma nova conta.
        
        # O uso de dois underlines (__) antes do nome ativa o ENCAPSULAMENTO RESTRITO (Private).
        # Isso esconde o atributo dentro da classe, impedindo que ele seja acessado ou alterado diretamente de fora.
        self.__titular = titular    # Atributo privado para guardar o nome do titular
        self.__cpf = cpf            # Atributo privado para o CPF
        self.__agencia = agencia    # Atributo privado para a agência
        self.__n_conta = n_conta    # Atributo privado para o número da conta
        self.__saldo = saldo        # Atributo privado para o saldo da conta

    # 3. CONCEITO DE GETTER E SETTER (Para acessar o que está escondido)

    @property  # O @property cria um GETTER. Ele permite LER o valor de self.__titular com segurança.
    def titular(self):
        # Quando alguém digitar: print(conta.titular), este método roda e devolve o nome.
        return self.__titular

    @titular.setter  # O @titular.setter cria um SETTER. Ele serve para ALTERAR o valor de self.__titular.
    def titular(self, novo_titular):
        # Quando alguém digitar: conta.titular = "Novo Nome", este método é acionado.
        # Aqui você poderia colocar uma validação (ex: ver se o nome não está vazio).
        self.__titular = novo_titular
    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self):
        return self.__cpf
    
    @property
    def agencia(self):
        return self.__agencia
    
    @agencia.setter
    def agencia(self):
        return self.__agencia

    @property
    def n_conta(self):
        return self.__n_conta

    @n_conta.setter
    def n_conta(self):
        return self.__n_conta

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self):
        return self.saldo

    # método da interface
    def consultar_conta(self):
        print(f"{'-'*20} Dados da conta {'-'*20}")
        print(f"Nome do tiular: {self.__nome}")
        print(f"CPF do tiular: {self.__cpf}")
        print(f"Agencia: {self.__agencia}")
        print(f"Conta: {self.__Conta}")
        print(f"Saldo : $ {self.__saldo}")

    def depositar(self,valor):
        self.__saldo += valor # incremento: saldo + valor
        return self.__saldo
    def sacar(self,valor):
        self.__saldo -= valor # decremento? saldo - valor
        return self.__saldo
    




    

    
    