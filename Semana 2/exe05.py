from massa_de_dados_situacao_teste import lista_pessoas

# Função 1
def lista_simples(lista_pessoas):
    lista =[]
    for item in lista_pessoas:
        if type(item[4]) is tuple:
            lista.append((item[0], item[4]))
        else:
            lista.append((item[0], item[5]))
    return lista

# Função 2
def lista_simples2(lista_pessoas):
    lista2 =[]
    for item in lista_pessoas:
        if item == ' ':
            lista2.append((item))
    return lista2

# Função 3
def lista_simples3(lista_pessoas):
    lista =[]
    for item in lista_pessoas:
        if type(item[4]) is tuple:
            lista.append((item[0], item[4]))
        else:
            lista.append((item[0], item[5]))
    return lista

# Teste 1
pedaco = slice(0, 2)
entrada = lista_pessoas[pedaco]
saida_esperada = [('daniellemosley',('33.93113', '117.54866')),('rhodesrichard',('39.00622', '-77.4286'))]
saida = lista_simples(entrada)
assert(saida == saida_esperada)

# Teste 2
entrada2 = []
saida_esperada2 = []
saida2 = lista_simples2(entrada2)
assert(saida2 == saida_esperada2)

# Teste 3
entrada3 = "string"
saida_esperada3 = []
saida3 = lista_simples3(entrada3)
assert(saida3 == saida_esperada3)





