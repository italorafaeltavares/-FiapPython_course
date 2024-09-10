import json # Importa o modulo JSON
import os   # Importa o modulo OS

# inventario={} Criar o iventário em forma de dicionário vazio

if os.path.exists("inventario_json.json"):
    # Verificar se o arquivo exite
    with open("inventario_json.json", "r") as arq_json: 
    # Utiliza o arquivo inventario_json para acressenatar o dados
        inventario = json.load(arq_json)
else: # Cria o arquivo caso não exista
    inventario = {}


opcao = int(input("Digite: <1> para registrar ativo"
                " <2> para exibir ativos armazenados: "))
while opcao > 0 and opcao < 3:
    if opcao == 1:
        resp ="S"
        while resp == "S":
            inventario[input("Digite o número patrimonial: ")] = [
                input("Digite a data da última atualização: "),
                input("Digite a descrição: "),
                input("Digite o departamento: ")]
            resp = input("Digite <S> para continuar: ").upper()
            with open("inventario_json.json", "w") as arq_json:
                json.dump(inventario, arq_json)
            print("JSON gerado!!!!")

    elif opcao == 2:
        with open("inventario_json.json", "r") as arq_json:
            resultado = json.load(arq_json)
            for chave, dado in resultado.items():
                print("Data.........: ", dado[0])
                print("Descrição....: ", dado[1])
                print("Departamento.: ", dado[2])
        
    opcao = int(input("Digite: <1> para registrar ativo"
                " <2> para exibir ativos armazenados: "))