# TODO: parte 03 atibidade 01
"""
Crie um prorgama que calcule o peso de uma pessoa em um planeta do sistema solar escolhido por ela.

# NOTE: pesquisar pela aceleração da gravidade em cada planeta.
# NOTE: inclua a Lua na lista de planetas.

abrir o programa, bota o peso, selecionar o planeta, 
"""
import os
import atividades_pt3.atv01.atv01.modulo as modulo
"""
Mercúrio	0,38	3,73
Vênus	0,89	8,73
Terra	1,00	9,81
Marte	0,38	3,73
Júpiter	2,54	24,92 (ou ~24,79)
Saturno	1,07	10,50
Urano	0,80	8,63
Netuno	1,20	11,77
Plutão (planeta anão)	~0,06	~0,60
"""
print("Calculadora Intergalatica")
print("Selecione a opção do planeta desejado")
print("1 - Mercurio")
print("2 - Vênus")
print("3 - Terra")
print("4 - Marte")
print("5 - Júpiter")
print("6 - Saturno")
print("7 - Urano")
print("8 - Netuno")
print("9 - Lua")
# dicionario

m = 0.38
ve = 0.89
mar = 0.38
ju = 2.54
sat = 1.07
ura = 0.80
net = 1.20
lua = 0.16
opcao = input("Digite a opção desejada.")
peso = float(input("Digite o seu peso").replace(",","."))
while True:
    match opcao:
        case "1":
            print(f"O seu peso em Mercurio é {peso*m} Kilos.")
            break
        case "2":
            print(f"O seu peso em Venus é {peso*ve} Kilos.")
            break
        case "3":
            print(f"O seu peso em Terra é {peso*1} Kilos.")
            break
        case "4":
            print(f"O seu peso em Marte é {peso*mar} Kilos.")
            break
        case "5":
            print(f"O seu peso em Jupiter é {peso*ju} Kilos.")
            break
        case "6":
            print(f"O seu peso em Saturno é {peso*sat} Kilos.")
            break
        case "7":
            #NOTE: SIX SEVEN
            print(f"O seu peso em Urano é {peso*ura} Kilos.")
            break
        case "8":
            print(f"O seu peso em Netuno é {peso*net} Kilos.")
            break
        case "9":
            print(f"O seu peso na Lua é {peso*lua} Kilos.")
            break
        case "10":
            print("Programa finalizado com sucesso!")
            break
        case _:
            print("Não foi possivel realizar o programa")
        





    
    


