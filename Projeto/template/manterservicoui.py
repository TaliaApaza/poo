import streamlit as st
import pandas as pd
import time
from service import Service

class ManterServicoUI:
    def main():
        st.subheader("Cadastro de Serviços")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: ManterServicoUI.listar()
        with tab2: ManterServicoUI.inserir()
        with tab3: ManterServicoUI.atualizar()
        with tab4: ManterServicoUI.excluir()
    def listar():
        servicos = Service.servico_listar()
        if len(servicos) == 0: st.write("Nenhum serviço cadastrado")
        else:
            list_dic = []
            for obj in servicos: 
                departamento = departamento.departamento_listar_id(obj.get_id_departamento())
                if departamento != None: departamento = departamento.get_diretor()
                list_dic.append({"id" : obj.get_id(), "descricao" : obj.get_descricao(),
                "valor" : obj.get_valor(), "departamento" : departamento})
            df = pd.DataFrame(list_dic)
            st.dataframe(df)
                ##list_dic.append(obj.to_json())
           ## df = pd.DataFrame(list_dic)
            ##st.dataframe(df)
    def inserir():
        departamentos = Service.departamento_listar()
        descricao = st.text_input("Informe a descrição")
        valor = st.text_input("Informe o valor")
        departamento = st.selectbox("Informe o departamento", departamentos, index = None)
        if st.button("Inserir"):
            id_departamento = None
            if departamento != None: id_departamento = departamento.get_id()
            Service.servico_inserir(descricao, float(valor), id_departamento)
            st.success("Serviço inserido com sucesso")
            time.sleep(2)
            st.rerun()
    def atualizar():
        servicos = Service.servico_listar()
        if len(servicos) == 0: st.write("Nenhum serviço cadastrado")
        else: 
            departamento = Service.departamento_listar()
            op = st.selectbox("Atualização de Serviços", servicos)
            descricao = st.text_input("Nova descrição", op.get_descricao())
            valor = st.text_input("Novo valor", op.get_valor())
            id_departamento = None if op.get_id_departamento() in [0, None] else op.get_id_departamento()
            if st.button("Atualizar"):
                id_departamento = None
                id = op.get_id()
                if departamento != None: id_departamento = departamento.get_id()
                Service.servico_atualizar(id, descricao, float(valor), id_departamento)
                st.success("Serviço atualizado com sucesso")
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