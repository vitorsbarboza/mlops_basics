
import streamlit as st
import numpy as np
import streamlit.components.v1 as components


st.title("Calculadora de Juros Compostos")


tab1, tab2 = st.tabs(["Calcular", "Sobre"])

with tab1:
    principal = st.number_input("Montante inicial (R$)", min_value=0.0, value=1000.0)
    aporte = st.number_input("Aporte mensal (R$)", min_value=0.0, value=0.0)
    taxa_tipo = st.radio("Tipo de taxa de juros:", ["Mensal", "Anual"], horizontal=True)
    if taxa_tipo == "Mensal":
        rate = st.number_input("Taxa de juros mensal (%)", min_value=0.0, value=1.0)
        juros_mensal = rate / 100
    else:
        rate = st.number_input("Taxa de juros anual (%)", min_value=0.0, value=12.0)
        juros_mensal = (1 + rate/100) ** (1/12) - 1
    meses = st.number_input("Tempo (meses)", min_value=1, value=12)

    if st.button("Calcular"):
        n = int(meses)
        i = juros_mensal
        P = principal
        A = aporte
        # Usando numpy para valor futuro
        if i > 0:
            montante = -np.fv(i, n, -A, -P)
        else:
            montante = P + A * n
        total_aportado = P + A * n
        juros_ganhos = montante - total_aportado
        st.success(f"Valor final: R$ {montante:.2f}")
        st.info(f"Juros ganhos: R$ {juros_ganhos:.2f}")
        st.info(f"Total investido: R$ {total_aportado:.2f}")

with tab2:
    st.markdown("## Como funciona\nEsta calculadora utiliza a fórmula de juros compostos com aportes mensais:")
    # Renderização da equação com MathJax
    mathjax = r'''
    <div style="background-color:#f8f9fa;padding:10px;border-radius:8px;">
    <strong>Fórmula:</strong><br>
    <span style="color:#d6336c;font-size:1.2em;">
    <script type="text/x-mathjax-config">
      MathJax.Hub.Config({tex2jax: {inlineMath: [['$','$'], ['\\(','\\)']]}});
    </script>
    <script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
    <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
    $$\text{Montante Final} = P (1 + i)^n + A \frac{(1 + i)^n - 1}{i}$$
    </span>
    </div>
    '''
    components.html(mathjax, height=120)
    st.markdown("""
    **Onde:**
    - **P**: Montante inicial
    - **A**: Aporte mensal
    - **i**: Taxa de juros mensal (decimal)
    - **n**: Número de meses
    """)
