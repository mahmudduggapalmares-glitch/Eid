import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Eid Mubarak", page_icon="🌙")

# Estilo personalizado con CSS
st.markdown("""
    <style>
    .main {
        background-color: #0e1117;
    }
    .eid-title {
        font-size: 50px;
        font-weight: bold;
        color: #FFD700;
        text-align: center;
        margin-top: 20px;
    }
    .eid-message {
        font-size: 24px;
        text-align: center;
        color: #ffffff;
    }
    </style>
    """, unsafe_allow_status=True)

# Contenido de la página
st.markdown('<p class="eid-title">🌙 ¡Eid Mubarak! 🌙</p>', unsafe_allow_status=True)

st.write("---")

st.markdown('<p class="eid-message">Espero que la pasen demasiado bien y lo disfruten al máximo en este Eid.</p>', unsafe_allow_status=True)

# Botón interactivo para celebrar
if st.button('¡Celebrar! 🎉'):
    st.balloons()
    st.success("¡Que sea un día lleno de bendiciones y alegría!")

# Pie de página
st.caption("Hecho con ❤️ para este Eid")

