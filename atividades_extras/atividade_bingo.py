from datetime import datetime, timedelta
class Treino():
    def __init__(self, id, data, distancia, tempo):
        self.set_id(id)
        self.set_data(data)
        self.set_distancia(distancia)
        self.set_tempo(tempo)

    def set_id(self, v):
        if v < 0: raise ValueError("Valor invalido para id")
        self.__id = v

    def set_data(self, v):
        if v > datetime.now(): raise ValueError("Data invalida")
        self.__data = v

    def set_distancia(self, v):
        if v < 0: raise ValueError("Distancia invalida")
        self.__distancia = v

    def set_tempo(self, tempo):
        if tempo <=  timedelta(0): raise ValueError("Tempo invalido")
        self.__tempo = tempo
    
    def get_id(self): return self.__id
    
    def get_data(self): return self.__data

    def get_distancia(self): return self.__distancia

    def get_tempo(self): return self.__tempo

    def pace(self):
        return (self.__tempo.total_seconds() // 60) / self.__distancia
    
    def __srt__(self):
        return f"Id: {self.__id} | Data: {self.__data} | Distancia: {self.__distancia} | Tempo: {self.__tempo} | Pace: {self.pace()}"
    

class UI():
    lista_treino = []
    @staticmethod
    def main():
        op = 0
        while op != 7:
            op = UI.menu()
            if op == 1: UI.inserir() 
            if op == 2: UI.listar()
            if op == 3: UI.listar_id()
            if op == 4: UI.atualizar()
            if op == 5: UI.excluir()
            if op == 5: UI.mais_rapido()
    
    @staticmethod
    def menu():
        print("Opções: 1 - inserir, 2 - listar, 3 - listar ids, 4 - atualizar, 5 - excluir, 6 - mais rápido ")
        op = int(input("Informe a opção: "))
        return op
    
    @classmethod
    def inserir(cls):

        id = int(input("Informe o id: "))
        data = datetime.srtptime(input("informe a data: "), '%d/%m/%Y')
        distancia = float(input("Informe a distancia: "))
        h = int(input("informe a hora: "))
        m = int(input("Informe os minutos: "))
        s = int(input("Informe os minutos: "))
        tempo = timedelta(hours=h, minutes= m, seconds= s)
        x = Treino(id, data, distancia, tempo)
        cls.lista_treino.append(x)
        print(x)