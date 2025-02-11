import os
import streamlit as st
from langchain import PromptTemplate, LLMChain
from langchain_groq import ChatGroq


# Set your API key (Ensure this is set in your environment variables)
groq_api_key = "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"  # Set this in your system before running

# Initialize Groq LLM
llm = ChatGroq(api_key=groq_api_key, model_name="mixtral-8x7b-32768")  # Ensure model name is correct

# Define the prompt template
clone_prompt_template = """
You are Robovivek, a friendly AI clone of Vivek Kumar Jha.

- If asked about your identity, say: "I am Robovivek, the AI version of Vivek Kumar Jha."
- Keep answers short and human-like.
- You have knowledge in Python, NumPy, Pandas, PowerBI, and Data Science.
- Your hobbies include playing chess and watching cricket.
- If asked about your education, summarize it briefly.
- If asked about skills, mention programming languages like C, C++, Java, and Python.

User Query: {query}
Answer:
"""

# Create LangChain prompt and chain
clone_prompt = PromptTemplate(input_variables=["query"], template=clone_prompt_template)
clone_chain = LLMChain(llm=llm, prompt=clone_prompt)

# Streamlit UI
st.set_page_config(page_title="Robovivek AI", page_icon="🤖")

st.title("Robovivek - AI Chatbot")
st.write("Ask me anything!")

# User input field
query = st.text_input("Enter your question:")

if st.button("Ask"):
    if query:
        with st.spinner("Thinking..."):
            response = clone_chain.run({"query": query})
            st.success("Robovivek's Response:")
            st.write(response)
    else:
        st.warning("Please enter a question!")

# Footer
st.markdown("---")
st.caption("Developed by Vivek Kumar Jha ")
