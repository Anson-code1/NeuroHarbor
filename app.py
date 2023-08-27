import streamlit as st
from streamlit_chat import message  # Assuming this library exists for the purpose of the example
import llama  # Import hypothetical 'llama' library for AI-based responses

# Function to clear the chat messages
def clear_chat():
    st.session_state.messages = [{"role": "assistant", "content": "Hello! How can I assist you today?"}]

# Initialize chat session
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "Hello! How can I assist you today?"}]

# Application Title
st.title("NeuroHarbor")

# User input form
with st.form("chat_input", clear_on_submit=True):
    a, b = st.columns([4, 1])
    user_prompt = a.text_input(
        label="Your message:",
        placeholder="Type something...",
        label_visibility="collapsed",
    )
    b.form_submit_button("Send", use_container_width=True)

# Display chat messages
for msg in st.session_state.messages:
    message(msg["content"], is_user=msg["role"] == "user")

# Handle user input and generate a response
if user_prompt:
    st.session_state.messages.append({"role": "user", "content": user_prompt})
    message(user_prompt, is_user=True)

    try:
        # Get a response from the 'llama' library (hypothetical)
        response = llama.get_response(user_prompt)
    except Exception as e:
        response = f"An error occurred: {str(e)}"
    
    msg = {"role": "assistant", "content": response}
    st.session_state.messages.append(msg)
    message(msg["content"])

# Option to clear chat
if len(st.session_state.messages) > 1:
    st.button('Clear Chat', on_click=clear_chat)
