import streamlit as st

st.set_page_config(page_title="Surpresa BB", layout="centered")

st.markdown(
    """
    <style>
        body {
            background-color: #e6f0ff;  /* azul bem clarinho */
        }
        * {
            color: #222222 !important;  /* texto escuro visível */
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.header("💍 Surpresa especial")
st.write("Você sabe que dia é hoje?\n\nIsso mesmo, o seu primeiro Dia dos Namorados NOIVAAAA 🤍")

nome = st.text_input("Qual o seu nome? (Dica: começa com L...)")

if nome.strip().lower() == "larissa":
    confirmar = st.radio("Vamos descobrir o que a sua noiva aprontou pra você?", ("Não", "Sim"))
    if confirmar == "Sim":
        st.write("🥹 Espero que esteja pronta então!\n")
        mensagem = """
        **Desde o dia em que voltamos a nos falar, eu senti dentro de mim que você era diferente.**
        (… texto completo …)
        **FELIZ DIA DAS NAMORADAAAAAS!!!** 🤍🤍🤍✨

        *Com amor, Kaw 🤍💍*
        """
        st.markdown(mensagem)
    elif confirmar == "Não":
        st.write("🙊 Ahhh... então tá bom... até a próxima!")
elif nome != "":
    st.warning("❌ Ops! Só a Larissa pode continuar... tente de novo!")
