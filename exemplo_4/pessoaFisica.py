from pessoa import Pessoa
from pessoaJuridica import PessoaJuridica
from base_dados import Base

class PessoaFisica(Pessoa):
    def __init__(self, CPF, nome, idade):
        super().__init__(nome, idade)
        self.__CPF = CPF

    def getCPF(self):
        return self.__CPF

    def getDados(self, usuario, base):
        self.visu = base.getDados()
        print(self.visu['fisica'][usuario])
        print(f'Nome: {self.visu["fisica"][usuario][1]}')
        print(f'CPF: {self.visu["fisica"][usuario][2]}') 
        print(f'Idade: {self.visu["fisica"][usuario][3]}')
        print(f'Nome Usuário: {usuario}')
        print(f'Senha: {self.visu["fisica"][usuario][0]}')

    def solicitarContratacao(self, tempoE, email, empresa, lista):
        return empresa.contratar(tempoE, email, lista)



