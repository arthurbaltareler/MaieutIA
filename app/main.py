
import streamlit as st

from core.engine import DialogueEngine
from core.errors import mensagem_fallback
from core.submission import submeter_entrada
from core.chat_history import adicionar_mensagem
import traceback

st.set_page_config(
    page_title="Maieut-IA | Coach ICPC",
    page_icon="💡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
    .block-container {
        max-width: 1100px;
        padding-top: 2rem;
    }

    .titulo {
        font-size: 2.2rem;
        font-weight: 700;
        margin-bottom: 0;
    }

    .subtitulo {
        color: #9CA3AF;
        margin-top: 5px;
        margin-bottom: 25px;
    }
</style>
""", unsafe_allow_html=True)


# Cabeçalho
st.markdown(
    '<div class="titulo">💡 Maieut-IA</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitulo">'
    'Coach de Maratona ICPC — Aprenda a resolver problemas '
    'por meio do raciocínio.'
    '</div>',
    unsafe_allow_html=True
)

st.divider()


# Inicialização do estado da aplicação
if "motor" not in st.session_state:
    st.session_state.motor = None

if "historico_visual" not in st.session_state:
    st.session_state.historico_visual = []


# Organização principal
col_entrada, col_dialogo = st.columns([1, 1], gap="large")


# Área de entrada
with col_entrada:
    st.subheader("📝 Problema ou código")

    st.caption(
        "Cole o enunciado do problema ou o código "
        "que você está tentando desenvolver."
    )

    with st.form("formulario_submissao"):
        entrada = st.text_area(
            "Sua entrada",
            placeholder="Digite ou cole seu problema ou código...",
            height=300,
            label_visibility="collapsed"
        )

        enviar = st.form_submit_button(
            "Enviar ao Maieut-IA",
            use_container_width=True
        )

    if enviar:
        if not entrada.strip():
            st.warning("Digite um problema ou código antes de enviar.")

        else:
            try:
                if st.session_state.motor is None:
                    st.session_state.motor = DialogueEngine()

                resposta = submeter_entrada(
                    st.session_state.motor,
                    entrada
                )

                # Registra os dois lados do turno
                adicionar_mensagem(
                    st.session_state.historico_visual,
                    "user",
                    entrada
                )

                adicionar_mensagem(
                    st.session_state.historico_visual,
                    "assistant",
                    resposta
                )

                st.success("Resposta recebida!")

            except Exception as erro:
                print("\n===== ERRO AO PROCESSAR SOLICITAÇÃO =====")
                print(f"Tipo: {type(erro).__name__}")
                print(f"Mensagem: {erro}")
                traceback.print_exc()
                print("========================================\n")

                st.error(mensagem_fallback(erro))


# Área de diálogo
with col_dialogo:
    st.subheader("💬 Diálogo com o Maieut-IA")

    with st.container(border=True):
        if not st.session_state.historico_visual:
            with st.chat_message("assistant"):
                st.write(
                    "Olá! Sou o Maieut-IA. "
                    "Vamos trabalhar juntos na resolução do problema."
                )

        else:
            for mensagem in st.session_state.historico_visual:
                with st.chat_message(mensagem["role"]):
                    st.markdown(mensagem["content"])

st.divider()

st.caption(
    "Maieut-IA | Assistente socrático para programação competitiva"
)
