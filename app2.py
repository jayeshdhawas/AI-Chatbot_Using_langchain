import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# load API key from secrets
api_key = st.secrets["GOOGLE_API_KEY"]

# Streamlit UI
st.title("Gemini AI Chatbot using LangChain")

# user input
input_text = st.text_input("Ask your question:")

# prompt template
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    ("user", "Question: {question}")
])

# Gemini model
model = ChatGoogleGenerativeAI(
    model="gemini-3-flash-preview",
    google_api_key=api_key
)

# output parser
output_parser = StrOutputParser()

# chain
chain = prompt | model | output_parser

# response
if input_text:
    response = chain.invoke({"question": input_text})
    st.write(response)