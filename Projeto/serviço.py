from modelos.cliente import Cliente
from modelos.clientedao import ClienteDAO

from modelos.serviço import Servico
from modelos.serviçodao import ServicoDAO

from modelos.profissional import Profissional
from modelos.profissionaldao import ProfissionalDAO


class Service:

    __clienteDAO = ClienteDAO()
    __serviçoDAO = ServicoDAO()
    __profissionalDAO = ProfissionalDAO()

    #CLIENTE
    @staticmethod
    def cliente_inserir(id, nome, email, fone, senha):
        obj = Cliente(id, nome, email, fone, senha)
        Service.__clienteDAO.inserir(obj)

    @staticmethod
    def cliente_listar():
        return Service.__clienteDAO.listar()

    @staticmethod
    def cliente_listar_nome(nome):
        return Service.__clienteDAO.listar_nome(nome)

    @staticmethod
    def cliente_atualizar(id, nome, email, fone, senha):
        obj = Cliente(id, nome, email, fone, senha)
        Service.__clienteDAO.atualizar(obj)

    @staticmethod
    def cliente_excluir(id):
        Service.__clienteDAO.excluir(id)

    #SERVIÇO
    @staticmethod
    def servico_inserir(id, descricao, valor):
        obj = Servico(id, descricao, valor)
        Service.__serviçoDAO.inserir(obj)

    @staticmethod
    def servico_listar():
        return Service.__serviçoDAO.listar()

    @staticmethod
    def servico_listar_id(id):
        return Service.__serviçoDAO.listar_id(id)

    @staticmethod
    def servico_atualizar(id, descricao, valor):
        obj = Servico(id, descricao, valor)
        Service.__serviçoDAO.atualizar(obj)

    @staticmethod
    def servico_excluir(id):
        Service.__servçoDAO.excluir(id)

    @staticmethod
    def servico_listar_descricao(self, inicio):
        return self.serviçoDAO.listar_descricao(inicio)
    
    #PROFISSIONAL
    @staticmethod
    def profissional_inserir(id, nome, email, senha, especialidade):
        obj = Profissional(id, nome, email, senha, especialidade)
        Service.__profissionalDAO.inserir(obj)

    @staticmethod
    def cliente_listar():
        return Service.__profissionalDAO.listar()

    @staticmethod
    def cliente_listar_nome(nome):
        return Service.__profissionalDAO.listar_nome(nome)

    @staticmethod
    def cliente_atualizar(id, nome, email, senha, especialidade):
        obj = Cliente(id, nome, email, senha, especialidade)
        Service.__profissionalDAO.atualizar(obj)

    @staticmethod
    def cliente_excluir(id):
        Service.__profissionalDAO.excluir(id)
