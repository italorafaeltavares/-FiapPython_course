# with open("teste.txt", "r") as arquivo:
#     conteudo = arquivo.read()

with open("teste.txt", "w") as arquivo:
    arquivo.write("Nunca foi tão fácail criar um arquivo.")

# with open("teste.txt", "w") as arquivo:
#     arquivo.write("Continuação do texto.")

with open("teste.txt", "a") as arquivo:
    arquivo.write("\n""Continuação do texto.")