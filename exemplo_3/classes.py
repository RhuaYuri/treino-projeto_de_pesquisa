class CarrinhoDeCompras():
    def __init__(self):
        self.produtos = []
    
    def inserir_produto(self, produto):
        self.produtos.append(produto)

    def listar_produto(self):
        if len(self.produtos) == 0:
            print('O carrinho esta vazio!')
        else:
            for produto in self.produtos:
                print(produto.nome, produto.valor)

    def somar_total(self):
        total = 0
        for produto in self.produtos:
            total += produto.valor
        return total


class Produto():
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor