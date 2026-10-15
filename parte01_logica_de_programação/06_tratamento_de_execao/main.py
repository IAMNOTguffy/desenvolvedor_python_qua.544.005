# tratamento de exeção # FIXME: salvar fix
try: 
    nome = input("Informe seu nome:  ").strip().title()
    idade =int(input("Informe sua idade:  "))


    print (f"Nome do usuario:  {nome}")
    print(f"Idade do usuario:  {idade}  anos.")
except Exception as e: 
    print(f"Não foi possível executar a {e}")
finally:
    print("Programa finalizado com sucesso!")

