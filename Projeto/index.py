from template.manterclienteui import ManterClienteUI
from template.manterservicoui import ManterServicoUI
from template.manterhorarioui import ManterHorarioUI
from template.manterprofissional import ManterProfissionalUI
from template.manteratendimentoui import ManterAtendimentoUI
from template.manterdepartamentoui import ManterDepartamentoUI
from template.abrircontaui import AbrirContaUI
from template.loginui import LoginUI
from template.perfilclienteui import PerfilClienteUI
from service import Service
import streamlit as st

class IndexUI:
    def menu_admin():
        Service.cliente_criar_admin()
        op = st.sidebar.selectbox("Menu", ["Cadastro de Clientes", "Cadastro de Serviços", "Cadastro de Horários", "Cadastro de Profissionais", "Cadastro de Atendimentos", "Cadastro de Departamentos", "Entrar no Sistema"])
        if op == "Cadastro de Clientes": ManterClienteUI.main()
        if op == "Cadastro de Serviços": ManterServicoUI.main()
        if op == "Cadastro de Horários": ManterHorarioUI.main()
        if op == "Cadastro de Profissionais": ManterProfissionalUI.main()
        if op == "Cadastro de Atendimentos": ManterAtendimentoUI.main()
        if op == "Cadastro de Departamentos": ManterDepartamentoUI.main()
        if op == "Entrar no Sistema": LoginUI.main()

    def menu_visitante():
        op = st.sidebar.selectbox("Menu", ["Entrar no Sistema","Abrir Conta"])
        if op == "Entrar no Sistema": LoginUI.main()
        if op == "Abrir Conta": AbrirContaUI.main()
    def menu_cliente():
        op = st.sidebar.selectbox("Menu", ["Meus Dados"])
        if op == "Meus Dados": PerfilClienteUI.main()

    def sair_do_sistema():
        if st.sidebar.button("Sair"):
            del st.session_state["usuario_id"]
            del st.session_state["usuario_nome"]
            st.rerun()
    def sidebar():
        if "usuario_id" not in st.session_state:
            IndexUI.menu_visitante()
        else:
            admin = st.session_state["usuario_nome"] == "admin"
            st.sidebar.write("Bem-vindo(a), " + st.session_state["usuario_nome"])
            if admin: IndexUI.menu_admin()
            else: IndexUI.menu_cliente()
            IndexUI.sair_do_sistema()
    def main():
        IndexUI.sidebar()
IndexUI.main()