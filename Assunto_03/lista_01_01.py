from datetime import datetime
class Pacientes():
    def __init__(self, id, n, cpf, tel, nasc):
        self.set_id(id)
        self.set_nome(n)
        self.set_cpf(cpf)
        self.set_telefone(tel)
        self.set_nascimento(nasc)
        #12-cpf
    
    def set_id(self, v):
        if v > 0: self.__id = v
        else: raise ValueError()

    def set_nome(self, v):
       if v == "": raise ValueError("não pode ser vazio")
       self.__nome = v

    def set_cpf(self, v):
        if len(v) == 12: self.__cpf = v
        else: raise ValueError()

    def set_telefone(self, v):
        if len(v) >=9: self.__telefone = v
        else: raise ValueError()

    def set_nascimento(self, v):
        if v > datetime.now():raise ValueError()
        self.__nascimento = v

    def get_id(self): return self.__id
    def get_nome(self): return self.__nome
    def get_cpf(self): return self.__cpf
    def get_telefone(self): return self.__telefone
    def get_nascimento(self): return self.__nascimento

    def __str__(self):
        return f"{self.__id} | {self.__nome} | {self.__cpf} | {self.__telefone}" + \
              f"{self.__nascimento.strftime("%d/%m/%Y")}"
    
    def idade(self):
        tempo = datetime.now - self.__nascimento # medido em dias, horas, .. timedelta
        anos = tempo.days // 365
        meses = tempo.days % 365 // 30
        return f"{anos} ano(s) e {meses} mes(ses)"
    
x = Pacientes(1, "Eduardo", "123456789012", "84900090909" , datetime(1990, 10, 5))

print(x)
print(x.idade())

class PacienteUI():
    lista_pacientes= []

    @staticmethod
    def main():
        op = 0 
        while op!= 7:
            op == PacienteUI.menu()
            if op == 1: PacienteUI.inserir()
            if op == 2: PacienteUI.listar()
            if op == 3: PacienteUI.atualizar()
            if op == 4: PacienteUI.excluir()
            if op == 5: PacienteUI.pesquisar()
            if op == 6: PacienteUI.aniversariantes()
    @staticmethod
    def menu():
        print("Opções: 1 - Inserir, 2 - Listar, 3 - Atualizar, 4 - Excluir, 5 - Pesquisar, 6 _ Aniversariantes")
        return int(input("Escolha uma opção: "))

    @classmethod
    def inserir(cls):
        id = int(input("Informe o id: "))
        n = input("informe o nome: ")
        cpf = input("informe o cpf: ")
        tel = input("informe o numero: ")
        nasc = datetime.strptime(input("Informe a data de nascimento: "), "%d/%m/%Y")
        x = Pacientes(id, n, cpf, tel, nasc)
        cls.lista_pacientes.append(x)
        print(x)

    @classmethod
    def listar(cls):
        if len(cls.lista_pacientes) == 0: print("Nenhum paciente cadastrado")
        else: 
            for x in cls.lista_pacientes: print(x, x.idade())
    @classmethod
    def atualizar(cls):
        id_atualizar = int(input("informe o id que deseja atualizar os dados: "))
        for x in cls.lista_pacientes:
            if x.get_id() == id_atualizar:
                novo_telefone = input("informe o  novo numero do paciente: ")
                cls.set_nome(novo_telefone)
                print(x)

    @classmethod
    def excluir(cls):
        id_excluir = int(input("Informe o id que será excluido: "))


    @classmethod
    def pesquisar(cls):

    @classmethod
    def aniversariantes(cls):
    