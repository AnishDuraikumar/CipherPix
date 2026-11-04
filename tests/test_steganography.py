
from encryption.encrypt import encrypt_message
from encryption.decrypt import decrypt_message

from steganography.encode import encode_message
from steganography.decode import decode_message

from PIL import Image


# Create a test PNG image.
Image.new(
    "RGB",
    (500, 500),
    color=(120, 150, 200)
).save("tests/original.png")


# Secret message.
message = "Welcome to CipherPix!"

password = "CipherPix@2026"


# Encrypt the message.
encrypted_data = encrypt_message(message, password)

print("Encryption completed!")


# Hide encrypted data in the image.
encode_message(
    "tests/original.png",
    "tests/secret.png",
    encrypted_data
)

print("Secret message hidden inside PNG!")


# Extract encrypted data.
extracted_data = decode_message("tests/secret.png")

print("Hidden data extracted!")


# Decrypt the extracted message.
decrypted_message = decrypt_message(
    extracted_data,
    password
)

print("Decrypted message:", decrypted_message)

assert decrypted_message == message

print("COMPLETE TEST PASSED!")
