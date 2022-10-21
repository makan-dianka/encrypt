from secret import Confidence
import os
import cmd 

keyword = 'mk'

listcmd = cmd.getcmd()

try:
    path = listcmd[2]
    option0 = listcmd[0]
    option1 = listcmd[1]
    option3 = listcmd[3]
    optionk = listcmd[-2]
    keyname = listcmd[-1]
except:
    raise Exception(f"\033[31mSyntax Error, assurez vous de donner toutes les arguments: {keyword} --help pour voir l'aide\n")
else:
    key = keyname+'.key'

    def files_for_encrypt():
        if option0.lower() == keyword:
            if option1 in ['-e', '--encrypt']:
                if os.path.exists(path):
                    if os.path.isdir(path):
                        if option3 in ['-f', '--file']:
                            f = listcmd[4:-2]
                            return f
    f = files_for_encrypt()

    def encrypt_files():
        if f != None:
            for file_ in f:
                filename = os.path.join(path, file_)
                if os.path.exists(filename):
                    if os.path.isfile(filename):
                        if optionk in ['-ku', '--key-use']:
                            if key in os.listdir('keys'):
                                Confidence().encrypt(key, filename)
                                print(f'\033[33mFichier encrypté avec succès: {filename}')
                                continue
                            else:
                                print(f'Cette clé d\'encryptage n\'existe pas: {keyname}')
                        else:
                            raise Exception(f"{keyword} ne reconnait cette option: {optionk}")
                    else:
                        pass
                        # print(f"Ceci est un dossier: {filename}")
                else:
                    print(f"Ce fichier n'existe pas: {filename}")


    def encrypt_all_files():
        if option0.lower() == keyword:
            if option3 in ['--fs', '--files']:
                elements = os.listdir(path)
                for element in elements:
                    p = os.path.join(path, element)
                    if os.path.isfile(p):
                        if optionk in ['-ku', '--key-use']:
                            if key in os.listdir('keys'):
                                Confidence().encrypt(key, p)
                                print(f'\033[33mFichier encrypté avec succès: {p}')
                                continue
                            else:
                                print(f'Cette clé d\'encryptage n\'existe pas: {keyname}')
                        else:
                            raise Exception(f"{keyword} ne reconnait cette option: {optionk}")
                    else:
                        pass
                        # print(f"Ceci est un dossier: {p}")


    def files_for_decrypt():
        if option0.lower() == keyword:
            if option1 in ['-d', '--decrypt']:
                if os.path.exists(path):
                    if os.path.isdir(path):
                        if option3 in ['-f', '--file']:
                            f = listcmd[4:-2]
                            return f

    f_decrypt = files_for_decrypt()

    def decrypt_files():
        for file_ in f_decrypt:
            filename = os.path.join(path, file_)
            if os.path.exists(filename):
                if os.path.isfile(filename):
                    if optionk in ['-ku', '--key-use']:
                        if key in os.listdir('keys'):
                            Confidence().decrypt(key, filename)
                            print(f'\033[32mFichier decrypté avec succès: {filename}')
                            continue
                        else:
                            print(f'Cette clé de decryptage n\'existe pas: {keyname}')
                    else:
                        raise Exception(f"{keyword} ne reconnait cette option: {optionk}")
                else:
                    pass
                    # print(f"Ceci est un dossier: {filename}")
            else:
                print(f"Ce repertoire n'existe pas: {filename}")


    def decrypt_all_files():
        if option0.lower() == keyword:
            if option3 in ['--fs', '--files']:
                elements = os.listdir(path)
                for element in elements:
                    p = os.path.join(path, element)
                    if os.path.isfile(p):
                        if optionk in ['-ku', '--key-use']:
                            if key in os.listdir('keys'):
                                Confidence().decrypt(key, p)
                                print(f'\033[32mFichier decrypté avec succès: {p}')
                                continue
                            else:
                                print(f'Cette clé de decryptage n\'existe pas: {keyname}')
                        else:
                            raise Exception(f"{keyword} ne reconnait cette option: {optionk}")
                    else:
                        pass
                        # print(f"Ceci est un dossier: {p}")