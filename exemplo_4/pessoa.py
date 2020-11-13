class Pessoa:
    def __init__(self, nome, idade):
        self.__nome = nome
        self.__idade = idade

    def getNome(self):
        return self.__nome

    def getIdade(self):
        return self.__idade

    def setNome(self, nome2):
        self.__idade = nome2

    def setIdade(self, idade2):
        self.__idade = idade2

    def getDados(self):
        return None