
from encryption.encrypt import encrypt_message
from encryption.decrypt import decrypt_message


# Original message
message = "Welcome to CipherPix!"

# Password
password = "CipherPix@2026"


# Encrypt
encrypted = encrypt_message(message, password)

print("Original message:", message)
print("Encrypted data:", encrypted.hex())
print("Encryption successful!")


# Decrypt
decrypted = decrypt_message(encrypted, password)

print("\nDecrypted message:", decrypted)

assert decrypted == message

print("Decryption successful!")
print("Encryption and decryption test passed!")


# Test incorrect password
try:
    decrypt_message(encrypted, "WrongPassword")
except ValueError:
    print("Incorrect password test passed!")
else:
    raise AssertionError("Incorrect password was accepted.")
