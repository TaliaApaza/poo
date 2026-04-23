print("digite três valores")
a = int(input())
b = int(input())
c = int(input())
d = int(input())
if a > b: a,b = b,a 
if a > c: a,c = c,a
if a > d: b,c = c,b
if b > c: b,c= c,b
if b > d: b,d = d,b
if c> d: c,d= d,c
print(a, b, c, b)

