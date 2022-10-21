# Encrypt & Decrypt files

encrypt and decrypt files using python


# To have a copy of this project 

```git clone git@github.com:makan-dianka/encrypt.git```

move to the project folder

```cd encrypt```

install the dependances

```pip install -r requirements.txt```


# Encrypt and Decrypt files
execute ```python makan.py``` to encrypt or decrypt files
## Generate cryptage's key
execute ```python genkey.py``` to generate cryptage's key

### Option in input :
```mk``` ```--generate-key``` or ```-gk``` following by key name

### Exemple usage :
```mk --generate-key private``` to generate key private

```mk -gk private``` to generate key private

## Encrypt some files

### Options in input :
```mk``` then ```-e``` or ```--encrypt``` following by folder name to encrypt then ```-f``` or ```--file``` following by filesname e.g [filename1 filename2 filename3 ...] then  ```-ku``` or ```--key-use``` following by keyname.

## Encrypt all files
- ```-fs``` or ```--files``` encrypt all files in the folder

### Exemple usage :
```mk -e /home/pydev/ -f toto.pdf titi.txt --key-use private``` encrypt file toto.pdf and titi using private key.

```mk -encrypt /home/pydev/ --file toto.pdf titi.txt --key-use private``` encrypt file toto.pdf and titi using private key.

```mk -e /home/pydev/ --files -ku private``` encrypt all files in folder /home/pydev/ using private key

## Decrypt some files : 
```mk``` ```-d``` or ```--decrypt``` following by folder name to decrypt then ```-f``` or ```--file``` following by filesname e.g [filename1 filename2 filename3 ...] then  ```-ku``` or ```--key-use``` following by keyname.

## Decrypt all files :
- ```-fs``` or ```--files``` decrypt all the files in the folder

# Exemple usage :
```mk -d /home/pydev/ -f toto.pdf titi.txt --key-use private``` decrypt file toto.pdf and titi.txt in folder /home/pydev/ using default key

```mk --decrypt /home/pydev/ --files -ku private``` decrypt all files in folder /home/pydev/ using private key

# Becarefull
the key that you use to encrypt the files, you must you the same key to decrypt the same files.
e.g ```mk -e /home/pydev/ --file toto.pdf titi.txt --key-use default``` here i use default key to encrypt the files. To decrypt the files is mandatory to you the same key e.g ```mk --decrypt /home/pydev/ --file toto.pdf titi.txt --key-use default``` here i use the same key default to decrypt the same files