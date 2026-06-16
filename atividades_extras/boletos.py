from enum import Enum
from datetime import datetime

class Pagamento(Enum):
            EM_ABERTO = 1
            PAGO_PARCIALMENTE = 2
            PAGO = 3

class Boletos():
      def __init__(self, cod, data_emissao, data_vencimento, valor_boleto):
            self.set_codigo_barras(cod)
            self.set_data_emissao(data_emissao)
            self.set_data_vencimento(data_vencimento)
            self.set_valor_boleto(valor_boleto)
            self.__valor_pago = 0 
            self.__data_pagamento = None
            self.__situacao_pagamento = Pagamento.EM_ABERTO

      def set_codigo_barras(self, v):
            if len(v) != 10: raise ValueError("CODIGO INVALIDO")
            self.__codigo_barras = v

      def set_data_emissao(self, v):
            if v > datetime.now(): raise ValueError("data invalida")
            self.__data_emissao = v

      def set_data_vencimento(self, v):
            if v < datetime.now(): raise ValueError("data invalida")
            self.__data_vencimento = v

      def set_valor_boleto(self, v):
            if v < 0: raise ValueError("Valor invalido")
            self.__valor_boleto = v
      

      def pagar(self, valor_pago):
            if valor_pago < 0: raise ValueError("errado")
            if self.__situacao_pagamento != Pagamento.EM_ABERTO: raise ValueError("ja pagou")
            self.__valor_pago = valor_pago
            self.__data_pagamento = datetime.now()
            if self.__valor_pago == self.__valor_boleto:
                   self.__situacao_pagamento = Pagamento.PAGO
            else: 
                   self.__situacao_pagamento = Pagamento.PAGO_PARCIALMENTE
                   
      def situacao_pagamento(self): return self.__situacao_pagamento

      def get_codigo_barras(self): return self.__codigo_barras
      def get_data_emissao(self): return self.__data_emissao
      def get_data_vencimento(self): return self.__data_vencimento
      def get_valor_boleto(self): return self.__valor_boleto
      def get_valor_pago(self): return self.__valor_pago
      def get_data_pagamento(self): return self.__data_pagamento
      def get_situacao_pagamento(self): return self.__situacao_pagamento

      def __str__(self):
            s = f" COdigo de barras: {self.__codigo_barras} | Data de emissão: {self.__data_emissao.strftime('%d/%m/%Y')} | Data de vencimento: {self.__data_vencimento.strftime('%d/%m/%Y')} \n"
            s += f"Valor do Boleto: {self.__valor_boleto} | Situação de pagamento: {self.__situacao_pagamento}\n"
            if self.__situacao_pagamento != Pagamento.EM_ABERTO:
                   s+= f"valor pago: {self.__valor_pago} | data de pagamento: {datetime.strftime(self.__data_pagamento, '%d/%m/%Y')}"
            
            return s
      
class BoletoUI:
      __boletos = []
      @staticmethod
      def main():
        op = 0
        while op != 10:
            op = BoletoUI.menu()
            if op == 1: BoletoUI.inserir()
            if op == 2: BoletoUI.listar()
            if op == 3: BoletoUI.atualizar()
            if op == 4: BoletoUI.excluir()
            if op == 5: BoletoUI.boletos_em_aberto()
            if op == 6: BoletoUI.boletos_pagos()
            if op == 7: BoletoUI.boletos_a_vencer()
            if op == 8: BoletoUI.boletos_vencidos()
            if op == 9: BoletoUI.pagar_boleto()
      @staticmethod
      def menu():
        print("---------------------------------------------")
        print(" 1-Inserir, 2-Listar, 3-Atualizar, 4-Excluir ")
        print(" 5-Boletos em Aberto, 6-Boletos Pagos        ")
        print(" 7-Boletos a Vencer,  8-Boletos Vencidos     ")
        print(" 9-Pagar Boleto,      10-Fim                 ")
        print("---------------------------------------------")
        return int(input("Escolha uma opção: "))
      @classmethod
      def inserir(cls):
        cod = input("Informe o código com 10 dígitos: ")
        emissao = datetime.strptime(input("Informe a data de emissão dd/mm/yyyy: "), "%d/%m/%Y")
        venc = datetime.strptime(input("Informe a data de vencimento dd/mm/yyyy: "), "%d/%m/%Y")
        valor = float(input("Informe o valor: "))
        x = Boletos(cod, emissao, venc, valor)
        cls.__boletos.append(x)
      @classmethod
      def listar(cls):
        for x in cls.__boletos: print(x)
      @classmethod
      def boletos_em_aberto(cls):
          for boletos in cls.__boletos:
                if boletos.get_situacao_pagamento() == Pagamento.EM_ABERTO:
                  print(boletos)
      @classmethod
      def boletos_pagos(cls):
          for boletos in cls.__boletos:
                if boletos.get_situacao_pagamento() == Pagamento.PAGO or Pagamento.PAGO_PARCIALMENTE:
                  print(boletos)

      @classmethod
      def boletos_a_vencer(cls):
           for boleto in cls.__boletos:
                if boleto.get_data_vencimento() > datetime.now() and boleto.get_situacao_pagamento() == Pagamento.EM_ABERTO:
                     print(boleto)
      @classmethod
      def boletos_vencidos(cls):
           for boleto in cls.__boletos:
                if boleto.get_data_vencimento() < datetime.now() and boleto.get_situacao_pagamento() == Pagamento.EM_ABERTO:
                     print(boleto)
      @classmethod
      def pagar_boleto(cls):
           cod_cop = input("informe o codigo de barras que deseja pagar: ")
           valor_pago = float(input("Informe o valor pago: "))
           for boleto in cls.__boletos:
                if boleto.get_codigo_barras() == cod_cop:
                     boleto.pagar(valor_pago)
                     print("Boleto pago")
                     print(boleto)
            
          
            