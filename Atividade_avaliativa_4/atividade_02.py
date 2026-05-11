class Playlist():
    def __init__(self, id_p, nome,desc ):
        self.set_id(id)
        self.set_nome(nome)
        self.set_estado(desc)
    
    def set_id(self, v):
        if v >= 0: self.__id = v
        else: raise ValueError()

    def set_nome(self, v):
        if len(v) >= 0: self.__nome = v
        else: raise ValueError()

    def set_descricao(self, v):
        if len(v) >= 3: self.__descricao = v
        else: raise ValueError()

    def get_id(self):
        return self.__id
    
    def get_nome(self):
        return self.__nome

    def get_descricao(self):
        return self.__descricao
    
    def __str__(self):
        return f"id da música: {self.__id} | nome da playlist: {self.__nome} | Descrição da playlist: {self.__descricao}"

class Musica():
    def __init__(self, id_m, titulo, artista, album):
        self.set_id_musicas(id_m)
        self.set_titulo(titulo)
        self.set_nome_artista(artista)
        self.set_album(album)

    def set_id_musica(self, v):
        if v >= 0: self.__id_musica = v
        else: raise ValueError()

    def set_titulo(self, v):
        if len(v) >= 0: self.__titulo = v
        else: raise ValueError()

    def set_nome_artista(self, v):
        if len(v) >= 3: self.__nome_artista = v
        else: raise ValueError()

    def set_album(self, v):
        if v > 0: self.__album = v
        else: raise ValueError()

    def get_id_musica(self):
        return self.__id_musica
    
    def get_titulo(self):
        return self.__titulo

    def get_artista(self):
        return self.__nome_artista
    
    def get_album(self):
        return self.__album
    
    def __str__(self):
        return f"id da música: {self.__id_musica} | titulo da música: {self.__titulo} | nome do artista: {self.__nome_artista} | Album: {self.__album}"
    
class PlayListlem(Playlist, Musica):
    def __init__(self, id, id_p, id_m):
        self.set_id_musica(id_m)
        self.set_id_playlist(id_p)
        self.set_nome_id(id)

    def set_id_musica(self, v):
        if v >= 0: self.__id_musica = v
        else: raise ValueError()

    def set_id_playlist(self, v):
        if v >= 0: self.__id_playlist = v
        else: raise ValueError()


    def set_nome_id(self, v):
        if len(v) >= 3: self.__id= v
        else: raise ValueError()

    def get_id_musica(self):
        return self.__id_musica
    
    def get_id_playlist(self):
        return self.__id_playlist

    def get_id(self):
        return self.__id
    
    def sequencia():
        

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

 

        