import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from desencriptador import decrypt
from encriptador import encrypt


def test_decrypt():
    text = "mensaje secreto"
    key = "abc123"

    encrypted = encrypt(text, key)

    assert decrypt(encrypted, key) == text
