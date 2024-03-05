import streamlit as st

st.header("XOR cipher")

st.text_area("Plain Text:")

st.text_input("Key:")

st.button("Submit")

if not key:
    st.error("Invalid key")
else:
    if plaintext in key:
        if len(plaintext.decode()) >= len(key.decode()):
            ciphertext = xor_encrypt(plaintext, key)
            st.write("Ciphertext:",ciphertext.decode())
                
            decrypted = xor_decrypt(ciphertext, key)
            st.write("Decrypted:",decrypted.decode())
        else:
            st.write("Plaintext length should be equal or greater than the length of the key")
    else:
        st.write("Plaintext should not be equal to the key")
    
