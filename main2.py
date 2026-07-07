import streamlit as st

st.set_page_config(page_title="Assistant")

st.title("🤖 My Assistant")

command = st.text_input("Enter command")

cmd = command.lower().strip()

if "open youtube" in cmd:
    st.success("YouTube Ready")
    st.link_button(
        "▶ Open YouTube",
        "https://www.youtube.com",
        use_container_width=True
    )

elif "open google" in cmd:
    st.success("Google Ready")
    st.link_button(
        "🌐 Open Google",
        "https://www.google.com",
        use_container_width=True
    )

elif "open gmail" in cmd:
    st.success("Gmail Ready")
    st.link_button(
        "📧 Open Gmail",
        "https://mail.google.com",
        use_container_width=True
    )

elif "open github" in cmd:
    st.success("GitHub Ready")
    st.link_button(
        "💻 Open GitHub",
        "https://github.com",
        use_container_width=True
    )

elif "open instagram" in cmd:
    st.success("Instagram Ready")
    st.link_button(
        "📷 Open Instagram",
        "https://instagram.com",
        use_container_width=True
    )

elif "open facebook" in cmd:
    st.success("Facebook Ready")
    st.link_button(
        "📘 Open Facebook",
        "https://facebook.com",
        use_container_width=True
    )

elif command != "":
    st.error("Command not found.")
