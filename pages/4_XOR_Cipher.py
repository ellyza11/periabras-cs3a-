import streamlit as st

st.header("XOR cipher")

st.text_area("Plain Text:")

st.text_input("Key:")

st.button("Submit")

def xor_encrypt(plaintext, key):
    if len(plaintext) < len(key):
        raise ValueError("Plaintext length should be equal or greater than the length of the key")
    if plaintext == key:
        raise ValueError("Plaintext should not be equal to the key")
    
    ciphertext = bytearray()
    for i in range(len(plaintext)):
        plaintext_byte = ord(plaintext[i])
        key_byte = ord(key[i % len(key)])

        print(f"Plaintext byte:  {format(plaintext_byte, '08b')} = {chr(plaintext_byte)}")
        print(f"Key byte:        {format(key_byte, '08b')} = {chr(key_byte)}")

        xor_result = plaintext_byte ^ key_byte
        ciphertext.append(xor_results)
        print(f"XOR result:      {format(key_byte, '08b')} = {chr(key_byte)}")
        print("---------------------")
    return ciphertext

def xor_decrypt(ciphertext, key):
    decrypted_text = bytearray()
    for i in range(len(ciphertext)):
        ciphertext_byte = ciphertext[i]
        key_byte = ord(key[i % len(key)])

        decrypted_byte = ciphertext_byte ^ key_byte
        decrypted_text.append(decrypted_byte)
    return decrypted_text.decode('utf-8')
