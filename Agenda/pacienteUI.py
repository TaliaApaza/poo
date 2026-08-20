import streamlit as st
from paciente import Paciente
from datetime import date, datetime

class PacienteUI:
    def main():
        st.header("Dados do paciente")
        nome= st.text_input("Informe o nome do paciente")
        cpf = st.text_input("Imforme o cpf do paciente")
        tel = st.text_input("Imforme o telefone do paciente")
        data_nasc = st.date_input("Imforme a data de nascimento do paciente", min_value = date(1900, 1, 1), max_value=date.today(), value=date(200, 1, 1), format=('DD/MM/YYYY'))
        nasc = datetime.combine(nasc, datetime.min.time())
        if st.button("Idade!"):
         x = Paciente(nome, cpf, tel, data_nasc)
         st.write(f"Idade = {x.idade()}")
        
