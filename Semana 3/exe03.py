import csv


def find_born_in(lista, birth_year='1996'):
    for l in lista:
        if l[4].startswith(birth_year):
            print (l)

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
    #find_born_in(lista)
    find_born_in(lista, '1982')