import argparse

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes


def decrypt_text(key: bytes, encrypted_text: str) -> str:
    # Convertir el string recibido en la CLI a objeto bytes
    encrypted_bytes = eval(encrypted_text)

    # Separar IV y ciphertext
    iv = encrypted_bytes[:16]
    ciphertext = encrypted_bytes[16:]

    # Crear cifrador AES en modo CBC con el mismo IV
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()

    # Desencriptar
    padded_plaintext = decryptor.update(ciphertext) + decryptor.finalize()

    # Remover padding PKCS7
    unpadder = padding.PKCS7(128).unpadder()
    plaintext = unpadder.update(padded_plaintext) + unpadder.finalize()

    return plaintext.decode()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Desencriptador AES CLI")
    parser.add_argument("key", help="Clave de 16, 24 o 32 caracteres")
    parser.add_argument(
        "encrypted_text",
        help="Texto encriptado en formato bytes (ej: b'\\x12\\x34...')",
    )
    args = parser.parse_args()

    key = args.key.encode()
    decrypted = decrypt_text(key, args.encrypted_text)
    print(f"Texto desencriptado: {decrypted}")
