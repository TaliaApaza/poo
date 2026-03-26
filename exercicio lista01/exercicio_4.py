print("difite uma sequencia de números separados por vírgula")
a=input()
x= a.split(",")
soma= 0
for i in x:
    soma = soma + int(i)# int converte a string em número
                    # i será cada item da lista que foi dividida
print(soma) 

