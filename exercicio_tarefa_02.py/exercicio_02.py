class Pais:# Classe é um modelo de um triangulo
    # atributo- dados vão ser amarzenados: b - base, h - altura
    def __init__(self):
        self.nome = input("nome do pais: ")
        self.populacao = int(input("população: "))
        self.area = float(input("area: "))

    # metodo - calculo que vão ser feitos
    def calc_densidade(self):
        return self.populacao/ self.area
print("calcular a densidade demografica")

pais_1= Pais()
pais_2= Pais()
pais_3= Pais()
pais_4= Pais()
pais_5= Pais()
pais_6= Pais()
pais_7= Pais()
pais_8= Pais()
pais_9= Pais()
pais_10= Pais()

maior= max(pais_1.calc_densidade(), pais_2.calc_densidade(),pais_3.calc_densidade(),pais_4.calc_densidade(),pais_5.calc_densidade(),pais_6.calc_densidade(),pais_7.calc_densidade,pais_8().calc_densidade,pais_9.calc_densidade(),pais_10.calc_densidade())
if maior==pais_1.calc_densidade():
    pais_maior=pais_1.nome

if maior==pais_2.calc_densidade():
    pais_maior=pais_2.nome


if maior==pais_3.calc_densidade():
    pais_maior=pais_3.nome


if maior==pais_4.calc_densidade():
    pais_maior=pais_4.nome


if maior==pais_5.calc_densidade():
    pais_maior=pais_5.nome


if maior==pais_6.calc_densidade():
    pais_maior=pais_6.nome


if maior==pais_7.calc_densidade():
    pais_maior=pais_7.nome


if maior==pais_8.calc_densidade():
    pais_maior=pais_8.nome


if maior==pais_9.calc_densidade():
    pais_maior=pais_9.nome


if maior==pais_10.calc_densidade():
    pais_maior=pais_10.nome

print(f"pais com maior densidade é{pais_maior}")

