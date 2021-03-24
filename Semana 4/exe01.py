
from datetime import datetime
import locale

#configuracoes do usuario

locale.setlocale(locale.LC_ALL, "")

hoje=datetime.today()

anoAtual= hoje.strftime("%Y")
mesAtual= hoje.strftime("%m")
diaAtual= hoje.strftime("%d")

dataNascimento = []

print ("Digite sua data de nascimento no formato: dia<ENTER>mes<ENTER>ano<ENTER> ")
print (" Para mes digite apenas 1 e nao 01, 2 e nao 02\n1-Janeiro\n2-Fevereiro\n3-Março\n4-Abril\n5-Maio\n6-Junho\n7-Julho\n8-Agosto\n9-Setembro\n10-Outubro\n11-Novembro\n12-Dezembro ")
print
print ("Data de Nascimento: ")

dia=input()
mes=input()
ano=input()

dataNascimento.append(dia)
dataNascimento.append(mes)
dataNascimento.append(ano)

print ("Data de Nascimento: ", dataNascimento, "\n")

#Converte a data para inteiro

anoAtual=int(anoAtual)
mesAtual=int(mesAtual)
diaAtual=int(diaAtual)

# Verifica a idade do usuario

idade = anoAtual-int(dataNascimento[2])

if mesAtual > int(dataNascimento[1]):
   idade=idade

elif int(dataNascimento[1]) == mesAtual and diaAtual >= int(dataNascimento[0]):
   idade=idade

else:
   idade= idade-1


quantidadeAnosBissextos= idade/4

idadeEmDias=(idade*365)+quantidadeAnosBissextos

print ("Sua idade em dias:",idadeEmDias,)