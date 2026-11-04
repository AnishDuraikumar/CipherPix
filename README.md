# CipherPix – Secure Image Steganography

**CipherPix** is a web-based image steganography application that allows users to hide secret messages inside PNG images securely.

The application combines AES-256-GCM encryption with Least Significant Bit (LSB) steganography to provide an additional layer of privacy for digital communication.

## Features

- **AES-256-GCM Encryption:** Encrypts secret messages before embedding them into images.
- **Password Protection:** Uses PBKDF2-HMAC-SHA256 for secure encryption key derivation.
- **Image Steganography:** Hides encrypted messages inside PNG images using the LSB technique.
- **Message Extraction:** Recovers hidden messages from generated images.
- **Web Interface:** Provides separate interfaces for hiding and extracting messages.
- **Password Verification:** Rejects incorrect passwords during decryption.

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Flask | Web application framework |
| HTML | Web page structure |
| CSS | User interface styling |
| JavaScript | Frontend interactions |
| Pillow | Image processing |
| Cryptography | AES encryption and key derivation |
| Pytest | Application testing |

## Project Structure

```text
CipherPix/
│
├── encryption/
│   ├── __init__.py
│   ├── encrypt.py
│   └── decrypt.py
│
├── steganography/
│   ├── __init__.py
│   ├── encode.py
│   └── decode.py
│
├── static/
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── app.js
│
├── templates/
│   └── index.html
│
├── tests/
│   ├── __init__.py
│   ├── test_encryption.py
│   └── test_steganography.py
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/CipherPix.git
cd CipherPix
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

**Windows PowerShell:**

```powershell
.\venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 5. Run the application

```bash
python app.py
```

### 6. Open in your browser

```text
http://127.0.0.1:5000
```

## How It Works

### Hiding a Secret Message

1. Select a PNG image.
2. Enter the secret message.
3. Provide an encryption password.
4. CipherPix encrypts the message using AES-256-GCM.
5. The encrypted data is embedded into the image using LSB steganography.
6. Download the generated image.

### Extracting a Secret Message

1. Upload the generated CipherPix image.
2. Enter the correct encryption password.
3. The application extracts the hidden encrypted data.
4. AES-256-GCM decrypts the data.
5. The original secret message is displayed.

## Security

CipherPix uses:

- AES-256-GCM authenticated encryption.
- PBKDF2-HMAC-SHA256 key derivation.
- Random salts and nonces.
- Password-based decryption.

**Note:** Image steganography is not a replacement for encryption. CipherPix encrypts the message before hiding it inside the image.

## Testing

Run the test suite using:

```bash
python -m pytest
```

The tests cover encryption, decryption, password validation, and image-based message hiding and extraction.

## Limitations

- The current implementation supports PNG images.
- Image compression or resizing may destroy hidden data.
- The receiver needs the correct password to recover the original message.
- The application is currently designed for local development.

## Future Enhancements

- User registration and authentication.
- User dashboard and usage tracking.
- Free and premium subscription plans.
- Payment gateway integration.
- Support for hiding files inside images.
- Public deployment and additional security improvements.

## Author

**Anish D**

## License

No license has been assigned to this project yet.