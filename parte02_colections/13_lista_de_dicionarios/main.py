
usuarios = [
    {
        'nome': "Alex Machado",
        'idade': 21,
        'email': "Alex@gmail.com",

    },
    {
        'nome': "Karol De Sousa",
        'idade': 39,
        'email': "Karol@gmail.com",
    
    },

    {
        'nome': "Carlos Augusto",
        'idade': 21,
        'email': "Carlos@gmail.com",
        },

]




# exibr od fsfod fr yofod od udustiod

for usuario in usuarios:
    for chave, valor in usuario.items():
        print(f"{chave.capitalize()}: {valor}")
    print(f"{'-'*40}")