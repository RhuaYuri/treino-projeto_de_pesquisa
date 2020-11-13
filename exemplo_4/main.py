#Simulando Base de dados
from base_dados import Base
from pessoaFisica import PessoaFisica
from pessoaJuridica import PessoaJuridica
from adm import Adm
bd = Base()
dados = {
    'fisica': {'ronaldo@gmail.com': [ 'Ronaldo', '12345678912', 20], 'carlos@gmail.com': ['Carlos', '782897392821', 25],
    'joao@gmail.com': ['João', '782901635123', 13], 'andressa@gmail.com': ['Andressa', '78782983645279', 18], 'elena@gmail.com': ['Elena', '78938624138093', 36]},
        }
    
espera = {'fisica': {'renata@gmail.com': [ 'Renata', '782617829301', 19], 'debora@gmail.com': ['Débora', '892918128371', 32]}}

def instansiar(chave, usuario, dados1=None, esp=None):
    nome = bd.dados[chave][usuario][1]
    codigo = bd.dados[chave][usuario][2]
    idade = bd.dados[chave][usuario][3]
    if chave == 'adm':
        return Adm(codigo, nome, idade)
    elif chave == 'fisica':
        return PessoaFisica(codigo, nome, idade)
    else:
        return PessoaJuridica(codigo, nome, idade, dados1, esp)
    
armazem = {}
esp = {}
while True:
    a = int(input('1 - Tela de Login\n2 - Cadastrar Usuário\n3 - Sair do Programa\nDigite uma opção: '))
    if a == 3:
        break#Encerra Programa

    #Tela de Login
    elif a == 1:
        print('Tela de Login')
        usuario = input('Digite seu email: ')
        senha = input('Digite sua senha: ')
        if usuario in bd.dados['adm'].keys():
            if senha == bd.dados['adm'][usuario][0]: 
                usuarioAgora = instansiar('adm', usuario)
                while True:
                    print('1 - Vizuarlizar Lista de Usuários\n2 - Remover Usuário\n3 - Cadastar Usuário\n4 - Deslogar')
                    a = int(input('Digite uma opção: '))
                    if a == 1:
                        usuarioAgora.getDados()
                    elif a == 2:
                        nome = input('Digite o nome do usuário: ')
                        print(usuarioAgora.remover(nome, bd))
                    elif a == 3:
                        email = input('Digite o email do usuário: ')
                        nome = input('Digite o nome do usuário: ')
                        codigo = input('digite o codigo de indetificação do usuário: ')
                        idade = input('Digite a idade do usuário: ')
                        senha = 'admin'
                        print('Senha padrão so usuário: admin')
                        lista = [senha, nome, codigo, idade]
                        print(usuarioAgora.cadastar(email, lista, bd))
                    elif a == 4:
                        break
                    else:
                        print('Opção Inválida')

            else:
                print('Senha Inválida')
       
        elif usuario in bd.dados['fisica'].keys():
            if senha == bd.dados['fisica'][usuario][0]:
                usuarioAgora = instansiar('fisica', usuario)
                #Intanciando o Objeto PessoaFisica
                while True:
                    print('1 - Vizuarlizar Seus Dados\n2 - solicitar emprego\n3 - Deslogar')
                    a = int(input('Digite uma opção: '))
                    if a == 1:
                        print('-----------------------')
                        usuarioAgora.getDados(usuario, bd)
                        print('-----------------------')
                    elif a == 2:
                        experiencia = int(input('Quantos anos de experiencia você tem? '))
                        email = input('Digite o email da Empresa que deseja trabalhar: ')
                        empresa = instansiar('juridica', email)
                        lista = [usuarioAgora.getNome(), usuarioAgora.getCPF(), usuarioAgora.getIdade()]
                        print(usuarioAgora.solicitarContratacao(experiencia, usuario, lista, empresa))
                    elif a == 3:
                        break
                    else:
                        print('Opção Inválida')

            else:
                print('Senha Inválida')
                
        elif usuario in bd.dados['juridica'].keys():
                if senha == bd.dados['juridica'][usuario][0]:
                    if usuario in armazem.keys():
                        usuarioAgora = instansiar('juridica', usuario, armazem[usuario], esp[usuario])
                    else:
                        usuarioAgora = instansiar('juridica', usuario, dados, espera)
                    while True:
                        print('1 - Vizuarlizar Dados dos Funcionários\n2 - Cadastrar Funcionário\n3 - Demitir Fucionário\n4 - Deslogar')
                        a = int(input('Digite uma opção: '))
                        if a == 1:
                            usuarioAgora.getDados(usuarioAgora)
                        elif a == 2:
                            nome = input('Digite o nome do funcionário: ')
                            cpf = input('Digite o CPF do funcionário: ')
                            idade = input('Digite a idade do funcionário: ')
                            email = input('Digite o email: ')
                            lista = [nome, cpf, idade]
                            print(usuarioAgora.cadastrar(email, lista, bd, usuarioAgora))
                        elif a == 3:
                            email = input('Digite o email do funcionário: ')
                            print(usuarioAgora.demitir(email, usuarioAgora))
                        elif a == 4:
                            if usuario in armazem.keys():
                                del armazem[usuario] 
                                del esp[usuario]   
                            armazem.update({usuario: usuarioAgora.getRetornarDados()})
                            esp.update({usuario: usuarioAgora.getRetornarEspera()})
                            break
                        else:
                            print('Opção inválida')
                        
                        
                else:
                    print('Senha incorreta')

        else:
            print('Email inválido')

    #Tela de Cadastro
    elif a == 2:
        nome = input('Digite seu nome: ')
        idade = input('Digite sua idade: ')
        cpf = input('Digite seu CPF: ')
        email = input('Digite seu email (usuário): ')
        senha = input('Digite uma senha: ')
        lista = [senha, nome, cpf, idade]
        bd.gravar(email, lista)
        
    else:
        print('Opção Inválida!')