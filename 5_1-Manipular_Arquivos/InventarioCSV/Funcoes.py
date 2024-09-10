def chamarMenu():
    opcao = int(input("Digite: "
                    "<1> para registrar ativo "
                    "<2> para persitir em arquivo "
                    "<3> para exibir ativos armazenados: " ))
    return opcao

def registrar(dicionario):
    resp ="S"
    while resp == "S":
            dicionario[input("Digite o número patrimonial: ")]=[
            input("Digite a data da última atualização: "),
            input("Digite a descrição: ").upper(),
            input("Digite o departamento: ").upper()]
            resp=input("Digite <S> para continuar: ").upper()

def persitir(dicionario):
    with open("inventario.csv", "a") as inv:
            for chave, valor in dicionario.items():
                inv.write(chave + ";" + valor[0] + ";" + 
					valor[1] + ";" + valor[2] +"\n")
    return print("Persistido com sucesso!")


def exibir():
    with open("inventario.csv", "r") as inv:
        linhas = inv.readlines()
    return linhas            