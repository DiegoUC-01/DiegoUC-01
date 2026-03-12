import base64
import sys

from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto.Util.Padding import pad


def generate_key(key_text):
    return SHA256.new(key_text.encode()).digest()


def encrypt(text, key_text):
    key = generate_key(key_text)
    cipher = AES.new(key, AES.MODE_ECB)
    encrypted = cipher.encrypt(pad(text.encode(), AES.block_size))
    return base64.b64encode(encrypted).decode()


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: uv run encryptor.py 'texto' 'clave'")
        sys.exit(1)

    text = sys.argv[1]
    key = sys.argv[2]

    print(encrypt(text, key))
