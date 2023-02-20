#!/usr/bin/python3
from secret import Confidence
import sys
import os

path_home_user = os.path.expanduser("~/")

def dir_exist(dir_name):
    path = f"{path_home_user}{dir_name}"
    if os.path.exists(path) and os.path.isdir(path):
        return path

def decrypt_files(dirname, key="private.key"):
    directory = dir_exist(dirname)
    if directory:
        files = Confidence()
        for element in os.listdir(directory):
            file = f"{directory}/{element}"
            if os.path.isfile(file):
                files.decrypt(key, file)
                print(f'\033[32mFichier decrypté avec succès: {file}\033[00m')
    else:
        print(f"\nDossier \033[31m{path_home_user}{dirname}\033[00m n'existe pas\n")

if __name__=="__main__":
    args = sys.argv
    if len(args) > 1:
        current_file, params = args[0], args[1:]
        if len(params) == 2:
            if params[0] in ['-fld', '--folder']:
                decrypt_files(params[1])
            else:
                print(f"\n Flag \033[31m{params[0]}\033[00m n'est pas reconnu.")
                print("\n\033[33mINFO USAGE\033[00m [    \033[33m-fld\033[00m   or  \033[33m--folder\033[00m   ] + \033[33mfolder name\033[00m\n")
        else:
            print("\n\033[33mUSAGE\033[00m [    \033[33m-fld\033[00m   or  \033[33m--folder\033[00m   ] + \033[33mfolder name\033[00m\n")
    else:
        print("\n\033[33mUSAGE\033[00m [    \033[33m-fld\033[00m   or  \033[33m--folder\033[00m   ] + \033[33mfolder name\033[00m\n")
