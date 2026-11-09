import os
# TODO PEGAR DO REPOSITORIO DO PROFESSOR DIA 09/11/2026
from model import Empresa, Departamento

def limpar():
    os.system("cls" if os.name == "nt" else "clear")

def main():
    departamento = Departamento(nome="")
    empresa = Empresa(razao_social="",nome_fantasia="",cnpj="",departamento=departamento)

    limpar()
    print("Defina os dados da empresa:")
    empresa.razao_social = input("Infomre a razão social: ").strip
    empresa.nome_fantasia = input("Infomre o nome: ").strip
    empresa.cnpj = input("Infomre o CNPJ: ").strip
    empresa.departamento = input("Infomre o departamento em que trabalha: ").strip

    limpar()
    print(empresa.detalhes())

if __name__ == "__main__":
    main()