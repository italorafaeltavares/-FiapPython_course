from socket import *

servidor="127.0.0.1"
porta=43210

obj_socket = socket(AF_INET, SOCK_STREAM)   # Criação do Objeto socket por meio da função socket | TCP
obj_socket.bind((servidor,porta))           # Associação do objeto socket com o servidor e porta
obj_socket.listen(2)                        # Definir o máximo de clientes para utilizar o servidor

print("Aguardando cliente....")

while True:
    con, cliente = obj_socket.accept()      # Aguarda concexao do cliente
    print("Conectado com: ", cliente)
    while True:
        msg_recebida = str(con.recv(1024))
        print("Recebemos: ", msg_recebida)
        msg_enviada = b'Olah cliente'
        con.send(msg_enviada)
        break
    con.close()