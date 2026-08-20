from template.manterclienteui import ManterClienteUI
from template.manterservicoui import ManterServicoUI
import streamlit as st

class IndexUI:
    def main():
        op = st.sidebar.selectbox("Menu", ["Clientes", "Serviços"])
        if op == "Clientes": ManterClienteUI.main()
        if op == "Serviços": ManterServicoUI.main()

IndexUI.main()