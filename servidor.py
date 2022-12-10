import socket
import threading
from alg_busca_sig_dicio import buscaSignificado


def main():

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #IPV4 e TCP 

    try:
        server.bind(('localhost', 60000)) #vinculado host e porta
        server.listen() #servidor escutando
    except:
        print('Não foi possível iniciar o servidor.')

    while True:
        try:
            client, addr = server.accept()

            thread = threading.Thread(target=escutandoCliente, args=[client])
            thread.start()

        except:
            pass


def escutandoCliente(client):
    
    while True:
        try:
            msg = client.recv(1024)
            print(msg.decode())
            resultado = buscaSignificado(msg.decode())
            client.send(resultado.encode('utf-8'))
        except:
            pass


main()
