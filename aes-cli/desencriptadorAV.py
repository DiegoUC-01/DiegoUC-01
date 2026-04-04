import argparse
import hashlib
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad


def desencriptar(texto_encriptado: bytes, llave: str) -> str:
    key = hashlib.sha256(llave.encode()).digest()

    cipher = AES.new(key, AES.MODE_ECB)

    decrypted = cipher.decrypt(texto_encriptado)

    texto = unpad(decrypted, AES.block_size)

    return texto.decode()


def main():
    parser = argparse.ArgumentParser(description="CLI para desencriptar texto AES")

    parser.add_argument("-t", "--texto", required=True, help="Texto encriptado en HEX")
    parser.add_argument("-k", "--llave", required=True, help="Llave usada para encriptar")

    args = parser.parse_args()

    # convertir HEX a bytes
    texto_bytes = bytes.fromhex(args.texto)

    resultado = desencriptar(texto_bytes, args.llave)

    print("Texto desencriptado:")
    print(resultado)


if __name__ == "__main__":
    main()