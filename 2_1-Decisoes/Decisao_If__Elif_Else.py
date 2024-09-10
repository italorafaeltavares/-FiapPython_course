nome = input("Digite o nome: ")
idade = int(input("Digite a idade: "))
doenca_infectocontagiosa = input("Suspeita de doença infecto-contagiosa? ").upper()

if idade >= 65:
    print("O paciente {} possui atendimento prioritário".format(nome))
elif doenca_infectocontagiosa == "SIM":
    print("O paciente {} deve ser direcionado para a sala de espera reservada".format(nome))
else:
    print("O paciente {} possui não atendimento prioritário e pode aguaradar na sala comum!".format(nome))    