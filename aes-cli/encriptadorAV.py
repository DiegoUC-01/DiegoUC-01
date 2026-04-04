import argparse
import hashlib
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad


def encriptar(texto: str, llave: str) -> str:
    # convertir la llave a 32 bytes usando SHA256
    key = hashlib.sha256(llave.encode()).digest()

    cipher = AES.new(key, AES.MODE_ECB)

    texto_bytes = texto.encode()

    encrypted = cipher.encrypt(pad(texto_bytes, AES.block_size))

    # devolver en formato HEX (más fácil de copiar)
    return encrypted.hex()


def main():
    parser = argparse.ArgumentParser(description="CLI para encriptar texto usando AES")

    parser.add_argument(
        "-t", "--texto", required=True, help="Texto que se quiere encriptar"
    )

    parser.add_argument(
        "-k", "--llave", required=True, help="Llave secreta para encriptación"
    )

    args = parser.parse_args()

    resultado = encriptar(args.texto, args.llave)

    print("Texto encriptado:")
    print(resultado)


if __name__ == "__main__":
    main()
