# motivo pra criar a venv é isolar a dependencia do projeto
# NOTE DEPENDENCIAS, biblioteca criadas pela comunidade 
# primeira coisa a fazer instalar biblioteca

# digita pip install "nome da biblioteca"

# importando a biblioteca instalada
from translate import Translator
import os

def limpar():
    os.system("cls" if os.name == "nt" else "clear")

def traduzir(texto):
    tradutor = Translator(to_lang="pt")
    return tradutor.translate(texto)

def main():
    limpar()
    texto = input("Digite um texto que deseja traduzir para pt-br: ")
    print(f"\nTexto traduzido:\n{traduzir(texto)}")

if __name__ == "__main__":
    main() 



# NOTE pip freeze > requirements.txt
# é usado para identificar os requerimentos
