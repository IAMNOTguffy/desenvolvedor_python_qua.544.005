from abc import ABC, abstractclassmethod
from dataclasses import dataclass
# NOTE Define a regra da classe, que precisa ter isso

# interface
class IConta(ABC):
    @abstractclassmethod 
    def consultar(self):
        pass

    @abstractclassmethod
    def depositor(self,valor):
        pass

    @abstractclassmethod
    def sacar(self,valor):
        pass

@dataclass
class Pessoa:
    nome: str
    cpf: str

    def __str__(self):
        return (f"Objeto {self.nome} destrída com sucesso!")

@dataclass
class Conta(IConta):
    agencia: str
    n_conta: str    
    tipo_conta: str
    saldo: float
    titular: Pessoa

    def __str__(self):
        return f"{'-'*20} DADOS DO TITULAR DA CONTA {'-'*20}\n{self.titular}\n\n{'-'*20} DADOS DA CONTA {'-'*20}\n"

    def __float__(self):
        return self.saldo

    def __del__(self):
        print("Conta destruída com sucesso!")

    def consultar(self):
        print("Titular da conta: ")
        print(self.titular)
        print(f"Agência: {self.agencia}")
        print(f"Número da conta: {self.n_conta}")
        print(f"Saldo: $ {self.saldo:.2f}")
        print(f"Tipo de conta: {self.tipo_conta}")

    def depositor(self, valor):
        self.saldo += valor
        return self.saldo

    def sacar(self, valor):
        self.saldo -= valor
        return self.saldo

@dataclass
class ContaCorrente(Conta):
    taxa: float

    def sacar(self,valor):
        self.saldo -= self.taxa
        return super().sacar(valor)

@dataclass
class ContaPoupanca(Conta):
    juros: float

    def depositor(self, valor):
        self.saldo += self.saldo*(self.juros/100)
        return super().depositar(valor)

