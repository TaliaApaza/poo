from modelos.profissional import Profissional
import json

class ProfissionalDAO:

    def __init__(self):
        self.__arquivo = "profissionais.json"
        self.__ptofissionais = []
        self.__abrir()

    def inserir(self, obj):
        maior = 0

        for profissional in self.__profissionais:
            if profissional.get_id() > maior:
                maior = profissional.get_id()

        obj.set_id(maior + 1)
        self.__profissionais.append(obj)
        self.__salvar()

    def listar(self):
        return self.__profissionais

    def listar_id(self, id):
        for obj in self.__profissionais:
            if obj.get_id() == id:
                return obj
        return None

    def listar_nome(self, inicio):
        lista = []

        for profissional in self.__profissionais:
            if profissional.get_nome().lower().startswith(inicio.lower()):
                lista.append(profissional)

        return lista

    def atualizar(self, obj):
        aux = self.listar_id(obj.get_id())

        if aux is not None:
            self.__profissionais.remove(aux)
            self.__profissionais.append(obj)
            self.__salvar()

    def excluir(self, id):
        aux = self.listar_id(id)

        if aux is not None:
            self.__profissionais.remove(aux)
            self.__salvar()

    def __abrir(self):
        try:
            arquivo = open(self.__arquivo, "r")
            lista = json.load(arquivo)
            arquivo.close()

            self.__profissionais = []

            for dic in lista:
                obj = Profissional.from_json(dic)
                self.__profissionais.append(obj)

        except FileNotFoundError:
            pass

    def __salvar(self):
        arquivo = open(self.__arquivo, "w")

        json.dump(
            self.__profissionais,
            arquivo,
            default=Profissional.to_json,
            indent=2
        )

        arquivo.close()