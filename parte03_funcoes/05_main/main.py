# biblioteca
import math
import os

# função
def raiz(n):
    return math.sqrt(n) #math.sqrt é raiz quadrada

def limpar():
    os.system("cls" if os.name == "nt" else "clear")

# algoritmo principal
def main():
    # todo
    pass


# algoritmo principal protegido
if __name__ == "__main__":
    main()
    n = float(input("Infomre um número inteiro: ").replace(",","."))
    print(f"Raíz de {n} é {raiz(n)}")