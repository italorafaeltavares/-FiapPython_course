from socket import *

servidor = "127.0.0.1"                          # Define ip do servidor a conectar
porta = 43210                                   # Define a porta do servidor a conectar

msg = bytes(input("Digite algo: "),'utf-8')     # Conversão do conteúdo em bytes utilizando a funcao bytes()
obj_socket=socket(AF_INET, SOCK_STREAM)         # Criação do Objeto socket por meio da função socket() | AF_INET: identifiar por host ou ip
obj_socket.connect((servidor, porta))           # Conexão com o servidor por meio da função connect()
obj_socket.send(msg)                            # Enviar mensagem utilizando o método send()
resposta = obj_socket.recv(1024)                # Resposta retornada 
print("Recebemos: ", resposta)
obj_socket.close()                              # Fecha a conexão
