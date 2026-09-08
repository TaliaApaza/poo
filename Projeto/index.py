from template.manterclienteui import ManterClienteUI
from template.manterservicoui import ManterServicoUI
from template.manterhorarioui import ManterHorarioUI
import streamlit as st

class IndexUI:
    def main():
        op = st.sidebar.selectbox("Menu", ["Clientes", "Serviços", "Horários"])
        if op == "Clientes": ManterClienteUI.main()
        if op == "Serviços": ManterServicoUI.main()
        if op == "Horários": ManterHorarioUI.main()

IndexUI.main()