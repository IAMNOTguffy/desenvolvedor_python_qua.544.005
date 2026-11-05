# classe
class Pessoa:
    # construtor
    def __init__(self,nome,idade,email,cpf):# self esta relacionado a pessoa, individuo
        """
        O __init__ é o construtor. Ele cria o seu objeto na memória.
        O 'self' representa o indivíduo que está sendo criado agora.
        As linhas abaixo criam as 'caixinhas' (atributos) que vão guardar as informações dele.
        """
        # atributos
        self.nome = nome
        self.idade = idade
        self.email = email
        self.cpf = cpf

    def exibir_dados(self):
        """
        Este é um método (uma ação). Ele lê o que está guardado nas 
        caixinhas (self.nome, self.idade...) deste indivíduo e mostra na tela.
        """
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade} anos")
        print(f"E-mail: {self.email}")
        print(f"CPF: {self.cpf}")


def main():
    # instanciar a classe
    # Aqui você cria o 'usuario' usando o molde da classe Pessoa.
    # Passar "" e 0 cria um usuário com as caixinhas temporariamente zeradas.
    usuario = Pessoa(nome="",idade=0,email="",cpf="")# deixa aberto "" para o usuario botar e definir

    # insere valores nos atributos
    # O input captura o que o usuário digita. O sinal de '=' pega esse texto e 
    # joga direto para dentro do atributo do objeto 'usuario'.
    usuario.nome = input("Informe o nome: ").strip().title()
    usuario.idade = int(input("Informe a idade: "))
    usuario.email = input("Informe o e-mail: ").strip().lower()
    usuario.cpf = input("Informe o CPF: ").strip()

    # exibe os atributos na tela
    # Agora que o objeto 'usuario' está com todos os atributos preenchidos, 
    # você chama o método dele para mostrar tudo formatado.
    usuario.exibir_dados()

if __name__ == "__main__":
    """
    Esta linha testa se este arquivo é o principal que você acabou de dar 'Play'.
    Se for, ele chama a função main() para começar a pedir os dados.
    """
    main()