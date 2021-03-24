import csv
import json


def carregar_dicionario_websites(path):
    fp =open(path)
    csv_reader = csv.reader(fp)
    lista = []
    for l in csv_reader:
        contato = {l[1] : l[4]}
        lista.append(contato)
    return lista



if __name__ == "__main__":
    path = 'names.csv'
    dicionario = {}
    dicionario = carregar_dicionario_websites(path)
    json_object = json.dumps(dicionario, indent=4)
    print(json_object)