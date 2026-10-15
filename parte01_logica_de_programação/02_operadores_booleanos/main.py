"""
and = e (Duas condicionais verdadeiras)
or = ou (uma das duas ou mais seja verdadeira, mas uma)
not = não (Eu quero que a setença seja obregatoriamente falsa)


"""
# declaração de variavis

nome = input("Informe seu nome:  ").strip().title()
idade = int(input("Informe sua idade:  "))
altura = float(input("Informe sua altura em metros:  ").replace(",","."))

             
# verificar se o pagante possui os requisitos
if idade >= 12 and altura >= 1.35:
   print(f"{nome} passou no teste, é pode entrar no brinquedo!!")
else:
   print(f"{nome} nao conseguiu passar no teste")    
   