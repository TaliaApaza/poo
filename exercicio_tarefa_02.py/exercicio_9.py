print("Digite algo com espaço pliss, tenkiu, next")
t = input()
palavras = t.split()#(divisão de palavras de acordo com o que foi informado ex: (/))
for x in palavras:
     x = x[::-1]# pontinhos(inicio e fim) -1(passo)
     print(x)
