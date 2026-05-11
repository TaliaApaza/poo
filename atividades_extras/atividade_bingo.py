import random
class Bingo:
    def __init__(self):
        self.nu_bolas = 0
        self.bolas = []
        self.sorteados = []
    def iniciar(self):
        if self.nu_bola >= 0:
            a = 0
            while a <= self.nu_bolas:
                a += 1
                self.bolas.append(a)
        else: raise ValueError("numero invalido")
    def sortear(self):
        random.shuffle(self.bolas)#embaralha a lista que contem as bolas
        b = self#pop para retirar um elemento
        self.sorteados.append(b)
        return b
    
    def sorteado(self):
        return self.sorteados

