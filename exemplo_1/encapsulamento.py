'''

Exemplo de Encapsulamento.
Sitema de Cadastro de clientes


'''

import cliente as c

controlador = 0
bd = c.BaseDeDados()
while True:
    a = input('1 - inserir cliente\n2 - listar clientes\n3 - apagar cliente\n4 - finalizar o programa\n digite uma opção: ')
    if a == '4':
        break
    else:
        if int(a) < 0 or int(a) > 4:
            print('Erro!')
        elif a == '1': 
            controlador += 1
            nome = input('Digite o nome do cliente: ')
            bd.inserir_cliente(controlador, nome)
        elif a == '2':
            bd.lista_clientes()
        elif a == '3':
            id = int(input('insira o id do cliente: '))
            bd.apagar_cliente(id)


