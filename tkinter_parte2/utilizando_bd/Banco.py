#importando módulo do SQlite
import sqlite3
class Banco():

    def __init__(self):
        self.conexao = sqlite3.connect("banco.db")
        self.createTable()

    def createTable(self):
        c = self.conexao.cursor()

        c.execute("""create table if not exists produto (
                    idproduto integer primary key autoincrement ,
                    nome text,
                    fornecedor text,
                    preco text,
                    marca text);""")
        self.conexao.commit()
        c.close()