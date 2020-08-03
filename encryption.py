import string
alphabet= string.ascii_lowercase+string.ascii_uppercase
#alphabet='abcdefghijklmnopqrstuvwxyz'
key=6
encode=' '
decode=' '
message=input("enter  a msg")
#ENCRYPTION
for ch in message:
    index=alphabet.find(ch)
    #new_index=(index+key)%26
    new_index=(index+key)%52
    encode+=alphabet[new_index]
print(encode)
#DECRYPTION
for ch in encode:
    #Change the variables
    index_dec=alphabet.find(ch)
    #new_index2=(index_dec-key)%26
    new_index2=(index_dec-key)%52
    decode+=alphabet[new_index2]
print(decode)
