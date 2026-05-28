from enum import Enum
from datetime import datetime

class Pagamento(Enum):
    EM_ABERTO = 1
    PAGO_PARCIAL = 2
    PAGO = 3

class Boleto():
    def __init__(self, cod, emissao, venc, valor):
        self.set_cod_barras(cod)
        self.set_data_emissao(emissao)
        self.set_data_vencimento(venc)
        self.set_valor_boleto(valor)
        #atributos com valor inicial definido

        self.__data_pagamento = None
        self.__valor_pago = 0
        self.__situacao_de_pagamento = Pagamento.EM_ABERTO
    
    def set_cod_boleto(self, cod):
        # supondo que o boleto deve ter 10 digitos
        if len(cod) != 10 : raise ValueError("codigo errado veyerr")
        self.__cod_barras = cod

    def set_data_emissao(self, emissao):
        if emissao > datetime.now(): raise ValueError("data errada pourra")
        self.__data_emissao = emissao

    def set_data_vencimento(self, venc):
        if venc < datetime.now(): raise ValueError("errado")
        self.__data_vencimento = venc
    
    def set_valor_boleto(self, valor):
        if valor < 0: raise ValueError("não pode")
        self.__valor_boleto = valor

    def pagar(self, valor_pago):
        if valor_pago <0: raise ValueError()
        if self.__situacao_de_pagamento != Pagamento.EM_ABERTO: raise ValueError("boleto pago")
        self.__valor_pago = valor_pago
        self.__valor_pago = datetime.now()
        if self.__valor_pago == self.__valor_boleto>= self.__valor_boleto: self.__situacao_de_pagamento = Pagamento.PAGO
        else: self.__situacao_de_pagamento = Pagamento.PAGO_PARCIAL
    
    def get_cod_barras(self): return self.__cod_barras
    def get_data_emissao(self): return self.__data_emissao
    def get_data_vencimento(self): return self.__data_vencimento
    def get_data_pagamento(self): return self.__data_pagamento
    def get_valor_boleto(self): return self.__valor_boleto
    def get_valor_pago(self): return self.__valor_boleto
    def get_valor_boleto(self): return self.__valor_boleto
