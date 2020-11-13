class Professor:
    def __init__(self, nome):
        self.__nome = nome #conceito de encapusulamento
        self.__salaDeAula = None
    
    def nome(self):
        return self.__nome
    
    def salaDeAula(self, sala):
        self.__salaDeAula = sala

    def EmAula(self):
        return 'Em aula'

class Sala:
    def __init__(self, numero):
        self.__numero = numero

    def numero(self):
        return self.__numero

    def FecharSala(self):
        return 'Porta foi fechada!'

