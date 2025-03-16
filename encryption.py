from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64
import hashlib

def generate_key(password):
    return hashlib.sha256(password.encode()).digest()

def encrypt_message(message, password):
    key = generate_key(password)
    cipher = AES.new(key, AES.MODE_EAX)
    nonce = cipher.nonce
    ciphertext, tag = cipher.encrypt_and_digest(message.encode('utf-8'))
    return base64.b64encode(nonce + ciphertext).decode('utf-8')

def decrypt_message(encrypted_message, password):
    data = base64.b64decode(encrypted_message)
    key = generate_key(password)
    nonce = data[:16]
    ciphertext = data[16:]
    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    plaintext = cipher.decrypt(ciphertext)
    return plaintext.decode('utf-8')
