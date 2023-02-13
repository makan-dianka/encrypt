from cryptography.fernet import Fernet
import os
from mysql import connector

class Confidence:

    def conndb(self):
        conn = connector.connect(
            user="pydev",
            password="pydev",
            database="confidence",
            auth_plugin='mysql_native_password'
        )

        cursor = conn.cursor()
        cursor.execute("SELECT cle FROM secret where nom='private';")
        key = cursor.fetchall()[0][0]
        return key

    def genkey(self, keyname):
        """Generate a key"""
        key = Fernet.generate_key()
        with open(f'keys/{keyname}.key', 'wb') as filekey:
            filekey.write(key)

    def readkey(self, keyname):
        keynam = os.path.expanduser(f"~/keys/{keyname}")
        with open(f'{keynam}', 'rb') as filekey:
            key = filekey.read()
        return key

    def encrypt(self, keyname, filename):
        """encrypt a files"""
        keynam = f"{keyname}"      
        key = self.readkey(keynam)
        fernet = Fernet(key)
        
        with open(filename, 'rb') as file:
            original = file.read()
            
        encrypted = fernet.encrypt(original)
        
        with open(filename, 'wb') as encrypted_file:
            encrypted_file.write(encrypted)

    def decrypt(self, keyname, filename):
        """Decrypt a file"""
        keynam = f"{keyname}"
        key = self.readkey(keynam)
        fernet = Fernet(key)

        with open(filename, 'rb') as enc_file:
            encrypted = enc_file.read()
        try:
            decrypted = fernet.decrypt(encrypted)
            with open(filename, 'wb') as dec_file:
                dec_file.write(decrypted)
        except:
            pass