import os
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
public_key = private_key.public_key().public_bytes(
    serialization.Encoding.PEM,
    serialization.PublicFormat.SubjectPublicKeyInfo
)

OAEP = padding.OAEP(
    mgf=padding.MGF1(algorithm=hashes.SHA256()),
    algorithm=hashes.SHA256(),
    label=None
)

def aes_decrypt(aes_key, iv, data):
    cipher = Cipher(algorithms.AES(aes_key), modes.CBC(iv))
    decrypteur = cipher.decryptor()
    données = decrypteur.update(data) + decrypteur.finalize()
    pad = données[-1]
    return données[:-pad]

def aes_encrypt(aes_key, message: bytes) -> bytes:
    iv = os.urandom(16)
    # Padding PKCS7
    pad = 16 - len(message) % 16
    pad_message = message + bytes([pad] * pad)
    cipher = Cipher(algorithms.AES(aes_key), modes.CBC(iv))
    encrypter = cipher.encryptor()
    encrypt_data = encrypter.update(pad_message) + encrypter.finalize()
    return iv + encrypt_data
