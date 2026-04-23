#Entidades
class Aluno:
    def __init__(self):
        self.__nome=""        #atributo encapsulado(qauhndo esta escondido)
        self.__matricula=""

    def set_nome(self,valor):# set recebe valor onde irá texta se oq foi recebido vale
        if len(valor) < 3: raise ValueError("nome tem menos de 2 caracteres")
        self.__nome= valor
    def get_nome(self):# armazena os dados do atributo, trabalha como um auxilio do set
        return self.__nome 
    
    def set_matricula(self,valor):
        if len(valor) <7: raise ValueError("matrucula sem os caracteres necessarios")
        self.__matricula = valor
    def get_matricula(self):# armazena os dados do atributo, trabalha como um auxilio do set
        return self.__matricula

    def ano_ingresso(self):  #metodo
        return int(self.matricula[:4]) #indices 
    #def __init__(self):
        self.__nome=""        #para esconder um atributo basta colocar duas linhas
        self.matricula=""
# Programa principal
class UI:
    def main():#operação principal. para fazer isso funcionar basta chamar a função
        x = Aluno()
        x.set_nome(input("Informe o nome"))#quando se enconder o atributo(ex: nome)
        #é necessario criar um metodo para chamar esse atributo. usa-se entt o set
        x.set_matricula(input("informe matricula"))
        print(f"aluno{x.get_nome()} matricula{x.get_matricula()}")#exibir nome
        print(f"ano de ingresso{x.ano_ingresso} ")
UI.main()
