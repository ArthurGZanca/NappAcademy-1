from matriz_de_dados import list_spend_money

def spend_by_subname(name):
    for lista in list_spend_money:
        if name in lista[0]:
            print(lista)

def sum_by_subname(name):
    soma = 0
    for lista in list_spend_money:
        if name in lista[0]:
            if lista[3] != '':
                soma+= float(lista[3])
                return soma       

if __name__ == "__main__":
    name = 'richardson'
    spend_by_subname(name.title())
    print("a soma é igual a: ")
    print(sum_by_subname(name.title()))
    