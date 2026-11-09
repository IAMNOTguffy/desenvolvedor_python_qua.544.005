class Motor:
    def __init__(self,potencia):
        self.__potencia 
# TODO PEGAR DO REPOSITORIO DO PROFESSOR 09/11/2026
    @property
    def potencia(self):
        return self.__potencia

    @potencia.setter
    def potencia(self,potencia):
        self.__potencia = potencia

    def info(self):
        return f"Potencia: motor de {self.__potencia} cv."

    class Carro:
        def __init_(self,fabricante,modelo,ano,cor,potencia):
            self.__fabricante =fabricante
            self.__modelo = modelo
            self.__potencia = potencia
            self.__ano = ano
            self.__cor = cor
            self.__motor = Motor(potencia) # composição

    @property
    def fabricante(self):
        return self.__fabricante

    @fabricante.setter
    def fabricante(self,fabricante):
        return self.__fabricante

    @property
    def modelo(self):
        return self.__modelo

    @fabricante.setter
    def modelo(self,modelo):
        return self.__modelo

    @property
    def ano(self):
        return self.__ano

    @fabricante.setter
    def ano(self,ano):
        return self.__ano

    @property
    def cor(self):
        return self.__cor

    @cor.setter
    def cor(self,cor):
        return self.__cor

    @property
    def motor(self):
        return self.__motor

    @motor.setter
    def motor(self,motor):
        return self.__motor

    def exibir_detalhes(self):
        return (f"Fabricante: {self.__fabricante}\nModelo: {self.__modelo}\nAno: {self.__ano}\nCor: {self.__cor}\nMotor: {self.__motor.info()}")



