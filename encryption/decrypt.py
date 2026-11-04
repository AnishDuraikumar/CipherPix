
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.exceptions import InvalidTag

from encryption.encrypt import (
    MAGIC,
    SALT_LENGTH,
    NONCE_LENGTH,
    derive_key
)


def decrypt_message(encrypted_data, password):
    """
    Decrypt CipherPix encrypted data using AES-256-GCM.
    """

    if not isinstance(encrypted_data, bytes):
        raise ValueError("Encrypted data must be bytes.")

    minimum_length = (
        len(MAGIC) +
        SALT_LENGTH +
        NONCE_LENGTH +
        16
    )

    if len(encrypted_data) < minimum_length:
        raise ValueError("Encrypted data is incomplete.")

    if encrypted_data[:len(MAGIC)] != MAGIC:
        raise ValueError("Invalid CipherPix data format.")

    position = len(MAGIC)

    salt = encrypted_data[
        position:position + SALT_LENGTH
    ]

    position += SALT_LENGTH

    nonce = encrypted_data[
        position:position + NONCE_LENGTH
    ]

    position += NONCE_LENGTH

    ciphertext = encrypted_data[position:]

    key = derive_key(password, salt)

    aesgcm = AESGCM(key)

    try:
        decrypted_data = aesgcm.decrypt(
            nonce,
            ciphertext,
            MAGIC
        )

        return decrypted_data.decode("utf-8")

    except InvalidTag:
        raise ValueError(
            "Decryption failed. Incorrect password "
            "or modified encrypted data."
        ) from None
