from random import randint
class BaseDeDados():
    def __init__(self):
        self.bd = {'2090-2':  'Rafael', '9018-0': 'Thalles'}#para teste

    def abrirConta(self, nome):
        while True:
            n4 = randint(1000, 10000)
            tn = randint(0, 10)
            junto = str(n4) + '-' + str(tn)
            if junto not in self.bd.keys:
                break
        self.bd[junto] = nome

    def removerConta(self, numero):
        if numero in self.bd.keys:
            del self.bd[numero]

    def historico(self, numero_conta):
        self.__historico = {numero_conta: a+1}
