from datetime import datetime

Bold = '\033[1m'
Bold_end = '\033[0m' 
# Atribui, Formata e Informa a data Atual
hoje = datetime.today().date()

#Data da copa formatada para o formato date
str_Data = '08/07/2014'
date_Data = datetime.strptime(str_Data, '%d/%m/%Y').date()

#Calcula os dias desde o jogo da copa
diferenca = hoje - date_Data

#transforma e formata a data atual em string
hoje_data = datetime.strftime(hoje, '%d/%m/%Y') 

print()
print("De acordo com a data de hoje: {}".format(hoje_data))
print("já se passaram:"
         "\n{} dias "
        "\nDesde o jogo da copa do mundo de 2014 em que o Brasil perdeu de 7 a 1.".format(diferenca.days))
print()
