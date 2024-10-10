```markdown
# Password Manager

## Overview

This project is a simple password manager designed to store user credentials securely on a single device. It allows users to generate strong passwords and manage their credentials efficiently, thereby helping to mitigate the risks associated with password reuse and data breaches. 

## Features

- **Secure Storage**: Credentials are encrypted and stored locally in a JSON file.
- **Strong Password Generation**: Generate secure and complex passwords using cryptographic randomness.
- **User-Friendly Interface**: A simple command-line interface for interacting with the password manager.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Security Model](#security-model)
- [Discussion](#discussion)
- [Limitations](#limitations)
- [License](#license)

## Installation

### Prerequisites

You need Python 3.6 or higher installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

### Clone the Repository

First, clone the repository from GitHub to your local machine:

```bash
git clone https://github.com/YOUR_USERNAME/PasswordManager.git
cd PasswordManager
```

### Set Up the Virtual Environment

Create a virtual environment and activate it:

```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

### Install Required Libraries

Install the necessary dependencies using pip:

```bash
pip install cryptography
```

### Generate Encryption Key

You need to generate an encryption key to store your credentials securely:

```bash
python -c "from encryption import generate_key; generate_key()"
```

This command will create a `key.key` file in your project directory.

## Usage

### Running the Application

To start the password manager, run the following command:

```bash
python password_manager.py
```

### Interacting with the Application

1. When prompted, choose one of the following actions:
   - **Add a Credential**: Type `add` to save a new service credential.
     - You will be prompted to enter the service name, username, and password (you have the option to generate a random password by leaving the password input blank).
   - **Retrieve a Credential**: Type `get` to retrieve an existing credential.
     - Enter the service name for which you want to retrieve the username and password. 
   - **Exit**: Type `exit` to close the application.

### Example Interaction

```plaintext
Do you want to add or get a credential? (add/get/exit): add
Enter the service name: Gmail
Enter your username: user@gmail.com
Enter your password (or leave blank to generate a random one): 
Generated password: J4uT!e&D*2sX
Credential saved.

Do you want to add or get a credential? (add/get/exit): get
Enter the service name to retrieve: Gmail
Username: user@gmail.com, Password: J4uT!e&D*2sX
```

![Screenshot from 2024-10-10 12-27-10.png](../../Pictures/Screenshots/Screenshot%20from%202024-10-10%2012-27-10.png "console example")
## Security Model

This password manager employs robust security measures to protect user credentials:

1. **Encryption**: 
   - Credentials are encrypted using AES (via the `cryptography` library) and stored in a local JSON file. The encryption ensures that stored passwords cannot be read without the corresponding key.

2. **Key Management**:
   - The encryption key is generated and stored in a separate file (`key.key`), ensuring it is not mixed with your data. It's crucial to keep this file safe, as losing it would mean losing access to the stored credentials.

3. **Password Generation**:
   - The application uses Python’s `secrets` module to generate strong passwords, utilizing a cryptographically secure random source to ensure unpredictability.

4. **Security Considerations**:
   - Major threats considered include unauthorized access to the device, malware, and physical theft. The application aims to protect against these threats by encrypting stored credentials.


## Discussion

### What Do We Protect Against?

The application is designed to protect against unauthorized access to stored credentials. Threat actors may include:

- **Intruders**: Individuals who gain unauthorized access to the device.
- **Malicious Software**: Malware that may try to access files.
- **Physical Theft**: If the device is stolen, ensuring data stored is encrypted protects user credentials.

### Security Considerations

- **Best Practices**: The app follows security guidelines by using established libraries for encryption and secure password generation.
- **User Behavior**: It's important for users not to share the `key.key` file and to maintain strong, unique passwords.

## Limitations

- **Single Device Storage**: The password manager currently supports storing credentials only on a single device. It does not synchronize across devices.
- **No User Authentication**: Currently, the application does not implement any user authentication method (like a master password) to unlock access to the credentials.

### Technical Answers:

1. **Programming Language/Technology**: Implemented in Python, a language known for its readability and wide range of libraries for security features.

2. **Local Database/Vault**: User credentials are managed in a local JSON file, offering simplicity and ease of use for single-device storage.

3. **Protection Measures**: Data is encrypted using AES, ensuring that unauthorized access to the database would not reveal credentials without the key.

4. **Cryptographic Decisions**: The `cryptography` library is used for encryption due to its robust features and widespread adoption, ensuring secure data handling.

5. **Password Generation**: Strong passwords are generated using Python's `secrets` module, which is designed specifically for cryptographic security.
---
```
