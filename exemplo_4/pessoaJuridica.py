from pessoa import Pessoa
from base_dados import Base
from time import sleep

class PessoaJuridica(Pessoa):
    def __init__(self, CNPJ, nome, idade, dados, espera):
        super().__init__(nome, idade)
        self.CNPJ = CNPJ
        self.dados = dados
        self.espera = espera
    
    def contratar(self, tempoE, email, lista, empresa):
        
        print('Analizando curriculo', end='')
        for c in range(3):
            sleep(2)
            print('.', end='')
        if email in empresa.dados['fisica'].keys():
            return '\nUsuário já contratado'

        elif email in empresa.espera['fisica'].keys():
            del empresa.espera['fisica'][email]
            empresa.dados['fisica'].update({email: lista})
            return '\nEstá contradado'

        else:
            if tempoE >= 5:
                empresa.dados['fisica'].update({email: lista})
                return '\nEstá contradado'
                

            elif tempoE < 5 and tempoE >= 3:
                empresa.espera['fisica'].update({email: lista})
                return '\nVocê esta na lista de espera'

            else:
                return '\nNão atende os requisitos mínimos'

    def cadastrar(self, email, lista, base, empresa):
        empresa.dados['fisica'].update({email: lista})
        if email in empresa.dados['fisica'].keys():
            return 'Usuário Foi cadastrado na Empresa'
        else:
            lista.insert(0, 'admin')
            base.gravar(email, lista)
            return 'Usuário Foi cadastrado na Empresa. Senha padrão: admin'

    def getRetornarDados(self):
        return self.dados

    def getRetornarEspera(self):
        return self.espera

    def getDados(self, empresa):
        for k in empresa.dados['fisica'].keys():
            print('-------------------------------')
            print(f'{k}')
            print(f'Nome: {empresa.dados["fisica"][k][0]}')
            print(f'CPF: {empresa.dados["fisica"][k][1]}')
            print(f'Idade: {empresa.dados["fisica"][k][2]}')
            print('-------------------------------')

    def demitir(self, usuario, base):
        if usuario in base.dados['fisica']:
            del base.dados['fisica'][usuario]
        else:
            return 'Usuário não encontrado.'
        return 'Processo de demição concluida'

        




