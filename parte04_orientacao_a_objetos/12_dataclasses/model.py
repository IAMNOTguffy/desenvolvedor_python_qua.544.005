from dataclasses import dataclass
# NOTE COM O DATACLASS ELE VIRA SE TORNANDO O CONSTRUTOR
# NOTE Esse vira a classe 
@dataclass
class Pessoa: # TODO definindo atribuidos fora do init
    # ATRIBUTOS
    nome: str
    cpf: str
    email: str
    idade: int
    altura: float
