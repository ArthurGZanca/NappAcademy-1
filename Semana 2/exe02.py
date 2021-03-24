from matriz_de_dados import list_spend_money
 

def spend_by_gender(genero):
      for lista in list_spend_money:
        if genero == lista[2]:
            print(lista)

def sum_by_gender(genero):
     soma = 0
     for lista in list_spend_money:
        if genero == lista[2]:
            if lista[3] != '':
                soma+= float(lista[3])
     return soma       

if __name__ == "__main__":
    genero = 'F'
    spend_by_gender(genero)
    print("a soma é igual a: ")
    print(sum_by_gender(genero))