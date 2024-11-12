import streamlit as st
import random
import numpy as np

st.set_page_config(page_title="Discovery", menu_items={
    "About": "Risk and PnL Analysis Bot"
})
st.header(":blue[Risk and PnL Analysis Bot]", divider=True)

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
        st.markdown(message["response"]["content"])

# Streamed response emulator
def response_generator():
    return random.choice(
        [
            {"content":"Hello there! How can I assist you today?","source":"Yahoo"},
            {"content":"Hi! Is there anything I can help you with?","source":"Bloomberg"},
            {"content":"Do you need help?","source":"Reuters"},
        ]
    )

# My callback function
def on_button_click(**kwargs):
    st.session_state.is_stream = True
    st.session_state.content_to_stream = kwargs["content"]

# Accept user input
if prompt := st.chat_input("What can I help with?") or st.session_state.is_stream:
    if st.session_state.is_stream:
        st.session_state.is_stream = False
        last_message = st.session_state.messages[-1]
        if "source" in last_message["response"]:
            st.expander("Source").write(last_message["response"]["source"])
        left, right = st.columns(2)
        if(st.session_state.content_to_stream=="Chart"):
            left.button("Data", icon=":material/dataset:", on_click=on_button_click, kwargs={"content":"Data"})
            right.button("Meeting", icon=":material/groups:", on_click=on_button_click, kwargs={"content":"Meeting"})
            st.bar_chart(np.random.randn(30,3))
        elif(st.session_state.content_to_stream=="Data"):
            left.button("Chart", icon=":material/bar_chart:", on_click=on_button_click, kwargs={"content":"Chart"})
            right.button("Meeting", icon=":material/groups:", on_click=on_button_click, kwargs={"content":"Meeting"})
            st.markdown("Display Data Grid")
        else:
            left.button("Data", icon=":material/dataset:", on_click=on_button_click, kwargs={"content":"Data"})
            right.button("Chart", icon=":material/bar_chart:", on_click=on_button_click, kwargs={"content":"Chart"})
            st.markdown("Once implemented, this will allow setting up a meeting with the Risk Manager and Desk Head")
    else:
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "response":{"content": prompt}})
        # Display user message in chat message container
        with st.chat_message("user"):
            st.markdown(prompt)

        # Display assistant response in chat message container
        with st.chat_message("assistant"):
            raw_response = response_generator()
            response = st.markdown(raw_response["content"])
            if "source" in raw_response:
                st.expander("Source").write(raw_response["source"])

            left, middle, right = st.columns(3)
            left.button("Data", icon=":material/dataset:", type="primary", on_click=on_button_click, kwargs={"content":"Data"})
            middle.button("Chart", icon=":material/bar_chart:", type="primary", on_click=on_button_click, kwargs={"content":"Chart"})
            right.button("Meeting", icon=":material/groups:", on_click=on_button_click, kwargs={"content":"Meeting"})
            
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "response": raw_response})