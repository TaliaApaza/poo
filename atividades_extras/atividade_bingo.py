import random
class Bingo:
    def __init__(self):
        self.nu_bolas = 0
        self.bolas = []
        self.sorteados = []
    def iniciar(self):
        if self.nu_bolas > 0:
            a = 0
            while a <= self.nu_bolas - 1:
                a += 1
                self.bolas.append(a)
        else: raise ValueError("numero invalido")
    def sortear(self):
        random.shuffle(self.bolas)#embaralha a lista que contem as bolas
        b = self.bolas.pop()#pop para retirar um elemento e b irá amarzenar esses elementos
        self.sorteados.append(b)
        return b
    
    def sorteado(self):
        return self.sorteados
    

class UI:
    @staticmethod
    def main():
        op = 0 #cria a variavel opção
        while op !=
        

