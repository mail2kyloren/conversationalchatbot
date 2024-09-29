from langchain_openai.chat_models import ChatOpenAI
from dotenv import load_dotenv
import os
import streamlit as st
from langchain.schema import HumanMessage, SystemMessage, AIMessage


## StreamLi UI

st.set_page_config(page_title="Conversational Q&A Chat bot")
st.header("Hey! How can i help you?")

from dotenv import load_dotenv
load_dotenv()
import os

chat = ChatOpenAI(openai_api_key= os.getenv("OPENAI_API_KEY"),model="gpt-4o",temperature=0.5)

if 'flowmessages' not in st.session_state:
    st.session_state['flowmessages'] = [
        SystemMessage(content = "You are a professional AI assistant")
    ]

def get_chatmodel_response(question):
    st.session_state['flowmessages'].append(HumanMessage(content=question))
    answer = chat.invoke(st.session_state['flowmessages'])
    st.session_state['flowmessages'].append(AIMessage(content=answer.content))
    st.write(st.session_state['flowmessages'])
    return answer.content
      
input=st.text_input("Input:", key="input")   
response = get_chatmodel_response(input)

submit = st.button("Send your query/comment.. ^ ^")

if submit:
    st.subheader("The Response is")
    st.write(response)


    
