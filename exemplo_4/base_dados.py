#Salvando Dados dos objetos
class Base:
    def __init__(self):
            self.dados = {
                'adm': {'ronaldo@adm.com': ['123', 'Ronaldo', '12345678912', 20], 'carlos@adm.com': ['321', 'Carlos', '782897392821', 25]},
                'fisica': {'joao@gmail.com': ['231', 'João', '782901635123', 13], 'andressa@gmail.com': ['12345', 'Andressa', '78782983645279', 18], 'elena@gmail.com': ['54321', 'Elena', '78938624138093', 36]},
                'juridica': {'joao@gmail.com': ['12d', 'Sepermecado Mec', '782789017278437821', 60], 'pedro@loja.com': ['@ff', 'Loja Pedro', '7872871672673928926', 25], 'trelo@trem.loja.com': ['bb', 'Loja Trelo', '78328732984759', 100]}
                }
            
    def getDados(self):
        return self.dados

    def gravar(self, nome, lista):
        self.us = nome.split('@')
        if self.us[1] in 'adm.com':
            self.dados['adm'].update({nome: lista})

        elif self.us[1] in 'gmail.com':
            self.dados['fisica'].update({nome: lista})

        else:
            self.dados['juridica'].update({nome: lista})
        print('------------------\nAção Concluída\n------------------')

        
'''import os
import pickle
def criarPasta(nome):
    if not os.path.isdir(nome):
        os.mkdir(nome)
        return True
    return False

def montarCaminho(nomeArq, nomeDir=None):
    if not nomeDir==None:
        return os.path.join(nomeDir, nomeArq)
    return nomeArq

def _salvarArquivoBin(nomeArq, conteudo, nomeDir=None):
    caminho_Arq = montarCaminho(nomeArq, nomeDir)
    arq = open(caminho_Arq, 'wb')
    arq.write(_serializar(conteudo))

def _serializar(conteudo):
    return pickle.dumps(conteudo)

def criarArquivoBin(nomeArquivo, conteudo, nomeDir=None):
    lista = []
    lista.append(conteudo)
    _salvarArquivoBin(nomeArquivo, lista, nomeDir)'''