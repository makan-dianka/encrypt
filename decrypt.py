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

if __name__=="__main__":
    args = sys.argv
    if len(args) > 1:
        current_file, params = args[0], args[1:]
        if len(params) == 2:
            if params[0] in ['-fld', '--folder']:
                decrypt_files(params[1])