class Retangulo():
    def __init__(self, b, h):
        self.set_base(b)
        self.set_altura(h)

    def set_base(self, v):
        if v >= 0: self.__b = v
        else: raise ValueError()
    
    def set_altura(self, v):
        if v >=0: self.__h = v
        else: raise ValueError()
    
    def get_base(self):
        return self.__b
    
    def get_altura(self):
        return self.__h
    def calc_area(self):
        return self.__b* self.__h
    
    def __str__(self):#proprio para texto(é uym metodo magico(se indentifica atraves do "__"))
        return f"Olá, eu sou um Triangulo, minha base é {self.__b} minha altura é {self.__h}"

        