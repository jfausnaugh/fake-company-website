import streamlit as st
import pandas

from send_inquiry import send_inquiry
st.header("Contact the Team")

df = pandas.read_csv("topics.csv")

with st.form(key="contact_form"):
    user_email = st.text_input("Your email address")
    user_topic = st.selectbox("What topic do you want to discuss?", df["topic"])
    raw_user_message = st.text_area("Your message")

# forms message that will be sent to the email
    message = f"""\
Subject: New inquiry from {user_email}

From: {user_email}
Topic: {user_topic}
{raw_user_message}
"""
    button = st.form_submit_button("Submit")
    # if the button is clicked then the email will be sent
    if button:
        send_inquiry(message)
        st.info("Your message was sent successfully!")