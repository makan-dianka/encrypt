# Encrypt and Decrypt files

## Encrypt
### Keyword :
- ```makan``` 
### Options :
- ```-e``` or ```--encrypt``` following by folder name to encrypt
- ```-d``` or ```--decrypt``` following by folder name to decrypt

### Option :
- ```-f``` or ```--file``` following by filesname e.g [filename1 filename2 filename3 ...]
- ```-fs``` or ```--files``` encrypt all files in the folder

### Option :
- ```-ku``` or ```--key-use``` following by keyname


# Exemple usage :
```makan -e /home/pydev/ -f toto.pdf titi.txt --key-use default``` encrypt file toto.pdf and titi.txt in folder /home/pydev/ using default key

```makan -d /home/pydev/ --files -ku private``` decrypt all files in folder /home/pydev/ using private key

# Note :

# Becarefull
the key that you use to encrypt the files, you must you the same key to decrypt the same files.
e.g ```makan -e /home/pydev/ --file toto.pdf titi.txt --key-use default``` here i use default key to encrypt the files. To decrypt the files is mandatory to you the same key e.g ```makan --decrypt /home/pydev/ --file toto.pdf titi.txt --key-use default``` here i use the same key default to decrypt the same files