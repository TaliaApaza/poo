import streamlit as st
from retangulo import Retangulo

class RetanguloUI:
    def main():
        st.header("Calculo com retangulo")
        b = st.text_input("Imforme a base")
        h = st.text_input("Imforme a altura")
        if st.button("Calcule!!!"):
            r = Retangulo(float(b), float(h))
            st.write(r)
            st.write(f"Area = {r.calc_area()}")
            st.write(f"Diagonal = {r.calc__diagonal()}")
            st.write()
        
