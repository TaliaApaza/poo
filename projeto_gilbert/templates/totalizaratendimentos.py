import streamlit as st
from service import Service

class TotalizarAtendimentosUI:
    @staticmethod
    def main():
        st.header("Totalizar Atendimentos")

        data_inicial = st.date_input("Data inicial")
        data_final = st.date_input("Data final")

        if st.button("Consultar"):
            if data_inicial > data_final:
                st.error("Informe um período válido.")
            else:
                resultado = Service.atendimento_totalizar_profissionais(
                    data_inicial, data_final
                )

                st.subheader("Totalização por Profissional")

                st.table(resultado)