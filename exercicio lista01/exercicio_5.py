class Pais:# Classe é um modelo de um triangulo
    # atributo- dados vão ser amarzenados: b - base, h - altura
    def __init__(self):
        self.nome = 0
        self.populacao = 0
        self.area = 0

    # metodo - calculo que vão ser feitos
    def calc_densidade(self):
        return self.populacao/ self.area
# x vai servi como referencia do objeto criado pela instruç~çao triangulo
# funciona como um link em html
x=Pais()
print(" informe o nome do pais")
x.nome = input()
print(" informe a população")
x.populacao = float(input())
print(" informe a area em km²")
x.area = float(input())
a = x.calc_densidade()
print(f"A densidade demográfica do {x.nome} é de {a:.2f} hab/km2")




