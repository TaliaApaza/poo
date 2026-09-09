import streamlit as st
import pandas as pd
import time
from service import Service

class ManterServicoUI:
    def main():
        st.header("Cadastro de Serviços")
        tab1, tab2, tab3, tab4, tab5 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir", "Listar_Id"])
        with tab1: ManterServicoUI.listar()
        with tab2: ManterServicoUI.inserir()
        with tab3: ManterServicoUI.atualizar()
        with tab4: ManterServicoUI.excluir()
        with tab5: ManterServicoUI.listar_id()
    def listar():
        servicos = Service.servico_listar()
        if len(servicos) == 0: st.write("Nenhum serviço cadastrado")
        else:
            list_dic = []
            for obj in servicos: list_dic.append(obj.to_json())
            df = pd.DataFrame(list_dic)
            st.dataframe(df)
    def listar_id():
        servicos = Service.servico_listar()
        if len(servicos) == 0:
            st.write("Nenhum serviço cadastrado")
        else:
            for obj in servicos:
                st.write(obj.get_id())
    def inserir():
        descricao = st.text_input("Informe a descrição")
        valor = st.text_input("Informe o valor")
        if st.button("Inserir"):
            valor = float(valor)
            Service.servico_inserir(descricao, valor)
            st.success("Serviço inserido com sucesso")
            time.sleep(2)
            st.rerun()
    def atualizar():
        servicos = Service.servico_listar()
        if len(servicos) == 0: st.write("Nenhum serviço cadastrado")
        else:
            op = st.selectbox("Atualização de Serviços", servicos)
            id = st.text_input("Novo id", op.get_id())
            descricao = st.text_input("Nova descrição", op.get_descricao())
            valor = st.text_input("Novo valor", op.get_valor())
            if st.button("Atualizar"):
                id = op.get_id()
                Service.servico_atualizar( id, descricao, valor)
                st.success("Serviço atualizado com sucesso")
                time.sleep(2)
                st.rerun()                
    def excluir():
        servicos = Service.servico_listar()
        if len(servicos) == 0: st.write("Nenhum serviço cadastrado")
        else:
            op = st.selectbox("Exclusão de Serviços", servicos)
            if st.button("Excluir"):
                id = op.get_id()
                Service.servico_excluir(id)
                st.success("Serviço excluído com sucesso")
                time.sleep(2)
                st.rerun()  
