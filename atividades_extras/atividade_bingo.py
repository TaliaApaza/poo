import random
class Bingo:
    def __init__(self):
        self.nu_bolas = 0
        self.bolas = []
        self.sorteados = []
    def iniciar(self):
        if self.nu_bola >= 0:
            a = 0
            while 1 <= self.nu_bolas:
                a += 1
                self.bolas.append(a)
    def sortear(self):
        b = random.shuffle(self.bolas)
        self.sorteados.append(b)
        return b
    
    def sorteado(self):
        return self.sorteados

