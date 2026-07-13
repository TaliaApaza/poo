from modelos.serviço import Servico
import json

class ServicoDAO:
    def _init_(self):
        self.__arquivo = "servicos.json"
        self.__objetos = []
        self.__abrir()

    def inserir(self, obj):
        maior = 0
        for servico in self.servicos:
            if servico.get_id() > maior:
                maior = servico.get_id()
        obj.set_id(maior + 1)
        self.servicos.append(obj)

    def listar(self): return self.__objetos

    def listar_id(self, id):
        for obj in self.__objetos:
            if obj.get_id() == id:
                return obj
        return None

    def atualizar(self, obj):
        aux = self.listar_id(obj.get_id())

        if aux != None:
            self.__objetos.remove(aux)
            self.__objetos.append(obj)
            self.__salvar()

    def excluir(self, id):
        aux = self.listar_id(id)

        if aux != None:
            self.__objetos.remove(aux)
            self.__salvar()

    def cliente_listar_nome(self, inicio):
         return self.clienteDAO.listar_nome(inicio)
    
    def listar_descricao(self, inicio):
        lista = []

        for servico in self.servicos:
            if servico.get_descricao().lower().startswith(inicio.lower()):
                lista.append(servico)

            return lista

    def __abrir(self):
        try:
            arquivo = open(self.__arquivo, mode="r")

            lista = json.load(arquivo)

            arquivo.close()

            self.__objetos = []

            for dic in lista:
                obj = Servico.from_json(dic)
                self.__objetos.append(obj)

        except FileNotFoundError:
            pass

    def __salvar(self):
        arquivo = open(self.__arquivo, mode="w")

        json.dump(
            self.__objetos,
            arquivo,
            default=Servico.to_json,
            indent=2
        )

        arquivo.close()