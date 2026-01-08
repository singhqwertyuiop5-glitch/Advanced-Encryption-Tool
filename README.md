COMPANY   : CODTECH IT SOLUTIONS
NAME      : ADITYA SINGH
INTERN ID : CT04DR3144
DOMAIN    : CYBER SECURITY & ETHICAL HACKING
DURATION  : 4 WEEKS
MENTOR    : NEELA SANTOSH


# Advanced Encryption Tool (AES-256)
The Advanced Encryption Tool (AES-256) is a Python-based application developed as part of an internship task to demonstrate modern cryptographic practices. The project focuses on secure file encryption and decryption using the AES-256 (Advanced Encryption Standard) algorithm, one of the most widely trusted and industry-approved encryption standards.
This tool is designed for educational and learning purposes only, helping users understand how encryption works in real-world applications, how sensitive data can be protected, and how cryptographic libraries are used responsibly in Python.

## Project Overview
In today’s digital world, protecting sensitive data is critical. Encryption ensures that even if data is accessed without authorization, it remains unreadable without the correct key. This project demonstrates how strong encryption can be implemented in a practical and user-friendly way.
The application allows users to encrypt files using a password, transforming readable data into encrypted content that cannot be understood without proper decryption. It also supports secure decryption using the same password. The tool uses password-based key derivation, ensuring that encryption keys are generated securely rather than using raw or hardcoded keys.

## How It Works
-Password-Based Key Derivation
The user provides a password.
A secure key is derived from the password using cryptographic techniques.
This prevents weak or predictable keys.
-AES-256 Encryption
The derived key is used with AES-256 to encrypt file contents.
Encrypted data is saved securely to disk.
-Decryption Process
The same password is required to decrypt the file.
If the password is incorrect, decryption fails, ensuring data confidentiality.
-Command-Line Interface
A simple, menu-driven interface guides the user through encryption and decryption steps.
Designed for ease of use and clarity.

## Features
Implements AES-256 file encryption
Secure password-based key derivation
Supports both file encryption and decryption
Menu-driven and user-friendly command-line interface
Modular and well-structured codebase
Uses industry-standard cryptographic practices
Ideal for beginners learning cybersecurity and cryptography

## Requirements
Python 3.7 or higher
cryptography library
Install dependencies using:
pip install cryptography

## Project Structure
advanced-encryption-tool/
├── encryptor.py
├── crypto_utils.py
├── README.md
├── requirements.txt
└── sample.txt

## output
<img width="1920" height="1020" alt="Image" src="https://github.com/user-attachments/assets/917c51ec-b456-41e4-93eb-ea3115cf0bb0" />

<img width="1920" height="1020" alt="Image" src="https://github.com/user-attachments/assets/1ee63894-b60f-4725-b84c-73daac8c2246" />

<img width="1920" height="1020" alt="Image" src="https://github.com/user-attachments/assets/9537a3c3-0d67-4a9e-b712-c9f4b10a0aa6" />
