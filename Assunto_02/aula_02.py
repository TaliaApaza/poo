# Entidade
class Triangulo:
    def __init__(self):
        self.__b = 0.0
        self.__h = 0.0
    def set_base(self, v):
        if v >= 0: self.__b = v
        else: raise ValueError()
    def set_altura(self, v):
        if v >= 0: self.__h = v
        else: raise ValueError()
    def get_base(self):
        return self.__b
    def get_altura(self):
        return self.__h
    def calc_area(self):
        return self.__b * self.__h / 2
class Circulo:
    def __init__(self):
        self.__r = 0.0
        self.__p = 0.0
    def set_raio(self, v):
        if v >= 0: self.__r = v
        else: raise ValueError()
    def set_pi(self, v):
        if v >= 3: self.__p = v
        else: raise ValueError()
    def get_raio(self):
        return self.__r
    def get_pi(self):
        return self.__p
    def calc_area(self):
        return self.__p * self.__r **2
    def calc_circuferencia(self):
        return (2*self.__p)*self.__r

class Viagem:
    def __init__(self):
        self.__d = 0.0
        self.__t = 0.0
    def set_distancia(self, v):
        if v >= 0: self.__d = v
        else: raise ValueError()
    def set_tempo(self, v):
        if v >= 3: self.__t = v
        else: raise ValueError()
    def get_distancia(self):
        return self.__d
    def get_tempo(self):
        return self.__t
    def calc_distancia_media(self):
        return  self.__d/self.__t
    

# Interface com o usuário
class UI:
    @staticmethod
    def main():
        op = 0
        while op != 9:
            op = UI.menu()
            if op == 1: UI.triangulo()
            if op == 2: UI.circulo()
    @staticmethod
    def menu():
        print("1-Triângulo 2-Círculo 3-Viagem 4-Conta Bancária, 5-Ingresso, 9-Fim")
        op = int(input("Escolha uma opção: "))
        return op
    @staticmethod
    def triangulo():
        print("Cálculo da área de um triângulo")
        x = Triangulo()
        x.set_base(float(input("Informe o valor da base: ")))
        x.set_altura(float(input("Informe o valor da altura: ")))
        area = x.calc_area()
        print(f"Um triângulo com base {x.get_base()} e altura {x.get_altura()} tem área = {area}")
    @staticmethod
    def circulo():
        print("Cálculo da área de um circulo")
        x = Circulo()
        x.set_raio(float(input("Informe o valor do raio: ")))
        x.set_pi(float(input("Informe o valor de pi: ")))
        area = x.calc_area()
        circuferencia = x.calc_circuferencia()
        print(f"Um circulo com raio {x.get_raio()} e pi {x.get_pi()} tem área = {area} e circuferencia{circuferencia}")
    @staticmethod
    def viagem():
        x = Viagem()
        x.set_distancia(float(input("Distancia")))
        x.set_tempo(int(input("tempo")))
        distancia_media=  
    @staticmethod
    def conta_bancaria():
    @staticmethod
    def ingresso():  
    @staticmethod
    def fim():  
        

UI.main()