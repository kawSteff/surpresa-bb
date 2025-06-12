import streamlit as st

st.set_page_config(page_title="Surpresa BB", layout="centered")

# Força fundo azul clarinho e texto escuro
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

# Entrada do nome
nome = st.text_input("Qual o seu nome? (Dica: começa com L...)")

if nome.strip().lower() == "larissa":
    # Radio sem opção selecionada no início
    confirmar = st.radio(
        "Vamos descobrir o que a sua noiva aprontou pra você?", 
        ("Não", "Sim"),
        index=None
    )
    
    if confirmar == "Sim":
        st.write("🥹 Espero que esteja pronta então!\n")
        
        mensagem = """
Desde o dia em que voltamos a nos falar, eu senti dentro de mim que você era diferente.
Eu sempre sonhei em ter um amor como o nosso mas nunca imaginei que um dia iria se tornar real.
Eu já não tenho mais palavras no meu vocabulário pra agradecer ou dizer o quanto eu amo você.
Se eu pudesse voltar no tempo pra mudar algo, não mudaria nada só pelo simples fato de que gostaria de viver esse amor contigo todos os dias,
pra sentir a mesma sensação de quando eu disse que te amava pela primeira vez.
Me desculpe por te magoar às vezes, mas sou um ser humano e estou aprendendo a viver essa vida com você,
estou aprendendo como é ser amada de verdade e como amar alguém como se não houvesse o amanhã.
Obrigada por me ouvir e me compreender, obrigada por sempre estar aqui e nunca desistir de mim ou de nós,
obrigada por cuidar do meu coração tão bem todos os dias, obrigada por me passar tanta confiança e por confiar em mim.

Saiba que eu viveria por você, pois morrer é muito fácil mas viver por alguém é uma das provas de amor mais puras que existe.

Obrigada por me fazer querer viver mais um dia, todos os dias.

**Larissa Figueredo Souza, eu te amo além da eternidade!**

**FELIZ DIA DAS NAMORADAAAAAS!!!** 🤍🤍🤍✨

*Com amor, Kaw 🤍💍*
"""
        st.markdown(mensagem)
    
    elif confirmar == "Não":
        st.write("🙊 Ahhh... então tá bom... até a próxima!")
else:
    if nome:
        st.error("❌ Ops! Só a Larissa pode continuar... tente de novo!\n")
