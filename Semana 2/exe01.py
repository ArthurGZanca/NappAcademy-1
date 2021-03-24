from matriz_de_dados import list_spend_money    

#registro = ('Orlando Saraiva ', 'prof.orlando', 'M', 100.00)
#registro[0] => String com Nome e sobrenome
#registro[1] => String com username
#registro[2] => string com o gênero . ‘F’ ou ‘M’
#registro[3] => Float com o valor do gasto


def spend_by_login(login):
    for lista in list_spend_money:
        if login == lista[1]:
            print(lista)

def sum_by_login(login):
    soma = 0
    for lista in list_spend_money:
        if login == lista[1]:
            if lista[3] != '':
                soma+= float(lista[3])
    return soma       

if __name__ == "__main__":
    login = 'william40'
    spend_by_login(login)
    print('A soma total é: ')
    print(sum_by_login(login))



