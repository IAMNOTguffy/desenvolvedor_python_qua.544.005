# classe
class Pessoa:
    """
    A classe 'Pessoa' funciona como a planta do arquiteto ou a fôrma de um objeto.
    Ela define que qualquer pessoa criada no seu sistema precisa ter um nome, idade e e-mail.
    """
    def __init__(self, nome, idade, email):
        """
        O __init__ é o construtor da classe. Ele roda sozinho assim que você cria a pessoa.
        O 'self' é a peça mais importante: ele diz ao Python que estas caixinhas de dados
        pertencem a ESTE indivíduo específico que está sendo gerado na memória agora.
        """
        self.nome = nome     # Guarda o nome enviado na caixinha 'nome' deste objeto
        self.idade = idade   # Guarda a idade enviada na caixinha 'idade' deste objeto
        self.email = email   # Guarda o e-mail enviado na caixinha 'email' deste objeto

    def cumprimentar(self):
        """
        Este é um método (uma ação que o objeto sabe fazer).
        Diferente do exemplo anterior que usava 'print', este método usa o 'return'.
        O 'return' faz a função DEVOLVER o texto pronto para quem chamou ela lá fora,
        permitindo que você guarde essa mensagem em uma variável ou decida o que fazer depois.
        """
        return f"Olá, boa tarde. Meu nome é {self.nome}, tenho {self.idade} anos, e meu e-mail é {self.email}."