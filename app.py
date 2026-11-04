
from flask import (
    Flask,
    render_template,
    request,
    send_file
)

from encryption.encrypt import encrypt_message
from encryption.decrypt import decrypt_message

from steganography.encode import encode_message
from steganography.decode import decode_message

from PIL import Image, UnidentifiedImageError

from io import BytesIO
from pathlib import Path
from tempfile import TemporaryDirectory


app = Flask(__name__)

# Maximum uploaded file size: 10 MB
app.config["MAX_CONTENT_LENGTH"] = 10 * 1024 * 1024


def validate_png(image_data):
    """Validate uploaded PNG image."""

    try:
        image = Image.open(BytesIO(image_data))

        if image.format != "PNG":
            raise ValueError("Please upload a PNG image.")

        width, height = image.size

        if width * height > 20_000_000:
            raise ValueError("Image dimensions are too large.")

        image.verify()

    except (UnidentifiedImageError, OSError):
        raise ValueError("Invalid or corrupted PNG image.") from None


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/hide", methods=["POST"])
def hide_message():

    message = request.form.get("message", "").strip()
    password = request.form.get("password", "")
    uploaded_file = request.files.get("image")

    if not message or not password or not uploaded_file:
        return render_template(
            "index.html",
            error="Please provide a message, password and PNG image.",
            active_tab="hide"
        )

    try:
        image_data = uploaded_file.read()

        if not image_data:
            raise ValueError("Uploaded image is empty.")

        validate_png(image_data)

        encrypted_data = encrypt_message(message, password)

        with TemporaryDirectory() as temp_dir:

            input_path = Path(temp_dir) / "original.png"
            output_path = Path(temp_dir) / "cipherpix_secret.png"

            input_path.write_bytes(image_data)

            encode_message(
                str(input_path),
                str(output_path),
                encrypted_data
            )

            result = output_path.read_bytes()

        return send_file(
            BytesIO(result),
            mimetype="image/png",
            as_attachment=True,
            download_name="cipherpix_secret.png"
        )

    except ValueError as error:
        return render_template(
            "index.html",
            error=str(error),
            active_tab="hide"
        )


@app.route("/extract", methods=["POST"])
def extract_message():

    password = request.form.get("password", "")
    uploaded_file = request.files.get("image")

    if not password or not uploaded_file:
        return render_template(
            "index.html",
            error="Please provide an image and password.",
            active_tab="extract"
        )

    try:
        image_data = uploaded_file.read()

        if not image_data:
            raise ValueError("Uploaded image is empty.")

        validate_png(image_data)

        with TemporaryDirectory() as temp_dir:

            image_path = Path(temp_dir) / "secret.png"

            image_path.write_bytes(image_data)

            encrypted_data = decode_message(str(image_path))

        message = decrypt_message(encrypted_data, password)

        return render_template(
            "index.html",
            extracted_message=message,
            active_tab="extract"
        )

    except ValueError as error:
        return render_template(
            "index.html",
            error=str(error),
            active_tab="extract"
        )


@app.errorhandler(413)
def file_too_large(error):
    return render_template(
        "index.html",
        error="File exceeds the 10 MB upload limit.",
        active_tab="hide"
    ), 413


if __name__ == "__main__":
    app.run(debug=True)

