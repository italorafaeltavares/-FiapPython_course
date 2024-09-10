nome = input("Digite o nome: ")
idade = int(input("Digite a idade: "))

if idade >= 65:
    print("O paciente {} possui atendimento prioritário".format(nome))
else:
    print("O paciente {} possui não atendimento prioritário".format(nome))    