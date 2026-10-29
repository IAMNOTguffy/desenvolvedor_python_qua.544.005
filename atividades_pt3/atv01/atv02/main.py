# TODO parte 03 atividade 02

"""
Crie um programa em que o usuario informe um numero inteiro e o programa retorne a sequencia fibonacci

se quencia de fibanacci é a somo  F_n = F_{n-1} + F_{n-2} (onde cada número é o resultado da soma dos dois que vêm antes dele).

"""
import os

def limpar():
    os.system("cls" if os.name == "nt" else "clear")

print("Sequenciador Fibonacci 3 Mill")


while True:
    def fibonacci(n):
        return n <= 1 if  ((n-1) + (n-2)) else print("Erro")


    limpar()
    n = int(input("Digite o numero que desejado: "))
    print(f"O seu numero na sequencia de fibonacci {fibonacci(n)}")

    try:

        def fibonacci(n):lambda: n == 1 if ((n-1) + (n-2))
    except Exception:
        print("Erro")

