import socket
from tkinter import *
from tkinter import Button

def receberMensagem(txt, client):
    try:
        msg = client.recv(1024).decode('utf-8')
        print('\nMensagem recebida do SERVIDOR: ' + msg)
        txt["text"] = msg
    except:
        print('Não foi possível permanecer conectado no servidor.')
        client.close()


def enviarMensagem(campo, client):
    try:
        msg = campo.get()
        print('\nCLIENTE: Mensagem prestes a ser enviada:' + msg)
        client.send(msg.encode('utf-8'))
    except:
        print('Não foi possível enviar sua mensagem.')


def printaResultado(campo, txt, client):
    enviarMensagem(campo, client)
    receberMensagem(txt, client)


def aplicacao():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client.connect(('localhost', 60000))
    except:
        return print('Não foi possível se conectar ao servidor.')

    print('\nConectado ao servidor')

    root = Tk()
    root.title("Dicionário")
    root.geometry('500x250')


    campo = Entry(root, width=35)
    campo.grid(row=0, column=1, padx=10, pady=10)

    botao = Button(root, text="Traga-me o significado", fg="white", bg="green", 
                   command=lambda: printaResultado(campo, txt_resultado, client))
    botao["width"] = 30
    botao.grid(row=1, column=1, padx=5, pady=5)


    txt_resultado = Label(root, text='', wraplength=500)
    txt_resultado["font"] = ("Arial", "10")
    txt_resultado.grid(row=2, column=1, padx=5, pady=5)
    #txt_resultado.grid(column=0, row=3, padx=10, pady=30)



    root.mainloop()


aplicacao()






