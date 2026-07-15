import streamlit as st

st.header("Welcome to the Home Page")

pg = st.navigation(
    [
        st.Page("pages/01_data_frame.py"),
        st.Page("pages/02_table.py")
        ]
    )
pg.run()