import os
import streamlit as st
from huggingface_hub import InferenceClient

# Connect to Hugging Face
client = InferenceClient(
    api_key=os.environ["HF_TOKEN"]
)

# Page configuration
st.set_page_config(
    page_title="My AI Assistant",
    page_icon="🤖"
)

# Title
st.title("🤖 kranthi POC - My AI Assistant ")
st.write("Ask a question and get an AI-generated answer.")

# User question
question = st.text_area(
    "Enter your question:",
    placeholder="Example: best christmas gifts?"
)

# Ask AI
if st.button("Submit"):

    if not question.strip():
        st.warning("Please enter a question.")

    else:
        with st.spinner("AI is thinking..."):

            response = client.chat.completions.create(
                model="openai/gpt-oss-120b",
                messages=[
                    {
                        "role": "user",
                        "content": question
                    }
                ]
            )

            answer = response.choices[0].message.content

        st.subheader("AI Answer")
        st.write(answer)




import os
import streamlit as st

from huggingface_hub import InferenceClient


# ---------------------------------------------------------
# Page Configuration
# ---------------------------------------------------------

st.set_page_config(
    page_title="AI Solution Lab",
    page_icon="🤖",
    layout="wide"
)


# ---------------------------------------------------------
# Connect to Hugging Face
# ---------------------------------------------------------

client = InferenceClient(
    api_key=os.environ["HF_TOKEN"]
)


# ---------------------------------------------------------
# Custom CSS
# ---------------------------------------------------------

st.markdown("""
<style>

    /* Main application */
    .stApp {
        background-color: #f7f8fa;
    }

    /* Header */
    .header {
        background: white;
        padding: 20px 30px;
        border-bottom: 1px solid #e5e7eb;
        margin-bottom: 20px;
    }

    .title {
        font-size: 28px;
        font-weight: 600;
        color: #111827;
    }

    .subtitle {
        font-size: 14px;
        color: #6b7280;
        margin-top: 5px;
    }

    /* Welcome section */
    .welcome {
        text-align: center;
        padding: 50px 20px 30px;
    }

    .welcome-icon {
        font-size: 45px;
    }

    .welcome-title {
        font-size: 30px;
        font-weight: 600;
        color: #111827;
        margin-top: 10px;
    }

    .welcome-text {
        color: #6b7280;
        font-size: 15px;
        margin-top: 8px;
    }

    /* Suggestions */
    .suggestion {
        background: white;
        border: 1px solid #e5e7eb;
        border-radius: 10px;
        padding: 12px;
        margin-top: 10px;
        color: #4b5563;
        font-size: 13px;
    }

    /* Footer */
    .footer-text {
        text-align: center;
        color: #9ca3af;
        font-size: 11px;
        margin-top: 10px;
    }

</style>
""", unsafe_allow_html=True)


# ---------------------------------------------------------
# Header
# ---------------------------------------------------------

st.markdown("""
<div class="header">

    <div class="title">
        🤖 Gen AI Assistant
    </div>

    <div class="subtitle">
        Ask questions and get intelligent answers using Generative AI.
    </div>

</div>
""", unsafe_allow_html=True)


# ---------------------------------------------------------
# Conversation History
# ---------------------------------------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []


# ---------------------------------------------------------
# Welcome Screen
# ---------------------------------------------------------

if len(st.session_state.messages) == 0:

    st.markdown("""
    <div class="welcome">

        <div class="welcome-icon">
            ✨
        </div>

        <div class="welcome-title">
            How can I help you?
        </div>

        <div class="welcome-text">
            Ask a question and let AI generate an intelligent response.
        </div>

    </div>
    """, unsafe_allow_html=True)

    # Suggestions
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="suggestion">
            💡 Explain Generative AI
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="suggestion">
            📄 Summarize a document
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="suggestion">
            🔎 Ask a general question
        </div>
        """, unsafe_allow_html=True)


# ---------------------------------------------------------
# Display Previous Messages
# ---------------------------------------------------------

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])


# ---------------------------------------------------------
# Chat Input
# ---------------------------------------------------------

question = st.chat_input(
    "Ask anything..."
)


# ---------------------------------------------------------
# Process Question
# ---------------------------------------------------------

if question:

    # Display user message
    with st.chat_message("user"):

        st.markdown(question)

    st.session_state.messages.append({
        "role": "user",
        "content": question
    })


    # Generate AI response
    with st.chat_message("assistant"):

        with st.spinner("AI is thinking..."):

            response = client.chat.completions.create(

                model="openai/gpt-oss-120b",

                messages=[
                    {
                        "role": "user",
                        "content": question
                    }
                ]
            )

            answer = response.choices[0].message.content


        # Display answer
        st.markdown(answer)


    # Save response
    st.session_state.messages.append({
        "role": "assistant",
        "content": answer
    })


# ---------------------------------------------------------
# Footer
# ---------------------------------------------------------

st.markdown("""
<div class="footer-text">
    AI-generated responses may contain errors. Please verify important information.
</div>
""", unsafe_allow_html=True)

