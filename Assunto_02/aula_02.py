# Entidade
class Triangulo:
    def __init__(self):
        self.__b = 0.0
        self.__h = 0.0
    def set_base(self, v):
        if v >= 0: self.__b = v
        else: raise ValueError()
    def set_altura(self, v):
        if v >= 0: self.__h = v
        else: raise ValueError()
    def get_base(self):
        return self.__b
    def get_altura(self):
        return self.__h
    def calc_area(self):
        return self.__b * self.__h / 2
class Circulo:
    def __init__(self):
        self.__r = 0.0
        self.__p = 0.0
    def set_raio(self, v):
        if v >= 0: self.__r = v
        else: raise ValueError()
    def set_pi(self, v):
        if v >= 3: self.__p = v
        else: raise ValueError()
    def get_raio(self):
        return self.__r
    def get_pi(self):
        return self.__p
    def calc_area(self):
        return self.__p * self.__r **2
    def calc_circuferencia(self):
        return (2*self.__p)*self.__r

class Viagem:
    def __init__(self):
        self.__d = 0.0
        self.__t = 0.0
    def set_distancia(self, v):
        if v >= 0: self.__d = v
        else: raise ValueError()
    def set_tempo(self, v):
        if v >= 3: self.__t = v
        else: raise ValueError()
    def get_distancia(self):
        return self.__d
    def get_tempo(self):
        return self.__t
    def calc_distancia_media(self):
        return  self.__d/self.__t
    
class Conta_Bancaria:
    def __init__(self):
        self.__nome = ""
        self.__numero_conta= 0
        self.__saldo= 0.0
    def set_nome(self, v):
        if len(v) > 3:
            self.__nome = v
        else:
            raise ValueError()

    def set_numero_conta(self, v):
        if v >= 0: 
            self.__numero_conta= v
        else:
            raise ValueError()
        
    def set_saldo(self, v):
        if v == 0.0: 
            self.__saldo = v
        else:
            raise ValueError()
        
    def set_deposito(self, valor):
        if valor >= 0:
            self.__saldo += valor
        else: raise ValueError()
  
    def get_nome(self):
        return self.__nome
    
    def get_numero_conta(self):
        return self.__numero_conta
    
    def get_saldo(self):
        return self.__saldo
    
    def depositar(self, valor):
        if valor >= 0:
            self.__saldo += valor
        else: raise ValueError()

    def sacar(self,valor):
        if valor >= 0 : 
            self.__saldo -= valor
        else:raise ValueError()
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
        

# Interface com o usuário
class UI:
    @staticmethod
    def main():
        op = 0
        while op != 9:
            op = UI.menu()
            if op == 1: UI.triangulo()
            if op == 2: UI.circulo()
            if op == 3: UI.viagem()
            if op == 4: UI.conta_bancaria()
            if op == 5: UI.ingresso()
        print("fim")
    @staticmethod
    def menu():
        print("1-Triângulo 2-Círculo 3-Viagem 4-Conta Bancária, 5-Ingresso, 9-Fim")
        op = int(input("Escolha uma opção: "))
        return op
    @staticmethod
    def triangulo():
        print("Cálculo da área de um triângulo")
        x = Triangulo()
        x.set_base(float(input("Informe o valor da base: ")))
        x.set_altura(float(input("Informe o valor da altura: ")))
        area = x.calc_area()
        print(f"Um triângulo com base {x.get_base()} e altura {x.get_altura()} tem área = {area}")
    @staticmethod
    def circulo():
        print("Cálculo da área de um circulo")
        x = Circulo()
        x.set_raio(float(input("Informe o valor do raio: ")))
        x.set_pi(float(input("Informe o valor de pi: ")))
        area = x.calc_area()
        circuferencia = x.calc_circuferencia()
        print(f"Um circulo com raio: {x.get_raio()} e pi: {x.get_pi()} tem área = {area} e circuferencia: {circuferencia}")

    @staticmethod
    def viagem():
        x = Viagem()
        x.set_distancia(float(input("Distancia")))
        x.set_tempo(float(input("tempo (ex: 13:30==13.5): ")))
        distancia_media= x.calc_distancia_media()
        print(f"a distancia: {x.get_distancia()} e tempo: {x.get_tempo()} velociade media: {distancia_media:.3f}")

    @staticmethod
    def conta_bancaria():
        x = Conta_Bancaria()
        x.set_nome(input("Nome: "))
        x.set_numero_conta(int(input("Número da conta: ")))
        x.set_saldo (0.0)

        print("Escolha uma opção sendo 1 = deposito e 2 = saque")
        opcao= int(input())

        if opcao==1:
            valor = float(input("valor do deposito: "))
            x.depositar(valor)

        elif opcao==2:
            valor = float(input("valor do saque: "))
            x.sacar(valor)
        else: 
            print("opção invalida")
        print(f"Nome do usuario:{x.get_nome()}. Número da conta do usuario:{x.get_numero_conta()}. Saldo atual:{x.get_saldo()}")

    @staticmethod
    def ingresso():
        x = Ingresso()
        x.set_dia (input( "Escreva um dia da semana(ex: Sábado): "))
        x.set_horario (int(input("Escreva um Horario (ex. 17)")))
        print(f"Dia: {x.get_dia()}. Horario: {x.get_horario()}h. valor do ingresso: {x.calc_ingresso()}")


UI.main()