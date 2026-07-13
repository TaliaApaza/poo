from modelos.cliente import Cliente 
import json

class ClienteDAO:
    def _init_(self):
        self.__arquivo = "clientes.json"
        self.__objetos = []
        self.__abrir()

    def inserir(self, obj):
        maior = 0

        for cliente in self.clientes:
            if cliente.get_id() > maior:
                maior = cliente.get_id()

        obj.set_id(maior + 1)
        self.clientes.append(obj)

    def listar(self):
        return self.__objetos

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

    def __abrir(self):
        try:
            arquivo = open(self.__arquivo, mode="r")
            lista = json.load(arquivo)
            arquivo.close()

            self.__objetos = []

            for dic in lista:
                obj = Cliente.from_json(dic)
                self.__objetos.append(obj)

        except FileNotFoundError:
            pass
    
    def listar_nome(self, inicio):
        lista = []

        for cliente in self.clientes:
            if cliente.get_nome().lower().startswith(inicio.lower()):
                lista.append(cliente)
                return lista

    def __salvar(self):
        arquivo = open(self.__arquivo, mode="w")

        json.dump(
            self.__objetos,
            arquivo,
            default=Cliente.to_json,
            indent=2
        )

        arquivo.close()