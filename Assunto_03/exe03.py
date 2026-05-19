from datetime import datetime

s =  input("Informe sua data de nascimento no formato de dd/ mm / aaaa")
data = datetime.strptime(s, "%d/%m/%Y")
print(data)
print(data.strftime("%d/&m/%Y"))

# strptime - passa uma string para date
# strftime - passa uma string para datetime

x = int(input("Informe o numero"))
d = datetime.strptime(input("informe um data: ", "%d/&m/%Y" ))
