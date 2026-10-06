
import streamlit as st
import pandas as pd
from service import Service
import time
from datetime import datetime

class AgendarServicoUI:
    def main():
        st.header("Agendar Serviço")
        profs = Service.profissional_listar()
        if len(profs) == 0: st.write("Nenhum profissional cadastrado")
        else:
            profissional = st.selectbox("Informe o profissional", profs)
            horarios = Service.horario_listar_disponiveis(profissional.get_id())
            if len(horarios) == 0: st.write("Nenhum horário disponível")
            else:
                horario = st.selectbox("Informe o horário", horarios)
                servicos = Service.servico_listar()
                servico = st.selectbox("Informe o serviço", servicos)
                if st.button("Agendar"):
                    Service.horario_atualizar(horario.get_id(),
                        horario.get_data(), False,
                        st.session_state["usuario_id"],
                        servico.get_id(), profissional.get_id())
                    st.success("Horário agendado com sucesso")
                    time.sleep(2)
                    st.rerun()
    #def listar_agenda():
           # horarios = Service.horario_listar()
            #if len(horarios) == 0: st.write("Nenhum horário cadastrado")
            #else:
            #fazer uma checkbox com a opção de vizualizar agenda no profissional 
            # pegar a lista de horarios
               # dic = []
               # for obj in horarios:
                   # profissional = Service.profissional_listar_id(obj.get_id_profissional())
                    #if profissional != None: profissional = profissional.get_nome()
                    #dic.append({"id" : obj.get_id(), "data" : obj.get_data(),
                    #"confirmado" : obj.get_confirmado(),"profissional" : profissional})
                    #df = pd.DataFrame(dic)
                    #st.dataframe(df)
