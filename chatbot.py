
import streamlit as st
from google import genai

st.set_page_config(
    page_title="Aurene AI",
    page_icon="✦",
    layout="centered"
)

st.markdown("""
<style>
.stApp {
    background-color: #F8F4EC;
    color: #49372C;
}
h1, h2, h3 {
    font-family: 'Playfair Display', serif;
    color: #49372C;
}
p {
    font-family: 'DM Sans', sans-serif;
}
[data-testid="stChatMessage"] {
    background-color: #EFE7DB;
    border-radius: 14px;
    padding: 14px;
}
</style>
""", unsafe_allow_html=True)

st.markdown(
    "<h1 style='text-align:center;'>AURENE AI ✦</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<p style='text-align:center;color:#8B796B;'>"
    "Your personal fashion & sustainability assistant"
    "</p>",
    unsafe_allow_html=True
)

st.divider()

if "aurene_messages" not in st.session_state:
    st.session_state.aurene_messages = [
        {
            "role": "assistant",
            "content": "Hello! I'm Aurene AI. Ask me about styling, "
                       "sustainable fashion, our collections or donations. ✦"
        }
    ]

for message in st.session_state.aurene_messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

user_input = st.chat_input("Ask Aurene anything...")

if user_input:
    st.session_state.aurene_messages.append(
        {"role": "user", "content": user_input}
    )

    with st.chat_message("user"):
        st.markdown(user_input)

    try:
        client = genai.Client(
            api_key=st.secrets["GEMINI_API_KEY"]
        )

        conversation = [
            "You are Aurene AI, the friendly fashion and sustainability "
            "assistant for Aurene, a sustainable fashion platform.",
            "Help users with outfit styling, sustainable fashion, "
            "upcycling, clothing donations and shopping guidance.",
            "Keep answers helpful, clear and conversational."
        ]

        for msg in st.session_state.aurene_messages[-11:]:
            role = "User" if msg["role"] == "user" else "Aurene AI"
            conversation.append(f"{role}: {msg['content']}")

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents="\n".join(conversation)
        )

        answer = response.text or "I couldn't generate a response. Please try again."

    except Exception as e:
        answer = "I couldn't connect right now. Please check the API setup and try again."

    st.session_state.aurene_messages.append(
        {"role": "assistant", "content": answer}
    )

    with st.chat_message("assistant"):
        st.markdown(answer)
