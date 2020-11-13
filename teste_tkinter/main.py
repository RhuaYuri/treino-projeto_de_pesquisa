import tkinter
from window2 import menu

def GET():
    global userbox, passbox, error
    S1 = userbox.get()
    S2 = passbox.get()

    if (S1 == "Yuri" and S2 =='123'):
        menu()
    elif (S1 == "Bia" and S2 =='321'):
        menu()
    else:
        error = tkinter.Label(bottomframe, text="USUÁRIO OU SENHA INVÁLIDO. DIGITE NOVAMENTE!", fg="red", font="bold")
        error.pack()

def Entry():
    global userbox, passbox, login, topframe, bottomframe, image_1
    root = tkinter.Tk()
    root.geometry("600x600")
    topframe = tkinter.Frame(root)
    topframe.pack()

    bottomframe = tkinter.Frame(root)
    bottomframe.pack()

    heading = tkinter.Label(topframe, text = "SISTEMA BANCÁRIO", bg='white', fg='orange', font='arial 16 bold italic')
    
    username = tkinter.Label(topframe, text = "Usuário :")
    userbox = tkinter.Entry(topframe)

    password = tkinter.Label(bottomframe, text = "Senha :")
    passbox = tkinter.Entry(bottomframe)

    login = tkinter.Button(bottomframe, text="LOGIN", font='arial 8 bold', command=GET)

    root.wm_iconbitmap(r'C:\\Users\\rhuan\Desktop\\arquivos_da_bolsa\\Projeto\\python\\projeto_de_pesquisa\\files\sistema_bancario\\icone\\favicon.ico')
    image = tkinter.PhotoImage(file="C:\\Users\\rhuan\Desktop\\arquivos_da_bolsa\\Projeto\\python\\projeto_de_pesquisa\\files\sistema_bancario\\img\\favicon.png")
    image=image.subsample(1,1)
    labelimg = tkinter.Label(image=image, height="300", width="500")
    labelimg.pack()
    heading.pack()
    username.pack()
    userbox.pack()
    password.pack()
    passbox.pack()
    login.pack()
    root.title("Sistema Bancário : LOGIN :")
    root.mainloop()

Entry()
    