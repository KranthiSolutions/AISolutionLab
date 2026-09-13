import os
import streamlit as st
from huggingface_hub import InferenceClient

# Connect to Hugging Face
client = InferenceClient(
    api_key=os.environ["HF_TOKEN"]
)

# Page configuration
st.set_page_config(
    page_title="Kranthi POC - My AI Assistant",
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



