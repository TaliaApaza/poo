from datetime import datetime, timedelta
class Treino():
    def __init__(self, id, data, distancia, tempo):
        self.set_id(id)
        self.set_data(data)
        self.set_distancia(distancia)
        self.set_tempo(tempo)
    
    def set_id(self, v):
        if v >= 0: self.__id = v
        else: raise ValueError("id invalido")

    def set_data(self, v):
        if v > datetime.now():raise ValueError()
        self.__data = v
    def set_distancia(self, v):
        if v >= 0: self.__distancia = v
        else: raise ValueError("id invalido")

    def set_tempo(self, v):
        if v < timedelta(0): raise ValueError("errado")
        self.__tempo = v

    def get_id(self):
       return self.__id
    
    def get_data(self):
       return self.__data

    def get_distancia(self):
       return self.__distancia

    def get_tempo(self):
       return self.__tempo
    
    def pace(self): 
        return  (self.__tempo.total_seconds() // 60) / self.__distancia 
    
    def __str__(self):
        return f" Id: {self.__id} | data: {self.__data} | tempo: {self.__tempo} | distancia: {self.__distancia} | tempo: {self.__tempo} | Pace: {self.pace()}"
    

class TreinoUI():
    lista_treino= []

    @staticmethod
    def main():
        op = 0 
        while op!= 7:
            op = TreinoUI.menu()
            if op == 1: TreinoUI.inserir()
            if op == 2: TreinoUI.listar()
            if op == 3: TreinoUI.atualizar()
            if op == 4: TreinoUI.excluir()
            if op == 5: TreinoUI.pesquisar()
            if op == 6: TreinoUI.maior_treino()
    @staticmethod
    def menu():
        print("Opções: 1 - Inserir, 2 - Listar, 3 - Atualizar, 4 - Excluir, 5 - Pesquisar, 6 _Treino mais rapido")
        return int(input("Escolha uma opção: "))

    @classmethod
    def inserir(cls):
        id = int(input("Informe o id: "))
        data = datetime.strptime(input("informe a data: "), '%d/%m/%Y')
        distancia = float(input("Infome adinstancia em km:" ))
        h = int(input("Infome as hora: "))
        tempo = timedelta(hours= h)
        x = Treino(id, data, distancia, tempo)
        cls.lista_treino.append(x)
        print(x)

    @classmethod
    def listar(cls):
        for treino in cls.lista_treino:
            print(treino)
    @classmethod
    def atualizar(cls):
        id_atualizar = int(input("informe o id que deseja atualizar os dados: "))
        for treino in cls.lista_treino:
            if treino.get_id() == id_atualizar:
                nova_data = datetime.strptime(input("informe a data: "), '%d/%m/%Y')
                nova_distancia = float(input("Infome adinstancia em km:" ))
                h = int(input("Infome as hora: "))
                novo_tempo = timedelta(hours= h)
                treino.set_tempo(novo_tempo)
                treino.set_data(nova_data)
                treino.set_distancia(nova_distancia)
                print(treino)

    @classmethod
    def excluir(cls):
        id_excluir = int(input("Informe o id que será excluido: "))
        for x in cls.lista_treino:
            if x.get_id() == id_excluir:
                cls.lista_treino.remove(x)

    @classmethod
    def pesquisar(cls):
        inicial = input("informe a inicial: ")
        for x in cls.lista_contato:
            if x.get_nome().startswith(inicial): print(x)

    @classmethod
    def maior_treino(cls):
        m = int(input("INforme o mes do aniversario: "))
        for x in cls.lista_pacientes:
            if x.get_nascimento().month == m: print(x)



TreinoUI.main()