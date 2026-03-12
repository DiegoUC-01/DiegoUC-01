from encriptadorAV import encriptar
from desencriptadorAV import desencriptar


def test_encriptar_y_desencriptar():
    texto = "hola mundo"
    llave = "clave123"

    encrypted = encriptar(texto, llave)

    # convertir de hex string a bytes
    encrypted_bytes = bytes.fromhex(encrypted)

    decrypted = desencriptar(encrypted_bytes, llave)

    assert decrypted == texto
