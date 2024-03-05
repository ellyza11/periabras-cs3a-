import streamlit as st

st.header("XOR cipher")

st.text_area("Plain Text:")

st.text_input("Key:")

if st.button("Submit")