basedados = []
with open("iris.data", "r") as arquivo:
    for registro in arquivo.readlines():
        basedados.append(registro.strip(","))

print(basedados[0][0])