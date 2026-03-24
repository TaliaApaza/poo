class Triangulo:# Classe é um modelo de um triangulo
    # atributo- dados vão ser amarzenados: b - base, h - altura
    def __init__(self):
        self.b = 0
        self.h = 0
    # metodo - calculo que vão ser feitos
    def calc_area(self):
        return self.b * self.h/2
    
x=Triangulo()
print(" informe a base do triangulo")
x.b = float(input())
print(" informe a altura do triangulo")
x.h = float(input())
a = x.calc_area()
print(f"a area do triangulo é{a:.2f}")

y = Triangulo()
print(" informe a base do segundo triangulo")
y.b = float(input())
print(" informe a altura do triangulo")
y.h = float(input())
a = x.calc_area()
print(f"a area do triangulo é{a:.2f}")


print(f"Primeiro Triangulo: base ={x.b}, altura = {x.h}, area ={x. calc_area()}")
