import tkinter
import tkinter.messagebox



def menu():
    global root1, buttom1, buttom2, buttom3, buttom4, buttom5, buttom6, userbox, passbox, error
    

    root1 = tkinter.Tk()
    root1.geometry("280x350")
    root1.title("Sistema Bancário : MANU :")
    m=tkinter.Label(root1, text="MENU", font='arial 16 bold italic', fg='gray')

    buttom1 = tkinter.Button(root1, text="REGISTAR CLIENTE FÍSICO :", bg='light blue', fg='black')
    buttom2 = tkinter.Button(root1, text="REGISTAR CLIENTE JURÍDICO :", bg='light green', fg='black')
    buttom3 = tkinter.Button(root1, text="COMPRAR PRODUTO :", bg='light blue', fg='black')
    buttom4 = tkinter.Button(root1, text="EXTRATO DA CONTA :", bg='light green', fg='black')
    buttom5 = tkinter.Button(root1, text="AFILIARES :", bg='light blue', fg='black')
    buttom6 = tkinter.Button(root1, text="SAIR :", bg='light green', fg='black')

    m.place(x=75,y=5)
    buttom1.pack(side=tkinter.TOP)
    buttom1.place(x=80,y=50)

    buttom2.pack(side=tkinter.TOP)
    buttom2.place(x=80,y=100)

    buttom3.pack(side=tkinter.TOP)
    buttom3.place(x=80,y=150)

    buttom4.pack(side=tkinter.TOP)
    buttom4.place(x=80,y=200)

    buttom5.pack(side=tkinter.TOP)
    buttom5.place(x=80,y=250)

    buttom6.pack(side=tkinter.TOP)
    buttom6.place(x=80,y=300)
    root1.mainloop()

menu()
    