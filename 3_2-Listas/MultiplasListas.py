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
    
for equipamentos in equipamentos:
    print("Equipamentos: ", equipamentos)