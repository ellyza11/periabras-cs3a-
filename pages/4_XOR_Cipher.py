import streamlit as st

st.header("XOR cipher")

st.text_area("Plain Text:")

st.text_input("Key:")

btn_submit = st.button("Submit")

if btn_submit:
    def xor_encrypt(plaintext, key):
        if len(plaintext) < len(key):
            st.write("Plaintext length should be equal or greater than the length of the key")
        if plaintext == key:
            st.write("Plaintext should not be equal to the key")
        
        ciphertext = bytearray()
        for i in range(len(plaintext)):
            plaintext_byte = ord(plaintext[i])
            key_byte = ord(key[i % len(key)])

            st.write(f"Plaintext byte: {format(plaintext_byte, '08b')} = {chr(plaintext_byte)}")
            st.write(f"Key byte:       {format(key_byte, '08b')} = {chr(key_byte)}")

            xor_result = plaintext_byte ^ key_byte
            ciphertext.append(xor_result)
            st.write(f"XOR result:     {format(key_byte, '08b')} = {chr(key_byte)}")
            st.write("---------------------")
        return ciphertext

    def xor_decrypt(ciphertext, key):
        decrypted_text = bytearray()
        for i in range(len(ciphertext)):
            ciphertext_byte = ciphertext[i]
            key_byte = ord(key[i % len(key)])

            decrypted_byte = ciphertext_byte ^ key_byte
            decrypted_text.append(decrypted_byte)
        return decrypted_text.decode('utf-8')
    
plaintext = input()
key = input()

ciphertext = xor_encrypt(plaintext, key)
print(f"Ciphertext: {ciphertext.decode()}")

decrypted = xor_decrypt(ciphertext, key)
print(f"Decrypted:" {decrypted})

plaintext = bytes(input().encode())
key = bytes(input().encode())     
