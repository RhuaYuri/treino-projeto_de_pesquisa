#Exemplo de Agregação. Sistema de Carrinho de Compras
import classes as c 

carrinho = c.CarrinhoDeCompras()

while True:
    print('1 - Adicionar produto\n2 - listar produtos\n3 - Calcular valor total\n4 - Sair do Programa')
    a = int(input('Escolha uma opção: '))
    if a == 4:
        break

    elif a > 3 or a < 0:
        print('------------------------------------')
        print('Erro! Tente novamente!')
        print('------------------------------------')

    else:
        if a == 1:
            print('------------------------------------')
            print('          Insira o Produto')
            print('------------------------------------')
            nome = input('Digite o nome do produto: ')
            valor = float(input('Digite o preço do produto: '))
            carrinho.inserir_produto(c.Produto(nome, valor))
            print('Produto inserido com sucesso!')
            print('------------------------------------')

        elif a == 2:
            print('------------------------------------')
            print('    Lista de produtos no Carrinho')
            print('------------------------------------')
            carrinho.listar_produto()
            print('------------------------------------')
        
        else:
            print('------------------------------------')
            print('            Total da Compra')
            print('------------------------------------')
            print(f'Valor Total: {carrinho.somar_total()}')
            print('------------------------------------')






