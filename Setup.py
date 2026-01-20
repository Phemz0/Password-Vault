import os
import json
import base64
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
from cryptography.hazmat.primitives import hashes, hmac
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from tqdm import tqdm
import time 


print("""
                                                                                                                       
 ██▓███   ▄▄▄        ██████   ██████  █     █░ ▒█████   ██▀███  ▓█████▄  ██▒   █▓ ▄▄▄       █    ██  ██▓    ▄▄▄█████▓   
▓██░  ██▒▒████▄    ▒██    ▒ ▒██    ▒ ▓█░ █ ░█░▒██▒  ██▒▓██ ▒ ██▒▒██▀ ██▌▓██░   █▒▒████▄     ██  ▓██▒▓██▒    ▓  ██▒ ▓▒   
▓██░ ██▓▒▒██  ▀█▄  ░ ▓██▄   ░ ▓██▄   ▒█░ █ ░█ ▒██░  ██▒▓██ ░▄█ ▒░██   █▌ ▓██  █▒░▒██  ▀█▄  ▓██  ▒██░▒██░    ▒ ▓██░ ▒░   
▒██▄█▓▒ ▒░██▄▄▄▄██   ▒   ██▒  ▒   ██▒░█░ █ ░█ ▒██   ██░▒██▀▀█▄  ░▓█▄   ▌  ▒██ █░░░██▄▄▄▄██ ▓▓█  ░██░▒██░    ░ ▓██▓ ░    
▒██▒ ░  ░ ▓█   ▓██▒▒██████▒▒▒██████▒▒░░██▒██▓ ░ ████▓▒░░██▓ ▒██▒░▒████▓    ▒▀█░   ▓█   ▓██▒▒▒█████▓ ░██████▒  ▒██▒ ░    
▒▓▒░ ░  ░ ▒▒   ▓▒█░▒ ▒▓▒ ▒ ░▒ ▒▓▒ ▒ ░░ ▓░▒ ▒  ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░ ▒▒▓  ▒    ░ ▐░   ▒▒   ▓▒█░░▒▓▒ ▒ ▒ ░ ▒░▓  ░  ▒ ░░      
░▒ ░       ▒   ▒▒ ░░ ░▒  ░ ░░ ░▒  ░ ░  ▒ ░ ░    ░ ▒ ▒░   ░▒ ░ ▒░ ░ ▒  ▒    ░ ░░    ▒   ▒▒ ░░░▒░ ░ ░ ░ ░ ▒  ░    ░       
░░         ░   ▒   ░  ░  ░  ░  ░  ░    ░   ░  ░ ░ ░ ▒    ░░   ░  ░ ░  ░      ░░    ░   ▒    ░░░ ░ ░   ░ ░     ░         
               ░  ░      ░        ░      ░        ░ ░     ░        ░          ░        ░  ░   ░         ░  ░            
                                                                 ░           ░                                          
""")

for i in tqdm(range(100)):
    time.sleep(0.02)

path = input("""
             
 -= USB path information =- 
    - Make sure to add two backslashes to the path! 
    - The file name must always be PasswordVault
    - The only interchangeable value should be the directory name (--> x:\\\PasswordVault) 
    - Example of what should be typed (D:\\\PasswordVault)
    
Enter USB path: """)


masterPasswordValue = input("""
                            
 -= Master password information =- 
    - This password can not be changed
    - You will be asked to use this password every time you want to access your vault
    - Forgetting this password will result in losing access to this instance of PasswordVault

Enter master password: """)


for i in tqdm(range(100)):
    time.sleep(0.05)
    
    
os.makedirs(path, exist_ok=True)


def saveVault (masterPassword: str):
    
    vault = {}
    
    passwordSalt = createSalt()
    key = deriveKey(masterPassword, passwordSalt)
    
    with open(os.path.join(path, "salt.bin"), "wb") as f:
        f.write(passwordSalt)
        
    HMACValue = hmac.HMAC(key, hashes.SHA256())
    HMACValue.update(b"check vault")
    verifyValue = HMACValue.finalize()
    with open(os.path.join(path,"verify.hash"), "wb") as f:
        f.write(verifyValue)
        
    encrypted = encryptVault(key, vault)
    with open(os.path.join(path,"vault.enc"), "wb") as f:
        f.write(encrypted)
        
def createSalt():
    return os.urandom(16)

def deriveKey (password: str, salt:bytes) -> bytes:
    kdf = Scrypt(salt=salt, length=32, n=2**14, r=8, p=1)
    return kdf.derive(password.encode())
        
def encryptVault(key: bytes, vaultData: dict) -> bytes:    
    aesgcm = AESGCM(key)
    nonce = os.urandom(12)
    jsonData = json.dumps(vaultData).encode()
    encrypted = aesgcm.encrypt(nonce, jsonData, None)
    return nonce + encrypted






















saveVault(masterPassword=f"{masterPasswordValue}")
