from template.manterclienteui import ManterClienteUI
from template.manterservicoui import ManterServicoUI
from template.manterhorarioui import ManterHorarioUI
from template.manterprofissional import ManterProfissionalUI
from template.manteratendimentoui import ManterAtendimentoUI
import streamlit as st
class IndexUI:
    def main():
        op = st.sidebar.selectbox("Menu", ["Clientes", "Serviços", "Horários", "Profissionais","Atendimentos"])
        if op == "Clientes": ManterClienteUI.main()
        if op == "Serviços": ManterServicoUI.main()
        if op == "Horários": ManterHorarioUI.main()
        if op == "Profissionais": ManterProfissionalUI.main()
        if op == "Atendimentos": ManterAtendimentoUI.main()

IndexUI.main()