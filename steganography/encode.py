
from PIL import Image
import struct


MAGIC = b"CPX1"


def encode_message(input_image, output_image, encrypted_data):
    """
    Hide encrypted bytes inside an RGB or RGBA PNG image
    using one least significant bit per colour channel.
    """

    if not isinstance(encrypted_data, bytes):
        raise TypeError("Encrypted data must be bytes.")

    image = Image.open(input_image)

    if image.format != "PNG":
        raise ValueError("Input image must be a PNG.")

    image = image.convert("RGB")

    # Store a 32-bit length before the encrypted payload.
    payload = struct.pack(">I", len(encrypted_data)) + encrypted_data

    binary_data = ''.join(
        format(byte, '08b') for byte in payload
    )

    pixels = list(image.getdata())

    available_bits = len(pixels) * 3

    if len(binary_data) > available_bits:
        raise ValueError(
            "Image is too small to hold this message."
        )

    modified_pixels = []
    bit_index = 0

    for pixel in pixels:
        red, green, blue = pixel

        channels = [red, green, blue]

        for i in range(3):
            if bit_index < len(binary_data):
                channels[i] = (
                    channels[i] & 254
                ) | int(binary_data[bit_index])

                bit_index += 1

        modified_pixels.append(tuple(channels))

    image.putdata(modified_pixels)

    image.save(output_image, format="PNG")

    return output_image
