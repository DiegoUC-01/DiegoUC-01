import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from desencriptador import decrypt
from encriptador import encrypt


def test_encrypt():
    text = "hola mundo"
    key = "clave123"

    encrypted = encrypt(text, key)
    decrypted = decrypt(encrypted, key)

    assert decrypted == text
