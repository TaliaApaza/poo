from template.manterclienteui import ManterClienteUI
from template.manterservicoui import ManterServicoUI
from template.manterhorarioui import ManterHorarioUI
from template.manterprofissional import ManterProfissionalUI
from template.manteratendimentoui import ManterAtendimentoUI
import streamlit as st

class IndexUI:
    def menu_admin():
        op = st.sidebar.selectbox("Menu", ["Cadastro de Clientes", "Cadastro de Serviços", "Cadastro de Horários", "Cadastro de Profissionais", "Cadastro de Atendimentos"])
        if op == "Cadastro de Clientes": ManterClienteUI.main()
        if op == "Cadastro de Serviços": ManterServicoUI.main()
        if op == "Cadastro de Horários": ManterHorarioUI.main()
        if op == "Cadastro de Profissionais": ManterProfissionalUI.main()
        if op == "Cadastro de Atendimentos": ManterAtendimentoUI.main()
    def sidebar():
        IndexUI.menu_admin()
    def main():
        IndexUI.sidebar()
IndexUI.main()