from datetime import datetime

class Paciente():
    def __init__(self, nome, cpf, tel, data_nasc):
        self.set_nome(nome)
        self.set_cpf(cpf)
        self.set_telefone(tel)
        self.set_data_nascimento(data_nasc)
    def set_nome(self, valor):
        if len(valor) < 3: raise ValueError("Nome Inválido")
        self.__nome = valor
    def set_cpf(self, valor):
        if len(valor) != 11: raise ValueError("Cpf Inválido")
        self.__cpf = valor
    def set_telefone(self, valor):
        if len(valor) > 9: raise ValueError("Telefone Inválido")
        self.__telefone = valor
    def set_data_nascimento(self, valor):
        if valor > datetime.now(): raise ValueError("Data de nascimento não pode ser maior que a data atual")
        self.__data_nascimento = valor
    
    def get_nome(self): return self.__nome
    def get_cpf(self): return self.__cpf
    def get_telefone(self): return self.__telefone
    def get_data_nascimento(self): return self.__data_nascimento

    def idade(self):
        tempo = datetime.now() - self.__data_nascimento
        anos = tempo.days // 365
        meses = tempo.days % 365 // 30
        return f"Anos: {anos} | Mes(es): {meses}"
    
    def __str__(self):
        return f" Nome do Paciente: {self.__nome} | Cpf do Paciente: {self.__cpf} | Telefone do Paciente: {self.__telefone} | Data de Nascimento do Paciente: {datetime.strftime(self.__data_nascimento,"%d/%m/%Y")}"
    

class PacienteUI():
    __lista_paciente = []
    @staticmethod
    def main():
        op = 0 
        while op !=7:
            op = PacienteUI.menu()
            if op == 1: PacienteUI.inserir()
            if op == 2: PacienteUI.listar()
            if op == 3: PacienteUI.atualizar()
            if op == 4: PacienteUI.excluir()
            if op == 5: PacienteUI.pesquisar()
            if op == 6: PacienteUI.aniversariantes()
        print("Fim de sessão")
    @staticmethod
    def menu():
        print(" Escolha as seguintes opções")
        print("-----------------------------------------------------------------------")
        print("|1- Inserir paciente, 2- Listar todos pacientes, 3- Atualizar paciente |")
        print("|4- Excluir paciente, 5- Pesquisar pacientes, 6- Aniversáriantes do mês|")
        print("-----------------------------------------------------------------------")
        op = int(input("Escolha a opção"))
        return op
    @classmethod
    def inserir(cls):
        nome = input("Informe o nome do paciente: ")
        cpf = input("Informe o cpf do paciente: ")
        tel = input("Informe o telefone do paciente: ")
        data_nasc = datetime.strptime(input("Informe a data de nascimento do paciente: "), "%d/%m/%Y")
        x = Paciente(nome, cpf, tel, data_nasc)
        cls.__lista_paciente.append(x)
        print(x)
    @classmethod
    def listar(cls):
        for paciente in cls.__lista_paciente:
            print(paciente)

    @classmethod
    def atualizar(cls):
        cpf_atualizar = input("Informe o cpf do paciente que deseja alterar os dados")
        for paciente in cls.__lista_paciente:
            if paciente.get_cpf() == cpf_atualizar: 
                novo_nome = input("informe o novo nome: ")
                novo_telefone = input("informe o novo telefone: ")
                paciente.set_nome(novo_nome)
                paciente.set_telefone(novo_telefone)
                print("Dados atualizados")
                print(paciente)

    @classmethod
    def excluir(cls):
        cpf_excluir = input("Informe o cpf do paciente que deseja excluir os dados")
        for paciente in cls.__lista_paciente:
            if paciente.get_cpf() == cpf_excluir: 
                cls.__lista_paciente.remove(paciente)
                print("Dados excluidos")

    @classmethod
    def pesquisar(cls):
        inicial = input("Infomer a inicial do paciente")
        for paciente in cls.__lista_paciente:
            if paciente.get_nome().startswith(inicial): print(paciente) #strtswith compara se o valor condiz

    @classmethod
    def aniversariantes(cls):
        m = int(input("Informe o mês: "))
        for paciente in cls.__lista_paciente:
            if paciente.get_data_nascimento().month == m: print(paciente)

PacienteUI.main()
