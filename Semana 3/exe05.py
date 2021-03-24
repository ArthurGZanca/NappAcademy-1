import csv


def find_born_in_month_and_gender(lista, paramether='03', gender='F'):
    p = int(paramether)
    if p == 1:
        menos1 = '12'
    if p > 9 and p <= 12:
        menor = p - 1
        menos1 = str(menor)
    if p < 10 and p > 1:
        menor = p - 1
        menos1 = '0' + str(menor)
    for l in lista:
        if gender in l[5]:
            if ('-' + menos1 + '-') in  l[4]:
                print (l)


def carregar_arquivo(path):
    fp = open(path)
    csv_reader = csv.reader(fp)
    #for l in csv_reader:
     #print(l)

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
    find_born_in_month_and_gender(lista)
    find_born_in_month_and_gender(lista, '01')
    find_born_in_month_and_gender(lista, '01', 'M')