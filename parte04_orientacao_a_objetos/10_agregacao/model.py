class Departamento:
    def __init__(self,nome):
        self.__nome = nome
# TODO PEGAR DO REPOSITORIO
    @property
    def nome(self):
        return self.__name

    @nome.setter
    def nome(self,nome):
        self.__nome = nome

class Empresa:
    def __init__(self, razao_social, nome_fantasia, cnpj, departamento):
        self.__razao_social = razao_social
        self.__nome_fantasia = nome_fantasia
        self.__cnpj = cnpj
        self.__departamento = departamento

        @property
        def razao_social(self):
            return self.__razao_social

        @razao_social.setter
        def razao_social(self,razao_social):
            return self.__razao_social
              
        @property
        def nome_fantasia(self):
            return self.__nome_fantasia
        
        @nome_fantasia.setter
        def nome_fantasia(self,nome_fantasia):
            return self.__nome_fantasia
        
        @property
        def cnpj(self):
            return self.__cnpj

        @cnpj.setter
        def cnpj(self, cnpj):
            return self.__cnpj
        @property
        def departamento(self):
            return self.__departamento

        @razao_social.setter
        def departamento(self,razao_social):
            return self.__departamento
        
        
        