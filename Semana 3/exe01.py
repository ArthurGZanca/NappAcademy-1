import csv


def find_subtring_credit_card(lista, parametro='322'):
    for l in lista:
        if parametro in l[2]:
            lista2 = []
            lista2.append(l)
            print (lista2)


def carregar_arquivo(path):
    fp = open(path)
    csv_reader = csv.reader(fp)
    for l in csv_reader:
        print(l)

    local_list = []
    with open(path, newline='\n') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for line in reader:
            local_list.append(line)
    return local_list


if __name__ == "__main__":
    path = 'usernames.csv'
    lista = []
    lista = carregar_arquivo(path)
    find_subtring_credit_card(lista)
    find_subtring_credit_card(lista, '222')