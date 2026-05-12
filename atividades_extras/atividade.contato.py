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
    def set_fone(self,v):

        if len(v) > 8: self.__fone = v
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
    lista_contato = []
    @staticmethod
    def main():
        op = 0
        while op != 6:
            op = contatoUI.menu()
            if op == 1: contatoUI.inserir_contato()
            if op == 2: contatoUI.listar_contato()
            if op == 3: contatoUI.atualizar_dados()
            if op == 4: contatoUI.excluir_contato()
            if op == 5: contatoUI.pesquisar_inicial()
        print("fim")
    @staticmethod
    def menu():
        print("escolha uma opção:  1-inserir contato, 2-listar contatos, 3-atualizar dados de contatos, 4-excluir contato, 5- pesquisar contato pela inicial do nome 6- sair")
        op = int(input("Informe a opção: "))
        return op
    @classmethod
    def inserir_contato(cls):
        id = int(input("Informe id: "))
        nome = input("Informe o nome do contato: ")
        email = input("Informe o email do contato: ")
        fone = input("Informe o fone do contato: ")
        x = Contato(id, nome, email, fone)
        cls.lista_contato.append(x)
        print(x)

    @classmethod
    def listar_contato(cls):
        for contato in cls.lista_contato:
            print(contato)

    @classmethod
    def atualizar_dados(cls):
        id_atualizar = int(input("Informe o id que irá atualizar: "))
        for contato in cls.lista_contato:
            if contato.get_id() == id_atualizar:
                nome_novo = input("Informe o nome novo do contato: ")
                email_novo = input("Informe o email novo do contato: ")
                fone_novo = input("Informe o fone novo do contato: ")
                contato.set_nome(nome_novo)
                contato.set_email(email_novo)
                contato.set_fone(fone_novo)
                print("Dados atualizados")
                print(contato)
    @classmethod       
    def pesquisar_inicial(cls):
        inicial = input("informe a inicial: ")
        for contato in cls.lista_contato:
            if contato.get_nome()[0] == inicial:
                print(contato)
        
contatoUI.main()