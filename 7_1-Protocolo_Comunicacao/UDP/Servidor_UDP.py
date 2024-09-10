from socket import *

servidor = "127.0.0.1"
porta = 43210

obj_socket = socket(AF_INET, SOCK_DGRAM)              # DGRAM determina usar o protocolo UDP
obj_socket.bind((servidor,porta))                     # bind do server com o endereço e porta especificada
print("Servidor pronto....")

while True:
    dados, origem = obj_socket.recvfrom(65535)         # Aguardando dados com tamanho limitado de 65535
    print("Origem..........:", origem)
    print("Dados recebidos.:", dados.decode())         # Converte bytes em string metodo decode()
    resposta = input("Digite a resposta: ")
    obj_socket.sendto(resposta.encode(), origem)       # Converte string em bytes metodo encode()
    resposta = input("Digite a resposta: ")
    
obj_socket.close()    
