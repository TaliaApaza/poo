class Retangulo():
    def __init__(self, b, h):
        self.set_baser(b)
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
    
    def get

        