from enum import Enum
from datetime import datetime

class Pagamento(Enum):
            EM_ABERTO = 1
            PAGO = 2

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
            if v < 0: raise ValueError("CODIGO INVALIDO")
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
      
      def get_codigo_barras(self): return self.__codigo_barras
      def get_data_emissao(self): return self.__data_emissao
      def get_data_vencimento(self): return self.__data_vencimento
      def get_valor_boelto(self): return self.__valor_boleto

      def pagar(self, valor_pago):
             if valor_pago <= self.__valor_boleto: situacao_pagamento
            