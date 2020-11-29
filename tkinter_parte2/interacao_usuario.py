from tkinter import *
class Aplicacao:
    def __init__(self, root):
        self.fonte = ("Arial", "10")
        self.bloco1 = Frame(root)
        self.bloco1["pady"] = 10
        self.bloco1.pack()

        self.bloco2 = Frame(root)
        self.bloco2["padx"] = 20
        self.bloco2.pack()

        self.bloco3 = Frame(root)
        self.bloco3["padx"] = 20
        self.bloco3.pack()

        self.bloco4 = Frame(root)
        self.bloco4["padx"] = 20
        self.bloco4.pack()

        self.titulo = Label(self.bloco1, text="Dados do Usuário")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()

        self.nomeL = Label(self.bloco2, text="None", font=self.fonte)
        self.nomeL.pack(side=LEFT)

        self.nome = Entry(self.bloco2)
        self.nome["width"] = 30
        self.nome["font"] = self.fonte
        self.nome.pack(side=LEFT)

        self.senhaL = Label(self.bloco3, text="Senha", font=self.fonte)
        self.senhaL.pack(side=LEFT)

        self.senha = Entry(self.bloco3)
        self.senha["width"] = 30
        self.senha["font"] = self.fonte
        self.senha["show"] = "*"
        self.senha.pack(side=LEFT)

        self.botao = Button(self.bloco4)
        self.botao["width"] = 15
        self.botao["text"] = "Autenticar Usuário"
        self.botao["font"] = self.fonte
        self.botao["command"] = self.verificarSenha
        self.botao.pack()

        self.msg = Label(self.bloco4, text="", font=self.fonte)
        self.msg.pack()

    def verificarSenha(self):
        usuario = self.nome.get()
        senha = self.senha.get()
        if usuario != "usuarioTeste" or senha != "123":
            self.msg["text"] = "Erro de Usuário"
        else:
            self.msg["text"] = "Usuário Autenticado"

root = Tk()
Aplicacao(root)
root.mainloop()