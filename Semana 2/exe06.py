
lista_antiga = [('Pessoa1', 20), ('Pessoa 2', 21), ('Pessoa 3', 22)]
lista_nova = [('Pessoa1', 20), ('Pessoa 2', 21), ('Pessoa 3', 22), ('Pessoa 4', 23), ('Pessoa 5', 24)]

def extrair_novos_registros(antigo,novo):
    if lista_nova in lista_antiga:
        print(lista_nova[3:])
    return print(lista_nova[3:])


lista_novos_registros = extrair_novos_registros(lista_antiga, lista_nova)
lista_novos_registros
[('Pessoa 4', 23), ('Pessoa 5', 24)]








