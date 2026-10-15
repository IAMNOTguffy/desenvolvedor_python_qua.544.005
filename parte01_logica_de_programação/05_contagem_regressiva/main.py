 # import as bibliotecas
import os
import time



# limpar o terminal
os. system("cls")


# declaração de variável
n = int(input("Informe um número inteiro: "))

# Contador
while n >= 0:
    os.system("cls")
    print(f"{n}...")
    time.sleep(1)
    n-= 1 
    
print("BOOOOMM!!!")

