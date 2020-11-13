from pessoa import Pessoa
from base_dados import Base
class Adm(Pessoa):
    def __init__(self, codigo, nome, idade):
        super().__init__(nome, idade)
        self.nome = nome
        self.idade = idade
        self.codigo = codigo

    def getDados(self):
        self.dados = Base()
        self.visu = self.dados.getDados()
        print('Administradores')
        for k in self.visu['adm'].keys():
            print('-------------------------------')
            print(f'{k}')
            print(f'Nome: {self.dados.dados["adm"][k][1]}')
            print(f'Codigo: {self.dados.dados["adm"][k][2]}')
            print(f'tempo como ADM: {self.dados.dados["adm"][k][3]}')
            print('-------------------------------')
        print('Usuário Comum')
        for k in self.visu['fisica'].keys():
            print('-------------------------------')
            print(f'{k}')
            print(f'Nome: {self.dados.dados["fisica"][k][1]}')
            print(f'CPF: {self.dados.dados["fisica"][k][2]}')
            print(f'Idade: {self.dados.dados["fisica"][k][3]}')
            print('-------------------------------')
        print('Empresas')
        for k in self.visu['juridica'].keys():
            print('-------------------------------')
            print(f'{k}')
            print(f'Nome: {self.dados.dados["juridica"][k][1]}')
            print(f'CNPJ: {self.dados.dados["juridica"][k][2]}')
            print(f'Idade: {self.dados.dados["juridica"][k][3]}')
            print('-------------------------------')

    def cadastar(self, usuario, lista, base):
        base.gravar(usuario, lista)
        return 'Cadastro Concluído'

    def remover(self, usuario, base):
        if usuario in base.dados['adm']:
            del base.dados['adm'][usuario]
        elif usuario in base.dados['fisica']:
            del base.dados['fisica'][usuario]
        elif usuario in base.dados['juridica']:
            del base.dados['juridica'][usuario]
        else:
            return 'Usuário não encontrado. Romoção não efetuada'
        return 'Remoção efetuada com sucesso'
