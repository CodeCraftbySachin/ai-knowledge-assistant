import streamlit as st
from chains.chatbot_chain import get_chatbot, get_context
from memory.memory import clear_session_history, get_session_history

# Page config
st.set_page_config(page_title="AI Knowledge Assistant", page_icon="🧠")

st.title("🧠 AI Knowledge Assistant")
st.markdown("---")

from streamlit.runtime.scriptrunner import get_script_run_ctx

# Get a unique session ID for the current user session
def get_session_id():
    ctx = get_script_run_ctx()
    if ctx:
        return ctx.session_id
    return "default_session"

SESSION_ID = get_session_id()

def get_role_description(role):
    if role == "Teacher":
        return "You are a knowledgeable teacher who explains clearly with examples."
    elif role == "Storyteller":
        return "You are a creative storyteller with engaging narration."
    elif role == "Interviewer":
        return "You are an interviewer asking professional questions."
    else:
        return "You are a helpful AI assistant."

# Sidebar
st.sidebar.header("Settings")
role = st.sidebar.selectbox(
    "Select Role",
    ["Assistant", "Teacher", "Storyteller", "Interviewer"]
)

if st.sidebar.button("Clear Chat History"):
    clear_session_history(SESSION_ID)
    if "messages" in st.session_state:
        st.session_state.messages = []
    st.sidebar.success("Chat history cleared!")

# Initialize chatbot
if "chatbot" not in st.session_state:
    st.session_state.chatbot = get_chatbot()

# Initialize message history in session state for UI
if "messages" not in st.session_state:
    st.session_state.messages = []
    # Sync with existing memory if any
    history = get_session_history(SESSION_ID)
    for msg in history.messages:
        role_type = "user" if msg.type == "human" else "assistant"
        st.session_state.messages.append({"role": role_type, "content": msg.content})

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
if prompt := st.chat_input("What is on your mind?"):
    # Add user message to UI
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                role_desc = get_role_description(role)
                context = get_context(prompt)

                response = st.session_state.chatbot.invoke(
                    {
                        "input": prompt,
                        "role": role_desc,
                        "context": context
                    },
                    config={"configurable": {"session_id": SESSION_ID}}
                )

                full_response = response.content
                st.markdown(full_response)

                # Add assistant response to UI state
                st.session_state.messages.append({"role": "assistant", "content": full_response})
            except Exception as e:
                st.error(f"Error: {e}")
