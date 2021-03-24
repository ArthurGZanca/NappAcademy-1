from datetime import datetime, timedelta
import locale

locale.setlocale(locale.LC_ALL, "")

# Atribui, Formata e Informa a data Atual
Data_atual = datetime.today() 
hoje = Data_atual.strftime('%d/%m/%y %H:%M')
print()
print('Data de Atual é: {} ' .format(hoje))

# Soma as 2 semanas e 3 horas à data atual
NovaData = datetime.today() + timedelta(days=14, hours=3)
DataFinal  = NovaData.strftime('%d/%m/%y %H:%M')

#Informa a nova data daqui a 2 semanas 
print()
print('E daqui a duas semanas e 3 horas será: {}'.format(DataFinal))
print()



