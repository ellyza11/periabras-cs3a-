import streamlit as st

st.header("Block cipher - XOR")

st.text_area("")

st.text_input("")

st.button("Submit")

def check_block_size(block_size):
    allowed_block_sizes = [8, 16, 32, 64, 128]
    if block_size