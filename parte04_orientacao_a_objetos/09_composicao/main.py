from model import Carro
# TODO PEGAR DO REPOSITORIO DO PROFESSOR 09/11/2026
def main():
    carro = Carro(fabricante="",modelo="",ano=0,cor="",potencia = 600)


    print("Dados que vai receber o motor:")
    carro.fabricante = input("Informe o fabricante: ").strip()
    carro.modelo = input("Informe o modelo: ").strip()
    carro.fano = int(input("Informe o fabricante: "))
    carro.cor = input("Informe a cor: ").strip()

    print(carro.exibir_detalhes())

if __name__ == "__main__":
    main()