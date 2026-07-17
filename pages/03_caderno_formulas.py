import streamlit as st
from services.caderno_de_formulas import Juros, JurosFlutuantes

st.subheader("Caderno de Fórmulas - CDBs-DIs-DPGE-LAM-LC-LF-LFS-LFSC-LFSN-IECI-RDB")
st.sidebar.subheader("Caderno de Fórmulas")

st.divider()
with st.expander("5 JUROS"):
    valor_nominal_atualizado = st.number_input("Valor Nominal Atualizado (VNa)", min_value=0.0, value=1000.0, step=0.01)
    fator_juros = st.number_input("Fator de Juros (FJ)", min_value=0.0, value=1.05, step=0.0001)

    if st.button("Calcular Valor Unitário dos Juros"):
        try:
            valor_unitario_juros = Juros.valor_unitario_juros(valor_nominal_atualizado, fator_juros)
            st.write(f"Valor Unitário dos Juros: {valor_unitario_juros:.8f}")
        except ValueError as e:
            st.error(str(e))

    st.divider()
    i = st.number_input("Taxa de Juros (i)", min_value=0.0, value=0.0000, step=0.0001, format="%.4f")
    dut = st.number_input("Dias Úteis (DUT)", min_value=0, value=252, step=1)
    dup = st.number_input("Dias Úteis (DUP)", min_value=0, value=252, step=1)
    if st.button("Calcular Fator de Juros"):
        if dut == 0:
            st.error("O número de dias úteis (DUT) não pode ser zero.")
        else:
            fator_juros = Juros.fator_juros(i, dut, dup)
            st.write(f"Fator de Juros (FJ): {fator_juros:.9f}")

with st.expander("6  JUROS FLUTUANTES"):
    form = st.form(key="juros_flutuantes_form")
    data_inicial = form.date_input("Data inicial (DD/MM/AAAA)", key='data_inicial')
    data_final = form.date_input("Data final (DD/MM/AAAA)", key='data_final')
    valor_a_ser_corrigido = form.number_input("Valor a ser corrigido", min_value=0.0, value=1000.0, step=0.01)
    percentual_cdi = form.number_input("% do CDI ", min_value=0.0, value=100.0, step=0.01, format="%.4f")
    if form.form_submit_button("Calcular Juros Flutuantes"):
        form.write("Dados básicos da correção pelo CDI")
        form.write(f"Data inicial: {data_inicial}")
        form.write(f"Data final: {data_final}")
        form.write(f"Valor a ser corrigido: {valor_a_ser_corrigido:,.2f}")
        form.write(f"% do CDI: {percentual_cdi:.4f}")
        resultado = JurosFlutuantes.taxa_cdi_ao_dia()
        form.write(f"Valor unitário dos juros flutuantes: {resultado:.8f}")

        st.table({
            "Data Inicial": [data_inicial],
            "Data Final": [data_final],
            "Valor a ser Corrigido": [valor_a_ser_corrigido],
            "% do CDI": [percentual_cdi],
            "Valor Unitário dos Juros Flutuantes": [resultado]
        })


#with st.expander("7  AMORTIZAÇÕES"):
#    st.selectbox("Tipo de Amortização:", ["SAC", "PRICE", "SACRE", "SACRE-FIXO", "SACRE-FLUTUANTE"])