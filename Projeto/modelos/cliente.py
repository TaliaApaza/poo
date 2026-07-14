class Cliente:

    def _init_(self, id, nome, email, fone, senha):
        self.set_id(id)
        self.set_nome(nome)
        self.set_email(email)
        self.set_fone(fone)
        self.set_senha(senha)

    #ToString
    def _str_(self):
        return f"{self.__id} - {self.__nome} - {self.__email} - {self.__fone} - {self.__senha}"

    def set_id(self, id):
        if id <= 0: raise ValueError("O id deve ser positivo")
        self.__id = id

    def set_nome(self, nome):
        if nome == "": raise ValueError("O nome deve ser informado")
        self.__nome = nome

    def set_email(self, email):
        if email == "": raise ValueError("O e-mail deve ser informado")
        self.__email = email

    def set_fone(self, fone):
        if fone == "": raise ValueError("O telefone deve ser informado")
        self.__fone = fone
    
    def set_senha(self, v):
        if len(v) != 4: raise ValueError("senha invalida. só pode 4 digitos")
        self.__senha = v
    def get_id(self):return self.__id
    def get_nome(self):return self.__nome
    def get_email(self):return self.__email
    def get_fone(self):return self.__fone
    def get_senha(self): return self.__senha

    def to_json(self):
        return {
            "id": self.__id,
            "nome": self.__nome,
            "email": self.__email,
            "fone": self.__fone,
            "senha": self.__senha
        }

    @staticmethod
    def from_json(dic):
        return Cliente(
            dic["id"],
            dic["nome"],
            dic["email"],
            dic["fone"],
            dic["senha"]
        )