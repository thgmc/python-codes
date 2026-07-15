import streamlit as st
from api.dadosabertos import get_json_serie

st.subheader("Table Page")

if st.button("Go to Data Frame Page"):
    response = get_json_serie()
    st.table(response)
