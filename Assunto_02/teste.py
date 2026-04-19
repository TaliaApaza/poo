class Ingresso:
    def __init__(self):
        self.__dia = ""
        self.__horario = 0
    def set_dia(self, v):
        if len(v)>=4:
            self.__dia = v
        else: raise ValueError()

    def set_horario(self,v):
        if self.__horario >= 0:
            self.__horario = v
        else: raise ValueError()
    def get_dia(self):
        return self.__dia
    
    def get_horario(self):
        return self.__horario
    
    def calc_ingresso(self):
        if self.__dia == "Segunda" or self.__dia == "Terça" or self.__dia == "Quinta":
            ingresso = 16.00
            if self.__horario>=17:
                ingresso = ingresso* 1.5

        elif self.__dia == "Sexta" or self.__dia == "Sábado" or self.__dia == "Domingo":
            ingresso = 20.00
            if self.__horario >= 17:
                ingresso = ingresso * 1.5
            
        elif self.__dia == "Quarta":
            ingresso = 8.00
        
        else: raise ValueError()
        
        return ingresso
    
x = Ingresso()
x.set_dia (input( "Escreva um dia da semana(ex: Sábado): "))
x.set_horario (int(input("Escreva um Horario (ex. 17)")))

print(f"Dia: {x.get_dia()}. Horario: {x.get_horario()}h. valor do ingresso: {x.calc_ingresso()}")

        
        








