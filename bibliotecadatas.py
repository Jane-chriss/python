from datetime import datetime, date, time, timedelta

data = date(1986, 2, 7)
print(data)

print(data.year)

print(data.month)

print(data.day)

datahoje = datetime.now()
print(datahoje.date())
print(datahoje.time())
print(datahoje.weekday())

#print(datahoje.hour())
#print(datahoje.minute())
#print(datahoje.second())

calendario = datahoje.isocalendar()
print(calendario.week)


def idade (nascimento):
    today = datetime.now()
    return today.year - nascimento.year - ((today.month, today.day) < (nascimento.month, nascimento.day))

def totaldiasvividos (nascimento):
    today = datetime.now()
    return abs ((nascimento - today).days)

def iniciofimsemana():
    if datetime.today().isoweekday() %7-1 <0:
        diainiciodasemana = 7-1
    else:
        diainiciodasemana = datetime.today().isoweekday()%7-1
    datainiciodasemana = datetime.today() - timedelta(days=diainiciodasemana)
    datafimdasemana = datainiciodasemana + timedelta (days=6)


datanascimento = input('informe a sua data de nascimento (dd/mm/aaaa)')
datanascimento = datetime.strptime (datanascimento, '%d/%m/%Y')

print(datanascimento)
print(f'Sua idade é: {idade(datanascimento)}')
print(f'vc ja viveu {totaldiasvividos(datanascimento)} dias abençoados')

iniciofimsemana()


