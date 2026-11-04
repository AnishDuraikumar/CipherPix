
from PIL import Image
import struct


def decode_message(input_image):
    """
    Extract encrypted bytes from an LSB-encoded PNG image.
    """

    image = Image.open(input_image)

    if image.format != "PNG":
        raise ValueError("Input image must be a PNG.")

    image = image.convert("RGB")

    pixels = list(image.getdata())

    bits = []

    for pixel in pixels:
        for channel in pixel:
            bits.append(str(channel & 1))

    # First 32 bits contain the payload length.
    length_bits = ''.join(bits[:32])

    payload_length = struct.unpack(
        ">I",
        int(length_bits, 2).to_bytes(4, byteorder="big")
    )[0]

    required_bits = 32 + payload_length * 8

    if required_bits > len(bits):
        raise ValueError("Image contains incomplete hidden data.")

    payload_bits = ''.join(bits[32:required_bits])

    encrypted_data = bytes(
        int(payload_bits[i:i + 8], 2)
        for i in range(0, len(payload_bits), 8)
    )

    return encrypted_data
