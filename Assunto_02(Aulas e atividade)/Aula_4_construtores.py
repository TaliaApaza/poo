class Triangulo():
    def __init__(self, b, h):#parametros são os que estão depois do "self""
        self.__b = 0
        self.__h = 0
    def __str__(self):#proprio para texto(é uym metodo magico(se indentifica atraves do "__"))
        return f"Olá, eu sou um TRiangulo, minha base é {self.__b} minha altura é {self.__h}"

x = Triangulo(10, 20)
print(x)