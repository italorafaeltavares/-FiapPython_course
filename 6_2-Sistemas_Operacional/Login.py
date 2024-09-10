import getpass

usuario = input("Digite o usuário: ").upper()
senha = getpass.getpass("Digite a senha: ")

if usuario == "BITMED" and senha == "FiAp1222":
    print("Usuário logado")
else:
    print("Login Negado")
    
# usuario=input("Digite o usuário: ").upper()
# senha= input("Digite a senha: ")

# if usuario == "BITMED" and senha == "FiAp1222":
#     print("Usuário logado")
# else:
#     print("Login Negado")    