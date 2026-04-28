class Viagem():
    def __init__(self, r, d, l):
        self.set_rumo(r)
        self.set_distancia(d)
        self.set_litros(l)

    def set_rumo(self,v):
        if len(v) >= 4: self.__r = v
        else: raise ValueError()

    def set_distancia(self,v):
        if v >= 0: self.__d = v
        else: raise ValueError()

    def set_litros(self,v):
        if v >= 0: self.__l = v
        else: raise ValueError()
    
    def get_rumo(self):
        return self.__d

    def get_distancia(self):
        return self.__d
    
    def get_litros(self):
        return self.__l
    
    def calc_consumo(self):
        return self.__d / self.__l
    
    def __str__(self):
        return f"destino: {self.__r} | distancia: {self.__d}| litros: {self.__l} | a media de litros gastos é de {self.calc_consumo():.2f}"
    
class UI:
    @staticmethod
    def main():
        op = 0
        while op != 9:
            op = UI.menu()
            if op == 1: UI.consumo()
        print("fim")
    @staticmethod
    def menu():
        print("Escolha uma opção: 1-consumo medio, 2- fim")
        op = int(input("Escolha uma opção: "))
        return op
    
    @staticmethod
    def consumo():
        r = input("Qual destino? ")
        d = float(input("Qual a distancia "))
        l = float(input("qual a quantidade de litros "))
        x = Viagem(r, d ,l)
        print(x)

UI.main()





