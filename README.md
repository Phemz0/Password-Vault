# Password-Vault


- This program is meant to be stored on a USB stick.
- To make this work on any PC you will need to package it, PyInstaller is recommended (Python 3.12 only)
- Fully secure.


- PasswordVault only supports Python 3.12 for the below: 
- pyinstaller --onefile --console --hidden-import=cryptography.hazmat.backends.openssl.backend yourscript.py
- Above for both files 

- Will add obfuscation


changes:
- the user select which application the vault should be showing the password and username for instead of displaying all the passwords at once
- once they picked something and it's displaying the username and password, the user should be able to select to have their username/password be copied to their clipboard
