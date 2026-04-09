print ('digite dois valores inteiros separados por um operador +,-,* ou /')
x = input()
if '+' in x:
    a = x.split('+')
    n1 = int(a[0])
    n2 = int(a[1])
    print(f'O resultado da operação é {n1+n2}')

if '-' in x:
    a = x.split('-')
    n1 = int(a[0])
    n2 = int(a[1])
    print(f'O resultado da operação é {n1-n2}')

if '*' in x:
    a = x.split('*')
    n1 = int(a[0])
    n2 = int(a[1])
    print(f'O resultado da operação é {n1*n2}')

if '/' in x:
    a = x.split('/')
    n1 = int(a[0])12 
    n2 = int(a[1])
    print(f'O resultado da operação é {n1/n2}')
   