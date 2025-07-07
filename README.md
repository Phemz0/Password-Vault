# Password-Vault


- This program is meant to be stored on a USB stick.
- To make this work on any PC you will need to package it, PyInstaller is recommended
- Fully secure.



- pyinstaller --onefile --console --hidden-import=cryptography.hazmat.backends.openssl.backend yourscript.py
- Above for both
