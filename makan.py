#!/usr/bin/env python3
import manager

if manager.option0 == manager.keyword:
    if manager.option1 in ['-e', '--encrypt']:
        if manager.option3 in ['-f', '--file']:
            manager.encrypt_files()
        if manager.option3 in ['-fs', '--files']:
            manager.encrypt_all_files()
    elif manager.option1 in ['-d', '--decrypt']:
        if manager.option3 in ['-f', '--file']:
            manager.decrypt_files()
        if manager.option3 in ['-fs', '--files']:
            manager.decrypt_all_files()
    else:
        raise Exception(f"{manager.keyword} ne reconnait cette option: {manager.option1}")
        print(f"taper: {manager.keyword} --help or {manager.keyword} -h pour voir les options")
else:
    print(f"keyword incorrect: {manager.option0}")