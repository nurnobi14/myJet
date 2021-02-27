import hashlib

flag = 0
pass_hass = input("Enter md5 hash :")
wordlistr =  input("type your search file name :")

try:
    pass_file = open(wordlistr+".txt", "r")
except:
    print("this file name is not existing")
    quit()

for word in pass_file:
    enc_word = word.encode('utf-8')
    digest = hashlib.md5(enc_word.strip()).hexdigest()

    if digest == pass_hass:
        print("code fined ")
        print("code is :" + word)
        flag = 1
        break
if flag==0:
    print("something is wrong ")