from tkinter import *
from produtos import Produtos

class Aplicacao:
    def __init__(self, root):
        #Fonte Padrão para a aplicação
        self.fonte = ("Arial", "9")

        #Incluindo os Conteines
        self.bloco1 = Frame(root)
        self.bloco1["pady"] = 10
        self.bloco1.pack()

        self.bloco2 = Frame(root)
        self.bloco2["padx"] = 20
        self.bloco2["pady"] = 5
        self.bloco2.pack()

        self.bloco3 = Frame(root)
        self.bloco3["padx"] = 20
        self.bloco3["pady"] = 5
        self.bloco3.pack()
        
        self.bloco4 = Frame(root)
        self.bloco4["padx"] = 20
        self.bloco4["pady"] = 5
        self.bloco4.pack()
        
        self.bloco5 = Frame(root)
        self.bloco5["padx"] = 20
        self.bloco5["pady"] = 5
        self.bloco5.pack()

        self.bloco6 = Frame(root)
        self.bloco6["padx"] = 20
        self.bloco6["pady"] = 5
        self.bloco6.pack()

        self.bloco7 = Frame(root)
        self.bloco7["padx"] = 20
        self.bloco7["pady"] = 5
        self.bloco7.pack()

        self.bloco8 = Frame(root)
        self.bloco8["padx"] = 20
        self.bloco8["pady"] = 5
        self.bloco8.pack()

        #Interface
        self.titulo = Label(self.bloco1, text="Dados Produtos :")
        self.titulo["font"] = ("Calibri", "12", "bold")
        self.titulo.pack ()

        self.textproduto = Label(self.bloco2, text="Id_Produto : ", font=self.fonte, width=10)
        self.textproduto.pack(side=LEFT)

        self.idproduto = Entry(self.bloco2)
        self.idproduto["width"] = 10
        self.idproduto["font"] = self.fonte
        self.idproduto.pack(side=LEFT)

        self.btn1 = Button(self.bloco2, text="Buscar", font=self.fonte, width=10)
        self.btn1["command"] = self.buscarProduto
        self.btn1.pack(side=RIGHT)

        self.textnome = Label(self.bloco3, text="nome : ", font=self.fonte, width=10)
        self.textnome.pack(side=LEFT)

        self.nome = Entry(self.bloco3)
        self.nome["width"] = 25
        self.nome["font"] = self.fonte
        self.nome.pack(side=LEFT)

        self.textfornecedor = Label(self.bloco4, text="fornecedor : ", font=self.fonte, width=10)
        self.textfornecedor.pack(side=LEFT)

        self.fornecedor = Entry(self.bloco4)
        self.fornecedor["width"] = 25
        self.fornecedor["font"] = self.fonte
        self.fornecedor.pack(side=LEFT)

        self.textpreco = Label(self.bloco5, text="preço : ", font=self.fonte, width=10)
        self.textpreco.pack(side=LEFT)

        self.preco = Entry(self.bloco5)
        self.preco["width"] = 25
        self.preco["font"] = self.fonte
        self.preco.pack(side=LEFT)

        self.textmarca = Label(self.bloco6, text="marca : ", font=self.fonte, width=10)
        self.textmarca.pack(side=LEFT)

        self.marca = Entry(self.bloco6)
        self.marca["width"] = 25
        self.marca["font"] = self.fonte
        self.marca.pack(side=LEFT)

        self.bntInserir = Button(self.bloco7, text="Inserir", font=self.fonte, width=12)
        self.bntInserir["command"] = self.inserirProduto
        self.bntInserir.pack(side=LEFT)

        self.bntAlterar = Button(self.bloco7, text="Alterar", font=self.fonte, width=12)
        self.bntAlterar["command"] = self.alterarProduto
        self.bntAlterar.pack(side=LEFT)

        self.bntExcluir = Button(self.bloco7, text="Excluir", font=self.fonte, width=12)
        self.bntExcluir["command"] = self.excluirProduto
        self.bntExcluir.pack(side=LEFT)

        self.msg = Label(self.bloco8, text="", font=self.fonte)
        self.msg.pack()




    def buscarProduto(self):
        self.prod = Produtos()
        idproduto = self.idproduto.get()

        self.msg["text"] = self.prod.selectUser(idproduto)

        self.preco.delete(0, END)
        self.preco.insert(INSERT, self.prod.idproduto)

        self.nome.delete(0, END)
        self.nome.insert(INSERT, self.prod.nome)

        self.fornecedor.delete(0, END)
        self.fornecedor.insert(INSERT,self.prod.fornecedor)

        self.preco.delete(0, END)
        self.preco.insert(INSERT, self.prod.preco)

        self.marca.delete(0, END)
        self.marca.insert(INSERT, self.prod.marca)



    def inserirProduto(self):
        self.prod = Produtos()

        self.prod.nome = self.nome.get()
        self.prod.fornecedor = self.fornecedor.get()
        self.prod.preco = self.preco.get()
        self.prod.marca = self.marca.get()

        self.msg["text"] = self.prod.insertUser()

        self.idproduto.delete(0, END)
        self.nome.delete(0, END)
        self.fornecedor.delete(0, END)
        self.preco.delete(0, END)
        self.marca.delete(0, END)
        
    def alterarProduto(self):
        self.prod = Produtos()

        self.prod.idproduto = self.idproduto.get()
        self.prod.nome = self.nome.get()
        self.prod.fornecedor = self.fornecedor.get()
        self.prod.preco = self.preco.get()
        self.prod.marca = self.marca.get()

        self.msg["text"] = self.prod.updateUser()

        self.idproduto.delete(0, END)
        self.nome.delete(0, END)
        self.fornecedor.delete(0, END)
        self.preco.delete(0, END)
        self.marca.delete(0, END)

    def excluirProduto(self):
        self.prod = Produtos()

        self.prod.idproduto = self.idproduto.get()

        self.msg["text"] = self.prod.deleteUser()

        self.idproduto.delete(0, END)
        self.nome.delete(0, END)
        self.fornecedor.delete(0, END)
        self.preco.delete(0, END)
        self.marca.delete(0, END)

        



root = Tk()
Aplicacao(root)
root.mainloop()

