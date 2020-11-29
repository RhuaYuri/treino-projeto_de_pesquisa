from Banco import Banco

class Produtos:
    def __init__(self, idproduto = 0, nome = "", fornecedor = "", preco = "", marca = ""):
        self.info = {}
        self.idproduto = idproduto
        self.nome = nome
        self.fornecedor = fornecedor
        self.preco = preco
        self.marca = marca


    def insertUser(self):

        banco = Banco()
        try:

            c = banco.conexao.cursor()

            c.execute("'insert into usuarios (nome, fornecedor, preco, marca) values ('" + self.nome + "', '" + self.fornecedor + "', '" + self.preco + "', '" + self.marca + "' );'")
            banco.conexao.commit()
            c.close()

            return "Usuário cadastrado com sucesso!"
        except:
            return "Ocorreu um erro na inserção do usuário"

    def updateUser(self):

        banco = Banco()
        try:

            c = banco.conexao.cursor()

            c.execute("update produtos set nome = '" + self.nome + "', fornecedor = '" + self.fornecedor + "', preco = '" + self.preco + "', marca = '" + self.marca + "' where idproduto = " + self.idproduto + " ")

            banco.conexao.commit()
            c.close()

            return "Usuário atualizado com sucesso!"
        except:
            return "Ocorreu um erro na alteração do usuário"

    def deleteUser(self):

        banco = Banco()
        try:

            c = banco.conexao.cursor()

            c.execute("delete from produto where iduproduto = " + self.idproduto + " ")

            banco.conexao.commit()
            c.close()

            return "Usuário excluído com sucesso!"
        except:
            return "Ocorreu um erro na exclusão do usuário"

    def selectUser(self, idproduto):
        banco = Banco()
        try:

            c = banco.conexao.cursor()

            c.execute("select * from produto where idproduto = " + idproduto + "  ")

            for linha in c:
                self.idproduto = linha[0]
                self.nome = linha[1]
                self.fornecedor = linha[2]
                self.preco = linha[3]
                self.marca = linha[4]

            c.close()

            return "Busca feita com sucesso!"
        except:
            return "Ocorreu um erro na busca do usuário"