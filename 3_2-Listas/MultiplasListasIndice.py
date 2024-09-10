equipamentos = []
valores = []
seriais = []
departamentos = []
resposta = "S"

while resposta == "S":
    equipamentos.append(input("Equipamentos: "))
    valores.append(float(input("Valores: ")))
    seriais.append(input("Seriais: "))
    departamentos.append(input("Departamento: "))
    resposta = input("Digite \"S\" para continuar: ").upper()
    
for indice in range(0, len(equipamentos)):
    print("Equipamentos: ", (indice+1))
    print("Nome.........: ", equipamentos[indice])
    print("Valor........: ", valores[indice])
    print("Serial.......: ", seriais[indice])
    print("Departamento........: ", departamentos[indice])