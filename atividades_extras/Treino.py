from datetime import datetime, timedelta
class Treino():
    def __init__(self, id, data, distancia, tempo):
        self.set_id(id)
        self.set_data(data)
        self.set_distancia(distancia)
        self.set_tempo(tempo)
    
    def set_id(self, v):
        if v < 0 : raise ValueError("Id invalido")
        self.__id = v
    
    def set_data(self, v):
        if v > datetime.now(): raise ValueError("Data invalida")
        self.__data = v
    def set_distancia(self, v):
        if v < 0: raise ValueError("Distancia invalida")
        self.__distancia = v

    def set_tempo(self, v):
        if v < 0: raise ValueError("tempo invalido")
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
        return self.__distancia // self.__tempo.minutes
    
    def __str__(self):
        return f" ID: {self.__id} | Data: {self.__data} | Distância: {self.__distancia} | Tempo: {self.__tempo}"
    

class TreinoUI():
    __lista_treino = []
    
    
        