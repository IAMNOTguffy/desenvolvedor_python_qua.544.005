# declaração de variaveis
x = float(input("informe um núnmero:  ").replace(",","."))
y = float(input("informe um núnmero:  ").replace(",","."))

# menu
print(f"{'-1*20'} Escolha uma operação `{'-'*20}")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

operador = input("Operação desejada:  ").strip()

#match...case

match operador:
    case "1":
        print(f"Resultado da soma: {x+y}")
    case "2":
        print(f"Resultado da subtração:  {x-y}")
    case "3":
        print(f"Resultado da Multiplicação {x*y}")
    case "4":
        print(f"Resultado da Divisão {x/y}")
    case _:
        print("Operação invalida.")