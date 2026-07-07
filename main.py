import streamlit as st
import webbrowser
from streamlit_mic_recorder import speech_to_text

st.set_page_config(
    page_title="My Assistant",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 My Voice Assistant")

st.write("🎤 Speak a command or type one below.")

# ----------------------------
# Voice Input
# ----------------------------
voice_text = speech_to_text(
    language="en",
    start_prompt="🎤 Start Voice",
    stop_prompt="⏹ Stop",
    just_once=True,
    use_container_width=True,
)

# ----------------------------
# Text Input
# ----------------------------
if "command" not in st.session_state:
    st.session_state.command = ""

if voice_text:
    st.session_state.command = voice_text

command = st.text_input(
    "Command",
    value=st.session_state.command
)

# ----------------------------
# Command Processor
# ----------------------------
def run_command(cmd):

    cmd = cmd.lower().strip()

    if cmd == "":
        st.warning("Please enter a command.")
        return

    if "open youtube" in cmd:
        webbrowser.open("https://www.youtube.com")
        st.success("Opening YouTube...")

    elif "open google" in cmd:
        webbrowser.open("https://www.google.com")
        st.success("Opening Google...")

    elif "open gmail" in cmd:
        webbrowser.open("https://mail.google.com")
        st.success("Opening Gmail...")

    elif "open github" in cmd:
        webbrowser.open("https://github.com")
        st.success("Opening GitHub...")

    elif "open facebook" in cmd:
        webbrowser.open("https://facebook.com")
        st.success("Opening Facebook...")

    elif "open instagram" in cmd:
        webbrowser.open("https://instagram.com")
        st.success("Opening Instagram...")

    elif "open chatgpt" in cmd:
        webbrowser.open("https://chatgpt.com")
        st.success("Opening ChatGPT...")

    elif cmd.startswith("search google "):
        query = cmd.replace("search google", "").strip()
        webbrowser.open(
            f"https://www.google.com/search?q={query}"
        )
        st.success(f"Searching Google: {query}")

    elif cmd.startswith("search youtube "):
        query = cmd.replace("search youtube", "").strip()
        webbrowser.open(
            f"https://www.youtube.com/results?search_query={query}"
        )
        st.success(f"Searching YouTube: {query}")

    else:
        st.error("Command not found.")

# ----------------------------
# Buttons
# ----------------------------
col1, col2 = st.columns(2)

with col1:
    if st.button("▶ Run"):
        run_command(command)

with col2:
    if st.button("🗑 Clear"):
        st.session_state.command = ""
        st.rerun()
