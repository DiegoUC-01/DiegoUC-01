import base64
import sys

from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto.Util.Padding import unpad


def generate_key(key_text):
    return SHA256.new(key_text.encode()).digest()


def decrypt(encrypted_text, key_text):
    key = generate_key(key_text)
    cipher = AES.new(key, AES.MODE_ECB)

    decoded = base64.b64decode(encrypted_text)
    decrypted = unpad(cipher.decrypt(decoded), AES.block_size)

    return decrypted.decode()


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: uv run decryptor.py 'texto_encriptado' 'clave'")
        sys.exit(1)

    encrypted = sys.argv[1]
    key = sys.argv[2]

    print(decrypt(encrypted, key))
