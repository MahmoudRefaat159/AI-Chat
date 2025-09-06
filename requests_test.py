import streamlit as st
import google.generativeai as gen

gen.configure()
model = gen.GenerativeModel("gemini-2.5-flash")
if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history=[])
st.set_page_config(page_title="AI Chat", layout="centered")
st.markdown("""
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" 
          rel="stylesheet">
    <style>
        
        div[data-testid="stButton"] > button:first-child {
            background-color: #0d6efd;
            color: white;
            border-radius: 8px;
            padding: 0.5rem 1rem;
            border: none;
        }
        div[data-testid="stButton"] > button:first-child:hover {
            background-color: #0b5ed7;
            color: white;
        }

        
        div[data-testid="stButton"]:nth-child(2) > button {
            background-color: #dc3545;
            color: white;
            border-radius: 8px;
            padding: 0.5rem 1rem;
            border: none;
        }
        div[data-testid="stButton"]:nth-child(2) > button:hover {
            background-color: #bb2d3b;
            color: white;
        }
    </style>
""", unsafe_allow_html=True)

col_1, col_2, col_3 = st.columns([5, 20, 5])
with col_2:
    st.header("🤖 How Can I Help You")

query = st.text_input("Enter Your Query ")

col1, col2 = st.columns(2)
with col1:
    send_clicked = st.button("🚀 Send")
with col2:
    reset_clicked = st.button("🔄 Reset Conversation")

if query and send_clicked:
    response = st.session_state.chat.send_message(query)
    st.success(response.text)

if reset_clicked:
    st.session_state.chat = model.start_chat(history=[])
    st.success("Conversation has been reset ✅")

if st.session_state.chat.history:
    st.subheader("Chat History")
    for msg in st.session_state.chat.history:
        role = "You" if msg.role == "user" else "Bot"
        st.markdown(f"**{role}:** {msg.parts[0].text}")
