# Open the file in read mode
with open('Source.txt', 'r') as file:
    content = file.read()  # Read the entire file

import random
import string

chars = list(" " + "\n" + "\t" + string.ascii_letters + string.digits + string.punctuation)
Key = chars.copy()
random.shuffle(Key)
YesOrNo = input("y for Decrypt: ")

crypted = "";
Strr = "";

if YesOrNo == 'y':
    #Decrypt
    KeyFile = open("Key.txt","r")
    Key = list(KeyFile.read())
    for x in content:
        index = Key.index(x)
        crypted += chars[index]
    writee = open('Source.txt',"w")
    writee.write(crypted)

else:
    #Encrypt
    KeyFile = open("Key.txt","w")
    for x in Key:
        Strr += x
    KeyFile.write(Strr)
    for x in content:
         index = chars.index(x)
         crypted += Key[index]
    writee = open('Source.txt',"w")
    writee.write(crypted)








