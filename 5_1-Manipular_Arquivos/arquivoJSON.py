import json

dicionario = {
    "CHAVES": ["CHAVES DO 8", "14/04/2017", "RECEP_01"],
    "QUICO": ["QUICO FOLRES", "24/04/2017", "RAIOX_02"],
    "FLORINDA": ["DONA FLORINDA", "18/04/2017", "RECEP_02"]
}
#print(dicionario)
with open("bd.json", "w") as json_file:
        json.dump(dicionario, json_file)