import streamlit as st
from datetime import datetime
from service import Service

class TotalizarAtendimentosUI:
    @staticmethod
    def main():
        st.header("Totalizar Atendimentos")
        
        data_inicio = st.text_input(Data_inicio, datetime.strptime("%d/%m/%Y"))

        data_fim = datetime.strptime(data_fim, "%d/%m/%Y")

        if st.button("Consultar"):
            if data_inicio > data_fim:
                st.error("Informe um período válido.")
            else:
                resultado = Service.atendimento_totalizar_profissionais(data_inicio, data_fim)
                st.subheader("Totalização por Profissional")

                st.dataframe(resultado,hide_index=True)