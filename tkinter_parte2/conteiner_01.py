#Aplicando Conceito de conteiner e mudança do estado do botão
from tkinter import *
class aplicacao:
    def __init__(self, parametro=None):
        self.bloco1 = Frame(parametro)
        self.bloco1.pack()
        self.msg = Label(self.bloco1, text="Primeiro Teste")
        self.msg["font"] = ("Calibri", "10", "italic")
        self.msg.pack()
        self.sair = Button(self.bloco1)
        self.sair["text"] = "Clique Aqui"
        self.sair["font"] = ("Calibri", "10")
        self.sair["width"] = 10
        self.sair["command"] = self.mudarTexto
        self.sair.pack()

    def mudarTexto(self):
        if self.msg["text"] == "Primeiro Teste":
            self.msg["text"] = "Botão Precionado"
        else:
            self.msg["text"] = "Primeiro Teste"

root = Tk()
aplicacao(root)
root.mainloop()
