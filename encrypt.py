from secret import Confidence
import sys
import os

path_home_user = os.path.expanduser("~/")

def dir_exist(dir_name):
    path = f"{path_home_user}{dir_name}"
    if os.path.exists(path) and os.path.isdir(path):
        return path

def encrypt_files(dirname, key="private.key"):
    directory = dir_exist(dirname)
    if directory:
        files = Confidence()
        for element in os.listdir(directory):
            file = f"{directory}/{element}"
            if os.path.isfile(file):
                files.encrypt(key, file)
                print(file, "OK encrypté.")
