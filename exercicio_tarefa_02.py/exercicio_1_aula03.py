class Circulo:# Classe é um modelo de um triangulo
    # atributo- dados vão ser amarzenados: r -  raio do circulo
    def __init__(self):
        self.r = 0
    # metodo - calculo que vão ser feitos
    def calc_area(self):
        return (self.r ** 2) * 3,14
    def calc_circunferencia(self):
        return self.r * (3,14 * 2)# 2 vezes pi vezes Raio

x=Circulo
print(" informe o raio do circulo")
x.r = float(input())
a = x.calc_area()
b= x.calc_circunferencia
print(f"a area do circulo é {a:.2f}")
print(f"a circuferencia do circulo é {b:.2f}")


