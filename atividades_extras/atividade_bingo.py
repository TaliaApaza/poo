import random
class Bingo():
    def __init__(self):
        self.nu_bolas = 0
        self.bolas = []
        self.sorteados = []
    def iniciar(self):
        if self.nu_bolas > 0:
            for a in range(1, self.nu_bolas + 1):#inicio sendo 1 e o fim sendo o valor informado mais 1
                self.bolas.append(a)
        else: raise ValueError("numero invalido")
        return self.bolas
    
    def sortear(self):
          bola = random.choice(self.bolas)#retorna o valor sorteados
          self.sorteados.append(bola)
          self.bolas.remove(bola)
          return bola
    def sorteado(self):
        return self.sorteados
    

class UI:
    x = Bingo()#o bingo se torna geral e não é necessario chala novamente
    @staticmethod
    def main():
        op = 0 #cria a variavel opção
        while op != 4:
            op = UI.menu()
            if op ==1: UI.iniciar_jogo()
            if op ==2: UI.sortear_num()
            if op == 3: UI.num_sorteados()
        print("fim")
    @staticmethod
    def menu():
        print("Escolha uma opção: 1-iniciar novo jogo, 2-sortear um número, 3-listar numeros sorteados")
        op = int(input("informe a opção: "))
        return op
    @staticmethod
    def iniciar_jogo():
        UI.x.nu_bolas = int(input("informe o numero de bolas"))
        print(f"o total de bolas a serem sorteadas é: {UI.x.iniciar()}")
    @staticmethod
    def sortear_num():
        print(f"numero sorteado: {UI.x.sortear()}")
    @staticmethod
    def num_sorteados():
        print(f"numeros sorteados: {UI.x.sorteado()}")

UI.main()
        




        

