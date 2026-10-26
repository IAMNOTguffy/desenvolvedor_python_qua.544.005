"""

Crie um programa que recebe o nome, a massa em kg e a altura em metros do usuario. calculçe seu IMC (indice de massa corporal) e finalize informando o dignostico do usuario com base no valor do IMC (se esta magro, gordo ou no peso ideal)


"""

nome = input("Digite seu Nome: ")
peso = float(input("Digite seu peso em kg: ").replace(",","."))
altura = float(input("Digite sua altura em metros: ").replace(",","."))


IMC = peso/(altura**2)

if IMC >= 40:
    print("Obsecidade Grau 3 Morbia, acima do peso ideal")
elif 35 <= IMC >= 39.9:
    print("Obsedidade Grau 2 Severa, acima do peso ideal")
elif 30 <= IMC >= 34.9:
    print("Obsediade Grau 1, acima do peso ideal")
elif 25 <= IMC >= 29.9:
    print("Sobre-Peso, acima do peso ideal")
elif 18.5 <= IMC >= 24.9:
    print("Parabens!!voce tem o peso ideal")
else:
    IMC <= 18.4
    print("Magreza, abaixo do peso ideal")

print(f" {nome} o valor do seu {IMC:.2f} é ")




