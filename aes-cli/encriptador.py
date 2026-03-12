import argparse
import os

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes


def encrypt_text(key: bytes, plaintext: str) -> bytes:
    # Generar IV aleatorio de 16 bytes
    iv = os.urandom(16)

    # Crear cifrador AES en modo CBC
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()

    # Aplicar padding PKCS7
    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(plaintext.encode()) + padder.finalize()

    # Encriptar
    ciphertext = encryptor.update(padded_data) + encryptor.finalize()

    # Retornar IV + ciphertext como bytes
    return iv + ciphertext


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Encriptador AES CLI")
    parser.add_argument("key", help="Clave de 16, 24 o 32 caracteres")
    parser.add_argument("text", help="Texto a encriptar")
    args = parser.parse_args()

    key = args.key.encode()
    encrypted = encrypt_text(key, args.text)
    print(f"Texto encriptado: {encrypted}")
