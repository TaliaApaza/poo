from enum import Enum
from datetime import datetime
class Pagamento(Enum):
    EM_ABERTO = 1
    PAGO_PARCIALMENTE = 2
    PAGO = 3

class Boleto:
      def __init__(self, cod, data_emissao, data_vencimento, valor_boleto, ):
            self.set_codigo_barras(cod)
            self.set_data_emissao(data_emissao)
            self.set_data_vencimento(data_vencimento)
            self.set_valor_boleto(valor_boleto) 
            self.__data_pagamento = None
            self.__valor_pago = 0
            self.__situacao_pagamento = Pagamento.EM_ABERTO

        
      def set_codigo_barras(self, cod):
            if cod < 0: raise ValueError("codigo de barras invalido")
            self.__codigo_barras = cod

      def set_data_emissao(self, data):
            if data > datetime.now(): raise ValueError("data invalida")
            self.__data_emissao = data
      def set_data_vencimento(self, data):
            if data < datetime.now(): raise ValueError("data invalida")
            self.__data_vencimento = data
        
      def set_valor_boleto(self, v):
            if v < 0: raise ValueError("Valor invalido")
            self.__valor_boleto = v

      def get_codigo_barras(self): return self.__codigo_barras
      def get_data_emissao(self): return self.__data_emissao
      def get_data_vencimento(self): return self.__data_vencimento
      def get_valor_boleto(self): return self.__valor_boleto

      def pagar(self, valor_pago):
            if valor_pago < 0 : raise ValueError("valor invalido")
            if self.__situacao_pagamento != Pagamento.EM_ABERTO: raise ValueError("Boleto já pago")
            self.__valor_pago = valor_pago
            self.__data_pagamento = datetime.now()
            if valor_pago >= self.__valor_boleto: self.__situacao_pagamento = Pagamento.PAGO
            else: self.__situacao_pagamento = Pagamento.PAGO_PARCIALMENTE

      def situacao(self): return self.__situacao_pagamento
      def __str__(self):
            s = f"Boleto: {self.__cod_barras} | Emissão: {self.__data_emissao.strftime('%d/%m/%Y')} | Vencimento: {self.__data_vencimento.strftime('%d/%m/%Y')}\n |Valor Boleto R$ {self.__valor_boleto:.2f} | Valor Pago R$ {self.__valor_pago:.2f} | Situação: {self.__situacao_pagamento}"
            if self.__data_pagamento != None:
                  s += f"Data de pagamento: {self.__data_pagamento.strftime('%d/%m/%Y')}\n"
            return s
              

