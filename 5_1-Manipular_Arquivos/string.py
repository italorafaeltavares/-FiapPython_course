texto = "Leia e Thor"
        #01234567890
        #10987654321 - 
print(texto[0:4])
print(texto[7:])
print(texto[-4:])
print(texto[::-1])#Inverte toda a String

# 0:4:2
# Inicio | Quantidade a pecorrer | Passos

texto_dois = "Eu amo Python!"
# find()
print(texto_dois.find("o"))
print(texto_dois[texto_dois.find("o")+1:].find("o"))

# split()
print(texto_dois.split(" "))
