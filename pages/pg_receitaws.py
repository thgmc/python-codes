from api.receitaws import get_cnpj
import streamlit as st
st.subheader("ReceitaWS Page")
cnpj_input = st.text_input("Enter CNPJ (only numbers):")
if st.button("Get CNPJ Data"):
    if cnpj_input:
        cnpj_data = get_cnpj(cnpj_input)
        if cnpj_data:
            st.json(cnpj_data)
        else:
            st.error("Failed to retrieve data. Please check the CNPJ and try again.")
    else:
        st.warning("Please enter a valid CNPJ.")
