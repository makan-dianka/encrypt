#!/usr/bin/env python3

import sys
if sys.version_info[0] !=3: 
    print("""--------------------------------------
    REQUIRED PYTHON 3.x
    use: python3 makan.py
    author: Makan
    website: www.makandianka.org
--------------------------------------""")
    sys.exit()

from secret import Confidence
import cmd
import os

keyword = 'mk'

def generate():
    command = cmd.getcmd()
    if "" in command:
        command.remove('')

    if len(command) > 3:
        raise Exception("SyntaxError : trop d'argument")
    elif len(command) < 3:
        raise Exception("SyntaxError : la commande incomplète, il manque d'argument")
    else:
        if command[0] == keyword:
            if command[1] in ['-gk', '--generate-key']:
                Confidence().genkey(command[2])  
                path = f"{os.getcwd()}/keys/{command[2]}.key"
                print(f"la clé de cryptage est généré : {path}")
                token = Confidence().readkey(command[2]+'.key')
                print(f"Token : {token.decode()}")
            else:
                print(f"{keyword} ne reconnait cette commande : {command[1]}")
        else:
            raise Exception(f"SyntaxEroor, ce mot clé n'est pas reconnu: {command[0]}")
            
if "__main__" == __name__:
    generate()