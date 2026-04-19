class Conta_Bancaria:
    def __init__(self):
        self.__nome = ""
        self.__numero_conta= 0
        self.__saldo= 0.0
        self.__deposito=0.0
        self.__saque=0.0

    def set_nome(self, v):
        if len(v) > 3:
            self.__nome = v
        else:
            raise ValueError()

    def set_numero_conta(self, v):
        if v >= 0: 
            self.__saldo = v
        else:
            raise ValueError()
        
    def set_saldo(self, v):
        if v == 0.0: 
            self.__saldo = v
        else:
            raise ValueError()
        
    def set_deposito(self, v):
        if v >= 0:
            self.__deposito = v
            return self.__saldo== self.__saldo + self.__deposito
        else: raise ValueError()

    def set_saque(self, v):
        if v >= 0: 
            self.__saldo = v
            return self.__saldo== self.__saldo - self.__saque
    
    def get_nome(self):
        return self.__nome
    
    def get_numero_conta(self):
        return self.__numero_conta
    def get_saldo(self):
        return self.__numero_conta
    
    def get_deposito(self):
        return self.__deposito
    
    def get_saque(self):
     return self.__saque
    
    def depositar(self):
        self.__deposito== self.__saldo + self.__deposito
        return self.__deposito
    
    def sacar(self):
        self.__saque==  self.__saque - self.__saldo 
        return self.__saque
    
x = Conta_Bancaria()
x.set_nome = input("Nome: ")
x.set_numero_conta = int(input("NUmero da conta: "))
x.set_saldo = float(input("digite 0.0 "))
print("Escolha uma opção sendo 1 = deposito e 2 = saque")
opcao= int(input())
if opcao==1:
    x.set_deposito(float(input("deposito")))
    print(f"saldo {x.depositar()}")
elif opcao==2:
    x.set_saque(float(input("saque")))
    print(f"nome {x.get_nome()} numero da conta {x.get_numero_conta()} saldo{x.sacar()}")
else: 
    print("opção invalida")