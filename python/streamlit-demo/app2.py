import streamlit as st
import random
import time
import numpy as np


st.title("Risk and PnL Analysis Bot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

if 'is_stream' not in st.session_state:
    st.session_state.is_stream = False

if 'content_to_stream' not in st.session_state:
    st.session_state.content_to_stream = None

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Streamed response emulator
def response_generator():
    response = random.choice(
        [
            "Hello there! How can I assist you today?",
            "Hi! Is there anything I can help you with?",
            "Do you need help?",
        ]
    )
    for word in response.split():
        yield word + " "
        time.sleep(0.05)

# My callback function
def on_button_click(**kwargs):
    st.session_state.is_stream = True
    st.session_state.content_to_stream = kwargs["content"]

# Accept user input
if prompt := st.chat_input("What can I help with?") or st.session_state.is_stream:
    if st.session_state.is_stream:
        st.session_state.is_stream = False
        expander = st.expander("Source")
        expander.write("The data is sourced from Finance Report and Yahoo News")
        left, middle, right = st.columns(3)
        left.button("Data", icon=":material/dataset:", type="primary", on_click=on_button_click, kwargs={"content":"Once implemented I will display a data grid here"})
        middle.button("Chart", icon=":material/bar_chart:", type="primary", on_click=on_button_click, kwargs={"content":"Chart"})
        right.button("Meeting", icon=":material/groups:", on_click=on_button_click, kwargs={"content":"Once implemented I will set up a meeting with Risk Managers/ Desk Trader"})
        if(st.session_state.content_to_stream=="Chart"):
            st.bar_chart(np.random.randn(30, 3))
        else:
            full_buffer = st.chat_message("assistant").write(st.session_state.content_to_stream)
        #st.session_state.messages.append({"role": "assistant", "content": full_buffer})
    else:
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        # Display user message in chat message container
        with st.chat_message("user"):
            st.markdown(prompt)

        # Display assistant response in chat message container
        with st.chat_message("assistant"):
            response = st.write_stream(response_generator())
            expander = st.expander("Source")
            expander.write("The data is sourced from Finance Report and Yahoo News")
            left, middle, right = st.columns(3)
            left.button("Data", icon=":material/dataset:", type="primary", on_click=on_button_click, kwargs={"content":"Data"})
            middle.button("Chart", icon=":material/bar_chart:", type="primary", on_click=on_button_click, kwargs={"content":"Chart"})
            right.button("Meeting", icon=":material/groups:", on_click=on_button_click, kwargs={"content":"Meeting"})
            #st.bar_chart(np.random.randn(30, 3))
            
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})