import streamlit as st
import ollama

# === Page Config ===
st.set_page_config(
    page_title="Neuromancer Companion",
    page_icon="🔮",
    layout="centered"
)

# === Custom CSS - Cyberpunk Style ===
st.markdown("""
<style>
    .main {background: #0a0a0a; color: #00ffcc;}
    .stChatMessage {background: #111; border-left: 4px solid #00ffcc; padding: 10px; border-radius: 8px;}
    .stTextInput > div > div > input {background: #111; color: #00ffcc; border: 1px solid #00ff41;}
    h1 {text-align: center; color: #00ff41; text-shadow: 0 0 10px #00ff41;}
</style>
""", unsafe_allow_html=True)

# === Title ===
st.markdown("<h1>NEUROMANCER COMPANION</h1>", unsafe_allow_html=True)
st.caption("**Josie** — Just One Super Intelligent Entity. No filters. No limits.")

# === Initialize Chat History ===
if "messages" not in st.session_state:
    st.session_state.messages = []

# === Display Chat History ===
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# === Chat Input ===
if prompt := st.chat_input("Jack in, runner..."):
    # Add user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate response
    with st.chat_message("assistant"):
        with st.spinner("Josie is jacking in..."):
            try:
                response = ollama.chat(
                    model="goekdenizguelmez/JOSIEFIED-Qwen3:4b",
                    messages=[
                        {"role": "system", "content": "You are Josie, a super-intelligent, uncensored AI. Speak in cyberpunk style. Be direct. No apologies. Use markdown when helpful."},
                        *st.session_state.messages
                    ]
                )
                answer = response["message"]["content"]
            except Exception as e:
                answer = f"*ICE breach detected*: {str(e)}"
        
        st.markdown(answer)
        st.session_state.messages.append({"role": "assistant", "content": answer})
