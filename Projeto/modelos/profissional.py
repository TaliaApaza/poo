class Profissional:

    def __init__(self, id, nome, email, senha, especialidade):
        self.__id = id
        self.__nome = nome
        self.__email = email
        self.__senha = senha
        self.__especialidade = especialidade

    def get_id(self):
        return self.__id

    def get_nome(self):
        return self.__nome

    def get_email(self):
        return self.__email

    def get_senha(self):
        return self.__senha

    def get_especialidade(self):
        return self.__especialidade

    def set_nome(self, nome):
        if len(nome) < 3:raise ValueError("nome invalido")
        self.__nome = nome

    def set_email(self, email):
        if len(email) < 5: raise ValueError(" email invalido")
        self.__email = email

    def set_senha(self, senha):
        if len(senha) != 4: raise ValueError("senha invalida")
        self.__senha = senha

    def set_especialidade(self, especialidade):
        if especialidade == "" : raise ValueError("Especialidade invalida")
        self.__especialidade = especialidade

    def __str__(self):
        return f"{self.__id} - {self.__nome} - {self.__especialidade}"

    def to_json(self):
        return {
            "id": self.__id,
            "nome": self.__nome,
            "email": self.__email,
            "senha": self.__senha,
            "especialidade": self.__especialidade
        }

    @staticmethod
    def from_json(dic):
        return Profissional(
            dic["id"],
            dic["nome"],
            dic["email"],
            dic["senha"],
            dic["especialidade"]
        )