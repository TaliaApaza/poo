class Contato():
    def __init__(self, id, nome, email, fone):
        self.set_id(id)
        self.set_nome(nome)
        self.set_email(email)
        self.set_fone(fone)
    
    def set_id(self, v):
        if v > 0: self.__id = v
        else: raise ValueError("Dado invalido")
    
    def set_nome(self,v):
        if len(v) > 3: self.__nome = v
        else: raise ValueError("Nome invalido")

    def set_email(self,v):
        if len(v) > 3: self.__email = v
        else: raise ValueError("email invalido")
    def set_nome(self,v):

        if v > 8: self.__fone = v
        else: raise ValueError("número invalido")
    
    def get_id(self):
        return self.__id
    
    def get_nome(self):
        return self.__nome
    
    def get_email(self):
        return self.__email
    
    def get_fone(self):
        return self.__fone
    
    def __str__(self):
        return f"Id do contato: {self.__id} | nome do contato: {self.__nome} | email do contato: {self.__email} | telefone do contato: {self.__fone}"
 

class contatoUI():
    @staticmethod
    def main():
        op = 0
        while op != 7:
            op = contatoUI.menu()
            if op ==

    def menu():
        print("escolha uma opção")
        op = int(input("Informe a opção: "))
        return op