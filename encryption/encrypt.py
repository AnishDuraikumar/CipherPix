
import os

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.ciphers.aead import AESGCM


# CipherPix encryption configuration

MAGIC = b"CPX1"
SALT_LENGTH = 16
NONCE_LENGTH = 12
KEY_LENGTH = 32
ITERATIONS = 600_000


def derive_key(password, salt):
    """
    Convert a password into a 256-bit encryption key.
    """

    if not password:
        raise ValueError("Password cannot be empty.")

    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=KEY_LENGTH,
        salt=salt,
        iterations=ITERATIONS
    )

    return kdf.derive(password.encode("utf-8"))


def encrypt_message(message, password):
    """
    Encrypt a message using AES-256-GCM.

    Returns:
        bytes: Version + salt + nonce + ciphertext and tag.
    """

    if not isinstance(message, str) or not message:
        raise ValueError("Message cannot be empty.")

    salt = os.urandom(SALT_LENGTH)
    nonce = os.urandom(NONCE_LENGTH)

    key = derive_key(password, salt)

    aesgcm = AESGCM(key)

    ciphertext = aesgcm.encrypt(
        nonce,
        message.encode("utf-8"),
        MAGIC
    )

    encrypted_data = MAGIC + salt + nonce + ciphertext

    return encrypted_data
