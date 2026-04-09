class agua:
    def __init__(self):
        self.mes = 0
        self.ano = 0
        self.consumo = 0

    def valor_conta(self):
        if self.consumo <= 10:
            return 38.00
        elif 11>= self.consumo <=20:
            return 38+(self.consumo-10)*5
        else:
            return 38 + 10*5 + (self.consumo -20)*6

            

x=agua()
print("informe o mês")
x.mes = int(input())
print("informe o ano")
x.ano = int(input())
print(" informe o total consumido em m³(exemplo:1m³=1000litros)")
x.consumo = float(input(  "m³"))
a = x.valor_conta()
print(f"mês e ano da conta e{x.mes}/{x.ano} e total consumido em m³ é {x.consumo} total a pagar {x.valor_conta()}")
