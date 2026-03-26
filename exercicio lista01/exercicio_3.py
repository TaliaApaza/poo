print("digite uma frase com números")
a= input()
soma = 0
for i in a:
    if i >= '0' and i <= '9':
        soma = soma + int(i)
print(soma)