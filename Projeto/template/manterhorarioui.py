import streamlit as st
import pandas as pd
from service import Service
import time
from datetime import datetime

class ManterHorarioUI:
    def main():
        st.header("Cadastro de Horários")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir","Atualizar","Excluir"])
        with tab1: ManterHorarioUI.listar()
        with tab2: ManterHorarioUI.inserir()
        with tab3: ManterHorarioUI.atualizar()
        with tab4: ManterHorarioUI.excluir()

    def listar():
        horarios = Service.horario_listar()
        if len(horarios) == 0: st.write("Nenhum horário cadastrado")
        else:
            dic = []
            for obj in horarios:
                cliente = Service.cliente_listar_id(obj.get_id_cliente())
                servico = Service.servico_listar_id(obj.get_id_servico())
                if cliente != None: cliente = cliente.get_nome() 
                if servico != None: servico = servico.get_descricao()
                dic.append({"id" : obj.get_id(), "data" : obj.get_data(),
                            "confirmado" : obj.get_confirmado(), "cliente" : cliente,"serviço" : servico})
                df= pd.DataFrame(dic)
                st.dataframe(df)