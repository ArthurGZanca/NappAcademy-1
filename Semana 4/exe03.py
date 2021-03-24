from datetime import datetime
import locale

locale.setlocale(locale.LC_ALL, "")

#Interação com o usuário
nome = input('Digite seu nome: ')

#Pega a data atual, transforma em int, 
Data_atual = datetime.today() 
ano_atual = int(Data_atual.strftime('%Y'))# 4 dígitos Ex: 1998


ano_nasci = int(input('\nDigite o ano em que você nasceu: ')) # 4 dígitos Ex:1998
resposta =  ano_atual - ano_nasci

print("\n", nome ,'você nasceu em', ano_nasci ,'então você têm' ,resposta ,'anos de idade.')