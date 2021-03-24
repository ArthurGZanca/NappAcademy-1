from matriz_de_dados import list_spend_money

def spend_by_login(login, limit=1000):
    for lista in list_spend_money:
        if login in lista[1]:
            if limit != '':
                print(lista)

def sum_by_login(login, limit=1000):
    soma = 0
    for lista in list_spend_money:
        if login in lista[1]:
            if lista[3] != '':
                if limit <= float(lista[3]):
                    soma += float(lista[3])
    return soma

if __name__ == "__main__":
    login = 'justin16'
    spend_by_login(login, 1200)
    print('A soma total até 600: ')
    print(sum_by_login(login, 600))
    print('A soma total até 1200: ')
    print(sum_by_login(login, 1200))
    