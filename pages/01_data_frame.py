import streamlit as st
from api.dadosabertos import get_json_serie


st.subheader("Data Frame Page")

def get_data():
    return get_json_serie()

if st.button("Go to Table Page"):
    response = get_data()
    st.dataframe(response)