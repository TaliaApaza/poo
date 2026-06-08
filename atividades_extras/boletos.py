from enum import Enum
from datetime import datetime
class Pagamento(Enum):
    EM_ABERTO = 1
    PAGO_PARCIALMENTE = 2
    PAGO = 3

class Boleto:
        def __init__(self, cod, data_emissao, data_vencimento, data_pagamento, valor_boleto, valor_pago, situ_pagamento):
              self.set_codigo_barras(cod)
              self.set_data_emissao(data_emissao)
              self.set_data_vencimento(data_vencimento)
              self.set_data_pagamento(data_pagamento)
              self.set_valor_boleto(valor_boleto)
              self.set_valor_pago(valor_pago)               
              self.set_situacao_pagamento(situ_pagamento)
        
        def set_codigo_barras(self, cod):
              if cod < 0: raise ValueError("codigo de barras invalido")
              self.__codigo_barras = cod

        def set_data_emissao(self, data):
              if data > datetime.now: raise ValueError("data invalida")
              self.__data_emissao = data
        def set_data_vencimento(self, data):
              if data < datetime.now: raise ValueError("data invalida")
              self.__data_emissao = data
        def set_data_pagamento(self, data):
              self.__data_pagamento = data
        
        def set_valor_boleto(self, v):
              if v < 0: raise ValueError("Valor invalido")
        def set_valor_pago(self, v):
              if v < 0: raise ValueError("Valor invalido")

              

