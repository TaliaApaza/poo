from datetime import datetime
class Atendimento:
    def __init__(self,id, data, queixa_principal, historico_saude, avaliacao, prescricao):
        self.set_id(id)
        self.set_data(data)
        self.set_queixa_principal(queixa_principal)
        self.set_historico_saude(historico_saude)
        self.set_avaliacao(avaliacao)
        self.set_prescricao(prescricao)
        self.id_horario(0)
   
    def set_id(self, id):
        if id < 0: raise ValueError("Id deve ser positivo")
        self.__id = id 
    def set_data(self, v): self.__data= v

    def set_queixa_principal(self, queixa):
        if queixa == "": raise ValueError("Queixa deve ser informado")
        self.__queixa_principal = queixa
    def set_historico_saude(self, historico):
        if historico == "": raise ValueError("Historico deve ser informado")
        self.__historico_saude = historico
    def set_avaliacao(self, avaliacao):
        if avaliacao == "": raise ValueError("Avaliação deve ser informado")
        self.__avaliacao = avaliacao
    def set_prescricao(self,v):
        if v == "": raise ValueError("Prescrição deve ser informado")
        self.__prescricao = v
    def set_id_horario(self, id_horario):self.__id_horario = id_horario

    def get_id(self) : return self.__id
    def get_data(self) : return self.__data
    def get_queixa_principal(self) : return self.__queixa_principal
    def get_historico_saude(self) : return self.__historico_saude
    def get_avaliacao(self): return self.__avaliacao
    def get_prescricao(self): return self.__prescricao
    def get_id_horario(self): return self.__id_horario

    def __str__(self):
        return f"{self.__id} - {self.__data.srtftime('d%/m%/Y%')} - {self.__queixa_principal} - {self.__historico_saude} - {self.__prescricao} - {self.__id_horario} - {self.__avaliacao} "
   
    def to_json(self):
        return { "id":self.__id, 
                "data":self.__data,
                "queixa_principal":self.__queixa_principal, 
                "historico_saude":self.__historico_saude, 
                "avaliacao":self.__avaliacao,
                "prescricao":self.__prescricao,
                "id_horario" :self.__id_horario
                }

    @staticmethod
    def from_json(dic):
        return Atendimento(dic["id"], 
                    datetime.strptime(dic["data"],"%d/%m/%Y%H:%M"),
                    dic["queixa_principal"], 
                    dic["historico_saude"],
                    dic["avaliacao"],
                    dic["prescricao"],
                    dic["id_horario"]
                       )
 #   @staticmethod
  #  def from_json(dic):
        atendimento = Atendimento(dic["id"], datetime.strptime(dic["data"],"%d/%m/%Y%H:%M")) 
        atendimento.set_queixa_principal(dic["queixa_principal"])
        atendimento.set_historico_saude(dic["historico_saude"])
        atendimento.set_avaliacao(dic["avaliacao"])
        atendimento.set_prescricao(dic["prescricao"])
        atendimento.set_id_horario(dic["id_horario"])
        return atendimento
