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
    lista_time = [] # para criar uma lista geral, é preciso cria- la na class UI
    lista_jogador = []
    @staticmethod
    def main():
        op = 0
        while op != 12:
            op = UI.menu()
            if op == 1: UI.inserir_time()
            if op == 2: UI.listar_time()
            if op == 3: UI.atualizar_time()
            if op == 4: UI.excluir_times()
            if op == 5: UI.inserir_jogador()
            if op == 6: UI.listar_jogadores()
            if op == 7: UI.atualizar_jogador()
            if op == 8: UI.excluir_jogador()
            if op == 9: UI.transferir_um_jogador()
            if op == 10: UI.listar_jogadores_time()
            if op == 11: UI.sair()
    @staticmethod
    def menu():
        print("Escolha uma opção: 1-inserir time, 2- listar time 3- atualizar time 4-excluir times, 5-inserir jogador, 6- listar jogadores 7- atualizar jogador, 8-excluir jogador 9-transferir um jogador, 10- sair ")
        op = int(input("Escolha uma opção: "))
        return op
    @staticmethod
    def inserir_time():
        id = int(input("Informe o id do time que será inserido "))
        n = input("Informe o nome do time")
        eft = input("informe o estado onde ele foi constituido ")
        x = Time(id, n, eft)
        UI.lista_time.append(x)
        print(x)
    @staticmethod
    def listar_time():
        for time in UI.lista_time:
            print(time)

    @staticmethod
    def atualizar_time():
        id_atualizar=int(input("informe o id do time que deseja atualizar"))
        for time in UI.lista_time:
            if time.get_id() == id_atualizar: # vai especificar o item que eu quero da lista(lembrando que get guarda o item da lista)
                nome_novo = input("Informe o novo nome a ser usado ou se não quiser alterar repita o mesmo nome: ")
                nome_estado = input("Informe o novo nome de estado a ser usado ou se não quiser alterar repita o mesmo nome: ")
                time.set_nome(nome_novo)
                time.set_estado(nome_estado)
                print("Atualizado") 
            print(time)
    @staticmethod
    def excluir_times():
        id_excluir = int(input("informe o id do time que deseja excluir"))
        for time in UI.lista_time:
            if time.get_id() == id_excluir: 
                UI.lista_time.remove(time)
                print("Excluido") 
            print(time)
    @staticmethod
    def inserir_jogador():
        id_j = int(input("Informe o id do jogador que será inserido: "))
        id = int(input("Informe o id do time do jogador: "))
        nome_j = input("informe o nome do jogador: ")
        camisa = int(input("informe a camisa do jogador: "))
        x = Jogadores(id_j, id, nome_j, camisa)
        UI.lista_jogador.append(x)
        print(x)
    @staticmethod
    def listar_jogadores():
        for jogador in UI.lista_jogador:
            print(jogador)
    
    @staticmethod
    def atualizar_jogador():
        id_atualizar = int(input("Informe o id do jogador que terá os dados atualizados: "))
        for jogador in UI.lista_jogador:
            if jogador.get_id_jogadores() == id_atualizar:
                id_novo_time = int(input("informe o novo id do time caso o jogador tenha mudado de time: "))
                camisa_novo = int(input("informe o nova camisa do jogador caso o jogador a tenha mudado: "))
                jogador.set_id(id_novo_time)
                jogador.set_camisa(camisa_novo)
            print(jogador)

    @staticmethod
    def excluir_jogador():
        id_excluir_j = int(input("Informe o id do jogador que será excluido"))
        for jogador in UI.lista_jogador:
            if jogador.get_id_jogadores() == id_excluir_j:
                UI.lista_jogador.remove(jogador)
                print("jogador removido")

            print(jogador)

    @staticmethod
    def transferir_um_jogador():
        id_atualizar = int(input("Informe o id do jogador que terá os dados atualizados: "))
        for jogador in UI.lista_jogador:
            if jogador.get_id_jogadores() == id_atualizar:
                id_novo_time = int(input("informe o novo id do time caso o jogador tenha mudado de time: "))
                jogador.set_id(id_novo_time)
                print("Jogador transferido")
            print(jogador)

    @staticmethod
    def listar_jogadores_time():
        id_igual = int(input("Informe o id dos jogadores para sabermos se são do mesmo time: "))
        for jogador in UI.lista_jogador:
            if jogador.get_id() == id_igual:
                print(jogador)
    @staticmethod
    def sair():
        print("Fim")
            
UI.main()

 

        