# 🔐 Python Password Manager

A secure command-line password manager built with Python.

## Features
- Encryption using Fernet (cryptography library)
- Add and retrieve saved credentials
- Data stored securely in JSON format
- Encryption key stored separately

## Technologies Used
- Python
- cryptography
- JSON
- Git

## How to Run

1. Install dependencies:
   py -m pip install cryptography

2. Run the program:
   py main.py

## Security Notes
- Do NOT delete key.key or saved passwords cannot be decrypted.
- data.json and key.key are ignored in Git for security.

---

Built as a learning project to understand encryption and file handling in Python.
