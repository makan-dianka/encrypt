from cryptography.fernet import Fernet

class Confidence:
    def genkey(self, keyname):
        """Generate a key"""
        key = Fernet.generate_key()
        with open(f'keys/{keyname}.key', 'wb') as filekey:
            filekey.write(key)

    def readkey(self, keyname):
        "read key"
        with open(f'keys/{keyname}', 'rb') as filekey:
            key = filekey.read()
        return key

    def encrypt(self, keyname, filename):
        """encrypt a files"""        
        key = self.readkey(keyname)
        fernet = Fernet(key)
        
        with open(filename, 'rb') as file:
            original = file.read()
            
        encrypted = fernet.encrypt(original)
        
        with open(filename, 'wb') as encrypted_file:
            encrypted_file.write(encrypted)

    def decrypt(self, keyname, filename):
        """Decrypt a file"""
        key = self.readkey(keyname)
        fernet = Fernet(key)

        with open(filename, 'rb') as enc_file:
            encrypted = enc_file.read()
        try:
            decrypted = fernet.decrypt(encrypted)
        except:
            pass
        else:
            with open(filename, 'wb') as dec_file:
                dec_file.write(decrypted)