import os

# lampdas [e uma forma simplicada de defifnir uma função]
limpar = lambda: os.system("cls" if os.name == "nt" else "clear")
area_traingulo = lambda b,h: (b*h)/2


# função principal
def main():
    limpar()
    b = float(input("Informe a base: ").replace(",",","))
    h = float(input("Informe a altura: ").replace(",",","))
    limpar()
    print(f"Àrea do triângulo: {area_traingulo(b,h)}.")

if __name__ == "__main__":
    main()
