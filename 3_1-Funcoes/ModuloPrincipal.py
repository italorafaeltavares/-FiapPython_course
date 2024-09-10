from IdentificadorDeFuncoes import *

minhaLista = []
print("Prenchendo")
prencherInventario(minhaLista)
print("Exibindo")
exibirInventario(minhaLista)


print("Pesquisando")
localizaPorNome(minhaLista)
print("Alternado")
depreciacaoPorNome(minhaLista, 20)


print("Excluindo")
excluirPorSerial(minhaLista)
exibirInventario(minhaLista)

print("Resmindo")
resumirValores(minhaLista)