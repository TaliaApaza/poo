class Time():
    def __init__(self, id, n, eft):
        self.set_id(id)
        self.set_nome(n)
        self.set_estado(eft)
    
    def set_id(self, v):
        if v >= 0: self.__id = v
        else: raise ValueError()

    def set_nome(self, v):
        if len(v) >= 0: self.__nome = v
        else: raise ValueError()

    def set_estado(self, v):
        if len(v) >= 3: self.__estado = v
        else: raise ValueError()

    def get_id(self):
        return self.__id
    
    def get_nome(self):
        return self.__nome

    def get_estado(self):
        return self.__estado
    
    def __str__(self):
        return f"id do time: {self.__id} | nome do time: {self.__nome} | Estado do time: {self.__estado}"

class Jogadores():
    def __init__(self, id_j, id, nome_j, camisa):
        self.set_id_jogadores(id_j)
        self.set_id(id)
        self.set_nome_jogador(nome_j)
        self.set_camisa(camisa)

    def set_id_jogadores(self, v):
        if v >= 0: self.__id_jogadores = v
        else: raise ValueError()

    def set_id(self, v):
        if v >= 0: self.__id = v
        else: raise ValueError()

    def set_nome_jogador(self, v):
        if len(v) >= 3: self.__nome_jogadores = v
        else: raise ValueError()

    def set_camisa(self, v):
        if v > 0: self.__camisa = v
        else: raise ValueError()

    def get_id_jogadores(self):
        return self.__id_jogadores
    
    def get_id(self):
        return self.__id

    def get_nome_jogadores(self):
        return self.__nome_jogadores
    
    def get_camisa(self):
        return self.__camisa
    
    def __str__(self):
        return f"id do jogador: {self.__id_jogadores} | id do time: {self.__id} | nome do jogador: {self.__nome_jogadores} | camisa do jogador: {self.__camisa}"
    



class UI:
    @staticmethod
    def main():
        op = 0
        while op != 9:
            op = UI.menu()
            if op == 1: UI.inserir_time()
            if op == 2: UI.listar_time()
            if op == 3: UI.atualizar_time()
            if op == 4: UI.excluir_times()
            if op == 5: UI.inserir_jogador()
            if op == 6: UI.listar_jogadores()
            if op == 7: UI.atualizar_jogador()
            if op == 8: UI.excluir_jogador()
            if op == 9: UI.transferir_um_jogador ()
            if op == 10: UI.sair()
    @staticmethod
    def menu():
        print("Escolha uma opção: 1-inserir time, 2- listar time 3- atualizar time 4-excluir times, 5-inserir jogador, 6- listar jogadores 7- atualizar jogador, 8-excluir jogador 9-transferir um jogador, 10- sair ")
        op = int(input("Escolha uma opção: "))
        return op
    @staticmethod
    def inserir_time():
                n = input("Informe o nome do Pais ")
        p = float(input("A população "))
        a = float(input("e a área "))
        x = Bingo(n, p, a)
        print(x)

        

 

        