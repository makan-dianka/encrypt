from secret import Confidence
import os

def getcmd():
    cmd = input("Commande > ")
    join = cmd.replace(' ', ';')
    listcmd = join.split(';')
    return listcmd

listcmd = getcmd()

path = listcmd[2]
option0 = listcmd[0]
option1 = listcmd[1]
option3 = listcmd[3]
optionk = listcmd[-2]
keyname = listcmd[-1]
key = keyname+'.key'

keyword = 'makan'


def files_for_encrypt():
    if option0.lower() == keyword:
        if option1 in ['-e', '--encrypt']:
            if os.path.exists(path):
                if os.path.isdir(path):
                    if option3 in ['-f', '--file']:
                        f = listcmd[4:-2]
                        return f
                    else:
                        print(f"makan ne reconnait cette option: {option3}")
                else:
                    print(f"Ceci est un repertoire: {path}")
            else:
                print(f"Ce fichier n'existe pas: {path}")
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
                            print(f'Fichier encrypté avec succès: {filename}')
                            continue
                        else:
                            print(f'Cette clé d\encryptage n\'existe pas: {keyname}')
                    else:
                        print(f"makan ne reconnait cette option: {optionk}")
                else:
                    print(f"Ceci est un dossier: {filename}")
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
                            print(f'Fichier encrypté avec succès: {p}')
                            continue
                        else:
                            print(f'Cette clé d\encryptage n\'existe pas: {keyname}')
                    else:
                        print(f"makan ne reconnait cette option: {optionk}")
                else:
                    print(f"Ceci est un dossier: {filename}")


def files_for_decrypt():
    if option0.lower() == keyword:
        if option1 in ['-d', '--decrypt']:
            if os.path.exists(path):
                if os.path.isdir(path):
                    if option3 in ['-f', '--file']:
                        f = listcmd[4:-2]
                        return f
                    else:
                        print(f"makan ne reconnait cette option: {option3}")


f_decrypt = files_for_decrypt()

def decrypt_files():
    for file_ in f_decrypt:
        filename = os.path.join(path, file_)
        if os.path.exists(filename):
            if os.path.isfile(filename):
                if optionk in ['-ku', '--key-use']:
                    if key in os.listdir('keys'):
                        Confidence().decrypt(key, filename)
                        print(f'Fichier decrypté avec succès: {filename}')
                        continue
                    else:
                        print(f'Cette clé de decryptage n\'existe pas: {keyname}')
                else:
                    print(f"makan ne reconnait cette option: {optionk}")
            else:
                print(f"Ceci est un dossier: {filename}")
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
                            print(f'Fichier decrypté avec succès: {p}')
                            continue
                        else:
                            print(f'Cette clé de decryptage n\'existe pas: {keyname}')
                    else:
                        print(f"makan ne reconnait cette option: {optionk}")
                else:
                    print(f"Ceci est un dossier: {filename}")