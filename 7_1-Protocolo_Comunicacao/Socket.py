import socket
resp = "S"
while(resp == "S"):
    url = input("Digite uma url: ")
    ip = socket.gethostbyname(url)
    print("O IP`referente à url informada é: ", ip)
    resp= input("Digite <S> para continuar: ").upper()

# Portas disponibilizadas nos serviços abaixo
print(socket.getservbyname("domain"))
print(socket.getservbyname("http"))
print(socket.getservbyname("ftp"))