class Pais():
    def __init__(self, n, p, a):
        self.set_nome(n)
        self.set_populacao(p)
        self.set_area(a)

    def set_nome(self,v):
        if len(v) >= 3: self.__n = v
        else: raise ValueError()

    def set_populacao(self,v):
        if v >= 0: self.__p = v
        else: raise ValueError()

    def set_area(self,v):
        if v >= 0: self.__a = v
        else: raise ValueError()

    def get_nome(self):
        return self.__n

    def get_populacao(self):
        return self.__p

    def get_area(self):
        return self.__a
    
    def calc_densidade(self):
        return self.__p / self.__a
    
    def __str__(self):
        return f"Nome do pais: {self.__n}| População: {self.__p} | Area: {self.__a} | Densidade: {self.calc_densidade()}"

class UI:
    @staticmethod
    def main():
        op = 0
        while op != 9:
            op = UI.menu()
            if op == 1: UI.calculo()
        print("fim")
    @staticmethod
    def menu():
        print("Escolha uma opção: 1-calculo medio, 2- fim")
        op = int(input("Escolha uma opção: "))
        return op
    
    @staticmethod
    def calculo():
        n = input("Informe o nome do Pais ")
        p = float(input("A população "))
        a = float(input("e a área "))
        x = Pais(n, p, a)
        print(x)

UI.main()