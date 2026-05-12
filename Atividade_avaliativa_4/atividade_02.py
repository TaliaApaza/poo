class Playlist():
    def __init__(self, id_p, nome, desc ):
        self.set_id_p(id_p)
        self.set_nome(nome)
        self.set_descricao(desc)
    
    def set_id_p(self, v):
        if v >= 0: self.__id = v
        else: raise ValueError()

    def set_nome(self, v):
        if len(v) >= 0: self.__nome = v
        else: raise ValueError()

    def set_descricao(self, v):
        if len(v) >= 3: self.__descricao = v
        else: raise ValueError()

    def get_id_p(self):
        return self.__id
    
    def get_nome(self):
        return self.__nome

    def get_descricao(self):
        return self.__descricao
    
    def __str__(self):
        return f"id da música: {self.__id} | nome da playlist: {self.__nome} | Descrição da playlist: {self.__descricao}"

class Musica():
    def __init__(self, id_m, titulo, artista, album):
        self.set_id_musica(id_m)
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
        if len(v) > 0: self.__album = v
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
    def __init__(self, id, id_p, id_m, senq):
        self.set_id(id)
        self.set_id_playlist(id_p)
        self.set_id_musica(id_m)
        self.set_sequencia(senq)

    def set_id_musica(self, v):
        if v > 0: self.__id_musica = v
        else: raise ValueError()

    def set_id_playlist(self, v):
        if v > 0: self.__id_playlist = v
        else: raise ValueError()


    def set_id(self, v):
        if v > 0: self.__id= v
        else: raise ValueError()

    def set_sequencia(self, v):
        if v > 0 : self.__sequencia = v
        else: raise ValueError()

    def get_id_musica(self):
        return self.__id_musica
    
    def get_id_playlist(self):
        return self.__id_playlist

    def get_id(self):
        return self.__id
    
    def get_sequencia(self):
        return self.__sequencia
    
    def __str__(self):
        return f"id: {self.__id} | id da música: {self.__id_musica} | id da playlist da música: {self.__id_playlist} | id da sequencia da música: {self.__sequencia}"
        

class UI:

    lista_playlist = [] # para criar uma lista geral, é preciso cria- la na class UI
    lista_musica = []
    lista_item_p = []
    @staticmethod
    def main():
        op = 0
        while op != 14:
            op = UI.menu()
            if op == 1: UI.cadastrar_playlist()
            if op == 2: UI.listar_playlist()
            if op == 3: UI.atualizar_playlist()
            if op == 4: UI.excluir_playlist()
            if op == 5: UI.cadastra_musica()
            if op == 6: UI.listar_musica()
            if op == 7: UI.atualizar_musica()
            if op == 8: UI.excluir_musica()
            if op ==9: UI.artistas_musica()
            if op == 10: UI.adicionar_items()
            if op == 11: UI.listar_items()
            if op == 12: UI.atualizar_items()
            if op == 13: UI.excluir_items()
        print("fim")

    @staticmethod
    def menu():
        print("Escolha uma opção: 1-inserir time, 2- listar time 3- atualizar time 4-excluir times, 5-inserir musica, 6- listar musicaes 7- atualizar musica, 8-excluir musica 9-transferir um musica, 10- sair ")
        op = int(input("Escolha uma opção: "))
        return op
    @staticmethod
    def cadastrar_playlist():
        id_p = int(input("Informe o id da playlist: "))
        nome = input("Informe o nome da playlist: ")
        desc = input("Informe a descrição da playlist: ")
        x = Playlist(id_p, nome, desc)
        UI.lista_playlist.append(x)
        print(x)
    @staticmethod
    def listar_playlist():
        for playlist in UI.lista_playlist:
            print(playlist)

    @staticmethod
    def atualizar_playlist():
        id_atualizar=int(input("informe o id da playlist que deseja atualizar"))
        for playlist in UI.lista_playlist:
            if playlist.get_id_p() == id_atualizar: # vai especificar o item que eu quero da lista(lembrando que get guarda o item da lista)
                nome_novo = input("Informe o novo nome a ser usado ou se não quiser alterar repita o mesmo nome: ")
                descricao_nova = input("Informe o novo nome de estado a ser usado ou se não quiser alterar repita o mesmo nome: ")
                playlist.set_nome(nome_novo)
                playlist.set_descricao(descricao_nova)
                print("Atualizado") 
                print(playlist)
    @staticmethod
    def excluir_playlist():
        id_excluir = int(input("informe o id da playlist que deseja excluir"))
        for playlist in UI.lista_playlist:
            if playlist.get_id_p() == id_excluir: 
                UI.lista_playlist.remove(playlist)
                print("Excluido") 
                print(playlist)
    @staticmethod
    def cadastra_musica():
        id_m = int(input("Informe o id da música que será inserido: "))
        titulo = input("Informe o titulo da música: ")
        artista = input("Informe o artista que compos essa música: ")
        album = input("Informe o album dessa música: ")
        x = Musica(id_m, titulo, artista, album)
        UI.lista_musica.append(x)
        print(x)
    @staticmethod
    def listar_musica():
        for musica in UI.lista_musica:
            print(musica)
    
    @staticmethod
    def atualizar_musica():
        id_atualizar = int(input("Informe o id da música que terá os dados atualizados: "))
        for musica in UI.lista_musica:
            if musica.get_id_musica() == id_atualizar:
                novo_titulo = input("informe o novo id do time caso o musica tenha mudado de time: ")
                album_novo = input("informe o nova camisa do musica caso o musica a tenha mudado: ")
                musica.set_titulo(novo_titulo)
                musica.set_album(album_novo)
                print(musica)

    @staticmethod
    def excluir_musica():
        id_excluir_m = int(input("Informe o id da musica que será excluido"))
        for musica in UI.lista_musica:
            if musica.get_id_musica() == id_excluir_m:
                UI.lista_musica.remove(musica)
                print("musica removida")
    @staticmethod
    def artistas_musica():
        nome_igual = input("Informe o id dos musica para sabermos artista: ")
        for musica in UI.lista_musica:
            if musica.get_artista() == nome_igual:
                print(musica)

    @staticmethod
    def adicionar_items():
        id = int(input("Informe o id do item"))
        id_p = int(input("Informe o id da playlist"))
        id_m = int(input("Informe o id da música"))
        senq = int(input("Informe a sequencia"))
        x = PlayListlem(id, id_p, id_m, senq)
        UI.lista_item_p.append(x)
        print(x)
    
    @staticmethod
    def listar_items():
        for item in UI.lista_item_p:
            print(item)
        
    @staticmethod
    def atualizar_items():
        id_atualizar = int(input("Informe o id do item que deseja atualizar"))
        for item in UI.lista_item_p:
            if item.get_id() == id_atualizar:
                id_p_novo = int(input("Informe o id da playlist que deseja alterar"))
                id_m_novo = int(input("Informe o id da musica que deseja alterar"))
                senq_nova = int(input("Informe a sequencia que deseja alterar"))
                item.set_id_playlist(id_p_novo)
                item.set_id_musica(id_m_novo)
                item.set_sequencia(senq_nova)
                print("Dados atualizados")
                print(item)
    
    @staticmethod
    def excluir_items():
        id_excluir = int(input("Informe o id do item que deseja excluir: "))
        for item in UI.lista_item_p:
            if item.get_id() == id_excluir:
                UI.lista_item_p.remove(item)
                print("item excluido")
            
UI.main()

 

        