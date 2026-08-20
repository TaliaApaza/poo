from datetime import datetime

class Paciente:
    def __init__(self, nome, cpf, tel, data_nasc):
        self.__nome = nome
        self.__cpf = cpf
        self.__tel = tel
        self.__data_nasc = data_nasc

    def __str__(self):
        return f"Nome: {self.__nome} | Cpf: {self.__cpf} | Telefone: {self.__tel} | Data de nascimento{self.__data_nasc.strftime('%d/%m/%Y')}"

    def idade(self):
        x = datetime.now() - self.__data_nasc
        dias = x.days
        anos = dias // 365
        meses = dias % 365 // 30
        f"{anos} ano(s) | {meses} mes(es)"
    
        